#Write a program which will mark a spot with an X.
#The map is made of 3 rows of blank squares.
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
vertical = int(position[0])
horizontal = int(position[1])
changed_in_row = map[horizontal-1]
changed_in_row[vertical-1]="X"
#map[horizontal-1][vertical-1]="X" alternative way
print(f"{row1}\n{row2}\n{row3}")

