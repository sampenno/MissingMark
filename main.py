# This script will import a markbook and allow you to estimate a mark
# Written by Samantha Pennington -6/06/2025
# Version 0.4
import numpy
import csv
from sklearn.linear_model import LinearRegression

# Input

# Import the data from a csv file.
# Assumes that the file is marks only.
# datafile is a string which is the name of the csv file to open
def importData (dataFile) : 
    marks = [] #creates an empty list
    marksFile = open(dataFile) # opens data file to read
    marksRaw = csv.reader(marksFile) #reads file
    
    # iterate over each row in the file
    for student in marksRaw : 
        studentMarksInt = []
        
        # iterate over each task converting from a string to an integer
        for mark in student :
            studentMarksInt.append(int(mark))
            
        marks.append(studentMarksInt)
        
    return marks

# Ask the user which Student and Task to estimate mark for
def getWhichTask () :
	student = int(input("Which student to estimate the mark for : "))
	task = int(input("Which task to estimate the mark for : "))
	return student, task


#Process

# Generate an estimated mark
# data is a two dimensional array of the marks and tasks
# student is an integer which is which student to estimate the mark for
# task is an integer which is which task to estimate the mark for
def processEstimate (data, student, task) :
	# Create base data with the task to estimate omitted
    tasksBase = [] # this needs to be an array of arrays with a single item
    marksBase = [] # this is a 1 dimensional array or marks in other tasks
    counter = 1
    for taskNumber in data[0] :
        if counter != task : # So that we omit the task that are estimating
            taskTitle = [counter]
            tasksBase.append(taskTitle)
            marksBase.append(data[student-1][counter - 1]) # -1 as zero indexing
        counter = counter + 1
    # Create the model
    model = LinearRegression()
    model.fit(tasksBase, marksBase)
    mark_prediction = model.predict([[task]])
    return mark_prediction[0]

# Output

# Simple output of the results
# student is an integer which is the student to estimate the mark for
# task is an integer which is which task to estimate the mark for
# estimate is an integer which is the estimated mark
def showResult (student, task, estimate) :
	print(f"Student {student} has an estimated mark of {estimate} for task {task}")

# Coordinates the program

def main():
    dataFile = 'marksSimple.csv'
    marks = importData (dataFile)
    print(marks)
    student, task = getWhichTask ()
    print (f"Student: {student}, Task: {task}")
    estimate = processEstimate (marks, student, task)
    #student = 4
    #task = 3
    #estimate = 81
    showResult (student, task, estimate)


main()


