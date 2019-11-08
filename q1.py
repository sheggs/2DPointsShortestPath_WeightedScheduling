### FIX ALL QUESTIONS BECAUSE U NEED INDICIES NOT CO-ORD
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
    #print("Middle Index: " + str(len(arr)/2))
    x, y = grabPoints(arr[middle - 1])
    x1, y1 = grabPoints((arr[middle]))
    x = float(x)
    x1 = float(x1)
    avg_splitline = x + x1
    #print("XCORD: " + str(avg_splitline / 2))
    return avg_splitline / 2,middle;
def findPos(x,arr):
    for i in range(0, len(arr)):
        if(arr[i] == x):
            return i
coord = "(-3.0, -6.0)/(-6.0, -5.0)/(-5.0, 3.0)/(1.0, 5.0)/(-4.0, -1.0)/(5.0, 6.0)/(-1.0, 4.0)/(6.0, -7.0)"
coord1 = "";
coord2 = "";
static_cord = coord.split("/")
array_cord = coord.split("/")

array_cord = sort(array_cord);
print("Length of Array: " + str(len(array_cord)))

# Question 1
print("Q1: Sort")
stringContainer = ""
for i in range(0,len(array_cord)):
    if(i == (len(array_cord) - 1)):
        stringContainer += (array_cord[i]);
    else:
        stringContainer += (array_cord[i]) + "/";
print(stringContainer)
stringContainer = ""
for i in range(0,len(array_cord)):
    if(i == (len(array_cord) - 1)):
        stringContainer += str(findPos(array_cord[i], static_cord))
    else:
        stringContainer += str(findPos(array_cord[i],static_cord)) + ","
print(stringContainer);
# Question 2
print("Q2: Middle co-ord")
middle,middleIndex = middleCoOrd(array_cord)
print(middle);
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
print(stringContainer)
coord1 = stringContainer.split("/")
LeftList = stringContainer.split("/")
stringContainer = ""
for i in range(0,len(LeftList)):
    if(i == (len(LeftList) - 1)):
        stringContainer += str(findPos(LeftList[i], static_cord))
    else:
        stringContainer += str(findPos(LeftList[i],static_cord)) + ","
#LEFT LIST
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
RightList = stringContainer.split("/")
coord2 = stringContainer.split("/")
stringContainer = ""
for i in range(0,len(RightList)):
    if(i == (len(RightList) - 1)):
        stringContainer += str(findPos(RightList[i], static_cord))
    else:
        stringContainer += str(findPos(RightList[i],static_cord)) + ","
print(stringContainer)
#RIGHT LIST
# Question 5
print("Q5: Split X-CORD")
# coord 1 = Left list | coord2 = Right lsit
print("Split for Left list, LL")
leftMiddle,LL = middleCoOrd(coord1);
print("Middle L: " + str(leftMiddle))
print("L Index (LL): " + str(LL))
print("Split for right List. LR")
rightMiddle,RR = middleCoOrd(coord2)
print("Middle R: " + str(rightMiddle))
print("R Index (LR): " + str(RR))
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
LL_ARR = stringContainer.split("/")
stringContainer = ""
for i in range(0,len(LL_ARR)):
    if(i == (len(LL_ARR) - 1)):
        stringContainer += str(findPos(LL_ARR[i], static_cord))
    else:
        stringContainer += str(findPos(LL_ARR[i],static_cord)) + ","
print(stringContainer)
# Question 7
print("Q7: Comma-separated indices of points to the right of LL but left of L")
stringContainer = ""
for i in range(0,len(array_cord)):
    x, y = grabPoints(array_cord[i])
    if float(x) > leftMiddle and float(x) < middle:
        stringContainer += (array_cord[i]) + "/"
print(stringContainer)
Q7_ARR = stringContainer.split("/")
stringContainer = ""
for i in range(0,len(Q7_ARR)):
    if(i == (len(Q7_ARR) - 1)):
        stringContainer += str(findPos(Q7_ARR[i], static_cord))
    else:
        stringContainer += str(findPos(Q7_ARR[i],static_cord)) + ","
print(stringContainer)

# Question 8
print("Q8: Comma-separated indices of points to the left of LR but right of L")
stringContainer = ""
for i in range(0,len(array_cord)):
    x, y = grabPoints(array_cord[i])
    if float(x) < rightMiddle and float(x) > middle:
        stringContainer += (array_cord[i])
