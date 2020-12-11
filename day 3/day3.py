adapters = []
with open('simpler.txt') as my_file:
    for line in my_file:
        adapters.append(int(line))

print(adapters)


def searchFunc(inputNum, runningArray, inputsArray):
  nPlus = [inputNum-1,inputNum-2,inputNum-3,inputNum-4,inputNum-5,inputNum-6]
  if inputNum == 0:
    runningArray.append(inputNum)
    return answerFunc(runningArray.reverse())
  else:
    for i in range(0,2):
      currNum = nPlus[i]
      inputNum = None
      if currNum in inputsArray:
        for j in range(3,5):
          if nPlus[j] in inputsArray:
            runningArray.append(currNum)
            runningArray.append(nPlus[j])
            inputNum = nPlus[j]
            return searchFunc(inputNum, runningArray, inputsArray)




def answerFunc(answerArray):
  oneJoltDiffCount = 0
  threeJoltDiffCount = 0
  for i in range(0,len(answerArray)-1):
    if (answerArray[i+1] - answerArray[i]) == 1:
      oneJoltDiffCount = oneJoltDiffCount + 1
    elif (answerArray[i+1] - answerArray[i]) == 3:
      threeJoltDiffCount = threeJoltDiffCount + 1
  
  print(oneJoltDiffCount)
  print(threeJoltDiffCount)
  return oneJoltDiffCount*threeJoltDiffCount



maxVolts = max(adapters) + 3
print(maxVolts)
runningArray = []
searchFunc(maxVolts,runningArray,adapters)