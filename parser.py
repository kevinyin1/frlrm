import csv
import glob, os

f1 = file('LowestFares.csv', 'r')
c1 = csv.reader(f1)

starting_airport = raw_input("What's the starting airport?: ")
howManyPeople = raw_input("How many adults are going?: ")
budgetForTrip = raw_input("What's your budget?: ")

totalTrip = 0

possibleDeals = []

for row in c1:
	if str(row[4]) == "LOWEST":
		if str(row[0].lower()) == str(starting_airport).lower():
			print("WOOP")
			flightInfo = {
				"from": row[0],
				"to": row[1],
				"flightDate": row[2],
				"totalPrice": row[5] + row[6],
				"score": row[7],
				"domestic": row[9]
			}
			possibleDeals.append(flightInfo)
	else:
		pass

def getHighestScore(possibleDeals):
	for flight in possibleDeals:
		if flight['score'] == 0:
			possibleDeals.remove(flight)
	
	print(possibleDeals)