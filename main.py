import create_keys
import sign_message
import verify_message

create_keys.create_keys()

sign_message.sign()

while(1==1):
    x = input("Naciśnij 3, aby sprawdzić wiadomość lub inny przycisk aby wyjść: ")
    x = int(x)
    if(x == 3):
        verify_message.verify()
    else:
        break

