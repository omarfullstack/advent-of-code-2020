# Doubles Code
expenses = []
numbersFound = []
with open('stuff.txt') as my_file:
    for line in my_file:
        expenses.append(int(line))


secondNum = 0
for i in range(0,len(expenses)):
  secondNum = 2020 - expenses[i]
  if secondNum in expenses:
    numbersFound.append([secondNum,expenses[i]])
  else:
    pass

print(numbersFound)




# Triplets Code
expenses = []
numbersFound = []
with open('stuff.txt') as my_file:
    for line in my_file:
        expenses.append(int(line))


total = 0
for i in range(0,len(expenses)):
  for j in range(0,len(expenses)-1):
    for k in range(0,len(expenses)-2):
      total = expenses[i] + expenses [j+1] + expenses[k+2]
      #print(str(expenses[i])+ ' , ' + str(expenses[j+1])+ ' , ' + str(expenses[k+2]))

      if total == 2020:
        numbersFound.append([expenses[i],expenses[j+1],expenses[k+2]])
      else:
        pass

print(numbersFound)

  

