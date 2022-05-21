from appJar import gui
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = gui("Email App", "1280x720")
app.setBg("#107373")
app.setFont(20)
app.addLabel("title", "Hello")
app.setLabelBg("title", "#0a284f")
app.addLabelEntry("Name of the receiver")
app.addLabelEntry("Email of the receiver")
app.addLabelEntry("Title of message")
app.addLabelEntry("Message")
app.setFocus("Message")

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        name = app.getEntry("Name of the receiver")
        email = app.getEntry("Email of the receiver")
        title = app.getEntry("Title of message")
        emailText = app.getEntry("Message")
        sendEmail(name, email, title, emailText)


app.addButtons(["Submit", "Cancel"], press)

def sendEmail(receiverName, receiverEmail, title, text):
    response = requests.post(
		"https://api.mailgun.net/v3/sandbox17d13d9dd0d748a5b06e1727acc4213e.mailgun.org/messages",
		auth=("api", os.getenv("MAILGUN_KEY")),
		data={"from": "Mailgun Sandbox <postmaster@sandbox17d13d9dd0d748a5b06e1727acc4213e.mailgun.org>",
			"to": receiverName + " <" + receiverEmail + ">",
			"subject": "Hello Ernesto Lopez -2",
			"html": '<h1 style="background-color: #ad213a; color: #ffff;">' + title + '</h1><p style="background-color: #0a284f; color: #fff">' + text + "</p>"})
    data = response.text
    print(os.environ.get("MAILGUN_KEY"))
    print(data)


app.go()