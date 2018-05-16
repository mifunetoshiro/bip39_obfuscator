import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3.x is required!")

bip39 = {}
bip39_cn = {}
input_words = []
input_codepoints = []
input_numbers = []
sheet1 = []
sheet2 = []
sheet3 = []

with open("english.txt") as wordlist:
    line = wordlist.readline()
    count = 1
    while line:
        bip39[count] = line.strip()
        line = wordlist.readline()
        count += 1
    if len(bip39) != 2048:
        raise ValueError("english.txt has " + str(len(bip39)) + " lines, expected 2048!")

with open("chinese_traditional.txt", encoding="utf-8") as wordlist:
    line = wordlist.readline()
    count = 1
    while line:
        bip39_cn[count] = line.strip()
        line = wordlist.readline()
        count += 1
    if len(bip39_cn) != 2048:
        raise ValueError("chinese_traditional.txt has " + str(len(bip39_cn)) + " lines, expected 2048!")

print("Do NOT run this script on a computer connected to the internet and"
      "\ndo NOT reconnect this computer to the internet without wiping/reformatting it first!"
      "\nA keylogger can steal your seed words!")
q = input("Type \"yes\" if you understand the risks, made precautions and want to proceed: ")
if q.lower() == "yes":
    while True:
        print("Enter '1' to map your seed words into Traditional Chinese Unicode codepoints.")
        print("Enter '2' to unmap your Unicode codepoints into English seed words.")
        try:
            x = int(input("Input: "))
            if x != 1 and x != 2:
                print("Invalid input.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input.")
            continue
    
    if x == 1:
        while True:
            flag = False
            words = input("\nEnter your 12, 18 or 24 seed words in \"cat dad jar...\" format: ").lower().split()
            if len(words) not in [12, 18, 24]:
                print(str(len(words)) + " words entered, please enter 12, 18 or 24 words.")
                continue
            else:
                if not flag:
                    for word in words:
                        if word not in bip39.values():
                            flag = True
                            input_words.clear()
                            print("'" + word + "' is not a valid BIP-39 word.")
                            continue
                        else:
                            input_words.append(word)
                if flag:
                    continue
                for w in input_words:
                    input_numbers.append(list(bip39.keys())[list(bip39.values()).index(w)])
                    input_codepoints.append(hex(ord(bip39_cn[list(bip39.keys())[list(bip39.values()).index(w)]])).upper()[2:])
                break
    else:
        while True:
            flag = False
            codepoints = input("\nEnter your 12, 18 or 24 Traditional Chinese codepoints in any format: ").replace(" ", "")
            parts = [codepoints[i:i + 4] for i in range(0, len(codepoints), 4)]
            if len(parts) not in [12, 18, 24]:
                print(str(len(parts)) + " codepoints entered, please enter 12, 18 or 24 codepoints.")
                continue
            else:
                if not flag:
                    for cp in parts:
                        if chr(int(cp, 16)) not in bip39_cn.values():
                            flag = True
                            input_codepoints.clear()
                            print("'" + cp + "' is not a valid Traditional Chinese BIP-39 seed word Unicode codepoint.")
                            continue
                        else:
                            input_codepoints.append(cp.upper())
                if flag:
                    continue
                for n in input_codepoints:
                    input_words.append(bip39[list(bip39.keys())[list(bip39_cn.values()).index(chr(int(n, 16)))]])
                    input_numbers.append(list(bip39.keys())[list(bip39_cn.values()).index(chr(int(n, 16)))])
                words = input_words
                break
    
    pos = range(1, len(input_words) + 1)
    if x == 1:
        headers = ["#", "English", "Number", "Chinese"]
        table = [headers] + list(zip(pos, input_words, input_numbers, input_codepoints))
    else:
        headers = ["#", "Chinese", "Number", "English"]
        table = [headers] + list(zip(pos, input_codepoints, input_numbers, input_words))
    print("\n")
    for a, b in enumerate(table):
        line = "| ".join(str(c).ljust(10) for c in b)
        print(line)
        if a == 0:
            print("-" * len(line))
    
    if x == 1:
        print("\nSplit the obfuscated seed words into '2-out-of-3' recovery sheets? (y/n)")
        while True:
                x = input("Input: ").lower()
                if x != "y" and x != "n":
                    print("Invalid input.")
                    continue
                else:
                    if x == "n":
                        break
                    else:
                        count = 1
                        while count <= len(words):
                            if count % 3 != 0:
                                string = "#" + str(count) + ": " + str(input_codepoints[count - 1])
                                sheet1.append(string)
                            if (count + 1) % 3 != 0:
                                string = "#" + str(count) + ": " + str(input_codepoints[count - 1])
                                sheet2.append(string)
                            if (count - 1) % 3 != 0:
                                string = "#" + str(count) + ": " + str(input_codepoints[count - 1])
                                sheet3.append(string)
                            count += 1
                        headers2 = ["Sheet 1", "Sheet 2", "Sheet 3"]
                        table2 = [headers2] + list(zip(sheet1, sheet2, sheet3))
                        print("\n")
                        for a, b in enumerate(table2):
                            line = "| ".join(str(c).ljust(11) for c in b)
                            print(line)
                            if a == 0:
                                print("-" * len(line))
                        print("\nEach sheet has two thirds of your obfuscated seed words."
                              "\nYou need any two sheets to recover your full mnemonic phrase."
                              "\nStore each at a different safe place or hand out to your family members or attorney."
                              "\nA single sheet cannot give access to your wallet, if you lose the other two, your funds are lost forever!")
                break
    
    input('\nPress enter to exit.')
