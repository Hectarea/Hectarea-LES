
# Hectarea Loop Encryption System



Encryption algorithm by Hectarea and Qrab & Nell, based on 16 function blocks that process and de-process individual bytes.

Each function block is randomly selected based on the (iv+(password[(nonce+index)%len(password)]))%(2**3), to guarentee a 
criptographically safe random output.

It accepts a byte array as input and another byte array with the same length as output.


## Installation

```bash
pip install HectareaLES  
```

## Basic Example
```python
from HectareaLES import LES

#Initialize the LES class
LES = LES()

#Parameters:

#Byte array to encrypt
secret_message = b'i know what the dog is doing'

#Any length password
password = b'random length password'

#Any length iv
iv = b'random length initial value'

#Any length nonce
nonce = b'some random nonce'


#Returns the encrypted byte array
EncryptedBytes = LES.encrypt(secret_message, password, iv, nonce)

print("\nEncrypted ByteArray: \n" + str(EncryptedBytes))

#Returns the original byte array
DecryptedBytes = LES.decrypt(EncryptedBytes, password, iv, nonce)

print("\nDecrypted ByteArray: \n" + str(DecryptedBytes))
```

## Result

```bash

Encrypted ByteArray:
b'\x1a \xce&\x84\x13\xbc\x13\xcfat\x98D\x84\xf4@\x83\x89ZXi\x0f\xd1d\xd2!\x83\x03'      

Decrypted ByteArray:
b'i know what the dog is doing'

```
