# do not change the method name
def main():
    email = input("Enter an email address: ")

    if " " in email:
        print("Email cannot contain spaces")
        return

    if email.count("@") == 0:
        print("Email must contain an @ symbol")
        return

    if email.count("@") > 1:
        print("Email must contain only one @ symbol")
        return

    at_index = email.find("@")
    if at_index == 0:
        print("Email must have characters before the @ symbol")
        return

    domain = email[at_index + 1:]
    if "." not in domain:
        print("Email must have a domain with a period after the @ symbol")
        return

    print("Valid email address!")


# do not change the following lines:
main()
