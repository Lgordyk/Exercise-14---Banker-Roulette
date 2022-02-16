
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Get total number of names in the list
length_of_list = len(names)-1

#Print a name from the name list at random between the first name to the last name in the list as the boundaries
print(f"{names[random.randint(0,length_of_list)]} is going to buy the meal today!")