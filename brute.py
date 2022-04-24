from Crypto.Hash import SHA256
import pyautogui

def hash(s):
   h = SHA256.new()
   h.update(s)
   return h.hexdigest()

match = "xx7xxxxax6x3fxxxxxf0x8xxxxxxxxxxxbxxxxxxxxxxxxxxxxxxxxx7xaxxxxbx"

alphbet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(26):
    for ii in range(26):
        for iii in range(26):
            for iiii in range(26):
                for iiiii in range(26):
                    for iiiiii in range(26):
                        for iiiiiii in range(26):
                            string = alphbet[i] + alphbet[ii] + alphbet[iii] + alphbet[iiii] + alphbet[iiiii] + alphbet[iiiiii] + alphbet[iiiiiii]
                            x = hash(string.strip().encode().lower())
                            if x[9] == "1":
                                if x[16] == "e":
                                    if x[22] == "1":
                                        if x[37] == "3":
                                            if x[38] == "9":
                                                if x[41] == "b":
                                                    if x[46] == "6":
                                                        pyautogui.alert(string)
                            iiiiiii += 1
                        iiiiii += 1
                    iiiii += 1
                iiii += 1
            iii += 1
        ii += 1
    i += 1