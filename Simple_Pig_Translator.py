def pig_it(text):
    sent=text.split()
    pigged=[]
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
    for i in range(len(sent)):
        if sent[i] in alpha and len(sent[i]) == 1:
            sent[i]+="ay"
        elif len(sent[i])>1:
            sent[i] = sent[i][1: -1]+ sent[i][-1]+  sent[i][0]+ "ay"

        pigged.append(sent[i])
            
    return " ".join(pigged)
        
