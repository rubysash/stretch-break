
"""
DESCRIPTION:
Simple screen saver/eye strain protection program to help me prevent headaches
And Back pain problems from not moving all day doing IT work

INSTRUCTIONS:
1. install the modules you need with 'pip install somemodule'
2. edit your words.json file, it must be valid json
3. save this script as stretch-break.py
4. create a .bat file with 1 line in it:  python eyerest2.py
5. copy font file into same location you save this file (arial.ttf)
6. test it:  python eyerest2.py, if it works great, else figure out why
7. Schedule task in windows task scheduler to run as you see fit.


for example, my "action" on my task is:
    C:\tools\rest.bat

The "start in" is:
    C:\tools\

Because that's where I saved the .json file, the .ttf file, the .bat and the .py files

"""



import pygame                 # pygame basics
import pygame.freetype        # pygame fonts
import sys                    # for a proper exit
import json                   # to read/write json
import random                 # to pick a random work from our list

# hide the stupid console window:
#pip install pywin32
# pythonw didn't work
import win32gui
import win32.lib.win32con as win32con
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)



"""
get_beast_mode():
	gets random word
	Demonstrates json, and definitions
	returns a random item from words.json
"""
def get_beast_mode():
    # open JSON file for reading
    data=[]
    with open('words.json', 'r') as infile:
        # put it into a dictionary called "data"
        data = json.load(infile)

    # just return desired choice
    return random.choice(data)



# pythonic way is to call a main, in main namespace
def main():

    # what is our current word?  
    beastmode = get_beast_mode()

    # have to init the module
    pygame.init()

    # setting screen to full screen takeover
    WSIZE = ( 0,0 )
    screen = pygame.display.set_mode(WSIZE)

    # create font object, requires the font to be in same directory
    GFONT = pygame.freetype.Font('arial.ttf',48)

    # create clock/timer object
    clock = pygame.time.Clock()

    # and set our alternate timer so we know when to stop
    timer = 0

    # rest for 10 fps * 1s (300 = 30s)
    rest = 300

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
        timer += 1

        # until it hits our rest counter
        if timer > rest:
            running = False

         # black screen
        screen.fill((0,0,0))
        
        # `render` and then blit the text surface ...
        text_surface, rect = GFONT.render(random_word, (255, 0, 0))
        screen.blit(text_surface, (40, timer))

        # or just `render_to` the target surface.
        GFONT.render_to(screen, (40, 300), random_word, (255, 255, 255))    

        # update screen    
        pygame.display.flip()

        # set to whatever fps.
        # as it's a rest, no movement, don't need to burn cpu cycles with fast fps
        clock.tick(10)
 

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()