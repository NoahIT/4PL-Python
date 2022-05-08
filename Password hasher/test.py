def generateKey(p_string, key):
    p_string = entry_1.get()
    keyword = entry_2.get()
    key = generateKey(p_string, keyword)
    cipher_text = cipherText(p_string, key)

    key = list(key)
    if len(p_string) == len(key):
        return(key)
    else:
        for i in range(len(p_string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cipherText(): #p_string, key):
    p_string = entry_1.get()
    keyword = entry_2.get()
    key = generateKey(p_string, keyword)
    cipher_text = cipherText(p_string, key)

    cipher_text = []
    for i in range(len(p_string)):
        x = (ord(p_string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))


def originalText(): #cipher_text, key):
    p_string = entry_1.get()
    keyword = entry_2.get()
    key = generateKey(p_string, keyword)
    cipher_text = cipherText(p_string, key)
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))


    p_string = entry_1.get()
    keyword = entry_2.get()
    key = generateKey(p_string, keyword)
    cipher_text = cipherText(p_string, key)