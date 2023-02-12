import re

nr_telefonu = input("Podaj numer telefonu: ")

is_match = re.fullmatch(r'[4-9][0-9]{8}', nr_telefonu) is not None

print("Numer jest prawidłowy" if is_match else "Numer nie jest prawidłowy")

# if re.fullmatch(r'[4-9][0-9]{8}', nr_telefonu):
#     print("Numer jest prawidłowy")
# else:
#     print("nieprawidłowy")

# tak nie robimy:
# print("Numer jest prawidłowy" if re.fullmatch(r'[4-9][0-9]{8}', input("Podaj numer telefonu: ")) else "Numer nie jest prawidłowy")
