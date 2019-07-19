def WordSentence(Sentence1):  
    words1 = Sentence1.split(" ") 
    newWords = [word[::-1] for word in words1] 
    newSentence = " ".join(newWords)   
    return newSentence 
Sentence1 = input()



print(WordSentence(Sentence1)) 
