import re

print("Example strong passwords: My_P@ssw0rd!   |   King$2025   |   SecurePass1#")
print("Example weak passwords: pass123   |   password   |   12345678   |   ABCDEF#")

password = input("Enter your password: ")
# At least 8 characters, 1 uppercase, 1 digit, 1 special character
pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
if re.match(pattern, password):
    print("Strong")
else:
    print("Weak")
