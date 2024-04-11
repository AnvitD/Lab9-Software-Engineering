def encode(password):
    encoded = []
    for i in range(len(password)):
        encoded.append(chr(ord(password[i]) + 3))

    return "".join(encoded)

def decode(enc):
    decoded = []
    for i in range(len(enc)):
        decoded.append(chr(ord(enc[i] - 3))

    return "".join(decoded)

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def main():

    while True:
        menu()

        choice = input("Please enter an option: ")

        global enc

        if choice == "1":
            password = input("Please enter your password to encode: ")
            enc = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            dec = decode(enc)
            print(f"The encoded password is {enc}, and the original password is {dec}")
        elif choice == "3":
            break
        else:
            print("Wrong input")

main()
