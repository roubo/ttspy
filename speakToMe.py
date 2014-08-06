#!/usr/bin/env python
# encoding: utf-8
"""
Make it speak to me
"""
import pyttsx
import os

def speakToMe(what, **justwith):
    """
    speak to me about something with some special
    justwith key:
        "speed": "slow","medium","fast"
        "faster": number type (1-10)
        "volume": "low", "medium","loud"
        "louder": number type(0.01-0.1)
    """
    defspeed={"slow":1,"medium":80,"fast":210}
    defvolume={"low":0.3,"medium":0.5,"loud":1}
    engine = pyttsx.init()
    if justwith == None :
        # Just say out
        engine.say(what)
    else:
        if justwith['speed'] != None:
            engine.setProperty('rate',defspeed[justwith['speed']])
        if justwith['volume']!= None:
            engine.setProperty('volume', defvolume[justwith['volume']])
        if justwith['faster'] != None:
            if isinstance(justwith['faster'], int):
                sp = engine.getProperty('rate')
                engine.setProperty('rate',sp+justwith['faster'])
        if justwith['louder'] != None:
            if isinstance(justwith['louder'], float):
                vo = engine.getProperty('volume')
                engine.setProperty('volume',vo+justwith['louder'])
        engine.say(what)
        engine.runAndWait()

if __name__ == '__main__':
    speakToMe("Hi, everyone.  \
               My name is Harold, and I am from ShangHai China.\
               Nice to talk to you"\
              ,speed="slow",volume="loud",faster=0,louder=0)
