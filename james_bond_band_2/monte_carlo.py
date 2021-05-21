import json
from random import randint

def estimate(m, t, level):
    result=1
    coefficient=1
    for i in range(level):
        result+=coefficient*t[i]
        coefficient*=m[i]
    return result

def promising(coded_message, start, i, words):
    return coded_message[start:i] in words

def decode(coded_message, t, m, words, start, level):
    if start==len(coded_message):
        return estimate(m, t, level)
    else:
        t[level]=len(coded_message)-start
        promising_nodes=[]
        for i in range(len(coded_message), start, -1):
            if promising(coded_message, start, i, words):
                m[level]+=1
                promising_nodes.append(i)
        return decode(coded_message, t, m, words, promising_nodes[randint(0,len(promising_nodes)-1)], level+1)


if __name__=="__main__":
    coded_message=input("Enter coded message: ").lower()
    result=0
    with open("words_dictionary.json") as f:
        words=json.load(f)
    for i in range(20):
        t,m=[0 for i in range(len(coded_message)+1)],[0 for i in range(len(coded_message)+1)]
        level=0
        result+=(decode(coded_message, t, m, words, 0, level))
    print("The estimated count of promising nodes is: {}".format(result//20))
