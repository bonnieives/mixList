"""

    ASSIGNMENT #1
    QUESTION 8
    AUTHOR: Bonnie Ives de Castro Nunes
    DATE: September 15th, 2023
    
"""

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

print(" ----- Lists informed ----- ")
print("List one:", listOne)
print("List two:", listTwo)

lenOne = len(listOne)
lenTwo = len(listTwo)

finalList = []

for itemOne in range(0,lenOne):

    if ((itemOne % 2) == 1):
        finalList.append(listOne[itemOne])

for itemTwo in range(0,lenTwo):

    if ((itemTwo % 2) == 0):
        finalList.append(listTwo[itemTwo])

print("\n ----- Final list -----")
print(finalList)
