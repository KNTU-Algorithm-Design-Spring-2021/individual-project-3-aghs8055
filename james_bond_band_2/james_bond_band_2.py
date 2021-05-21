import json

def promising(coded_message, start, i, words):
    return coded_message[start:i] in words

def decode(coded_message, message, words, start):
    if start==len(coded_message):
        print("The message is: {}".format(" ".join(message)))
        #To print all result comment exit()
        exit()
    else:
        for i in range(len(coded_message), start, -1):
            if promising(coded_message, start, i, words):
                message.append(coded_message[start:i])
                decode(coded_message, message, words, i)
                message.pop()

if __name__=="__main__":
    coded_message=input("Enter coded message: ").lower()
    message=[]
    with open("words_dictionary.json") as f:
        words=json.load(f)
    decode(coded_message, message, words, 0)
