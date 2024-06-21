import random

def roll(val):
    number = random.randint(1,val)
    print("Dice roll =", number)
    return number

def main():
    rolling = True

    while rolling == True:
        selection = int(input("Select die (D(4), D(6), D(8), D(10), D(12), D(20): "))
        print("\n")

        if selection == 4:
            print("D4 roll\n")
            roll(selection)
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True

        elif selection == 6:
            print("D6 roll\n")
            roll(selection)
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True            

        elif selection == 8:
            print("D8 roll\n")
            roll(selection)
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True

        elif selection == 10:
            print("D10 roll\n")
            roll(selection)
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True

        elif selection == 12:
            print("D12 roll\n")
            roll(selection)
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True

        elif selection == 20:
            print("D20 roll\n")
            roll(selection)
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True

        else:
            print("Invalid selection\nEnter a number: 4, 6, 8, 10, 12, 20")
        

main()
