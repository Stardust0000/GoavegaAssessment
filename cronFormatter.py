userInput = input()
data = userInput.split()
n = len(data)
def cronFieldValidation():
    for i in range(0, n):
        # Minutes
        if (i == 0):
                minVal = 0
                maxVal = 59
                cornPart = data[i]
                minute = specialCharacterRules(cornPart, minVal, maxVal)
        # Hours
        elif (i == 1):
                minVal = 0
                maxVal = 23
                cornPart = data[i]
                hours = specialCharacterRules(cornPart, minVal, maxVal)
        # Day of month:
        elif (i == 2):
                minVal = 1
                maxVal = 31
                cornPart = data[i]
                dayOfMonth = specialCharacterRules(cornPart, minVal, maxVal)
        # Month:
        elif (i == 3):
                cornPart = data[i]
                minVal = 1
                maxVal = 12
                month = specialCharacterRules(cornPart, minVal, maxVal)
        # Day of Week 
        elif (i == 4):
                cornPart = data[i]
                minVal = 1
                maxVal = 7
                dayOfWeek = specialCharacterRules(cornPart, minVal, maxVal)

    print("minute",end="        ")
    for i in range(0, len(minute)):
         print( minute[i],end=" ")            
    
    print()
    print("hours",end="         ")
    for i in range(0, len(hours)):
        print( hours[i],end=" ")
    print()
    print("day of month ",end=" ")
    for i in range(0, len(dayOfMonth)):
        print( dayOfMonth[i],end=" ") 

    print()
    print("month",end="         ")
    for i in range(0, len(month)):
        print( month[i],end=" ") 

    print()
    print("day of week ",end="  ")
    for i in range(0, len(dayOfWeek)):
        print( dayOfWeek[i],end=" ") 
   
    print()
    print(f"Command       {data[5]}")
        

def specialCharacterRules(data,minVal,maxVal):
    if "/" in data:
        result = forwardSlash(data, minVal, maxVal)
    elif "," in data:
        result = comma(data)
    elif "-" in data:
        result = dash(data)
    elif "*" in data:
        result = asterisk(minVal, maxVal)
    else:
        result = data
    return result 

# Special Character Rules
def forwardSlash(data, minVal, maxVal):
    strData = data.split('/')
    left = strData[0]
    right = strData[1]
    if left.isdigit():
        start = int(left)
    else:
        start = minVal
    stop = int(right)
    result = []
    for i in range(start,maxVal+1,stop):
        result.append(i)
    return result

def comma(data):
    strData = data.split(",")
    minVal = int(strData[0])
    maxVal = int(strData[1])
    result = [minVal, maxVal]
    return result

def dash(data):
    strData = data.split("-")
    minVal = int(strData[0])   
    maxVal = int(strData[1])
    result = []
    for i in range(minVal, maxVal+1):
        result.append(i)
    return result

def asterisk(minVal, maxVal):
    result = []
    for i in range(minVal, maxVal+1):
        result.append(i)
    return result

cronFieldValidation()
