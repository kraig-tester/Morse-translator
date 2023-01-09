translator = {
    "a": ".--", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", 
    "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--","n": "-.", 
    "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", 
    "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",

    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", "0": "-----",

    " ": " \ "
}

running = True
while running:
    to_morse = ""

    to_morse = input("Enter string to convert to morse. Type '!q' to quit: ").lower()
    
    if to_morse == "!q":
        running = False
        continue

    try:
        morse_code = ''.join([translator[letter] + " " for letter in to_morse])
    except KeyError:
        print("Invalid letters for encrypting. Note: signs(!,?,. .etc) are not allowed. Try again.")

    morse_code = morse_code.strip()
    print(f"Morse code: {morse_code}")