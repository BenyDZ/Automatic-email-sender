#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     20/01/2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import needed object
import os
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageFont, ImageDraw

def imageWriter(name):
    print(name)
    #open an image, return an object of type PIL.PngImagePlugin.PngImageFile
    im = Image.open("anb1x-anxiety-coffee-lg.jpeg")
    #define a font and the size for the text, return the object freeMono of type PIL.ImageFont.FreeTypeFont
    freeMono = ImageFont.truetype("FreeMono.ttf", size=50)
    #create an ImageDraw object, return an object of type PIL.ImageDraw.ImageDraw
    d = ImageDraw.Draw(im)
    #define the color of the text, return the object text_color of type tuple
    text_color = (250, 250, 000)
    #define the location of the text, return the object location of type tuple
    location = (280, 200)
    #whrite the text, return an object of type NoneType
    d.text(location, "NO COFFEE", font=freeMono, fill=text_color)
    location1 = (300, 250)
    #whrite the text, return an object of type NoneType
    d.text(location1, name+"?", font=freeMono, fill=text_color)
    #save the the new image with the text, return an object of type NoneType
    im.save("drawn_grid.png")

def writeMail(imageName,name):
    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgRoot = MIMEMultipart('related')
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    print(name)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)
    text = "Hi {}".format(name)
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
    fp = open(imageName, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    return msgRoot

def sendEmail(email,msgRoot):
    """
    functions to send an email to all members behind on their dues
    """
    #connect to the server ,return the object server of type smtplib.SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #Identify yourself to an SMTP server, return an object of type tuple
    server.ehlo()
    #Put the SMTP connection in TLS (Transport Layer Security) mode, return an object of type tuple
    server.starttls()
    #connect to the email account, return an object of type tuple
    server.login("patdenzoungany@gmail.com", "bermanpat")
    server.sendmail("patdenzoungany@gmail.com", email, msgRoot.as_string())
    server.quit()

name = input("Enter the name of the client : ")
email = input("Enter the email of the client : ")

imageWriter(name)
msgRoot = writeMail("drawn_grid.png",name)
sendEmail(email,msgRoot)

