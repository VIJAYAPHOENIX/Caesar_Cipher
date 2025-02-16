def caesar_cipher(command):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if command == "encode":
        message = input("enter message to encode :-\n")
        shift_value = int(input("enter the shift number :-\n"))
        cipher_text =""
        for letter in message:
            if letter == " ":
                cipher_text+=" "
            elif letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_value
                new_letter = alphabet[new_position]
                cipher_text+= new_letter
            else:
                cipher_text+= letter
        print(f"encoded cipher text is {cipher_text}")
    elif command == "decode":
        message = input("enter message to decode :-\n")
        shift_value = int(input("enter the shift number to decode :-\n"))
        plain_text =""
        for letter in message:
            if letter == " ":
                plain_text+=" "
            elif letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_value
                new_letter = alphabet[new_position]
                plain_text+= new_letter
            else:
                plain_text += letter
        print(f"Decoded cipher text is {plain_text}")
    else:
        print("Enter a valid command")
    
command = input("type 'encode' to encrpt, type 'decode' to decrypt \n").lower()
caesar_cipher(command)