import hashlib

# Prompt user for input string
message = input("Enter the string you would like to hash: ").encode()

# Generate hash values for the input string
md5 = hashlib.md5(message).hexdigest()
sha1 = hashlib.sha1(message).hexdigest()
sha256 = hashlib.sha256(message).hexdigest()
sha512 = hashlib.sha512(message).hexdigest()

# Print the hash values
print("MD5 Hash =", md5)
print("SHA1 Hash =", sha1)
print("SHA256 Hash =", sha256)
print("SHA512 Hash =", sha512)
print("End of list.")
