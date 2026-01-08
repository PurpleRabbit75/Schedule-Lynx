import os
import string
import pandas
import numpy as np
import pickle
import ast

# Example of a file path:
# "/home/adam/Desktop/This is my txt file!"

def pathExists(path):
    if (os.path.exists(path)):
        return True
    else:
        return False


def importFile(importPath, printing = True):
    if (pathExists(importPath) == False):
        importPath  = input("Please enter a valid file path to a .txt file:\n")
    with open(importPath, "r") as inputDocument:
        file = inputDocument.read()
        inputDocument.close()
    if (printing): print("Your file has been succesfully imported.\n")
    return file



# Example of a file path:
# "/home/adam/Desktop/This is my txt file!"
def makeNewFileName(oldName):
        newFileName = oldName
        if (os.path.exists(oldName)):
            while (os.path.exists(newFileName)):
                splitPath = os.path.split(oldName)
                fileBase = splitPath[0]
                fileName = splitPath[1]
                for i in range (10):
                    number = str(i)
                    if (fileName[len(fileName)-1] == number):        
                        newFileName = fileName[:(len(fileName))-1] + str(int(number)+1)
                        testedName = makeNewFileName(newFileName)
                        return testedName
                if (fileName[len(fileName)-1] != number):
                    newFileName = fileName + "0"
                    testedName = makeNewFileName(newFileName)
                    return testedName
        
        else:
            return newFileName
    

def exportFile(file, exportPath, printing = False):

    path = makeNewFileName(exportPath)
    strfile = str(file)
    with open(path, 'x') as outputDocument: # Change the 'x' to 'w' to allow overwrites.
        for i in range (len(strfile)):
            outputDocument.write(strfile[i])
        outputDocument.close()
    
    if (printing):
        print("Your file has been succesfully exported.")
        print("")
    
 

def importExcel(path, nanToNone = False):
    cols = []
    frame = pandas.read_excel(path)
    l,h = frame.shape
    if (nanToNone):
        frame = frame.replace(np.nan, None)
    cols.append(frame.columns.tolist())
        
    for j in range(h):
        row = []
        for i in range(l):
            item = frame.iloc[i,j]
            row.append(item)
        cols.append(row)

    transposed = cols
    return transposed



def exportExcel(file, path):
    print("Function exportExcel does not exist yet.")



def importPickle(path):
    with open(path, mode='r') as file:
        f = pickle.load(file)
    return f



def exportPickle(file, path):
    with open(path, mode = 'w') as outputFile:
        pickle.dump(outputFile, file)
   


def importJSON(path):
    print("importJSON is not yet written")


def exportJSON(file, path):
   print("exportJSON is not yet written")



def printList(List, addIndices = False, mode = "print", printing = True):
    if (mode == "print"):
        
        
        if (addIndices == True):
            if (printing): print("Now printing your list:\n\n")
            for i in range(len(List)):
                print(i, List[i])
            if (printing): print("\n\nYour list has finished printing now.\n")
            
        else:
            if (printing): print("Now printing your list:\n\n")
            for i in range(len(List)):
                print(List[i])
            if (printing): print("\n\nYour list has finished printing now.\n")
          
          
    elif (mode == "return"):
        if (addIndices == True):
            output = ""
            for i in range(len(List)):
                output = output + str(i) + " " + str(List[i]) + "\n"
            return output

        else:
            output = ""
            for i in range(len(List)):
                output = output + str(List[i]) + "\n"
            return output
        
        
    else:
        print("Invalid mode passed to function printList()/logList(). Proceeding by default to \"print\" mode.")
        printList(List, addIndices, "print")


def logList(List, addIndices = False, mode = "print", printing = True):
    printList(List, addIndices, mode, printing)
    
    
def clearDuplicates(List, printing = True):
    if (printing): print("Removing duplicates from your list...")
    newList = []
    for item in List:
        if (item not in newList):
            newList.append(item)
    if (printing): print("Your list contains no duplicates now.\n")
    return newList


