#For Loop
#Calculate the average height of the students.

heights = input("Input a list of student heights: ").split()
sum_height = 0
num = 0

for n in range(len(heights)):
    heights[n] = int(heights[n])
for h in heights:
    sum_height +=h
    num +=1
average_height = sum_height/num
print(f"The average height of the students is {average_height}.")

