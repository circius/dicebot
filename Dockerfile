FROM python:slim

ADD /src/dicebot dicebot/

CMD python3 dicebot/daemon.py