def sort(List): return sorted(List)


def dictionary(filePath = "/home/adam/Desktop/dictionary.txt"):
    dictionaryStr = ""
    dictionary = []
    
    if (pathExists(filePath)):
        dictionaryStr = importFile(filePath, printing = False)
    else:
        dictionaryStr = importFile(input("Please enter the file path of your dictionary file:\n"))
        
    for word in dictionaryStr.split("\n"):
        dictionary.append(word)
        
    return dictionary


def remove(List, item):
    newList = []
    for i in List:
        if (i != item):
            newList.append(i)
    return newList


def removeBlanks(List):
    newList = List
    for whitespace in (string.whitespace):
        newList = remove(newList, whitespace)
    return newList

def clearBlanks(List):
    return removeBlanks(List)


def setType(List, Type, mode = 'clip'):
    newList = []
    
    if (mode != "clip" and mode != "convert" and mode != "log"):
        print("ERROR: Invalid mode passed to setType(). Defaulting to \"log\" mode...")
        newList = setType(List, Type, "log")
    
    for item in List:
        if (type(item) == Type):
            newList.append(item)
        else:
            if (mode == "clip"):
                pass
            elif (mode == "convert"):
                newList.append(Type(item))
            elif (mode == "log"):
                print(item)
            
                
    return newList



def logLists(listOfLists, mode = "print"):
    
    def __makeColumn(data): # For internal calling in logLists()
        data = setType(data, str, "convert")
        longestLen = 0
        assembled = []
        
        for item in data:
            if (len(item) > longestLen):
                longestLen = len(item)
        
        for item in data:
            while (len(item) < longestLen):
                item = item + " "
            item = item + "|"
            assembled.append(item)
         
        return assembled



    def __makeTable(columns): # For internal calling in logLists()
        output = ""
        lenLongestList = len(columns[0])
        for i in range(lenLongestList):
            for List in columns:
                output = output + List[i]
            output = output + "\n"
        return output


        
    def __assembleData(colImmutable): # For internal calling in logLists()
        columns = colImmutable
        standardLen = 0
        for List in columns:
            if (len(List) > standardLen):
                standardLen = len(List)
            if (len(List) == 0):
                List.append(" ")
                
        for List in columns:
            while (len(List) < standardLen):
                List.append(" " * (len(List[0])-1) + "|")
        return columns
    
    columnated = []
    for List in listOfLists:
        columnated.append(__makeColumn(List))
    assembled = __assembleData(columnated)
    output = __makeTable(assembled)
    if (mode == "print"):
        print(output)
    elif (mode == "return"):
        return output
    else:
        print("Invalid mode entered. Returning your data through this function as a string.")
        return output


def printLists(listOfLists, mode = "print"):
    logLists(listOfLists, mode)

def toString(List, seperator = ""):
    output = ""
    for item in List:
        output = output + str(item) + seperator
    return output

def reverse(List):
    newList = []
    length = len(List)
    for i in range(length - 1, -1, -1):
        newList.append(List[i])
    return newList
        
       
def printAscii(start = 0, stop = 100):
    for i in range(start, stop):
        print(i, chr(i))
        
        
def primes(filePath = "/home/adam/Desktop/Primes_Index"):
    
    file = ""
    primes = []
    
    if (pathExists(filePath)):
        file = importFile(filePath, printing = False)
        
    else:
        while (pathExists(filePath) == False):
            file = importFile(input("Please enter the file path of your primes list .txt file:\n"))
        
    for num in file.split("\n"):
        primes.append(num)
        
    return primes


def intlen(Int):
    INT = Int
    counter = 0
    while (INT > 1):
        counter += 1
        INT = (INT / 10)
    return counter


def logDict(Dict):
    for key in list(Dict):
        print(key, Dict[key])


