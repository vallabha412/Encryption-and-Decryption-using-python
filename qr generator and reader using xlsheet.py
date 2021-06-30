from cryptography.fernet import Fernet as ft
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import pandas as pd

key = ft.generate_key()

df = pd.read_excel('qr.xlsx')

print(df.head(),end='\n\n\n\n')
def encryption_and_decryption():
     for index, values in df.iterrows():
          name = values['name']
          mobile = values['mobile']
          age = values['age']
          ID = values['ID']

          data = f'''
          name: {name}
          mobile: {mobile}
          age: {age}
          ID: {ID}
          '''
          # Encrypting the Data
          encrypted_message = ft(key).encrypt(bytes(data,'utf-8'))
          #print('Encrypted Text : ',encrypted_msg)
     
          # Generating QR code
          enc = pyqrcode.create(encrypted_message)
          enc.png(f'{name}.png',scale=6)
          #print(data)
     
          # Displaying QR
          qr = Image.open(f'{name}.png')
          #qr.show()

          # Decoding QR
          result = decode(qr)

          for i in result:
              a = i.data.decode()
              dec = ft(key).decrypt(bytes(a,'utf-8'))
              dec=dec.decode('utf-8')
              print('Decrypted : ',dec)
if __name__ == "__main__":
     encryption_and_decryption()
     

