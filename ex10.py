input_word = input("enter the word to verify: ")
if(len(input_word)>0):
    palindrome=True
    i=0
    j=len(input_word)-1
    while(i<j):
        if(input_word[i]!=input_word[j]):
            palindrome=False
            break
        else:
            i+=1
            j-=1
if(palindrome==True):
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")   