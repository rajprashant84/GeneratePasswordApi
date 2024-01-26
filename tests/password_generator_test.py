import string

from app.utility.password_generator import password_generate


def test_password_generate():
    length = 12
    uppercase = True
    digits = True
    special = True

    password = password_generate(length, uppercase, digits, special)

    assert len(password) == length
    assert any(char.isupper() for char in password)
    assert any(char.isdigit() for char in password)
    assert any(char in string.punctuation for char in password)


def test_password_generate_without_special():
    length = 10
    uppercase = True
    digits = True
    special = False

    password = password_generate(length, uppercase, digits, special)

    assert len(password) == length
    assert any(char.isupper() for char in password)
    assert any(char.isdigit() for char in password)
    assert all(char.isalpha() or char.isdigit() for char in password)


def test_password_generate_without_uppercase():
    length = 8
    uppercase = False
    digits = True
    special = True

    password = password_generate(length, uppercase, digits, special)

    assert len(password) == length
    assert any(char.isdigit() for char in password)
    assert any(char in string.punctuation for char in password)

def test_password_generate_without_digits():
    length = 15
    uppercase = True
    digits = False
    special = True

    password = password_generate(length, uppercase, digits, special)

    assert len(password) == length
    assert any(char.isupper() for char in password)
    assert not any(char.isdigit() for char in password)
    assert any(char in string.punctuation for char in password)
