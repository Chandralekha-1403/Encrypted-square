import math
class NoInput(Exception):
    pass
class InvalidInput(Exception):
    pass
def fun(n):
    n=n.lower() # to down case all the letters
    st=""
    cnt=0
    r=0
    c=0
    #to remove punctuation
    for i in n:
        if i.isalnum():
            st += i
    for i in st:    
        cnt=cnt+1 # count of the string
    print("The normalised code is: ",st)
    c=math.ceil(math.sqrt(cnt)) # to calculate no of columns
    r=math.ceil(cnt/c) # to calculate no of rows
    l=cnt
    k=0
    str=""
    s = [[0 for j in range(c) ]  #to initialize all elements to zero
        for i in range(r)]
    # string is copied to the matrix
    for i in range(r):
        for j in range(c):
            if k >= l:
                s[i][j] = ""
                k += 1
            else:
                s[i][j] = st[k]  
                k += 1
    for i in range(c): #to convert the normalized text to encrypted code
        for j in range(r):
            if s[j][i] == "" :
                continue
            str+=s[j][i]
        str=str+" "
    print("The encrypted code is: ",str)
if __name__=="__main__":
    try:
        n=input("Enter the code: ")
        if(n==''):
            raise NoInput
        if(len(n)<3):
            raise InvalidInput
        fun(n)
    except NoInput:
        print("Enter a valid English Text")
    except InvalidInput:
        print("Enter minimum 3 length String")
        fun(n)
