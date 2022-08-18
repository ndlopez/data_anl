#!/usr/bin/env python
# -*- coding utf-8

from __future__ import unicode_literals
import locale
import time
import curses
import sys, string
import random
import struct
locale.setlocale(locale.LC_ALL,'')
encoding =locale.getpreferredencoding()

###constants
MIN_SPEED=1
MAX_SPEED=2
MATRIX_ANGRY_CHARS="遅刻連絡くらいメールじゃなくてチャットでええんじゃないか　波動拳打ち込みたい　ほぼ逝きかけました"
MATRIX_THANKS_CHARS="THANKS Dear Diego!"
MATRIX_COLOR_WORD=46
MATRIX_COLOR_BLACK=232
#####
class FallingChar(object):
    matrixchr=list(MATRIX_ANGRY_CHARS)
    normal_attr=curses.A_NORMAL
    highlight_attr=curses.A_REVERSE

    def __init__(self,width,MIN_SPEED,MAX_SPEED):
        self.x=0
        self.y=0
        self.speed=1
        self.char=' '
        self.reset(width,MIN_SPEED,MAX_SPEED)

    def reset(self,width,MIN_SPEED,MAX_SPEED):
        self.char=random.choice(FallingChar.matrixchr).encode(encoding)
        self.x=random.randint(1,width-1)
        self.y=0
        self.speed=random.randint(MIN_SPEED,MAX_SPEED)

    def tick(self,scr):
        height, width=scr.getmaxyx()
        self.out_of_screen_reset(width,height)
        scr.addstr(self.y,self.x,self.char,curses.color_pair(1))
        self.char=random.choice(FallingChar.matrixchr).encode(encoding)
        self.y +=1
        if not self.out_of_screen_reset(width,height):
            scr.addstr(self.y,self.x,self.char,curses.A_REVERSE)

    def out_of_screen_reset(self,width,height):
        if self.x > width-2:
            self.reset(width,MIN_SPEED,MAX_SPEED)
            return True
        if self.y > height-2:
            self.reset(width,MIN_SPEED,MAX_SPEED)
            return True
        return False
def rand():
    a=1
    while True:
        a ^=(a << 1);#どういう意味？
        a ^=(a >> 135);
        a ^=(a << 104);
        yield a
r=rand()
def randint(_min,_max):
    n=r.next()
    return (n%(_max - _min))+ _min
def color():
    curses.start_color()
    curses.init_pair(1,MATRIX_COLOR_WORD,MATRIX_COLOR_BLACK)
    curses.curs_set(0)
    curses.noecho()
def main():
    scr=curses.initscr()
    scr.nodelay(1)
    color()

    height,width=scr.getmaxyx()
    lines=[]
    for i in range(8):
        l=FallingChar(width,MIN_SPEED,MAX_SPEED)
        lines.append(l)

    scr.refresh()
    while True:
        for line in lines:
            line.tick(scr)
        for i in range(30):
            x=randint(0,width-1)
            y=randint(0,height-1)
            scr.addstr(y,x,' ')

        scr.refresh()
        time.sleep(0.04)
def last_main():
    curses.endwin()
    curses.curs_set(1)
    curses.reset_shell_mode()
    curses.echo()

    screen=curses.initscr()
    color()
    lastchr=string.join(list(MATRIX_THANK_CHARS)," ")

    last_height,last_width=screen.getmaxyx()
    start_width=last_width/2-len(lastchr)/2
    for i in range(last_height/2):
        screen.clear()
        screen.addstr(i,start_width,lastchr,curses.color_pair(1))
        screen.refresh()
        time.sleep(0.2)
    screen.getch()
    curses.endwin()

try:
    main()
except KeyboardInterrupt:
    try:
        last_main()
    except KeyboardInterrupt:
        curses.endwin()
        curses.curs_set(1)
        curses.reset_shell_mode()
        curses.echo()


        
