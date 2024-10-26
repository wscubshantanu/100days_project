alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("type 'encode' to encrpyt,type 'decode' to decrpyt:\n").lower()
text = input("type your text:\n").lower()
shift = int(input("type the shift number:\n"))

#todo-1: create a function called 'encrypt()' that takes 'original_text' and 'shift_amount'as 2 inputs.

#todo-2: inside the 'encrypt()' function,shift each letter of the 'original_text' forwards in the alphabet
#by the shift amount and print the encrypted text.

#hello 2

def encrypt(original_text,shift_amount):
    cipher_text = ""  # j

#todo-4:what happens if you try to shift z forwards by 9? can you fix the code?
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet) # 0-25
        cipher_text += alphabet[shifted_position] # j

    print(f"here is the encoded result:{cipher_text}")

#todo-3: call the 'encrypt()' function and pass in the user inputs. you should be able to test the code and encrypt a
#message.

encrypt(original_text=text,shift_amount=shift )
