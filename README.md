# bip39_obfuscator
This script obfuscates your mnemonic seed words by mapping their numerical positions in the [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) English [wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) ([raw file](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt)) of 2048 words to the [Unicode](https://en.wikipedia.org/wiki/Unicode) codepoints of the characters at the same positions in the BIP-39 Traditional Chinese [wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/chinese_traditional.txt) ([raw file](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/chinese_traditional.txt)), both of which you need to download and put in the same folder as this script. Reversely, the script also accepts Unicode codepoints as input, so you can map them back to their original English words. It supports 12, 18 and 24 word seeds. To run the script, you need [Python 3.x](https://www.python.org/downloads/) installed on your system. Best of all, you don't even need this script or Python at all, you can do everything by hand if you want, "mapping_table.txt" is included for faster/easier lookup to save you the trouble.

## Purpose
The purpose of this is to be able to safely write down your mnemonic seed words obfuscated, without immediately making it obvious to a potential thief that he or she is dealing with a cryptocurrency mnemonic phrase, as the obfuscated seed words will look like random hexadecimal characters. Instead of writing down your mnemonic phrase as `mosquito dust hotel maximum rich kitten hair mother salute dream flush hospital` you could write it down as `5B F6 5B 57 61 62 72 38 6C 2E 6F C3 4E 4E 53 48 95 CA 52 E2 93 2F 4E 95`.

The script optionally splits the obfuscated seed words into "2-out-of-3" recovery sheets, where each sheet stores two thirds of your obfuscated seed words. You need to combine any two sheets to recover your full mnemonic phrase, a single sheet is not enough. Store each at a different safe place or hand out to your family members or attorney. Remember, you need at least two sheets, if you lose them, you will not be able to recover your wallet.

## Example usage
Let's say `mosquito dust hotel maximum rich kitten hair mother salute dream flush hospital` are your MetaMask seed words. You need to write them down somewhere and keep them safe, but writing the original words down is a security risk. If anyone finds your list of words, they can drain your wallet. Even if you use a passphrase, they could return and force you at gunpoint or torture you until you give them the correct one. Instead, map the English words' positions in the wordlist to the Unicode codepoints of the characters at the same positions in the Traditional Chinese wordlist (don't worry, you don't need to know or learn Chinese).

Given the above seed words, the script will output a table with the English words, their number and the Unicode codepoint of the Chinese counterpart character in the Traditional Chinese wordlist:

| #  | English  | Number | Chinese |
|----|----------|--------|---------|
| 1  | mosquito | 1153   | 5BF6    |
| 2  | dust     | 547    | 5B57    |
| 3  | hotel    | 882    | 6162    |
| 4  | maximum  | 1100   | 7238    |
| 5  | rich     | 1483   | 6C2E    |
| 6  | kitten   | 987    | 6FC3    |
| 7  | hair     | 835    | 4E4E    |
| 8  | mother   | 1154   | 5348    |
| 9  | salute   | 1527   | 95CA    |
| 10 | dream    | 533    | 52E2    |
| 11 | flush    | 719    | 932F    |
| 12 | hospital | 880    | 4E95    |

You can store the Chinese Unicode codepoints in multiple ways, since each is 4 characters long (just remember this fact when you want to rebuild your original seed words). You could write it unchanged: ```5BF6 5B57 6162 7238 6C2E 6FC3 4E4E 5348 95CA 52E2 932F 4E95```, or, to make it look even more random, as a bunch of hexadecimal characters that return useless nonsense when converted back to text (```[ö[Wabr8l.oÃNNSHÊRâ/N```), you could write it without spaces: ```5BF65B57616272386C2E6FC34E4E534895CA52E2932F4E95```, you could write it with a space every 2 characters: ```5B F6 5B 57 61 62 72 38 6C 2E 6F C3 4E 4E 53 48 95 CA 52 E2 93 2F 4E 95```, you could group two or more together: ```5BF65B57 61627238 6C2E6FC3 4E4E5348 95CA52E2 932F4E95```, etc. The script accepts Unicode codepoints in any format (with or without spaces) to later convert back into English words.

To lookup and convert the Unicode codepoints manually, just do a Google search of e.g. "4E95 unicode" or use Unicode.org's [Unihan Database Lookup](http://unicode.org/charts/unihan.html), then find the position of the character in the BIP-39 Traditional Chinese wordlist. I included a "mapping_table.txt" file for faster/easier lookup to save you the trouble.

Optionally, you can split the obfuscated seed words into 2-out-of-3 recovery sheets. The script will output a table:

| Sheet 1   | Sheet 2   | Sheet 3   |
|-----------|-----------|-----------|
| #1: 5BF6  | #1: 5BF6  | #2: 5B57  |
| #2: 5B57  | #3: 6162  | #3: 6162  |
| #4: 7238  | #4: 7238  | #5: 6C2E  |
| #5: 6C2E  | #6: 6FC3  | #6: 6FC3  |
| #7: 4E4E  | #7: 4E4E  | #8: 5348  |
| #8: 5348  | #9: 95CA  | #9: 95CA  |
| #10: 52E2 | #10: 52E2 | #11: 932F |
| #11: 932F | #12: 4E95 | #12: 4E95 |

Write down and store each sheet separately at a different location.

## Safe usage
Only run this script if you understand the code and what it does. Anyone can fork it, turn it malicious and trick you into using it if you don't understand the underlying code. This script does not require any networking modules to function. For safety reasons you should only run this script on an air-gapped computer that is not connected to the internet. Make sure to write down the obfuscated codepoints by hand, do not print them. Even better, stamp or engrave them on titanium plates to protect from fire or water damage.
