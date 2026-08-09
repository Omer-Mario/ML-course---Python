s = input('enter word: ')
n = len(s)

current_substring = s[0]
longer_substring = s[0]

for i in range(n-1):
    if s[i+1] >= s[i]:
        current_substring += s[i+1]
    else:
        if len(current_substring) > len(longer_substring):
            longer_substring = current_substring
        current_substring = s[i+1]
           
if len(current_substring) > len(longer_substring):
    longer_substring = current_substring
    
print('Longest substring in alphabetical order is: ' + str(longer_substring))