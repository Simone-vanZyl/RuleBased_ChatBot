# A Chatbot for Innovus presentation
from appJar import gui
from time import sleep
import thread
import re

# messages the bot can handle
inputmsgs = ["Hello", #0
             "What is your name?", #1 
             "What is the Mobile Programming Initiative?", #2 
             "How do we get there?", #3
             "Thank you" #4
            ] 
outputmsgs = ["Hi there! I'm Bubble.", #0
              "My name is Bubble", #1
              "", #2
              "Well, ...", #3 
              "Pleasure!", #4
              "Sorry. I don't understand." #last
             ]
# handle button events
def press(button):
    global QandA
    if button == "Ask":
        msg = app.getEntry("question")
        app.setTextArea("txt", msg + "\n", True);
        print(msg)
        thread.start_new_thread(respond, ("tread",msg))

# Generate responses to questions/input
def respond(threadname, msg):
    r = re.compile(".*"+msg.lower()+".*")
    i = 0
    index = [i for i,s in enumerate(inputmsgs) if r.match(s.lower())]
    #if any(r.match(question) for question in inputmsgs):
    print "match:"
    print index
    if (index):
        index = index[0]
        print outputmsgs[index]
        sleep(1)
        app.setTextArea("txt", outputmsgs[index] + "\n", True);
    else:
        s = outputmsgs[len(inputmsgs)]
        sleep(1)
        app.setTextArea("txt", s + "\n", True);


# create a GUI variable called app
app = gui("Bubble", "800x500")
app.setBg("cyan")
app.setFont(12)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Bubble")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "white")

app.addScrolledTextArea("txt")
app.addEntry("question")

# link the buttons to the function called press
app.addButton("Ask", press)
# start the GUI
app.go()
