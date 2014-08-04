尝试Test to speak
=================
JunJian from 2014.08.04

使用一套统一的wrapper
--------------------
>   pyttsx

感谢源码: https://github.com/parente/pyttsx.git

>   wrapper的依赖

nsss - NSSpeechSynthesizer on Mac OS X 10.5 and higher
sapi5 - SAPI5 on Windows XP, Windows Vista, and (untested) Windows 7
espeak - eSpeak on any distro / platform that can host the shared library

>   ubuntu上安装

sudo apt-get install espeak

>   使用实例

'''
import pyttsx
engine = pyttsx.init()
engine.say('Greetings!')
engine.say('How are you today?')
engine.runAndWait()
'''

>   api文档

http://pyttsx.readthedocs.org/