print(stringContainer)
Q8_ARR = stringContainer.split("/")
stringContainer = ""
for i in range(0,len(Q8_ARR)):
    if(i == (len(Q7_ARR) - 1)):
        stringContainer += str(findPos(Q7_ARR[i], static_cord))
    else:
        stringContainer += str(findPos(Q7_ARR[i],static_cord)) + ","
print(stringContainer)
#Question 9
print("Q9: Comma-separated indices of points to the right of LR ")

stringContainer = ""
for i in range(0,len(array_cord)):
    x, y = grabPoints(array_cord[i])
    if float(x) > rightMiddle:
        stringContainer += (array_cord[i])
print(stringContainer)


#Question 10: Completed on Java COM2031_CW file
print("Q10: Comma-separated indices of the points SL that are in the strip around LL (leave empty if none):")
min_d_fromJava = 5.0990195135927845;
lowerBound = leftMiddle - min_d_fromJava;
upperBound = leftMiddle + min_d_fromJava;
temp_array = [];
Q10coord_storage = ""
Q10point_storage = ""
for i in range(0,len(coord1)):
    x,y = grabPoints(coord1[i])
    x = float(x)
    if(x>lowerBound and x<upperBound):
        Q10coord_storage += coord1[i] + ","
        Q10point_storage += str(findPos(coord1[i], static_cord)) + ","
print("Upper Bound: " + str(upperBound) + " | Lower Bound: " + str(lowerBound))
print("- Coord : " + Q10coord_storage);
print("- Point : " + Q10point_storage)
# middle,middleIndex = middleCoOrd(array_cord)
# print(middle)
# print(middleIndex)
# stringContainer = ""
# d = 2.23606797749979
# print("INDEX LIST")
# for i in range(0,len(static_cord)):
#     x, y = grabPoints(static_cord[i])
#     if float(x) < middle and float(x) > middle - 2.23606797749979:
#         #print(float(x))
#         stringContainer += str(i) + ","
#
#     if float(x) > middle and float(x) < middle + 2.23606797749979:
#         #print("__ POINT __")
#         #print(float(x))
#         stringContainer += str(i) + ","
#
# print(stringContainer)

# Question 11: Completed on Java COM2031_CW file
print("Q11: Minimal distance dL between all points to the left of L: 5.0990195135927845")
# Strip Calculation: On Java use this {new Point(-6.0,-5.0),new Point(-5.0,3.0),new Point(-4.0,-1.0),new Point(-3.0,-6.0)}

print("Q12: Comma-separated list of indices i of the points SR that are in the δ-strip around LR (leave empty if none): dR 2.23606797749979 ")
min_d_fromJava = 2.23606797749979;
lowerBound = rightMiddle - min_d_fromJava;
upperBound = rightMiddle + min_d_fromJava;
Q11coord_storage = ""
Q11point_storage = ""
for i in range(0,len(coord2)):
    x,y = grabPoints(coord2[i])
    x = float(x)
    if(x>lowerBound and x<upperBound):
        Q11coord_storage += coord2[i] + ","
        Q11point_storage += str(findPos(coord2[i], static_cord)) + ","
print("Upper Bound: " + str(upperBound) + " | Lower Bound: " + str(lowerBound))
print("- Coord : " + Q11coord_storage);
print("- Point : " + Q11point_storage)


print("Q13: Minimal distance δR between all points to the right of L: 2.23606797749979")

print("Q14: Comma-separated list of indices i of the points that are in the δ-strip around L (leave empty if none):")
print("d = 2.236")
min_d_fromJava = 2.23606797749979;
lowerBound = middle - min_d_fromJava;
upperBound = middle + min_d_fromJava;
Q14coord_storage = ""
Q14point_storage = ""
for i in range(0,len(array_cord)):
    x,y = grabPoints(array_cord[i])
    x = float(x)
    if(x>lowerBound and x<upperBound):
        Q14coord_storage += array_cord[i] + ","
        Q14point_storage += str(findPos(array_cord[i], static_cord)) + ","
print("Upper Bound: " + str(upperBound) + " | Lower Bound: " + str(lowerBound))
print("- Coord : " + Q14coord_storage);
print("- Point : " + Q14point_storage)


print("Q15: d=2.23606797749979")

