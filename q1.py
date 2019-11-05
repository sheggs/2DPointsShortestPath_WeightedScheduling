
def grabPoints(value):
    value = value.replace('(',"")
    value = value.replace(")","")
    value = value.replace(" ","")

    value = value.split(",")
    return value[0],value[1]
def sort(array_cord):
    for i in range(0, len(array_cord)):
        for j in range(0, len(array_cord)):
            x1, y1 = grabPoints(array_cord[j])
            x2, y2 = grabPoints(array_cord[i])
            x1 = float(x1)
            x2 = float(x2)

            if (x2 < x1):
                #print(str(x1) + " " + str(x2))
                temp = array_cord[i]
                array_cord[i] = array_cord[j]
                array_cord[j] = temp;
    return array_cord;
def middleCoOrd(arr):
    middle = int(len(arr) / 2)
    print("Middle Index: " + str(len(arr)/2))
    x, y = grabPoints(arr[middle - 1])
    x1, y1 = grabPoints((arr[middle]))
    x = float(x)
    x1 = float(x1)
    avg_splitline = x + x1
    print("XCORD: " + str(avg_splitline / 2))
    return avg_splitline / 2,middle;

coord = "(-3.0, -6.0)/(-6.0, -5.0)/(-5.0, 3.0)/(1.0, 5.0)/(-4.0, -1.0)/(5.0, 6.0)/(-1.0, 4.0)/(6.0, -7.0)"
coord1 = "";
coord2 = "";
array_cord = coord.split("/")

array_cord = sort(array_cord);
print("Length of Array: " + str(len(array_cord)))

# Question 1
print("Q1: Sort")
# for i in range(0,len(array_cord)):
#     print(array_cord[i]);
# Question 2
print("Q2: Middle co-ord")
middle,middleIndex = middleCoOrd(array_cord)
# print(middle)
# print(array_cord[int(middle) - 1])
# Question 3
print("Q3: Left List")
stringContainer = ""
for i in range(0,middleIndex):
    if( i == (middleIndex - 1)):
        stringContainer += array_cord[i]
    else:
        stringContainer += array_cord[i] + "/"
#LEFT LIST
coord1 = stringContainer.split("/")
print(stringContainer)
# Question 3
print("Q4: Right List")
stringContainer = ""
for i in range(middleIndex, len(array_cord)):
    if( i == (len(array_cord) - 1)):
        stringContainer += array_cord[i]
    else:
        stringContainer += array_cord[i] + "/"

print(stringContainer)
#RIGHT LIST
coord2 = stringContainer.split("/")
# Question 5
print("Q5: Split X-CORD")
# coord 1 = Left list | coord2 = Right lsit
print("Split for Left list, LL")
leftMiddle,LL = middleCoOrd(coord1);
print("Split for right List. LR")
rightMiddle,RR = middleCoOrd(coord2)
RR = int(RR)
# Question 6
print("Q6: Comma-separated indices of points to the left of LL ")

stringContainer = ""
for i in range(0,LL):
    if (i == (LL - 1)):
        stringContainer += coord1[i]
    else:
        stringContainer += coord1[i] + "/"
print(stringContainer)

# Question 7
print("Q7: Comma-separated indices of points to the right of LL but left of L")
stringContainer = ""
for i in range(0,len(array_cord)):
    x, y = grabPoints(array_cord[i])
    if float(x) > leftMiddle and float(x) < middle:
        stringContainer += (array_cord[i])
print(stringContainer)


# Question 8
print("Q8: Comma-separated indices of points to the left of LR but right of L")
stringContainer = ""
for i in range(0,len(array_cord)):
    x, y = grabPoints(array_cord[i])
    if float(x) < rightMiddle and float(x) > middle:
        stringContainer += (array_cord[i])
print(stringContainer)

