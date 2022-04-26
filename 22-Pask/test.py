import bcrypt

password = b"SecretPassword55"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

username = request.form.get("username") # Or email
pasword = request.form.get("password").encode()



if bcrypt.checkpw(password, hashed):
    print("It matches!")
else:
    print("Didn't match")
