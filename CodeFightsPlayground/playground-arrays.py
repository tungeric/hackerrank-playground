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

# Create number matrix for a minesweeper game
def minesweeper(matrix):
    m = len(matrix)
    n = len(matrix[0])
    num_matrix = [[0 for x in range(n)] for y in range(m)]
    for row in range(0,m):
        for col in range(0,n):
            count = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0 <= row+x < m and 0 <= col+y < n:
                        if matrix[row+x][col+y] == True:
                            if not (x ==0 and y==0):
                                count += 1
                    num_matrix[row][col] = count
    return num_matrix

# Check if equation is correct
# input: predicate: "( 3 * ( 7 - 1 ) - 6 ) / 3 = 4"
# output: True

def arithmeticPredicate(predicate):
    predicate = predicate.replace(" ","")
    equal_idx = predicate.index('=')
    left_side = predicate[0:equal_idx]
    right_side = predicate[equal_idx+1:len(predicate)]
    left_ans = evaluate(left_side)
    right_ans = evaluate(right_side)
    if int(left_ans) == int(right_ans):
        return True
    return False

def evaluate(expression):
    if is_number(expression): return int(expression)
    exp_stack = []
    # find and eliminate parenthesis, add data to stack
    for char in expression:
        if char == ')':
            sub_expression = []
            while exp_stack[-1] != '(':
                sub_expression.insert(0,exp_stack.pop())
            exp_stack.pop() # to get rid of the '('
            exp_stack.append(evaluate(''.join(sub_expression)))
        elif is_number(char):
            if len(exp_stack) > 0 and is_number(exp_stack[-1]):
                exp_stack[-1] += char
            else:
                exp_stack.append(char)
        else:
            exp_stack.append(char)
    
    # find and execute * or /
    idx = 0
    while idx < len(exp_stack):
        if not is_number(exp_stack[idx]):
            num_1 = float(exp_stack[idx-1])
            num_2 = float(exp_stack[idx+1])
            operator = exp_stack[idx]
            if operator == '*' or operator == '/':
                del exp_stack[idx]
                del exp_stack[idx]
                if operator == '*':
                    exp_stack[idx-1] = str(num_1 * num_2)
                elif operator == '/':
                    exp_stack[idx-1] = str(num_1 / num_2)
                idx -=1
        idx += 1                       
    # find and execute + or -
    idx = 0
    while idx < len(exp_stack):
        if not is_number(exp_stack[idx]):
            num_1 = float(exp_stack[idx-1])
            num_2 = float(exp_stack[idx+1])
            operator = exp_stack[idx]
            if operator == '+' or operator == '-':
                del exp_stack[idx]
                del exp_stack[idx]
                if operator == '+':
                    exp_stack[idx-1] = str(num_1 + num_2)
                elif operator == '-':
                    exp_stack[idx-1] = str(num_1 - num_2)
                idx -=1
        idx += 1
    exp_stack[0] = str(round(float(exp_stack[0])))
    return exp_stack[0]
    

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False

# Christmas Thief!

def christmasThief(coworkers):
    # create hash table
    sender_hash = {}
    receiver_hash = {}
    gift_hash = {}
    thieves = []
    for pair in coworkers:
        if pair[0] == pair[1]:
            thieves.append(pair[0])
        else:
            gift_hash[pair[0]] = pair[1]
            if pair[0] in sender_hash:
                sender_hash[pair[0]] += 1
            else:
                sender_hash[pair[0]] = 1
            if pair[1] in receiver_hash:
                receiver_hash[pair[1]] += 1
            else:
                receiver_hash[pair[1]] = 1
    for sender, receiver in gift_hash.items():
        if not receiver in sender_hash:
            thieves.append(sender)
        elif sender_hash[receiver] < receiver_hash[receiver]:
            thieves.append(sender)
    return sorted(thieves)
        


# HELPFUL THINGS:
# interate through dictionary
    # for key, value in counter.items():
    #     if value == 1:
    #         char = key
    #         break

# create 2D array with default value of 0
    # w, h = 8, 5;
    # Matrix = [[0 for x in range(w)] for y in range(h)] 

