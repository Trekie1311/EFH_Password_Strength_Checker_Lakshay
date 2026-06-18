# Define variables to check password strength
pswd = input("Enter a password: ")
pswdU = False
pswdL = False
pswdD = False
hasSpecial = False
score = 0

#check if password is empty

if pswd == "":
	print("Password is empty")
else:
	print("password length: " , len(pswd))
     
#check if password has at least 8 characters

if len(pswd) >= 8:
    hasLength = True
else:
    hasLength = False

#define a list of special characters to check against and a list of common passwords to check against

special_chars = ["!", "@", "#", "$", "%", "&", "*"]
common_passwords = ["password", "123456", "admin", "qwerty"]

#check if password has at least one uppercase letter, one lowercase letter, and one digit

for i in pswd:
    if i.isupper():
        pswdU = True
    if i.islower():
        pswdL = True
    if i.isdigit():
        pswdD = True
    if i in special_chars:
        hasSpecial = True

#Adding to score based on criteria met
if hasLength:
    score += 20
if pswdU:
    score += 20
if pswdL:
    score += 20
if pswdD:
    score += 20
if hasSpecial:
    score += 20

#check if password meets all criteria
if pswd in common_passwords:
    print("Password is too common")
else:
    print("Password has at least 8 characters: ", hasLength)
    print("Password has at least one uppercase letter: ", pswdU)
    print("Password has at least one lowercase letter: ", pswdL)
    print("Password has at least one digit: ", pswdD)
    print("Password has at least one special character: ", hasSpecial)  

#Print password strength based on score
if score < 60:
    print("Password strength: weak, score: ", score)
elif score < 80:
    print("Password strength: medium, score: ", score)
elif score < 100:
    print("Password strength: strong, score: ", score)
else:    
    print("Password strength: very strong, score: ", score)

#suggest improvements for password strength
suggestions = []

if len(pswd) < 8:
    suggestions.append("Use more characters.")

if pswdL == False:
    suggestions.append("Add lowercase letters.")

if pswdD == False:
    suggestions.append("Add numbers.")

if hasSpecial == False:
    suggestions.append("Add special characters.")

if pswdU == False:
    suggestions.append("Add uppercase letters.")

 

