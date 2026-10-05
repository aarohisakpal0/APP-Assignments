import re
text = input("enter text=")
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+',text)
print("email found=")
for email in emails:
    print(email)