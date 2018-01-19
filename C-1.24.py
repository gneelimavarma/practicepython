## Write a short Python function that counts the number of vowels in a given
##character string.
text = input('enter a word')
list1 = list(text)
count = 0
for char in list1:
    if char == 'a' or char =='e' or char =='i' or char =='o' or char =='u':
        count += 1

print('total vowels found',count)
        
