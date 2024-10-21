#By Leon Liu
import sys
def encode(s): #Encoder function
    res = ""
    for char in s:
        res+= str((int(char)+3)%10) #Add three, then mod 10
    return res
def decode(s):
    res = ""
    for char in s:
        res+=str((int(char)-3)%10) #Minus three, then mod 10 
    return res
def main(): #Decoder function
    while True:
        print("\n--------\nMenu:\n1.Encode\n2.Decode\n3.Quit\n--------\n") #Printing menu
        try:
            choice = int(input("Enter an Option: "))
            if choice == 3:
                sys.exit() #Quits if the choice is 3
            elif choice ==1:
                s = input("Enter a string to encode: ")
                print(f"{s} encoded is {encode(s)}")
            elif choice ==2:
                s = input("Enter a string to decode: ")
                print(f"{s} decoded is {decode(s)}")
            else:
                raise ValueError #Catch value error if choice is not 1,2,3
        except ValueError:
            print("Invalid. Try Again.") #Re-prompts input
        


if __name__=="__main__":
    main()