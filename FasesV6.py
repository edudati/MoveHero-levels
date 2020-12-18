import random
import math

''' ************************ 
    VARIABLES YOU CAN CHANGE
*************************'''
fileName = "Name_of_output_file"
tGame = 601                     # Game time (seconds)
minInt = 0.27                   # Minimum possible interval between balls
maxInt = 0.70                   # Maximum possible interval between balls
weight = [35, 15, 0, 15, 35]    # Balls distribution by column (%)
validDistribution = 5           # Tolerance between balls distribution setted (weight) and the output (%)
kExternalBall = 1               # If two balls drop in oposite corners (1-5) or (5-1) in sequence. The time of 2nd ball will be multiplied by kExternalBall, thus you can increase the chosen time for 2nd ball changing this value and offer more time for the player to reach the ball in the opposite corner


''' Declare other variables (do not change)'''
tNow = 0
prevBall = 0
currentBall = 0
tempChooseBall = 0
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
validCol = []
validColList = []
population = [1, 2, 3, 4, 5]
nBalls = int(round(tGame / ((minInt + maxInt) / 2), 0))
colList = random.choices(population, weight, k=nBalls)

''' List with only the columns with balls'''
c = 0
while c < len(weight):
    if weight[c] != 0:
        validCol.append(c + 1)
    c += 1

''' Create the sequence of balls where the columns do not repeat'''
while True:
    for n in colList:
        if n == prevBall:
            while True:
                tempChooseBall = random.choice(validCol)
                if tempChooseBall != n:
                    break
            validColList.append(tempChooseBall)
            currentBall = tempChooseBall
        else:
            validColList.append(n)
            currentBall = n
        prevBall = currentBall
    '''validation of the list according values in weight'''
    difBall1 = round(validColList.count(1) / len(validColList) * 100, 2)
    difBall2 = round(validColList.count(2) / len(validColList) * 100, 2)
    difBall3 = round(validColList.count(3) / len(validColList) * 100, 2)
    difBall4 = round(validColList.count(4) / len(validColList) * 100, 2)
    difBall5 = round(validColList.count(5) / len(validColList) * 100, 2)
    if math.fabs(weight[0] - difBall1) <= validDistribution \
            and math.fabs(weight[1] - difBall2) <= validDistribution \
            and math.fabs(weight[2] - difBall3) <= validDistribution \
            and math.fabs(weight[3] - difBall4) <= validDistribution \
            and math.fabs(weight[4] - difBall5) <= validDistribution:
        break
    validColList.clear()
prevBall = 0

'''looping to fill the json file'''
for n in validColList:
    '''set the time value to be attributed to the ball'''
    addTime = round(random.uniform(minInt, maxInt), 2)
    if (n == 1 and prevBall == 5) or (n == 5 and prevBall == 1):
        addTime *= round(kExternalBall, 2)
    tNow += addTime
    prevBall = n

    ''' insert a time value in each column'''
    if n == 1:
        col1.append(round(tNow, 2))
    elif n == 2:
        col2.append(round(tNow, 2))
    elif n == 3:
        col3.append(round(tNow, 2))
    elif n == 4:
        col4.append(round(tNow, 2))
    else:
        col5.append(round(tNow, 2))

    '''end json'''
    if tNow >= tGame:
        break

print("\n-=-= SETTINGS OUTPUT -=-=-=\n")
print("Active collumns: {}".format(validCol))
print("Initial collumns setted:                  {}".format(colList))
print('Adjusted collumns with no repeated falls: {}\n'.format(validColList))

print("Time:{:.0f}minutes {:.0f}seconds".format(round(max(col1 + col2 + col3 + col4 + col5) // 60, 0),
                                                round(max(col1 + col2 + col3 + col4 + col5) % 60, 0)))
print("Total balls: {}".format(len(col1) + len(col2) + len(col3) + len(col4) + len(col5)))
print("The range interval between balls: {}sec to {}sec".format(minInt, maxInt))

print("\n% distribution of balls:")
print("Column 1: {}%".format(round(difBall1, 2)))
print("Column 2: {}%".format(round(difBall2, 2)))
print("Column 3: {}%".format(round(difBall3, 2)))
print("Column 4: {}%".format(round(difBall4, 2)))
print("Column 5: {}%".format(round(difBall5, 2)))
print(
    "The diference between the % setted and the % created is less than {}% for each collumn.".format(validDistribution))

print("\nRight side balls: {}%".format(round(difBall4 + difBall5, 2)))
print("Left side balls: {}%".format(round(difBall1 + difBall2, 2)))
print("Internal Balls: {}%".format(round(difBall2 + difBall3 + difBall4, 2)))
print("External Balls: {}%".format(round(difBall1 + difBall5, 2)))

print("\nCopy below this line and paste in a json file to create the notes for MoveHero:\n"
      "------------------------------------------------------------------------------\n")
print('["",', col1, ",\n", col2, ",\n", col3, ",\n", col4, ",\n", col5, "]")

'''create report file whit settings
report = open('REPORT-{}.txt'.format(fileName), 'w')
report.write("\n-=-= SETTINGS OUTPUT -=-=-=\n")
report.write("Active collumns: {}".format(validCol))
report.write("Initial collumns setted:                  {}".format(colList))
report.write('Adjusted collumns with no repeated falls: {}\n'.format(validColList))
report.write("Time:{:.0f}minutes {:.0f}seconds".format(round(max(col1 + col2 + col3 + col4 + col5) // 60, 0),
                                                       round(max(col1 + col2 + col3 + col4 + col5) % 60, 0)))
report.write("Total balls: {}".format(len(col1) + len(col2) + len(col3) + len(col4) + len(col5)))
report.write("The range interval between balls: {}sec to {}sec".format(minInt, maxInt))
report.write("\n% distribution of balls:")
report.write("Column 1: {}%".format(difBall1))
report.write("Column 2: {}%".format(difBall2))
report.write("Column 3: {}%".format(difBall3))
report.write("Column 4: {}%".format(difBall4))
report.write("Column 5: {}%".format(difBall5))
report.write(
    "Diference between the % setted and the % created is less than {}% for each collumn itself.".format(validDistribution))
report.write("\nRight side balls: {}%".format(round(difBall4 + difBall5, 2)))
report.write("Left side balls: {}%".format(round(difBall1 + difBall2), 2))
report.write("Internal Balls: {}%".format(round(difBall2 + difBall3 + difBall4), 2))
report.write("External Balls: {}%".format(round(difBall1 + difBall5, 2)))
report.write("\nCopy above this line and paste in a json file to create the notes for MoveHero:\n"
             "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
report.write('["",', col1, ",\n", col2, ",\n", col3, ",\n", col4, ",\n", col5, "]")
report.close()

create json file for MoveHero
notes = open('NOTES-{}.txt'.format(fileName), 'w')
notes.write('["",', col1, ",\n", col2, ",\n", col3, ",\n", col4, ",\n", col5, "]")
notes.close()'''
