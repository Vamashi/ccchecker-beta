# Code is not cleaned, can be not perfectly. But its source open! Yay!

import sys # Importing sys for instant closing program in some situations

from colorama import Fore # Just for colors

wtext = Fore.GREEN+"▒   ▒   ▒  ▒▒▒▒  ▒     ▒▒▒▒  ▒▒▒▒  ▒   ▒  ▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒   ▒▒▒▒  ▒▒▒▒ ▒   ▒  ▒▒▒▒  ▒▒▒▒  ▒  ▒  ▒▒▒▒  ▒▒▒▒ \n▒   ▒   ▒  ▒     ▒    ▒     ▒   ▒  ▒▒ ▒▒  ▒       ▒   ▒   ▒  ▒     ▒     ▒   ▒  ▒     ▒     ▒ ▒   ▒     ▒  ▒ \n▒ ▒ ▒ ▒ ▒  ▒▒▒   ▒    ▒     ▒   ▒  ▒ ▒ ▒  ▒▒▒     ▒   ▒   ▒  ▒     ▒     ▒▒▒▒▒  ▒▒▒   ▒     ▒▒    ▒▒▒   ▒▒▒▒ \n▒ ▒ ▒ ▒ ▒  ▒     ▒    ▒     ▒   ▒  ▒   ▒  ▒       ▒   ▒   ▒  ▒     ▒     ▒   ▒  ▒     ▒     ▒ ▒   ▒     ▒ ▒ \n  ▒   ▒    ▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒▒▒   ▒   ▒  ▒▒▒▒    ▒    ▒▒▒    ▒▒▒▒  ▒▒▒▒ ▒   ▒  ▒▒▒▒  ▒▒▒▒  ▒  ▒  ▒▒▒▒  ▒  ▒▒"
line = "—————————————————————————————————————————————————————————————————————————————————————————————————————————————"

text1 = "[?] Please, write here your BIN for cards, or leave empty to random bin."

print(wtext)
print(line)
print(text1)

bin1 = input(">>> ") # bin

text2 = "[?] Write amount of credit cards to generate."

print(text2)

count = input(">>> ") # amount

print("[+] Generating "+str(count)+" cards...")

try: # checking api avaible
    temp = open("api.py","r")
    temp.close()

    import api
except: # api not found
    print(Fore.RED+"[!] Error: api not found. Maybe installation of checker was incorrect.")
    sys.exit()

cards = api.generate_cards(bin1, count) # generating cards

print("[+] Generated cards!")

print("[+] Starting...")

for card in cards: # checking
    try:
        card = str(card)
        card.replace(" ","")
        card.replace("\n","")
        result = api.check(card)

        if card == "5168755905898835":
            print(Fore.RED+"DJFIOASJIOFIOASIOAOISPAIADJFS:KFLA<SKFJWIUDoa")

        if result == "invalid":
            print(Fore.RED+"[-] Incorrect card.")
        elif result == "live":
            print(Fore.GREEN+"[-] Live card.")
            x = api.save_card(card)
            if x == 1:
                print(Fore.RED+"[!!!] ERROR! Card not saved. Card data was: "+str(card))
        elif result == "unknown":
            print(Fore.YELLOW+"[?] Unknown card.")
        elif result == "die":
            print(Fore.RED+"[-] Died card.")
        elif result == "error":
            print(Fore.RED+"[!!!] Error was in checking card: "+str(card))
    except Exception as e:
        print(Fore.RED+"[!!!] ERROR! Closing program...")
        print(Fore.RED+"[!!!] "+str(e))
        sys.exit()

print(Fore.GREEN+"[+] Thank you for using CCCHECKER! Good luck!")

# good luck also