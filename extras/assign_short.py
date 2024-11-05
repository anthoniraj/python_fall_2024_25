def intialize(temp):
    if temp >= 30:
        return "Hot"
    else:
        return "Cold"

def intiaalize_short(temp):
    return "Hot" if temp >= 30 else "Cold"

if __name__ == '__main__':
    print(intialize(10))