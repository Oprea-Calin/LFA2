dict = {
    "S": ["aA", "dE"],
    "A": ["aB", "aS"],
    "B":["bC"],
    "C":["bD", "bB"],
    "D":["cD", " "],
    "E":[" "]
}

n = int(input("Care este lungimea maxima pentru cuvinte?"))
p=0
word=[]
for i in range(n):                        #pentru fiecare litera disponibila din cele n date, incercam sa construim un cuvant acceptat de automat
    if p==0:
        for r in dict["S"]:
            word.append(r)
        p+=1
    else:
        if p==1:
            tempword=[]
            for w in word:
                if(w[-1]!=" "):
                    for elem in dict[w[-1]]:
                        tempword.append(w[:-1]+elem)
            word=tempword
result=[]
for i in dict:
    ok=0
    for j in dict[i]:
        if j==" ":                     #caz special in caz ca lungimea maxima este 1
            ok=1
        if ok ==1:
            result.append(i)
for i in word:
    if len(i)==n+1:
        if i[n] in result:
            print(i[:-1])