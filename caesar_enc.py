abc = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ "
def encode(data, key):
    data = data.upper()
    encrypted_data = ""
    if key % len(abc) != 0:
        for e in data:
            for i in range(len(abc)):
                if e == abc[i]:
                    while True:
                        if i + key > len(abc):
                            key -= len(abc)
                        else:
                            encrypted_data += abc[i+key]
                            break
        return encrypted_data
    else:
        return "Nem jó kulcsot adtál meg!"

def decode(data, key):
    encrypted_data = ""
    data = data.upper()
    while True:
        if key > len(abc):
            key -= len(abc)
        else:
            break
    for e in data:
        for i in range(len(abc)):
            if e == abc[i]:
                encrypted_data += abc[i-key]
    return encrypted_data
