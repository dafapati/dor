# -*- coding: utf-8 -*-
import os
import sys
import time    
import platform
from xlpy import *


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

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0 / 90)

def main_menu():
    clear()
    
    print(
       u+ "           ..::Daftar Menu Tool Tembak XL::.." +
        "\n\nSilakan pilih menu yang ingin Anda mulai:"
        "\n[1] Purchase Package" + 
        "\n[2] Request OTP Code" +
        "\n[3] Menu utama"  
        
    )
    choice = str(input(" >> "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    print("              ..::Menu Tembak::..")
    print ("")
    msisdn = str(input("Masukan No Dengan Awalan 628xx >> "))
    po = str(input("Masukan OTP >> "))
    print (" 1) Xtra Kuota 30GB Rp. 10.000")
    print (" 2) Xtra Combo Lite 25GB, 30hr, 99.900")
    print (" 3) Xtra Combo Lite 17GB, 30hr, 79.900")
    print (" 4) Xtra Combo Lite 9GB, 30hr, 49.900")
    print (" 5) Xtra Combo Lite 5GB, 30hr, 29.900")
    print (" 6) Xtra Combo Lite 3GB, 30hr, 19.900")
    print (" 7) Combo Xtra 5GB + 5GB Rp. 59.000")
    print (" 8) Combo Xtra 10GB + 10GB Rp. 89.000")
    print (" 9) Combo Xtra 15GB + 15GB Rp. 129.000")
    print (" 10) HOTROD 24Jam 1.5GB Rp. 25.000")
    print (" 11) HOTROD 24Jam 3GB Rp. 30.000")
    print (" 12) HOTROD 24Jam 6GB Rp. 50.000")
    print (" 13) Super Ngebut 5,5GB")
    print (" 14) Super Ngebut 2,2GB") 
    go = str(input("Pilih Sesuai Keinginan >> "))
    if go == '1':
        c = "8110577"
    elif go == '2':
        c ="8210886"
    elif go == '3':
        c = "8210885"
    elif go == '4':
    	 c = "8210884"
    elif go == '5':
    	  c = "8210883"
    elif go == '6':
    	 c = "8210883"
    elif go == '7':
        c = "8211183"
    elif go == '8':
        c = "8211184"
    elif go == '9':
        c = "8211185"
    elif go == '10':
        c = "8211107"
    elif go == '11':
        c = "8211108"
    elif go == '12':
        c = "8211109"
    elif go == '13':
        c = "3210257"
    elif go == '14':
        c = "3210256"
    else:
        print("Pilihan salah !!!")
        time.sleep(2)
        menu_actions['1']()
    serviceid = c
    xl = XL(msisdn)
    r = xl.loginWithOTP(po)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
        decision = str(input("Ingin mengulangi prosesnya [Y/N]? >> "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
    else:
        print("Login failed try again")
        decision = str(input("Ingin mengulangi prosesnya [Y/N]? >> "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
    return
        
def menu_2():
    clear()
    print("⏩Minta Kode Otp⏪")
    msisdn = str(input("Masukan Nomor👉"))
    xl = XL(msisdn)
    print(xl.reqOTP()['message'])
    decision = str(input("Ulangi Proses[Y/N]? 👉 "))
    menu_actions['main']() if(decision in ['N','n']) else menu_2()

def menu_3():
     slowprint("loading")
     os.system('cd ..;python app.py')
   
    
def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
