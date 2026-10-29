class AgeError(Exception):
    pass


class InsufficientFundError(Exception):
    def __init__(self, bal, amt):
        self.bal = bal
        self.amt = amt
        super().__init__(f"Cannot withdraw {amt}. Current balance is only {bal}.")


class ExceptionDemoAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundError(self.balance, amount)
        self.balance -= amount
        return self.balance


def main():
    print("ZeroDivisionError & Full try-except-else-finally flow:")
    for denom in [0, 5]:
        try:
            print(f"Attempting 100 / {denom}:")
            res = 100 / denom
        except ZeroDivisionError:
            print("  -> Caught ZeroDivisionError: You cannot divide by zero!")
        else:
            print(f"  -> Else block executed! Result = {res}")
        finally:
            print("  -> Finally block executed: Clean up finished.")

    print("\nIndexError:")
    try:
        sample_list = [10, 20, 30]
        _ = sample_list[10]
    except IndexError as e:
        print("  -> Caught IndexError:", e)

    print("\nFileNotFoundError:")
    try:
        with open("non_existent_file_xyz123.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError as e:
        print("  -> Caught FileNotFoundError:", e)

    print("\nUser-Defined Exception: AgeError:")
    test_age = 15
    try:
        if test_age < 18:
            raise AgeError(f"Age {test_age} is invalid. Age must be 18 or above.")
        print("Valid age:", test_age)
    except AgeError as e:
        print("  -> Caught Custom AgeError:", e)

    print("\nUser-Defined Exception: InsufficientFundError:")
    bank_acc = ExceptionDemoAccount(balance=500)
    print("Bank account balance:", bank_acc.balance)
    try:
        print("Attempting to withdraw 1200...")
        bank_acc.withdraw(1200)
    except InsufficientFundError as e:
        print("  -> Transaction failed:", e)
    finally:
        print("  -> Thank you for banking with us.")


if __name__ == "__main__":
    main()
