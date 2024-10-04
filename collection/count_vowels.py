'''
Count number of vowels in a given name
Input: Programming
output: {'a':1, 'e': 0, 'i': 1, 'o':1, 'u':0}
'''
vowels = {'a':0, 'e': 0, 'i': 0, 'o':0, 'u':0}
name = input("Enter your name: ")
for char in name:
    if char in vowels.keys():
        vowels[char]+=1
print(vowels)