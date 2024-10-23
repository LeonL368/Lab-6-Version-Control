# By Leon Liu
import sys


def encode(s):  # Encoder function
    res = ""
    for char in s:
        res += str((int(char) + 3) % 10)  # Add three, then mod 10
    return res


def decode(s):
    decodedres = ""

    for char in s:
        res = str((int(char) - 3) % 10)
        decodedres += res

    return decodedres


def main():  # Decoder function
    password = ""
    while True:
        print("Menu\n-------------\n1.Encode\n2.Decode\n3.Quit\n")  # Printing menu
        try:
            choice = int(input("Please enter an Option: "))
            if choice == 3:
                sys.exit()  # Quits if the choice is 3
            elif choice == 1:
                s = input("Please enter your password to encode: ")
                password = encode(s)
                print("Your password has been encoded and stored!\n")
            elif choice == 2:
                print(f"The encoded password is {password}, and the original password is {decode(password)}.\n")
            else:
                raise ValueError  # Catch value error if choice is not 1,2,3
        except ValueError:
            print("Invalid. Try Again.")  # Re-prompts input


if __name__ == "__main__":
    main()
