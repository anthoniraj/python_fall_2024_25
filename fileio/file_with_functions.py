def read_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    data = []
    for line in lines[1:]:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    return data

def find_max(data):
    max_mark = 0
    for line in data:
        if line[2] > max_mark:
            max_mark = line[2]
    return max_mark

def find_min(data):
    min_mark = 20
    for line in data:
        if line[2] < min_mark:
            min_mark = line[2]
    return min_mark

def top_performers(data):
    top =  sorted(data, key=lambda x: x[2], reverse=True)
    return top[:15]

if __name__ == '__main__':
    content = read_file('mid_term_marks.csv')
    print(f"The maximum mark is {find_max(content)}")
    print(f"The minimum mark is {find_min(content)}")
    print(f"The top performers are:")
    for line in top_performers(content):
        print(f"{line[0]}-{line[1]}: {line[2]}")

