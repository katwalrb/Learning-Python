#List
state_midwest = ["Ohio","Indiana","Kentucky"]
state_midwest[1] = "Pennsylvania"
state_midwest.append("Indiana") #adding single item to the list
#print(state)
state_midwest.extend(["Michigan", "West Virginia"]) #adding multiple items to the list
#print(state)
state_west = ["California","Oregon","Washington"]
states = [state_midwest,state_west]
print(states)

