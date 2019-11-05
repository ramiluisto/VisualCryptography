import Image
import numpy
import random
import math
import scipy

# Name of the two plain images
PlainImage1 = "Rami.jpg"
PlainImage2 = "Anne.jpg"
# Name of the resulting image
ResultImage = "Heart.jpg"
# Name of the output files
OutputFile1 = "Output1.jpg"
OutputFile2= "Output2.jpg"
# Name of the output test image
TestOutput = "Overlay.jpg"


# A function to discretisize imagematrices.
# is assumes that the values of the imported
# image are between 0 (black) and 255 (white).
# It transforms them to the form of 
# 0 (black) - 1 (white) by "cutting up in the middle".
def matrixSimplifier(ImageMatrix):
    for j in range(len(ImageMatrix)):
        for i in range(len(ImageMatrix[j])):
            if ImageMatrix[j][i] > 127:
                ImageMatrix[j][i] = 1
            else:
                ImageMatrix[j][i] = 0


# A scaler to be used in the end 
# as an "inverse" for the matrixSimplifier
# function if needed.
def matrixComplifier(ImageMatrix):
    for j in range(len(ImageMatrix)):
        for i in range(len(ImageMatrix[j])):
            if ImageMatrix[j][i] != 0:
                ImageMatrix[j][i] = 255


def randomSelector(Amount, GivenList):
    # This function returns a specified
    # AMOUNT of disjoint random elements
    # of a GIVENLIST in a random order
    # in a list form.
    # This function requires the module
    # RANDOM.
    # If the specified AMOUNT is greater
    # than the length of GIVENLIST,
    # it is set to equal the length.
    # If the specified AMOUNT is less
    # than zero, it is set to equal 0.
    # If the specified AMOUNT is non-integer
    # it is turned into an integer with the
    # int()-method.

    # We create a copy of the input list 
    # in order to not alter the original.
    CopyOfGivenList = GivenList
    # Priming the original.
    ReturnedList = []

    # Sanitazing AMOUNT
    Amount = int(Amount)
    if Amount > len(GivenList):
        Amount = len(GivenList)
    if Amount < 0:
        Amount = 0

    # Here we pick the elements by taking a random
    # index and popping out the element in that
    # position.
    for j in range(Amount):
        randomIndex = random.randint(0,len(CopyOfGivenList)-1)
        randomListElement = CopyOfGivenList.pop(randomIndex)
        ReturnedList.append(randomListElement)

    return ReturnedList




# Opening the plain images
Plain1 = Image.open(PlainImage1)
Plain2 = Image.open(PlainImage2)
WantedResult = Image.open(ResultImage)

# Transforming the images into arrays.
Array1 = numpy.array(Plain1).tolist()
Array2 = numpy.array(Plain2).tolist()
Array3 = numpy.array(WantedResult).tolist()

# Simplifying the image arrays to 
# 0 - 1 -matrices.
matrixSimplifier(Array1)
matrixSimplifier(Array2)
matrixSimplifier(Array3)

# Check the discretized result. (For debugging.)
scipy.misc.imsave("Kuva1Tester.jpg",Array1)
scipy.misc.imsave("Kuva2Tester.jpg",Array2)
scipy.misc.imsave("Kuva3Tester.jpg",Array3)

# Getting image dimensions.
ImageHeight = len(Array1)
ImageWidth = len(Array1[0])

# Checking that all dimensions match.
if (len(Array1) != len(Array2)) or (len(Array1) != len(Array3)):
    print ""
    print "IMAGE DIMENSION MISMATCH! OVERFLOW MIGHT HAPPEN!"
    print ""    
if (len(Array1[0]) != len(Array2[0])) or (len(Array1[0]) != len(Array3[0])):
    print ""
    print "IMAGE DIMENSION MISMATCH! OVERFLOW MIGHT HAPPEN!"
    print ""    

# Creating result matrices.
OutputImage1 = numpy.zeros((2*ImageHeight,2*ImageWidth))
OutputImage2 = numpy.zeros((2*ImageHeight,2*ImageWidth))
ResultTester = numpy.zeros((2*ImageHeight,2*ImageWidth))

