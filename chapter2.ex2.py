score=[]#in this program, at first I get the scores from the users then I divide the the numbers 3 and 1, then calculate all the one and three that we have
for i in range(30):#gathering data from the user
    b=input()
    score.append(b)
#print("score=", score)

lose=[]
win=[]
equalities=[]
for i in range(len(score)):#dividing them in three lists

    if score[i]=='0':
        lose.append(score[i])
        #print('lose=', lose)
    elif score[i]=='1':
        equalities.append(score[i])
        #print('equalities= ',equalities )
    elif score[i]=='3':
        win.append(score[i])
Sum=win+equalities
#print(Sum)
total=0
for i in range(len(Sum)):#calculating the sum of all elements in the list Sum
    total=total+int(Sum[i])

print(total,Sum.count('3'))
