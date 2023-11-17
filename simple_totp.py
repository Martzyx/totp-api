import pyotp


def generate_totp(secret):
    """
    Generate a TOTP given a secret key.
    """
    totp = pyotp.TOTP(secret)
    return totp.now()


def main():
    """
    Main function to execute the script.
    """
    secret = input("Enter the secret key: ")
    totp = generate_totp(secret)
    print(f"The TOTP is: {totp}")


if __name__ == "__main__":
    main()