def replace(String, chunkA, chunkB):
    
    newString = ''
    Len = len(chunkA)
    pieces = []
    
    
    for char in String:
        pieces.append(char)
    
    
    skipIndex = -1
    for i in range(len(String) - Len):
        if (i > skipIndex):
            chunk = ''
            for j in range(Len):
                chunk = chunk + String[i+j]
                
            if (chunk == chunkA):
                pieces[i : i + Len] = chunkB
                skipIndex = i + Len
            else:
                pieces[i : i + Len] = chunk
         
         
    return ''.join(pieces)


def splitAtIndex(string, index):
    return string[:index], string[index:]


def toList(string_of_list):
    return ast.literal_eval(string_of_list)



# def toList(string_of_list):
#     string = string_of_list[1:len(string_of_list)-1]
#     stops = ["'", '"', "[", "(", "{"]
#     restarts = ["'", '"', "]", ")", "}"]
#     output = []
#     stopped = False
#     stopChar = ''
#     tempString = ''
#     for char in string:
#         print(char)
#         if (char in stops and not stopped):
#             stopChar = char
#             stopped = True
#             print("stopping...")
#         if (char in restarts and stopped and char == stopChar):
#             stopped = False
#             tempString = tempString + char
#             print("restarting...")
            
#         if stopped:
#             tempString = tempString + char
#             print("Stopped. Appending...")
#         else:
#             if (char == ","):
#                 output.append(tempString)
#                 tempString = ''
#             else:
#                 tempString = tempString + char
    
#     def checkForInt(string):
#         digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#         isAllDigits = True
#         for char in string:
#             if (char not in digits):
#                 isAllDigits = False
#         return isAllDigits
    
#     def checkForFloat(string):
#         digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
#         isAllDigits = True
#         for char in string:
#             if (char not in digits):
#                 isAllDigits = False
#         return isAllDigits

    
#     for i in range(len(output)):
#         item = output[i]
#         if (item == "None"):
#             output[i] = None
#         elif (item == "True"):
#             output[i] = True
#         elif (item == "False"):
#             output[i] = False
#         elif checkForInt(item):
#             output[i] = int(item)
#         elif checkForFloat(item):
#             output[i] = float(item)
#         elif (item[0] == "[" and item[len(item)] == "]" and "," in item):
#             output[i] = toList(output[i])
        
        

#     return output
        




            # if (char in ["'", '"']):
            #     if(stopped):
            #         stopped = False
            #     else:
            #         stopped = True


    # print(string)



   
#print(intlen(1000))




# def __makeColumn(data): # For internal calling in logLists()
#     data = setType(data, str, "convert")
#     longestLen = 0
#     assembled = []
#     
#     for item in data:
#         if (len(item) > longestLen):
#             longestLen = len(item)
#     
#     for item in data:
#         while (len(item) < longestLen):
#             item = item + " "
#         item = item + "|"
#         assembled.append(item)
#      
#     return assembled
# 
# 
# 
# def __makeTable(columns): # For internal calling in logLists()
#     output = ""
#     lenLongestList = len(columns[0])
#     for i in range(lenLongestList):
#         for List in columns:
#             output = output + List[i]
#         output = output + "\n"
#     return output
# 
# 
#     
# def __assembleData(colImmutable): # For internal calling in logLists()
#     columns = colImmutable
#     standardLen = 0
#     for List in columns:
#         if (len(List) > standardLen):
#             standardLen = len(List)
#         if (len(List) == 0):
#             List.append(" ")
#             
#     for List in columns:
#         while (len(List) < standardLen):
#             List.append(" " * (len(List[0])-1) + "|")
#     return columns
# 
# def logLists(listOfLists, mode = "print"):
#     columnated = []
#     for List in listOfLists:
#         columnated.append(__makeColumn(List))
#     assembled = __assembleData(columnated)
#     output = __makeTable(assembled)
#     if (mode == "print"):
#         print(output)
#     elif (mode == "return"):
#         return output
#     else:
#         print("Invalid mode entered. Returning your data through this function as a string.")
#         return output


        