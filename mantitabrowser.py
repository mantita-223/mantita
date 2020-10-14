#! /Users/hobbits/miniconda3/envs/HELLO_WORLD/bin/python

# -*- coding: UTF-8 -*-

from tkinter import *
from tkinterhtml import HtmlFrame
import urllib.request, time
import browserhelper


bkdict = {}

def bookmark_site():
	btnurl = entry.get()
	bkname = browserhelper.enterbox("Name your bookmark.", "Name the bookmark")
	def gotobk():
		
		def get_key(val):
			for key, value in bkdict.items(): 
				if val == value: 
					return key 
             		
        
		bk_var = get_key(bkname)
		frame.set_content(urllib.request.urlopen(get_key(bkname)).read().decode())
		theurl.set(bk_var)
	
	bkdict[btnurl] = bkname
	thebutton = Button(bookmarks_bar, height=2, text=bkdict[btnurl], command=gotobk)
	thebutton.pack(side="left")
	bkbutton['text'] = "✭︎"
	time.sleep(1)
	bkbutton['text'] = "✩"

def go():
	try:
		cururl = entry.get()
		frame.set_content(urllib.request.urlopen(cururl).read().decode())
	except:
		frame.set_content("<h1>404: Page not found</h1><br><br><h3>The page you were looking for was not found. Make sure you entered the URL correctly.</h3>")
			
			

browser_window = Tk()

browser_window.title('Mantita Browser') # the title
control_frame = Frame(browser_window) # the control frame
label = Label(control_frame, text= 'URL:') # the label
frame = HtmlFrame(browser_window, horizontal_scrollbar="auto") # the website box

theurl = StringVar(control_frame) # the variable
entry = Entry(control_frame, textvariable=theurl) # the url enter box

entry.insert(END, "http://info.cern.ch/hypertext/WWW/TheProject.html") # the default URL
button = Button(control_frame, height=2, text='Go', command = go)
bkbutton = Button(control_frame, height=2, text='✩', command = bookmark_site)


bookmarks_bar = Frame(browser_window) # BOOKMARKS Bar


control_frame.grid(column=1, row=1) # frame contains all the controls and stuff
bookmarks_bar.grid(column=1,row=2)
label.grid(column=1, row=1)
entry.grid(column=2, row=1, ipadx=130, ipady=5)
button.grid(column=3, row=1)
bkbutton.grid(column=4, row=1)
frame.grid(column=1, row = 3, sticky="ew", padx=0, pady=0)

go() # loads site automatically

browser_window.mainloop()