
# Part 1
freqArray = []
idArray = []
passArray = []
with open('passwords.txt') as my_file:
	for line in my_file:
		threeParts = line.split(' ')
		freqArray.append(threeParts[0])
		idArray.append(threeParts[1])
		passArray.append(threeParts[2].strip('\n'))

lowerbound = None
upperbound = None
identity = None
validCount = 0
currentPass = None
idCount = None

for i in range(0, len(freqArray)):
  minMax = freqArray[i].split('-')
  lowerbound = int(minMax[0])
  upperbound = int(minMax[1])
  identity = idArray[i][0]
  currentPass = passArray[i]
  idCount = currentPass.count(identity)
  # print(idCount)
  if idCount >= lowerbound and idCount <= upperbound:
    validCount = validCount + 1
    # print("valid pass found")
  else:
    # print("invalid pass found")
    pass

print(validCount)

# ----------------------------------------------------------------------------------------------------

# Part 2
freqArray = []
idArray = []
passArray = []
with open('passwords.txt') as my_file:
	for line in my_file:
		threeParts = line.split(' ')
		freqArray.append(threeParts[0])
		idArray.append(threeParts[1])
		passArray.append(threeParts[2].strip('\n'))

lowerbound = None
upperbound = None
identity = None
validCount = 0
currentPass = None
idCount = None

for i in range(0, len(freqArray)):
  minMax = freqArray[i].split('-')
  firstPos = int(minMax[0])
  secondPos = int(minMax[1])
  identity = idArray[i][0]
  currentPass = passArray[i]
  firstChar = currentPass[firstPos-1]
  secondChar = currentPass[secondPos-1]

  if firstChar != secondChar and (firstChar == identity or secondChar == identity):
    validCount = validCount + 1

print(validCount)  