# This is the main algorithm.
# We go through every pixel in original image,
# and break down what we do with three
# embedded if-clauses:
# "
# Is the pixel of HiddenImage (Array3) black or white?
#     Is the pixel of second input (Array2) black or white?
#         Is the pixel of first input (Array1) black or white?
#
#
for j in range(ImageHeight):
    for i in range(ImageWidth):
        # If Hidden is BLACK
        if Array3[j][i] == 0:
            # If Hidden is BLACK and input2 is BLACK
            if Array2[j][i] == 0:
                # If Hidden is BLACK and input2 is BLACK and input1 is BLACK
                if Array1[j][i] == 0:
                    TypeNumbers = randomSelector(2,range(4))
                    j1 = int(math.ceil(TypeNumbers[0]/2)) 
                    i1 = int(TypeNumbers[0] % 2)
                    j2 = int(math.ceil(TypeNumbers[1] / 2)) 
                    i2 = int(TypeNumbers[1] % 2)
                    OutputImage1[2*j + j1][2*i + i1] = 1
                    OutputImage2[2*j + j2][2*i + i2] = 1
                # If Hidden is BLACK and input2 is BLACK and input1 is WHITE
                elif Array1[j][i] == 1:
                    TypeNumber1 = random.randint(0,3)
                    TypeNumber2 = (TypeNumber1 + random.randint(1,3)) % 4
                    j1 = int(math.ceil(TypeNumber1/2)) 
                    i1 = int(TypeNumber1 % 2)
                    j2 = int(math.ceil(TypeNumber2 / 2)) 
                    i2 = int(TypeNumber2 % 2)
                    OutputImage1[2*j + j1][2*i + i1] = 1
                    OutputImage1[2*j + j2][2*i + i2] = 1
                    if TypeNumber1 != 0 and TypeNumber2 != 0:
                        TypeNumber3 = 0
                    elif TypeNumber1 != 1 and TypeNumber2 != 1:
                        TypeNumber3 = 1
                    elif TypeNumber1 != 2 and TypeNumber2 != 2:
                        TypeNumber3 = 2
                    elif TypeNumber1 != 3 and TypeNumber2 != 3:
                        TypeNumber3 = 3
                    j3 = int(math.ceil(TypeNumber3/2)) 
                    i3 = int(TypeNumber3 % 2)
                    OutputImage2[2*j + j3][2*i + i3] = 1
            # If Hidden is BLACK and input2 is WHITE
            if Array2[j][i] == 1:
                # If Hidden is BLACK and input2 is WHITE and input1 is BLACK
                if Array1[j][i] == 0:
                    TypeNumber1 = random.randint(0,3)
                    TypeNumber2 = (TypeNumber1 + random.randint(1,3)) % 4
                    j1 = int(math.ceil(TypeNumber1/2)) 
                    i1 = int(TypeNumber1 % 2)
                    j2 = int(math.ceil(TypeNumber2 / 2)) 
                    i2 = int(TypeNumber2 % 2)
                    OutputImage2[2*j + j1][2*i + i1] = 1
                    OutputImage2[2*j + j2][2*i + i2] = 1
                    if TypeNumber1 != 0 and TypeNumber2 != 0:
                        TypeNumber3 = 0
                    elif TypeNumber1 != 1 and TypeNumber2 != 1:
                        TypeNumber3 = 1
                    elif TypeNumber1 != 2 and TypeNumber2 != 2:
                        TypeNumber3 = 2
                    elif TypeNumber1 != 3 and TypeNumber2 != 3:
                        TypeNumber3 = 3
                    j3 = int(math.ceil(TypeNumber3/2)) 
                    i3 = int(TypeNumber3 % 2)
                    OutputImage1[2*j + j3][2*i + i3] = 1
                # If Hidden is BLACK and input2 is WHITE and input1 is WHITE
                elif Array1[j][i] == 1:
                    TypeNumber1 = random.randint(0,3)
                    TypeNumber2 = (TypeNumber1 + random.randint(1,3)) % 4
                    j1 = int(math.ceil(TypeNumber1/2)) 
                    i1 = int(TypeNumber1 % 2)
                    j2 = int(math.ceil(TypeNumber2 / 2)) 
                    i2 = int(TypeNumber2 % 2)
                    OutputImage1[2*j + j1][2*i + i1] = 1
                    OutputImage1[2*j + j2][2*i + i2] = 1
                    for k in range(2):
                        for m in range(2):
                            OutputImage2[2*j+k][2*i+m] = 1
                    OutputImage2[2*j + j1][2*i + i1] = 0
                    OutputImage2[2*j + j2][2*i + i2] = 0

        # If Hidden is WHITE
        if Array3[j][i] == 1:
            # If Hidden is WHITE and input2 is BLACK
            if Array2[j][i] == 0:
                # If Hidden is WHITE and input2 is BLACK and input1 is BLACK
                if Array1[j][i] == 0:
                    TypeNumber1 = random.randint(0,3)
                    j1 = int(math.ceil(TypeNumber1/2)) 
                    i1 = int(TypeNumber1 % 2)
                    OutputImage1[2*j + j1][2*i + i1] = 1
                    OutputImage2[2*j + j1][2*i + i1] = 1
                # If Hidden is WHITE and input2 is BLACK and input1 is WHITE
                elif Array1[j][i] == 1:
                    TypeNumber1 = random.randint(0,3)
                    TypeNumber2 = (TypeNumber1 + random.randint(1,3)) % 4
                    j1 = int(math.ceil(TypeNumber1/2)) 
                    i1 = int(TypeNumber1 % 2)
                    j2 = int(math.ceil(TypeNumber2 / 2)) 
                    i2 = int(TypeNumber2 % 2)
                    OutputImage1[2*j + j1][2*i + i1] = 1
                    OutputImage1[2*j + j2][2*i + i2] = 1
                    OutputImage2[2*j + j2][2*i + i2] = 1
            # If Hidden is WHITE and input2 is WHITE
            if Array2[j][i] == 1:
                # If Hidden is WHITE and input2 is WHITE and input1 is BLACK
                if Array1[j][i] == 0: 
                    TypeNumber1 = random.randint(0,3)
                    TypeNumber2 = (TypeNumber1 + random.randint(1,3)) % 4
                    j1 = int(math.ceil(TypeNumber1/2)) 
                    i1 = int(TypeNumber1 % 2)
                    j2 = int(math.ceil(TypeNumber2 / 2)) 
                    i2 = int(TypeNumber2 % 2)
                    OutputImage2[2*j + j1][2*i + i1] = 1
                    OutputImage2[2*j + j2][2*i + i2] = 1
                    OutputImage1[2*j +j2][2*i + i2] = 1
                # If Hidden is WHITE and input2 is WHITE and input1 is WHITE
                elif Array1[j][i] == 1:
                    TypeNumber1 = random.randint(0,3)
                    TypeNumber2 = (TypeNumber1 + random.randint(1,3)) % 4
                    j1 = int(math.ceil(TypeNumber1/2)) 
                    i1 = int(TypeNumber1 % 2)
                    j2 = int(math.ceil(TypeNumber2 / 2)) 
                    i2 = int(TypeNumber2 % 2)
                    OutputImage1[2*j + j1][2*i + i1] = 1
                    OutputImage1[2*j + j2][2*i + i2] = 1
                    OutputImage2[2*j + j1][2*i + i1] = 1
                    if TypeNumber1 != 0 and TypeNumber2 != 0:
                        TypeNumber3 = 0
                    elif TypeNumber1 != 1 and TypeNumber2 != 1:
                        TypeNumber3 = 1
                    elif TypeNumber1 != 2 and TypeNumber2 != 2:
                        TypeNumber3 = 2
                    elif TypeNumber1 != 3 and TypeNumber2 != 3:
                        TypeNumber3 = 3
                    j3 = int(math.ceil(TypeNumber3/2)) 
                    i3 = int(TypeNumber3 % 2)
                    OutputImage2[2*j + j3][2*i + i3] = 1




# Creating a matrix that looks what the overlay image
# should look like.
for j in range(len(ResultTester)):
    for i in range(len(ResultTester[j])):
        if OutputImage1[j][i] == 0 or OutputImage2[j][i] == 0:
            ResultTester[j][i] = 0
        else:
            ResultTester[j][i] = 1


# Changing matrix entries 0 -> 0, 1 -> 255.
matrixComplifier(OutputImage1)
matrixComplifier(OutputImage2)
matrixComplifier(ResultTester)


# Writing the matrices to image files.
scipy.misc.imsave(OutputFile1,OutputImage1)
scipy.misc.imsave(OutputFile2,OutputImage2)
scipy.misc.imsave(TestOutput,ResultTester)
