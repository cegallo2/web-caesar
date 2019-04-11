def alphabet_position(letter):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    idx = 0
    for i in range(len(alphabet)):
        if alphabet[i] == letter.lower():
            idx = i
    return idx

def rotate_character(char, rot):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_idx = (alphabet_position(char) + rot)%26
    if char.isupper():
        return alphabet[new_idx].upper()
    else:
        return alphabet[new_idx].lower()

def rotate_string(text, rot):
    new_text = ''
    for i in range(len(text)):
        if text[i].isalpha():
            new_text = new_text + rotate_character(text[i],rot)
        else:
            new_text = new_text + text[i]
    return new_text


