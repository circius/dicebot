## summary

This is a discord bot that's a thin wrapper around
[dice](https://pypi.org/project/dice/). It can be addressed in a
discord channel with a string that dice-notation can parse as dice and
will reply with a result.

## functionality

``` shell
user: $roll 3d6
dicebot: [1, 5, 1]
user: $roll 3d6t
dicebot: 10
user: $roll 1d6e3 # 1d6 > 3 ?
dicebot: 1
user: $roll 1d6e3 # 1d6 > 3 ?
dicebot: 0
```

For a full list of functionality refer to the dice
[readme](https://github.com/borntyping/python-dice)

## configuration

dicebot depends on the environment variable DISCORD_API_KEY being
properly set. For guidance on how to get an API key for a discord bot,
see [here](https://discordpy.readthedocs.io/en/latest/discord.html).

## usage

first, set the environment variable in some shell

``` shell
$ export DISCORD_API_KEY={your-key-here}
# of course you can put this in your .bashrc (or equivalent) for persistence
```
then do one of 

``` shell
# in the root of the repository:
$ pip install -e ./
# then, system-wide:
$ dicebot
```

or 

``` shell
# in the root of the repository:
$ python3 src/dicebot/daemon.py
```

or

``` shell
# in the root of the repository
$ docker image build -t dicebot ./
$ docker run dicebot
```
