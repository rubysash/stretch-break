#!/usr/bin/python3

"""
DESCRIPTION:
Simple screen saver/eye strain protection program to help me prevent headaches
And Back pain problems from not moving all day doing IT work
"""

import pygame	# pygame basics
import pygame.locals	# so I type just quit
import pygame.freetype	# pygame fonts
import sys		# for a proper exit and os detection
import json		# to read/write json
import random	# to pick a random work from our list
import textwrap	# to wrap text automagically
import os 		# so we can find the json files

# Determine the directory this script is in
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to verses.json relative to the script's directory
verses_path = os.path.join(script_directory, 'verses.json')

# it's setup for linux by default
if sys.platform == 'linux':
	print("Linux Detected")
elif sys.platform == 'Win32':
	# hide the stupid console window:
	# note: it will close the dos prompt you test from too
	print("Windows Detected")
	import win32gui
	import win32.lib.win32con as win32con
	the_program_to_hide = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
else:
	print("Unknown OS (darwin/other)")
	pygame.quit()
	sys.exit()


# slurps up the json file into memory as a dict, create blank dict
verses = {}
# Use the constructed path when opening the file
with open(verses_path, 'r') as infile:
    verses = json.load(infile)

"""
gets random verse
Demonstrates json, and definitions
returns a random item from words.json
"""
def get_random_verse():
	# get the verses, then rebuild
	keys = list(verses.keys())

	# just return desired choice
	return(random.choice(keys))

"""
wraps text at x chars
puts into a returned list
"""
def wrap_tex(value):
	wrapper = textwrap.TextWrapper(width=45)
	word_list = wrapper.wrap(text=value)
	return(word_list)


# pythonic way is to call a main, in main namespace
def main():

	# what is our current word?  
	verse = get_random_verse()
	verse_cat = verses[verse][0]
	verse_txt = wrap_tex(verses[verse][1])

	# have to init the module
	pygame.init()

	# anyway, create a "screen" that we'll draw on later
	screen = pygame.display.set_mode((1152, 864),0,24)

	# SysFont works without including the font file
	# but it must exist:  print(pygame.font.get_fonts())
	GFONT = pygame.font.SysFont('arial',48)
	IFONT = pygame.font.SysFont('arial',48, italic=True)

	# create clock/timer object
	clock = pygame.time.Clock()

	# and set our alternate timer so we know when to stop
	# using 255 "ticks" so it can tick the RGB values (R,G,B are from 0-255)
	timer = 255

	# rest for 10 fps * 1s (300 = 30s)
	rest = 1

	# loop until event says to stop
	running = True
	while running:

		# pygame processes events like keys, group them all here
		for event in pygame.event.get():
			
			# if it is somehow told to "quit", do it
			if event.type == pygame.QUIT:
				running = False

			# check our keystrokes
			if event.type == pygame.KEYDOWN:
				
				# if we hit the escape key, "quit" too.
				if event.key == pygame.K_ESCAPE:
					running = False

		# update our timer outside of the event loop
		# this will tick once everytime our FPS ticks by decrementing
		timer -= 1

		# until it hits our rest counter
		# so it really goes 255,254,253 down to "rest" (40)
		# and we are using "timer" as a left margin so it knows where to stop
		# otherwise it would scroll too far left and look weird.  
		# margins are nicer
		if timer < rest:
			running = False

		 # black screen
		screen.fill((0,0,0))
		
		# this is the blue word at the top, the category
		# rendering first so red word overwrites
		# the category  portion fades from blue to green
		# here are using timer to change the color
		cat_surf = GFONT.render(verse_cat, True, (0, 128, timer))
		
		# blit does the actual draw onto "screen" object
		screen.blit(cat_surf, (40, 50))

		# this is the red verse that scrolls from right side on timer countdown
		verse_surf = GFONT.render(verse,  True, (204, 0, 0))

		# here we are using timer to change the x position 
		screen.blit(verse_surf, (timer, 150))

		# these are the verse lines from a list thanks to wordwrap module
		vertical = 250
		
		# using textwrap to break verse into lines, then adding some size to vertical on loop
		for line in verse_txt:
			# the "verse line" is in white text (255,255,255)
			line_surf = IFONT.render(line,  True, (255, 255, 255))
			screen.blit(line_surf, (40, vertical))
			vertical += 50

		# update screen    
		pygame.display.flip()

		# set to whatever fps.
		# as it's a rest, no movement, don't need to burn cpu cycles with fast fps
		# 255 on the timer, ticking down 10 per sec, until it hits 40
		# 255-1 10x a second until it hits 40 = 21 seconds approximately
		clock.tick(10)
 

if __name__ == '__main__':
	main()
	
	# the proper way to quit pygame is to do both pygame.quit
	pygame.quit()
	
	# AND sys.exit
	sys.exit()
