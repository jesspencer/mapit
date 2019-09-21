#! /usr/bin/env python3
#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard


import webbrowser
import sys
import pyperclip

#webbrowser.open("https://google.com/maps/place/ 600b H St NE Washington, DC 20002/")

if len(sys.argv) > 1:
    # Get address from commandline
    address = ''.join (sys.argv[1:])
else:
    # Get addrss from cipboard
    address = pyperclip.paste()

webbrowser.open('https://google.com/maps/place/' + address )
#TOO: Get address from cipboard
