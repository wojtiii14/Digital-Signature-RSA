from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA3_256
from Crypto.PublicKey import RSA

def verify():

    # Odczytujemy publiczny klucz

    key = RSA.import_key(open('public.key').read())

    # Odczytujemy wiadomość i nasz podpis

    file_in = open("message.txt", "rb")
    message=file_in.read()
    file_in.close()

    file_in = open("signature.pem", "rb")
    signature=file_in.read()
    file_in.close()

    h = SHA3_256.new(message)

    # Porównujemy hash wiadomości z pliku z tym zawartym w podpisie

    try:
        pkcs1_15.new(key).verify(h, signature)
        print ("Dane są zgodne.")
    except (ValueError, TypeError):
        print ("Dane nie są zgodne, ktoś mógł ingerować w plik.")
