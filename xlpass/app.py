# -*- coding: utf-8 -*-
#Ini Import
import os
import sys
import time
import base64
#kode warna
g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"
#sebelum mulai harus ini
try:
    import platform
    from xlpy import *
except Exception as err:
    os.system('pip install --upgrade pip')
    os.system('pip install requests')
    os.system('pip install -r requirements.txt')
    os.system('python app.py')()
except KeyboardInterrupt:
	  print (m+"[" + p + "Fail To Import" + m + "]")
	  sys.exit()
#Otak Santai Print
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0 / 90)
#Menu awal
def menu_1():
try:
        clear()
        slowprint(g+"Minta Password Dulu!")
        print ("")
        msisdn = str(input(gt+"Masukan Nomor Xl 62XX >> "+p))
        xl = XL(msisdn)
        print(xl.reqPassword()['message'])
        print (gt+"___________________________________________________________")
        decision = str(input("Mau Lanjut Nembak  [Y/N]? >> "))
        menu_actions['2']() if(decision in ['N','n']) else menu_actions['1']()
#Menu Beli Paket
def menu_2():
    try:
        print(g+"Menu Beli Paketnya")
        print ("")
        msisdn = str(input(gt+"Input your MSISDN >> "+p))
        passwd = str(input(gt+"Input your password >> "+p))
        print (g+"              ..::List Menu Tembak Paket Xl::..") 
        print (p+" 01"+gt+") "+p+"Paket Xtra Kuota 30GB Rp. 10.000")
        print (p+" 02"+gt+") "+p+"XL GO IZI 10 GB Rp. 0")
        print (p+" 03"+gt+") "+p+"xtra 3GB Rp. 22.900")
        beli = str(input(gt+"Select one >> "+p))
        if beli == '1' or beli == '01':
            c = b'\xff\xfe8\x001\x001\x000\x005\x007\x007\x00'
        if beli == '2' or beli == '02':
            c = b'\xff\xfe8\x002\x001\x001\x002\x003\x001\x00'
        serviceid = c.decode('utf-16')
        xl = XL(msisdn)
        r = xl.loginWithPassword(passwd)
        if(r != False):
            print(xl.purchasePackage(serviceid)['message'])
        decision = str(input("Ingin mengulangi prosesnya [Y/N]? >> "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['0']()
        
def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

def main_menu():
    try:
        clear()

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "0" : exit
}

if __name__ == "__main__":
    main_menu()
