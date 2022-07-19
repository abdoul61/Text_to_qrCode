import pyqrcode
import png
from pyqrcode import QRCode

s = input("Enter words or document to transcode : ")

# Here we create the qrcode

qr = pyqrcode.create(s)

# Here is the creation of the png or svg

tp = input("Enter p if you would like to have it in png or s for svg : ")

if tp == 's':
	qr.svg("myQr.svg",scale=8)
elif tp == 'p':
	qr.png("myQr.png",scale=6)
else:
	Print("You enter a wrong format")



