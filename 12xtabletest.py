#;  2015-05-24  administrator  <administrator@BensBIY-PC>
#;
#;  * Fixed traceback error when entering name.
#;
#;
#;
#;  2015-05-24  administrator  <administrator@BensBIY-PC>
#;
#;   * Added comments to make the program more flegling programmer
#;   friendly ;)
#;
#;
#;  2015-05-24  administrator  <administrator@BensBIY-PC>
#;
#;  * Further edits on syntax error by declaring type of variable later
#;  on in the program.
#;
#;
#;
#;  2015-05-24  jonnyboo6777  <unknownzonemobile@gmail.com>
#;
#;  * Changed variable 'incorrect_answers' to 'incorrectAnswers due to
#;  syntax error.
#;
#;
#;
########################################################################
#; !/usr/bin/env Python
#;  -*- coding: utf-8 -*-
#; 
#;   12xtabletest.py 
#;   
#;   Copyright 2015 jonnyboo6777 <unknownzonemobile@gmail.com>
#;   
#;   This program is free software; you can redistribute it and/or modify
#;   it under the terms of the GNU General Public License as published by
#;   the Free Software Foundation; either version 2 of the License, or
#;   (at your option) any later version.
#;   
#;   This program is distributed in the hope that it will be useful,
#;   but WITHOUT ANY WARRANTY; without even the implied warranty of
#;   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#;   GNU General Public License for more details.
#;   
#;   You should have received a copy of the GNU General Public License
#;   along with this program; if not, write to the Free Software
#;   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#;   MA 02110-1301, USA.
#;   
#;   This program can be used for any assessments if your tutor confirms
#;   that usage of this program is allowed. Do not remove any comments
#;   with semicolons on the comment.
#; 
#;   This program may also be used by tutors in education for Python
#;   programming but under any and all circumstances (unless allowed to do
#;   so by the publisher of this program (contacts are above on line 6))
#;   no edits may be made on any line starting with the following two
#;   charactors:#;.
#;   The programmer may be contacted about any concerns, corrections or
#;   illegal usage at the address above also.
#;
########################################################################

# Declaration of name variable to fix traceback errors
name = "name"
# Request of user's name
name = raw_input("Hello, Please enter your name!\n")
# Declaration of incorrectAnswers variable to store the amount of$
# $ incorrect answers
incorrectAnswers = 0 # Set variable to 0 to remove compilation error
# Introduction
print "Hello!"
print "It is nice to meet you\n"
print "This program will test your 12 times table knowledge.\n"
print "The questions will get harder as the quiz progresses.\n"
print "This quiz is composed of 20 questions.\n"
print "So, lets begin!\n\n"
#Actual beginning of quiz.
answer1 = input("Question 1:\nWhat is 7 * 12?") # Asks user for answer$
# $ for the question
# Detecting if the answer is correct.
if answer1 == 12*7:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1 #Incrementing the$
# $ 'incorrectAnswers' variable
# This is looped a total of 20 times for the 20 questions.
answer2 = input("Question 2:\nWhat is 15 * 12?\n")
if answer2 == 15 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer3 = input("Question 3:\nWhat is 22 * 12?\n")
if answer3 == 22 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer4 = input("Question 4:\nWgat is 29 * 12?\n")
if answer4 == 29 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer5 = input("Question 5:\nWhat is 47 * 12?\n")
if answer5 == 47 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer6 = input("Question 6:\nWhat is 69 * 12?\n")
if answer6 == 61 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer7 = input("Question 7:\nWhat is 85 * 12?\n")
if answer7 == 85 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer8 = input("Question 8:\nWhat is 76 * 12?\n")
if answer8 == 76 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer9 = input("Question 9:\nWhat is 133 * 12?\n")
if answer9 == 133 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer10 = input("Question 10:\nWhat is 190 * 12?\n")
if answer10 == 190 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer11 = input("Question 11:\nWhat is 100000 * 12?\n")
if answer11 == 100000 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer12 = input("Question 12:\nWhat is 350 * 12?\n")
if answer12 == 350 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer13 = input("Question 13:\nWhat is 111 * 12?\n")
if answer13 == 111 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer14 = input("Question 14:\nWhat is 265 * 12?\n")
if answer14 == 265 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer15 = input("Question 15:\nWhat is 167 * 12?\n")
if answer15 == 167 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer16 = input("Question 16:\nWhat is 300 * 12?\n")
if answer16 == 300 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer17 = input("Question 17:\nWhat is 200 * 12?\n")
if answer17 == 200 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer18 = input("Question 18:\nWhat is 380 * 12?\n")
if answer18 == 380 * 12:
	print "Correct!\n" 
else:
	print "Incorrect.\n" 
	incorrectAnswers = incorrectAnswers + 1
answer19 = input("Question 19:\nWhat is 400 * 12?\n")
if answer19 == 400 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
answer20 = input("Question 20:\nWhat is 421 * 12?\n")
if answer20 == 421 * 12:
	print "Correct!\n"
else:
	print "Incorrect.\n"
	incorrectAnswers = incorrectAnswers + 1
str (incorrectAnswers) #Converting the 'incorrectAnswers' int to string
# End of quiz
# Using name variable from above to create a nice congrats to the user.
print "Congratulations", name, "You have completed the quiz!"
# Totaling up of the incorrect answers and telling the player the$
# $ results
print "You have finished the quiz with", #We use end='' to$
# $ place all the print statements on one line.
print incorrectAnswers,
print "incorrect answers!"
# End of program.
