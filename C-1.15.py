##C-1.15 Write a Python function that takes a sequence of numbers and determines
##if all the numbers are different from each other (that is, they are distinct).

def duplicate(seq):
    for val in range(len(seq)):
        k=val+1
        while(k < len(seq)):
              if(seq[val] == seq[k]):
                  print('Found duplicate of',seq[val])
                  return
              k+=1
    print('all values are distinct')

def duplicateSimple(list1):
    set1 = set(list1)
    if(len(set1)==len(list1)):
        print('No duplicates found')
    else:
        print('Duplicates found')

##duplicate([2,3,4,5,5])
duplicateSimple([2,5,3,6])
