number = int(input("Enter number of students: "))
maxscore = -1
smaxscore = -2
maxstudent = ''
smaxstudent = ''
for i in range (0, number):
    name = str(input("Enter student's name: "))
    score = int(input("Enter score: "))
    if score > maxscore:
        smaxscore = maxscore
        smaxstudent = maxstudent
        maxscore = score
        maxstudent = name
    elif score > smaxscore:
        smaxscore = score
        smaxstudent = name

print("Highest is {0}: {1}".format(maxstudent, maxscore))
print("Second highest is {0}: {1}".format(smaxstudent, smaxscore))


    
