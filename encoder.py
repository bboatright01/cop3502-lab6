# Main author: Erick Leaf

MENU_STRING = """Menu
-------------
1. Encode
2. Decode
3. Quit
"""

def encode(password):
    return "".join(map(lambda c: str((int(c) + 3) % 10), password))

def main():
    encoded = None

    while True:
        print(MENU_STRING)

        selected_option = int(input("Please enter an option: ").strip().split(" ")[0])
        
        if selected_option == 1:
            # User wants to encode a password
            encoded = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif selected_option == 2:
            print("The encoded password is " + encoded + ", and the original password is " + decode(encoded))
        elif selected_option == 3:
            return

if __name__ == "__main__":
    main()
