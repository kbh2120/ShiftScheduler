# ShiftScheduler


##Team Members

Kristen Howard kbh2120 

Sandya Sankarram ss4119 

Ami Kumar ak3284

Sara Garner skg2122


## High Level Description
###Problem

Given a large number of people with varying time constraints, randomly place them in a preset number of groups / event shifts subject to these constraints.

###Example

We are hosting an all­day hackathon and we have 100 volunteers. We want to break them up (randomly) and assign them to 8 different 2 hour shifts. But some people can only do certain shifts, whereas other people are free all day. We want to find the optimal way to assign people to shifts such that we accommodate those conflicts and have the same number of volunteers in each shift. Our project will output the best assignments for people to a shift, noting any issues so that the manager can deal with those manually.

###Solution

This problem can be modeled as a Constraint Satisfaction Problem (CSP) and solved using a CSP solver. Our work will be to take this problem and create appropriate data structures and variables to use a CSP solver. Our goal (depending on time) is to also create a user­friendly (non­programmer) interface to input this data (the available shifts, the people, and their constraints). This could be reading from a .csv or excel document, or it could be in some GUI using TkInter .



## Architecture
Key classes we will define:
### ￼FileParser

Parses the input data from a Google Form given a filename and produces a SSProblem.

### SSProblem

Represents the Constraint Satisfaction Problem. Contains the variables (an array of Person objects) and their constraints (Shifts).

###Person

Represents a person with constraints. Keeps track of what Shifts the person can and cannot do (their constraints), as well as any information about the person (name, phone number, etc.)

###Shift
Represents an event shift. Contains any information the user wants to keep about the shift, such as start and end time, location, etc.

###FileWriter
Creates a user­friendly csv or excel file given the solution to a SSProblem

###ShiftScheduler
Master program that controls the entire program and problem solving process.



##Libraries Used
###￼￼￼￼￼Constraint
￼￼CSP Solver. Solves the problem of scheduling given a SSProblem
###￼￼￼￼￼TkInter
￼￼￼￼GUI for specifying what fields to read when creating the Person and Shift classes
###￼Pandas
￼￼￼￼Reading and writing of excel and csv files.



## ￼Division of Labor
###All
Model problem as a CSP with variables, constraints (conceptually)
###Kristie
Create FileWriter for user­friendly output of solution (print to csv file) Create FileParser for inputting problem (both using pandas)
###Sandya
Create sample form data for parsing (how to create a Google Form that outputs data in the correct format for our parser)
Create simple TkInter GUI for specifying which fields to read for the Person class and for the Shift class (from the sample form)
###Sara
Create and map conceptual problem to an instance of a SSProblem
###Ami
Create ShiftScheduler class to manage program, including Person and Shift classes
