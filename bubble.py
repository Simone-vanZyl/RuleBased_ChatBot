# A Chatbot for Innovus presentation
from appJar import gui
from time import sleep
import thread
import re

import pygame
pygame.init()

pygame.mixer.music.load("Pop.mp3")
pygame.mixer.music.play()
#pygame.event.wait()
print "sound played"

# messages the bot can handle
inputmsgs = ["Hello", #0
             "What is your name?", #1 
             "What is the Mobile Programming Initiative?", #2 
             "How do we get there?", #3
             "How do we keep children interested?", #4
             "What about money?" #5
             "Thank you", #6
             "How are you" #7
            ] 

# bad intentation but good output
outputmsgs = ["* Hi there! I'm Bubble.", #0
              "* My name is Bubble", #1
              "* The Mobile Programming Initiative aims to teach children to program.", #2
              "* Well, the first step was comming to Innovus. Well done!\
              \n* You should consider doing a pilot study. \n* You will also\
 need to approach potential investors or sponsors.\n* Consider\
 offering a holiday program to streamline the teaching material.", #3
              "* Children enjoy interactive learning experiences most, consider\
 a tangible result. \n* Rewards like treats and certificates will motivate\
 them.\n* Also consider having brainpower snacks available", #4
              "* A holiday program will be a great way to produce profit.\
\n* However to become a Non-Profit Organisation you will have to consult with\
 large organisations for sponsorships as well as host fundraising\
 opportunities", #5
              "* Pleasure!", #6
              "* I am feeling bubbly today", #7
              "* Sorry. I don't understand." #last
             ]
# handle button events
def press(button):
    global QandA
    if button == "Ask":
        msg = app.getEntry("question")
        app.setTextArea("txt", msg + "\n", True)
        print(msg)
        thread.start_new_thread(respond, ("tread",msg))

# Generate responses to questions/input
def respond(threadname, msg):
    r = re.compile(".*"+msg.lower()+".*")
    i = 0
    index = [i for i,s in enumerate(inputmsgs) if r.match(s.lower())]
    if any(r.match(question) for question in inputmsgs):
        print question
    print "match:"
    print index
    if (index):
        index = index[0]
        changed = False

        # look confused when asked 'how do we get there'
        if (index == 3) :
            app.setImage("simple", "bluethink.png")
            changed = True
            sleep(1)
        sleep(1)

        # add the message to the text area
        app.setTextArea("txt", outputmsgs[index] + "\n", True);
        
        # change expression back to a smile
        if (changed):
            app.setImage("simple", "bluehappy.png")

        # Makes the text area sroll to the end.
        txtArea.yview_pickplace("end")
        txtArea.see("end")
    else:
        # Bubble doesn't understand
        app.setImage("simple", "blueconfused.png")
        s = outputmsgs[len(inputmsgs)]
        sleep(2)
        app.setTextArea("txt", s + "\n", True);
        app.setImage("simple", "bluehappy.png")


# create a GUI variable called app
app = gui("Bubble", "800x700")
app.setBg("DodgerBlue")
app.setFont(12)

# add & configure widgets - widgets get a name, to help referencing them later
app.startLabelFrame("Bubble", 0, 0)
app.addImage("simple", "bluehappy.png")
app.stopLabelFrame()

txtArea = app.addScrolledTextArea("txt")
app.setScrolledTextAreaFg("txt", "red")
app.addEntry("question")

# link the buttons to the function called press
app.addButton("Ask", press)
# start the GUI
app.go()
