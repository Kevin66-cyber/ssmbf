#!/usr/bin/python3
import re
import os
import sys
import shutil
import requests
from lib import Main
from getpass import getpass
from usr import login,banner,start
def menu():
    os.system("clear")
    banner.banner()
    banner.menu()
    print()
    zet = input("\nPilih •• ")
    if zet == '':
        menu()
    elif zet == '1':
        fr = run.parser.get("/me").find_all("a",string="Teman")
        for x in fr:
            if "friends/center" in x["href"]:
                continue
            else:
                users = run.friendlist(x["href"])
                print()
                start.sorting(users)
    elif zet == "2":
        url = input("\nLing Postingan •• ")
        if "https://www.facebook.com" in url:
            url = url.replace("https://www.facebook.com",'')
        elif "https://m.facebook.com" in url:
            url = url.replace("https://m.facebook.com",'')
        elif "https://mbasic.facebook.com" in url:
            url = url.replace("https://mbasic.facebook.com",'')
        else:
            exit("Ling Error")
        like = run.parser.get(url)
        try:
            react = re.findall('href="(/ufi.*?)"',str(like))[0]
        except IndexError:
            exit("#Error")
        users = run.likes(react)
        print()
        start.sorting(users)
    elif zet =="3":
        username = run.bysearch("/search/people/?q=" + input("\nNama Yang Kamu Mau •• "))
        print()
        start.sorting(username)
    elif zet == '4':
        grub = input("\nID Grup •• ")
        users = run.fromGrub("/browse/group/members/?id=" + grub)
        print()
        if len(users) == 0:
            exit("# wrong Id")
        start.sorting(users)
    elif zet == '5':
        zet = input("\n ID/Username •• ")
        if zet.isdigit():
            user = "/profile.php?id=" + zet
        else:
            user = "/" + zet
        try:
            user = run.parser.get(user).find('a',string="Teman")["href"]
            username = run.friendlist(user)
            start.sorting(username)
        except TypeError:
            exit("# user not found ")
    elif zet == '6':
        query = input("\n Tag •• ")
        username = run.hashtag("/hashtag/"+query)
        print()
        if len(username) == 0:
            exit("\nGak ada")
        start.sorting(username)
    elif zet == '7':
        r = open("results-check.txt").read().strip()
        c = open("results-life.txt").read().strip()
        res = r + c
        final = set(res.split("\n"))
        print(f"• {str(len(final))} accounts to check")
        start.sorting(final,True)
    else:
        exit("Salah")
def cek():
    os.system('clear')
    banner.banner()
    print()
    print("\t       ╦    ╔═╗  ╔═╗  ╦  ╔╗╔\n\t       ║    ║ ║  ║ ╦  ║  ║║║\n\t       ╩═╝  ╚═╝  ╚═╝  ╩  ╝╚╝\n")
    cookie = input("\n Cookies •• ")
    if login.val(host, cookie):
        with open("usr/cookies","w") as f:
            f.write(cookie)
        return cookie
    else:
        getpass("Cookies Error")
        cek()
def main():
    try:
        cookies = open("usr/cookies").read()
        if login.val(host, cookies):
            return cookies
        else:
            os.remove("usr/cookies")
            exit("Sesi Mati")
    except FileNotFoundError:
        return cek()
if "__main__" == __name__:
    try:
        os.system('clear')
        banner.banner()
        try:
            shutil.rmtree("usr/__pycache__")
            shutil.rmtree("lib/__pycache__")
            shutil.rmtree("./__pycache__")
        except FileNotFoundError:
            pass
        if len(sys.argv) == 2:
            if sys.argv[1] == 'free':
                host = "https://free.facebook.com{}"
            else:
                print("# Usage")
                exit("# Use <python3 mbf.py free> for free data")
        else:
            os.system("git pull")
            host = "https://mbasic.facebook.com{}"
        kuki = main()
        run = Main(kuki)
        menu()
    except requests.exceptions.ConnectionError:
        exit("# bad connection")
    except (KeyboardInterrupt,EOFError):
        exit("# Exit")
