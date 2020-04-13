FROM python:slim

WORKDIR dicebot/

ADD ./ ./

RUN pip install -e ./

CMD dicebot
       
