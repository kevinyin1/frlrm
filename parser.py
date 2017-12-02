import csv
import glob, os
import random

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
			flightInfo = {
				"from": row[0],
				"to": row[1],
				"flightDate": row[2],
				"totalPrice": float(row[5]) + float(row[6]),
				"score": row[7],
				"domestic": row[9]
			}
			possibleDeals.append(flightInfo)
	else:
		pass

def getBestDeal(possibleDeals):
	highestScore = 0
	bestFlight = None
	for flight in possibleDeals:
		print flight['score']
		if flight['score'] == 0:
			possibleDeals.remove(flight)
			continue
		elif int(flight['score']) > highestScore:
			highestScore = flight['score']
			bestFlight = flight

	if highestScore == 0:
		lowestPrice = 100000
		for flight in possibleDeals:
			if flight['totalPrice'] == 0:
				possibleDeals.remove(flight)
				continue
			elif float(flight['totalPrice']) < float(lowestPrice):
				print("NEW LOW -- WAS: " + str(lowestPrice) + " NOW: " + str(flight['totalPrice']))
				lowestPrice = flight['totalPrice']
				bestFlight = flight

	#print(possibleDeals)
	return bestFlight

print getRandomDeal(possibleDeals)
