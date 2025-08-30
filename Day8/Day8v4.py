from art import logo
print(logo)

continue_program = True
while continue_program:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    def caesar(any_text, any_shift, any_direction):
        end_text = ""
        if any_direction == 'encode':
            for n in any_text:
                if n not in alphabet:
                    end_text += n
                else:
                    position = alphabet.index(n)
                    if (position+any_shift)<len(alphabet):
                        end_text += alphabet[position+any_shift]
                    else:
                        end_text += alphabet[position+any_shift-(len(alphabet))]
            print(f"The encoded text is {end_text}.")
        else:
            for letter in any_text:
                if letter not in alphabet:
                    end_text += letter
                else:
                    position = alphabet.index(letter)
                    if (position-any_shift)>=0:
                        end_text += alphabet[position-any_shift]
                    else:
                        end_text += alphabet[position-shift+len(alphabet)]
            print(f"The decoded text is {end_text}.")

    caesar(any_text=text,any_shift=shift,any_direction=direction)
    answer = input("Do you want to restart? Type 'yes' or 'no': ")
    if answer == 'no':
        continue_program = False
        print("program has ended")