from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA3_256
from Crypto.PublicKey import RSA

def sign():

    # Wprowadzanie wiadomości do zakodowania

    message = input('Wpisz swoją wiadomość: ').encode()
    key = RSA.import_key(open('private.key').read()) # Importujemy klucz prywatny z pliku
    h = SHA3_256.new(message) # Tworzymy hash dla naszej wiadomości

    # Podpisujemy naszą wiadomość

    signer=pkcs1_15.new(key)
    signature=signer.sign(h)

    # print(signature.hex())

    # Zapisujemy podpis i wiadomość

    file_out = open("signature.pem", "wb")
    file_out.write(signature)
    file_out.close()

    file_out = open("message.txt", "wb")
    file_out.write(message)
    file_out.close()
