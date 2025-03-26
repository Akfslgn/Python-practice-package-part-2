import sys

# do not change the method name


def main():
    encoded_message = input("Enter the encoded message: \n")
    try:
        step_size = int(input("Enter the step size: \n"))
        if step_size <= 0:
            raise ValueError
    except ValueError:
        print("Error: Step size must be a positive integer")
        sys.exit(1)

    decoded_message = encoded_message[::step_size]
    print(f"Decoded Message: {decoded_message}")


# do not change the following lines:
if __name__ == "__main__":
    main()
