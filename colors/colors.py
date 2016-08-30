#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-13 23:48:50
# @Last Modified by:   john
# @Last Modified time: 2016-08-14 00:27:41


from colorama import *

# These are meant to be shorthand function calls to quickly turn a string
# into something with color. 

def G(string): return Fore.GREEN + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def g(string): return Fore.GREEN + string + Fore.RESET
def B(string): return Fore.BLUE + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def b(string): return Fore.BLUE + string + Fore.RESET
def R(string): return Fore.RED + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def r(string): return Fore.RED + string + Fore.RESET
def Y(string): return Fore.YELLOW + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def y(string): return Fore.YELLOW + string + Fore.RESET
def M(string): return Fore.MAGENTA + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def m(string): return Fore.MAGENTA + string + Fore.RESET
def C(string): return Fore.CYAN + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def c(string): return Fore.CYAN + string + Fore.RESET
def W(string): return Fore.WHITE + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def w(string): return Fore.WHITE + string + Fore.RESET 
