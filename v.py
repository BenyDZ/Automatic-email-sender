#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      user
#
# Created:     20/01/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Define these once; use them twice!
strFrom = 'patdenzoungany@gmail.com'
strTo = 'patdenzoungany@gmail.com'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)
text = "HI beny"
text1 = "I hate being a pest, but it seems I'm destined to imitate one :-)"
text2 = "Just wanted to see if my offer of coffee and a catch-up made it through your bulging inbox?"
text3 = "If you've 30mins it'd be lovely to just hear what's new for you with life and work."
text4 = "Let me know or just book in a time that suits."
text5 = "Kindest"
text6 = "Beny"

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('{}<br> <img src="cid:image1"><br><br>{}<br>{}<br>{}<br>{}<br><br><br>{}<br><br><br>{}'.format(text,text1,text2,text3,text4,text5,text6), 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('anb1x-anxiety-coffee-lg.jpeg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
#connect to the server ,return the object server of type smtplib.SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
#Identify yourself to an SMTP server, return an object of type tuple
server.ehlo()
#Put the SMTP connection in TLS (Transport Layer Security) mode, return an object of type tuple
server.starttls()
#connect to the email account, return an object of type tuple
server.login("patdenzoungany@gmail.com", "bermanpat")

server.sendmail("patdenzoungany@gmail.com", "patdenzoungany@gmail.com", msgRoot.as_string())
server.quit()