def get_num_words(text):
    return len(text.split())

def get_num_of_each_char(text):
    chars = {}
    
    for char in text.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    return chars

def sort_on(items):
    return items["num"]

def sorted_chars(chars):
    sorted_arr = []

    for key in chars:
        dict = {}

        dict["char"] = key
        dict["num"] = chars[key]

        sorted_arr.append(dict)

    sorted_arr.sort(reverse=True, key=sort_on)

    return sorted_arr