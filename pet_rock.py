import time
import sys

def type_out(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def stat_countdown():
    global happy, clean, hungry
    happy -= 1
    clean -= 1
    hungry += 1

def mood():
    if happy > 5 or clean > 5 or hungry < 5:
        print("\n\no(＾▽＾)o")
    elif happy > 3 or clean > 3 or hungry < 7:
        print("\n\n(•‿•)")
    elif happy > 1 or clean > 1 or hungry < 9:
        print("\n\n(•︵•)")
    else:
        print("\n\n(ಥ﹏ಥ)")

def cool_rock():
    print("(•_•)".ljust(20), end='\r')
    time.sleep(0.5)
    print("( •_•)>⌐■-■".ljust(20), end='\r')
    time.sleep(0.5)
    print("(⌐■_■)".ljust(20), end='\r')

def status():
    type_out(f"\nHappiness: {happy}\n")
    type_out(f"Cleanliness: {clean}\n")
    type_out(f"Hunger: {hungry}\n")

print("""
 ____      _     ____            _      ____  _           
|  _ \ ___| |_  |  _ \ ___   ___| | __ / ___|(_)_ __ ___  
| |_) / _ \ __| | |_) / _ \ / __| |/ / \___ \| | '_ ` _ \ 
|  __/  __/ |_  |  _ < (_) | (__|   <   ___) | | | | | | |
|_|   \___|\__| |_| \_\___/ \___|_|\_\ |____/|_|_| |_| |_|""")

type_out("\n\nwhat do you want to name your pet rock:")
pet_name = input("\n")
type_out(f"Congratulations! You now have a pet rock named {pet_name} Take good care of it!")
time.sleep(1)
happy = 5
clean = 5
hungry = 5

while True:
    mood()
    if happy <= 0 or clean <= 0 or hungry >= 10:
        type_out(f"{pet_name} has run away due to neglect.\n")
        type_out("Your only friend is gone.\n")
        type_out("You feel sad and lonely.\n")
        type_out("GAME OVER\n")
        sys.exit()
    status()
    action = input(f"What do you want to do with your pet rock?\n 1- Play with {pet_name}\n 2- Clean, {pet_name}\n 3- Feed, {pet_name}\n")
    if action == "1":
        print("You play with", pet_name, "It seems happy!")
        happy += 2

    if action == "2":
        type_out(f"you take {pet_name} to the bath and set it in")
        look = input("do you look away y/n\n")
        if look == "y":
            type_out(f"you look away then back and {pet_name} has eroded away")
            type_out("your only friend is gone")
            type_out("you feel sad and lonely")
            type_out("GAME OVER")
            sys.exit()
        print(f"{pet_name} looks more clean now")
        clean += 2
        
    if action == "3":
         while hungry >= 0 or hungry <= 10:
            type_out(f"you feed {pet_name} ")
            hungry -= 2
            feed = input("do you want to feed it more y/n\n").lower()
            if feed == "y":
                continue
            elif feed == "n":
                break
            if hungry < 0:
                type_out(f"{pet_name} has overeaten and cracked\n")
                type_out("your only friend is gone\n")
                type_out("you feel sad and lonely\n")
                type_out("GAME OVER")
                sys.exit()
            elif hungry > 10:
                type_out(f"{pet_name} has starved and imploded on itself causing a small black hole and destroying the earth")
                type_out("everyone is gone")
                type_out("GAME OVER")
                sys.exit()
    elif action == "4":
        print("you stare at", pet_name, "for a while")
        print("you see a hammer and a vail of liquid")
        stare = input(f"do you want to use the hammer or pour the on {pet_name} 1- pick up the hammer\n 2- grab the liquid\n").lower()
        if stare == "1":
            type_out(f"you pick up the hammer and smash {pet_name} into pieces\n")
            type_out("your only friend is gone\n")
            type_out("you feel sad and lonely\n")
            type_out("GAME OVER")
            sys.exit()
        elif stare == "2":
            type_out(f"you pour the liquid on {pet_name}\n")
            type_out(f"{pet_name} has melted away\n")
            type_out("your only friend is gone\n")
            type_out("you feel sad and lonely\n")
            type_out("GAME OVER")
            sys.exit()
    elif action == "5":
        print(f"you find glasses and put them on {pet_name}")
        cool_rock()
        break

    stat_countdown()

while True:
    cool_rock()
    if happy <= 0 or clean <= 0 or hungry >= 10:
        type_out(f"{pet_name} has run away due to neglect.\n")
        type_out("Your only friend is gone.\n")
        type_out("You feel sad and lonely.\n")
        type_out("GAME OVER\n")
        sys.exit()
    status()
    action = input(f"What do you want to do with your pet rock?\n 1- Play with {pet_name}\n 2- Clean, {pet_name}\n 3- Feed, {pet_name}\n")
    if action == "1":
        print("You play with", pet_name, "It seems happy!")
        happy += 2

    if action == "2":
        type_out(f"you take {pet_name} to the bath and set it in")
        look = input("do you look away y/n\n")

        if look == "y":
            type_out(f"you look away then back and {pet_name} has eroded away")
            type_out("your only friend is gone")
            type_out("you feel sad and lonely")
            type_out("GAME OVER")
            sys.exit()
        print(f"{pet_name} looks more clean now")
        clean += 2
        
    if action == "3":
         while hungry >= 0 or hungry <= 10:
            type_out(f"you feed {pet_name} ")
            hungry -= 2
            feed = input("do you want to feed it more y/n\n").lower()
            if feed == "y":
                continue
            elif feed == "n":
                break
            if hungry < 0:
                type_out(f"{pet_name} has overeaten and cracked\n")
                type_out("your only friend is gone\n")
                type_out("you feel sad and lonely\n")
                type_out("GAME OVER")
                sys.exit()
            elif hungry > 10:
                type_out(f"{pet_name} has starved and imploded on itself causing a small black hole and destroying the earth")
                type_out("everyone is gone")
                type_out("GAME OVER")
                sys.exit()

    if action == "4":
        print("you stare at", pet_name, "for a while")
        print("you see a hammer and a vail of liquid")
        stare = input(f"do you want to use the hammer or pour the on {pet_name} 1- pick up the hammer\n 2- grab the liquid\n").lower()
        if stare == "1":
            type_out(f"you pick up the hammer and smash {pet_name} into pieces\n")
            type_out("your only friend is gone\n")
            type_out("you feel sad and lonely\n")
            type_out("GAME OVER")
            sys.exit()
        elif stare == "2":
            type_out(f"you pour the liquid on {pet_name}\n")
            type_out(f"{pet_name} has melted away\n")
            type_out("your only friend is gone\n")
            type_out("you feel sad and lonely\n")
            type_out("GAME OVER")
            sys.exit()

    stat_countdown()
