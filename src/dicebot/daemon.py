import dice
import discord
from discord import message
import os
from typing import Union


def get_env_var_checked(varname: str) -> Union[str, bool]:
    """gets the value of an environment variable. raises an exception and
returns False if the variable is not set.

    """
    value = os.getenv(varname)
    try:
        assert value != None and value != ""
    except AssertionError:
        print(f"{varname} unset! terminating...")
        return False
    return value


def parse_roll_message(message: message) -> str:
    """parses a message instructing dicebot to roll dice and produces the
first whitespace-delimited word, ignoring the rest of the message.

    """
    return message.content.split()[1]


def message_is_roll_commandP(message: message) -> bool:
    """consumes a discord.py message and produces true if it should be
interpreted as a roll command by dicebot, false otherwise

    """
    return message.content.split()[0] == "$roll"


def message_is_help_commandP(message: message) -> bool:
    """consumes a dusord.py message and produces true if it should be
interpreted as a request for help by dicebot, false otherwise.

    """
    return mentions_includes_name(message.mentions, "dicebot")


def mentions_includes_name(mentions: list, name: str) -> bool:
    """consumes a list of mentions from a discord.py message and produces
true if one of the users mentioned has the supplied NAME, false
otherwise.

    """
    return any(map(lambda x: x.name == name, mentions))

def main():

    api_token = get_env_var_checked("DISCORD_API_TOKEN")

    try:
        assert api_token != False
    except:
        exit(1)

    client = discord.Client()

    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message_is_roll_commandP(message):
            result = dice.roll(parse_roll_message(message))
            await message.channel.send(result)

        if message_is_help_commandP(message):
            await message.channel.send(
                """
I understand everything dice.py understands: https://pypi.org/project/dice/
to invoke a roll, write a message where I can see it like this: `$roll 1d6`            
"""
            )

    client.run(api_token)


if __name__ == "__main__":
    main()
