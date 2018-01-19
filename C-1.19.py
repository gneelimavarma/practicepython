##C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
##the list [ a , b , c , ..., z ], but without having to type all 26 such
##characters literally.

##ascii_value = ord('a')
##print(ascii_value)
i=0
start = 97 ##ascii of 'a'
result = []
while(i<26):
    result.append(chr(start+i))
    i+=1
print(result)
    
