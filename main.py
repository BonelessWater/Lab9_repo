import encoder
import decoder

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

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored! ")
        
        elif choice == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}. ")
        
        elif choice == "3":
            break

if __name__ == "__main__":
    
    main()
