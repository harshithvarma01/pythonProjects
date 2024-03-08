alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_keys):
    cipher_text=""
    for char in plain_text:
      if char in alphabets:
        position=alphabets.index(char)
        new_position=(position+shift_keys)%26
        cipher_text+=alphabets[new_position]
      else:
        cipher_text+=char
    print(cipher_text)
def decryption(plain_text,shift_keys):
    plain_text=""
    for char in plain_text:
      if char in alphabets:
        position=alphabets.index(char)
        new_position=(position+shift_keys)%26
        plain_text+=alphabets[new_position]
      else:
        plain_text+=char
    print(plain_text)
want_to_end=False
while not want_to_end:
    what_to_do = input("Type'encrypt' for encryption and 'decrypt' for decryption").lower()
    text = input("Enter your message: \n")
    shift = int(input("Enter shift keys: \n"))
    if what_to_do == "encrypt":
        encryption(text, shift)
    elif what_to_do == "decrypt":
        decryption(text, shift)
    play_again=input("Would you like to play! type 'yes' or 'no' to continue").lower()
    if play_again=='no':
        want_to_end=True
        print("Thanks for playing!")
