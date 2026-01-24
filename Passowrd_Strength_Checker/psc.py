import re

def min_length_check(password):
    return len(password) >= 8

def num_check(password):
    return re.search(r"\d", password) is not None

def char_check(password):
    return re.search(r"[^a-zA-Z0-9\s]", password) is not None

def upper_check(password):
    return any(c.isupper() for c in password)

def lower_check(password):
    return any(c.islower() for c in password)


def strength_check(password):

    rules = [
        (min_length_check, "at least 8 characters"),
        (num_check, "a number"),
        (char_check, "a special character"),
        (upper_check, "an uppercase letter"),
        (lower_check, "a lowercase letter"),
    ]

    passed = 0
    failed_reasons = []

    for check_func, message in rules:
        if check_func(password):
            passed += 1
        else:
            failed_reasons.append(message)

    if passed == 5:
        print("Password strength: STRONG")
    elif passed >= 3:
        print("Password strength: MEDIUM")
    else:
        print("Password strength: WEAK")

    if failed_reasons:
        print("Missing:")
        for reason in failed_reasons:
            print("-", reason)


def main():
    while True:
        user_input = input("Enter your password (or 'n' to exit): ")

        if user_input == 'n':
            break

        strength_check(user_input)


main()
