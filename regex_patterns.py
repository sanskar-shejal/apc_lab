import re


def main():
    sample_email = "virajpotdar4@gmail.com"
    print(f"Sample String: '{sample_email}'")

    words = re.findall(r"\w+", sample_email)
    print("re.findall(r'\\w+'):", words)

    pattern = re.compile(r"\w+@\w+\.\w+")
    compiled_match = pattern.search(sample_email)
    print("re.compile() + search():", compiled_match.group() if compiled_match else "No match")

    parts = re.split(r"@", sample_email)
    print("re.split(r'@'):", parts)

    replaced = re.sub(r"gmail", "yahoo", sample_email)
    print("re.sub('gmail' -> 'yahoo'):", replaced)

    escaped = re.escape(sample_email)
    print("re.escape():", escaped)

    print("\nReal-World Validators:")

    def check_email(email_str):
        email_pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
        is_valid = bool(re.match(email_pattern, email_str))
        print(f"  - Email '{email_str}' valid?: {is_valid}")
        return is_valid

    def check_phone(phone_str):
        phone_pattern = r"^[0-9]{10}$"
        is_valid = bool(re.match(phone_pattern, phone_str))
        print(f"  - Phone '{phone_str}' (10 digits) valid?: {is_valid}")
        return is_valid

    def check_password_strength(pwd_str):
        pwd_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@_]).{8,}$"
        is_valid = bool(re.match(pwd_pattern, pwd_str))
        print(f"  - Password '{pwd_str}' strong?: {is_valid}")
        return is_valid

    check_email("test.user@domain.com")
    check_email("invalid_email@domain")
    check_phone("9876543210")
    check_phone("12345")
    check_password_strength("Pass@1234")
    check_password_strength("weakpass")


if __name__ == "__main__":
    main()
