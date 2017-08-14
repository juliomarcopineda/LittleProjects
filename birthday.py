# This script demonstrates the "Birthday Problem" or "Birthday Paradox."
# This shows that if there are 23 students in a classroom, the probability
# of having 2 students with the same birthday is 50 percent.
#
# Author: Julio Marco Pineda


import random

NUMBER_OF_STUDENTS = 23
TRIALS = 10000 # Trials can also be interpreted as classrooms

# Return true if a list of birthdays have duplicates. Otherwise return false.
def has_duplicates(lst):

	for i in range(len(lst)):

		if lst.count(lst[i]) > 1:
			return True

	return False

# Given the number of students, assign random birthdays to each.
def generateRandomBirthdays(numberStudents):

	randomBirthdays = []

	for i in range(numberStudents):

		randomBirthdays.append(random.randint(1, 365))

	return randomBirthdays

# Return the proportion of the trials that had duplicate birthdays.
def proportion(trials):

	duplicateCount = 0

	for i in range(trials):

		if has_duplicates(generateRandomBirthdays(NUMBER_OF_STUDENTS)):

			duplicateCount = duplicateCount + 1

	return float(duplicateCount) / TRIALS

if __name__ == "__main__":

	result = proportion(TRIALS)
	print("In %d classrooms with %d students, %.1f%% had students with duplicate birthdays." \
	% (TRIALS, NUMBER_OF_STUDENTS, proportion(TRIALS) * 100))