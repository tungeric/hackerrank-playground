# FIRST DUPLICATE

def firstDuplicate(a):
    counter = {}
    idx = 0
    duplicate = -1
    while idx < len(a):
        if a[idx] in counter:
            duplicate = a[idx]
            break
        else:
            counter[a[idx]] = 1
        idx += 1
    return duplicate

# FIRST ONE WITHOUT DUPLICATES

def firstNotRepeatingCharacter(s):
    counter = {}
    idx = 0
    bucket = []
    while idx < len(s):
        if s[idx] in counter:
            counter[s[idx]] += 1
            if s[idx] in bucket:
                bucket.remove(s[idx])
        else:
            counter[s[idx]] = 1
            bucket.append(s[idx])
        idx += 1
    if len(bucket) == 0:
        return '_'
    return bucket[0]

# ROTATE IMAGE

def rotateImage(a):
    w = len(a)
    rotatedImage = [[0 for x in range(w)] for y in range(w)]
    for x in range(0,w):
        for y in range(0,w):
            rotatedImage[y][w-x-1] = a[x][y]
    return rotatedImage

# CRYPT

def isCryptSolution(crypt, solution):
    solutionHash = createSolutionHash(solution)
    numWordArray = []
    for word in crypt:
        numWordArray.append(convertToNum(word, solutionHash))
    
    # check if anything starts with 0
    for val in numWordArray:
        if len(val) > 1 and val[0] == '0':
            return False
    
    # check if numbers add up
    numArray = []
    for numWord in numWordArray:
        numArray.append(int(numWord))
    if not numArray[0] + numArray[1] == numArray[2]:
         return False
    return True
    
def createSolutionHash(solution):
    solutionHash = {}
    for subArray in solution:
        solutionHash[subArray[0]] = subArray[1]
    return solutionHash
    
def convertToNum(str, solutionHash):
    numCharArray = []
    for char in str:
        numCharArray.append(getNumForChar(char, solutionHash))
    return "".join(numCharArray)

def getNumForChar(char, solution):
    return solution[char]


# CHRISTMAS TOYS
# input: toys: [[6,2,4], 
            #  [], 
            #  [], 
            #  [], 
            #  [5,1], 
            #  [], 
            #  [3]]
# output: [[0], 
            #  [6,2,4], 
            #  [3,5,1]]

def christmasToys(toys):
    topNode = findTopNode(toys)
    result = []
    currLevel = [topNode]
    while currLevel:
        result.append(currLevel)
        nextLevel = []
        for node in currLevel:
            for nextNode in toys[node]:
                nextLevel.append(nextNode)
        currLevel = nextLevel
    return result
    
def findTopNode(toys):
    root = -1
    flattenedToys = []
    for i in toys:
        for j in i:
            flattenedToys.append(j)
    numToys = len(toys)
    for x in range(0, numToys):
        if not x in flattenedToys:
            root = x
            break
    return root

# Solving linear equations
# input: question: [["11=2x+5","2"], 
#  ["18=5x-2","4"]]
# output: 50

def gradingHomework(question):
    score_array = []
    for equation in question:
        prompt, answer = equation
        equal_index = prompt.index('=')
        x_index = prompt.index('x')
        y = int(prompt[0:equal_index])
        m = int(prompt[equal_index+1:x_index])
        if x_index < len(prompt)-1:
            b = int(prompt[x_index+1:])
            x = (y - b) / m
        else:
            x = y / m
        if x == int(answer):
            score_array.append(100)
        else:
            score_array.append(0)
    avg_score = round(sum(score_array) / len(score_array),3)
    return avg_score

    



# HELPFUL THINGS:
# interate through dictionary
    # for key, value in counter.items():
    #     if value == 1:
    #         char = key
    #         break

# create 2D array with default value of 0
    # w, h = 8, 5;
    # Matrix = [[0 for x in range(w)] for y in range(h)] 

