from appJar import gui
import requests

app = gui("Email App")
app.addLabel("title", "Hello")
app.setLabelBg("title", "#0a284f")
app.addLabelEntry("Email text")

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        emailText = app.getEntry("Email text")

app.addButtons(["Submit", "Cancel"], press)

def sendEmail():
    response = requests.post(
		"https://api.mailgun.net/v3/customer-service.sercbot.com/messages",
		auth=("api", "7f4907c825d6e95145364d1298e031b3-100b5c8d-c8853f0e"),
		data={"from": "SERC-BOT <password-reset@customer-service.sercbot.com>",
		"to": "",
		"subject": "password reset | SERC-BOT",
		"text": "Here's your password reset code: "})
    data = response.text
    print(data)


app.go()