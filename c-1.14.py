##Write a short Python function that takes a sequence of integer values and
##determines if there is a distinct pair of numbers in the sequence whose
##product is odd.

def findPair(input):
    
    result = []
    for k in range(len(input)):
        for m in range(k+1,len(input)):
            if((input[k]*input[m])%2!=0):
                result.append((input[k],input[m]))
    print(result)   
findPair([3,2,9])        


