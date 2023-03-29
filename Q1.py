#Lior Vanounou
#313333106
#Q1

def revword(Word:str):
    Word = Word.lower()[::-1]
    return(Word)
    
def countword():
    text_1 = open("text.txt","r")
    text_1=text_1.read()
    text_1 = text_1.strip().split()
    word = text_1[0]
    count=1
    for i in text_1:
        if revword(i) == word:
            count = count+1
    return (count)
            
