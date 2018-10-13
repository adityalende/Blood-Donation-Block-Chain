import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("set.csv", "set.csv.aes", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("set.csv.aes", "set1.csv", password, bufferSize)