
import hashlib
cript=hashlib.md5()
cript.update(b"ola")
cript.hexdigest()

### 2 ###

import hashlib

text = input('Digite o que deseja ser criptografado: ')
mdc=hashlib.md5()
mdc.update(text)
mdc.hexdigest()
