#By Leon Liu
import sys
def encode(s): 
    res = ""
    for char in s:
        res+= str((int(char)+3)%10)
    return res

def main():
    while True:
        print("\n--------\nMenu:\n1.Encode\n2.Decode\n3.Quit\n--------\n")
        try:
            choice = int(input("Enter an Option: "))
            if choice == 3:
                sys.exit() 
            elif choice ==1:
                s = input("Enter a string to encode: ")
                print(f"{s} encoded is {encode(s)}")
            elif choice ==2:
                s = input("Enter a string to decode: ")
                print(f"{s} decoded is {decode(s)}")
            else:
                raise ValueError 
        except ValueError:
            print("Invalid. Try Again.") 
        


if __name__=="__main__":
    main()