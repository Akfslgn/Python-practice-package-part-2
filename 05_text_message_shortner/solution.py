# do not change the method name
def main():
    # Prompt the user to enter a text message
    original_message = input("Enter a message: ")

    # Define the replacements
    replacements = {
        "with": "w/",
        "for": "4",
        "to": "2",
        "and": "&",
        "at": "@"
    }

    # Shorten the message using the replacements
    shortened_message = original_message
    for word, abbreviation in replacements.items():
        shortened_message = shortened_message.replace(word, abbreviation)

    # Trim the message if it's longer than 160 characters
    if len(shortened_message) > 160:
        shortened_message = shortened_message[:157] + "..."

    # Capitalize the first letter of the shortened message
    if shortened_message:
        shortened_message = shortened_message[0].upper(
        ) + shortened_message[1:]

    # Display both the original message and the shortened message
    print(
        f"Original message ({len(original_message)} chars): {original_message}")
    print(
        f"Shortened message ({len(shortened_message)} chars): {shortened_message}")
    print(
        f"You saved {len(original_message) - len(shortened_message)} characters!")


# do not change the following lines:
main()
