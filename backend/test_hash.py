from app.auth.hashing import hash_password, verify_password

password = "Admin@123"

hashed = hash_password(password)

print("Password :", password)
print("Hash     :", hashed)
print("Verified :", verify_password(password, hashed))