
# Variables
quitting = False
code = None
# Methods
def encode(in_code):
    """Password encoder by Ethan Van. Adds 3 to each digit of the password.

    Args:
        in_code (str): Password input
    Return:
        str: Encoded password
    """

    code = str(in_code)
    new_code = ""
    for i in code:
        digit = (int(i) + 3) % 10
        new_code = new_code + str(digit)
    
    return new_code
def decode(encoded_code):
    code = str(encoded_code)
    decoded_code = ""
    for i in code:
        digit = (int(i)-3) % 10
        decoded_code = decoded_code + str(digit)

    return decoded_code

if __name__ == "__main__":
    while quitting is False:
        # Menu
        print("Menu")
        print(13*"-")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # User selection
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            code = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            decoded = decode(code)
            print(f"The encoded password is {code}, and the original password is {decoded}")
        elif user_input == 3:
            quitting = True


