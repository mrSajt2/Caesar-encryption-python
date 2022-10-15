abc = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ "

def crack(data):
    for key in range(len(abc)):
        encrypted_data = ""
        for e in data:
            for i in range(len(abc)):
                if e == abc[i]:
                    encrypted_data += abc[i-key]
        print(encrypted_data, key)