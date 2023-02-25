# If you wish you can import any modules from the standard library
# Do not use modules that are not in the standard library
import sys


def processArray(array):
    '''Modify this function to process `array` as indicated
    in the question. At the end, return the appropriate 
    value.

    Please create appropriate classes, and use appropriate
    data structures as necessary.

    Do not print anything in this function.

    Submit this entire program (not just this function)
    as your answer
    '''
    count = 0 
    sm = 0
    array.append(1)
    for i in array:
        num = i 
        ctr = 0
        while(num):
            ctr+=1
            num//=10
        if(ctr==2):
            sm+=i
        else:
            if(sm>=75):
                count+=1
            sm = 0 
    return count   # modify this appropriately
                # make sure to return an int (not float/string)


def run():
    array = []
    for line in sys.stdin:
        intval = int(line)
        if intval < 0:
            break
        array.append(intval)
    result = processArray(array)
    print(result)

if __name__ == '__main__':
    run()
