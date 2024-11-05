def covert_to_caps(list_of_string):
    result = []
    for string in list_of_string:
        result.append(string.upper())
    return result

def convert_to_caps_short(list_of_string):
    return [string.upper() for string in list_of_string]

if __name__ == '__main__':
    print(covert_to_caps(['Python', 'Java', 'Ruby', 'Rust']))
    print(convert_to_caps_short(['Python', 'Java', 'Ruby', 'Rust']))