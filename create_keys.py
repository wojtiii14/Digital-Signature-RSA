import twitter
from Crypto.PublicKey import RSA

def create_keys():

    # Generowanie liczby zasilającej RSA w oparciu o utworzony przeze mnie TRNG

    number = twitter.generate()

    if number < 85:
        length = 1024

    elif (number >= 85) and (number < 170):
        length = 2048

    else:
        length = 4092

    # Generowanie pary kluczy

    key = RSA.generate(length)

    private_key = key.export_key()
    file_out = open("private.key", "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open("public.key", "wb")
    file_out.write(public_key)
    file_out.close()