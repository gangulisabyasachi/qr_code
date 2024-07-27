import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/watch?v=Kpc0ZJbs5Ro&list=RDKpc0ZJbs5Ro&start_radio=1"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("d:/code/projects/qrcode/qrcode.svg", scale = 8) 