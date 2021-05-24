import bcrypt

password = b"mypass"
pass_hash = bcrypt.hashpw(password, bcrypt.gensalt())

print(pass_hash)