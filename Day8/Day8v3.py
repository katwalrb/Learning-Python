alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_message = ""
    for n in plain_text:
        if n == ' ':
            cipher_message += ' '
        else:
            position = alphabet.index(n)
            if (position+shift_amount)<len(alphabet):
                cipher_message += alphabet[position+shift_amount]
            else:
                cipher_message += alphabet[position+shift_amount-(len(alphabet))]
    print(f"The encoded text is {cipher_message}.")

def decrypt(cipher_text,shift_amount):
    org_text = ""
    for letter in cipher_text:
        if letter == " ":
            org_text = " "
        else:
            position = alphabet.index(letter)
            if (position-shift_amount)>=0:
                org_text += alphabet[position-shift_amount]
            else:
                org_text += alphabet[position-shift+len(alphabet)]
    print(f"The decoded text is {org_text}.")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)

        


