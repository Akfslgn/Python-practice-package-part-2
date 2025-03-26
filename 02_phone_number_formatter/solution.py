# do not change the method name
def main():
    # your solution goes here
    format_phone_number()


def format_phone_number():
    phone_number = input(
        "Enter a 10-digit phone number, no spaces, special characters or spaces: ")

    # Validate input
    (len(phone_number) == 10 and phone_number.isdigit()) or (
        print("Error: Please enter exactly 10 digits.\nNo spaces, special characters and alphabetical characters."), exit()
    )

    # Format and print phone number
    formatted_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    print(f"Formatted Phone Number: {formatted_number}")


# do not change the code below
if __name__ == "__main__":
    main()
