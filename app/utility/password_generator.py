# app/password_generator.py
import secrets
import string


def password_generate(length: int, uppercase: bool, digits: bool, special: bool) -> str:
    try:
        # Default password char set with both lowercase and uppercase letters
        pass_charset = string.ascii_letters
        if uppercase:
            pass_charset += string.ascii_uppercase
        if digits:
            pass_charset += string.digits
        if special:
            pass_charset += string.punctuation

        # Ensure that the length of password char set is not greater than the required password length
        charset_length = min(len(pass_charset), length)

        # Generate a new secure password every time while the function is called
        password = ''.join(secrets.choice(pass_charset) for p in range(charset_length))

        return password

    except Exception as e:
        # Handle exceptions (you may want to log the exception or take appropriate action)
        print(f"An error occurred: {e}")
        return "Error occurred, password generation failed."
