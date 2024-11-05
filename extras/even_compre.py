def find_even(mlist):
    even_number_list = []
    for value in mlist:
        if value % 2 == 0:
            even_number_list.append(value*2)
    return even_number_list

def find_even_short(mlist):
    return [ value*2 for value in mlist if value % 2 == 0]

if __name__ =='__main__':
    print(find_even([1,2,3,4,5,6]))
    print(find_even_short([1,2,3,4,5,6]))