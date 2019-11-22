def anagrams(word, words):
    list=[]
    worddic={}
    for i in word:
        if i not in worddic:
            worddic[i]=0
        else:
            worddic[i] += 1
    for j in words:
        wordsdic={}
        for k in j:
            if k not in wordsdic:
                wordsdic[k]=0
            else:
                wordsdic[k] += 1
        if wordsdic==worddic:
            list.append(j)
    
    return list
      
