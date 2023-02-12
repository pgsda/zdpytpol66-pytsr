import re

nr_telefonu = input("Podaj email: ").lower()

is_match = re.fullmatch(r'[_\.+\-a-z0-9]+@[a-z0-9\-_\.]+', nr_telefonu) is not None

print("email jest prawidłowy" if is_match else "email nie jest prawidłowy")