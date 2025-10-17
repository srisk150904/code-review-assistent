# sample.py - intentionally messy code for testing review

import os, sys

def processData(data, flag = False):
    result = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            result.append(data[i]*2)
        else:
            result.append(data[i]*3)
    if flag == True:
        for j in range(len(result)):
            print("Value is " + str(result[j]))
    return result


def very_long_function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t):
    total = 0
    for x in range(100):
        if x % 2 == 0:
            total += x
        else:
            total -= x
    return total


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    output = processData(nums, True)
    print(output)
