## summary

This is a discord bot that's a thin wrapper around
[dice](https://pypi.org/project/dice/). It can be addressed in a
discord channel with a string that dice-notation can parse as dice and
will reply with a result.

## functionality

` user: $roll 3d6
  dicebot: [1, 5, 1]
  user: $roll 3d6t
  dicebot: 10
  user: $roll 1d6e3 # 1d6 > 3 ?
  dicebot: 1
  user: $roll 1d6e3 # 1d6 > 3 ?
  dicebot: 0
`

For a full list of functionality refer to the dice
[readme](https://github.com/borntyping/python-dice)

## configuration

dicebot depends on the environment variable DISCORD_API_KEY being
properly set. For guidance on how to get an API key for a discord bot,
see [here](https://discordpy.readthedocs.io/en/latest/discord.html).

## usage

``` shell
$ dicebot
```

