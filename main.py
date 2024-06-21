import random

def d4_roll():
    number = random.randint(1,4)
    print("Dice roll (D4) =", number)
    return number

def d6_roll():
    number = random.randint(1,6)
    print("Dice roll (D6) =", number)
    return number

def d8_roll():
    number = random.randint(1,8)
    print("Dice roll (D8) =", number)
    return number

def d12_roll():
    number = random.randint(1,12)
    print("Dice roll (D12) =", number)
    return number

def d20_roll():
    number = random.randint(1,20)
    print("Dice roll (D20) =", number)
    return number

def main():
    rolling = True

    while rolling == True:
        selection = input("Select die (D(4), D(6), D(8), D(12), D(20): ")
        print("\n")

        if selection == '4':
            d4_roll()
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True

        elif selection == '6':
            d6_roll()
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True            

        elif selection == '8':
            d8_roll()
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True

        elif selection == '12':
            d12_roll()
            repeat = input("Roll again? (y/n): ")
            repeat_yn = repeat.lower()
            if repeat_yn == 'n':
                rolling = False
            elif repeat_yn == 'y':
                rolling = True
            else:
                print("Invalid, try again")
                rolling = True

        elif selection == '20':
            d20_roll()
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
            print("Invalid selection\nEnter a number: 4, 6, 8, 12, 20")
        

main()
