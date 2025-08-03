import qrcode
from PIL import Image
def genqr():
    data=input("Enter the data to be encrypted in QR code: ")
    img= qrcode.make(data)
    name=input("Enter the name of the qr to save as: ")
    img.save(name + ".png")
    print("Your QR is saved in the folder!")
genqr()
while True:
    ans=input("Do you want to generate another QR code? (y/n): ")
    if ans=='y':
        genqr()
    else:
        break
