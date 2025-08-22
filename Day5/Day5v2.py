#Determine the highest score
student_scores = input("Input a list of student scores: \n").split()

for i in range(len(student_scores)):
    student_scores[i] = int(student_scores[i])

score = 0
max_score = 0
for s in student_scores:
    if s>=score:
        max_score = s
        score = s
    else:
        max_score = score
print(f"The highest score in the class is: {max_score}.")




