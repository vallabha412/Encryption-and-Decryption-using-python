from cryptography.fernet import Fernet as ft
from PIL import Image
import pyqrcode
from pyzbar.pyzbar import decode

key = ft.generate_key()
def data_input():
    name = input('Enter Name : ')
    mobile = input('Enter Mobile No. : ')
    aadhar = input('Enter Aadhar No. : ')
    message = name + ' ' + mobile + ' ' + aadhar
    return message

def data_encryption():
    message = data_input()
    try:
        encrypted_message = ft(key).encrypt(bytes(message,'utf-8'))
    except exception:
        print("Unable to encrypt the Message")
    print("Encrypted Message : \n ",encrypted_message)
    return encrypted_message


def QR_generation():
    encrypted_message = data_encryption()
    try:
        qr = pyqrcode.create(encrypted_message)
    except exception:
         print('Unable to generate QR code')
    return qr

def saving_QR():
    qr = QR_generation()
    try:
        qr.png('x.png',scale=6)
    except exception:
         print('Unable to Save QR')
    qr.show()

def QR_decode_and_decryption():
    img = Image.open('x.png')
    try:
        result = decode(img)
        
    except exception:
         print('Unable to decode QR')

    for i in result:
        a = i.data.decode()
        print('Decoded Message : \n ',a)
        dec = ft(key).decrypt(bytes(a,'utf-8'))
        dec=dec.decode('utf-8')
        dec = dec.split()
        print('Decrypted Message')
        print('name : ',dec[0])
        print('mobile : ',dec[1])
        print('AAdhar : ',dec[2])
        
if __name__ == "__main__":
    
    saving_QR()
    QR_decode_and_decryption()
