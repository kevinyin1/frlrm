import csv
import glob, os
import random
from random import randint
from datetime import datetime

f1 = file('LowestFares.csv', 'r')
c1 = csv.reader(f1)

starting_airport = "JFK" #raw_input("What's the starting airport?: ")
#howManyPeople = raw_input("How many adults are going?: ")
#budgetForTrip = raw_input("What's your budget?: ")
startDate = "12/01/2017" #aw_input("What's your start date?: ")
endDate = "2/25/2017" #raw_input("What's your end date?: ")
totalTrip = 0

def getDeals(startDate = None, endDate = None):
	possibleDeals = []

	for row in c1:
		if str(row[4]) == "LOWEST":
			if not startDate == None:
				if datetime.strptime(startDate, "%m/%d/%Y").date() < datetime.strptime(row[2], "%m/%d/%Y %H:%M").date() and datetime.strptime(endDate, "%m/%d/%Y").date() > datetime.strptime(row[2], "%m/%d/%Y %H:%M").date():
					continue

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
			continue
	else:
		return possibleDeals

def getBestDeal():
	possibleDeals = getDeals(startDate, endDate)
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
				#print("NEW LOW -- WAS: " + str(lowestPrice) + " NOW: " + str(flight['totalPrice']))
				lowestPrice = flight['totalPrice']
				bestFlight = flight

	#print(possibleDeals)
	return bestFlight

coords = ["{lat: 35.0433333, lng: -106.6129085}", "{lat: 41.2569516, lng: -70.0637506}", "{lat: 42.7487124, lng: -73.8054981}", "{lat: 17.1417911, lng: -61.790564}", "{lat: 33.6407282, lng: -84.4277001}", "{lat: 24.441938, lng: 54.6500736}", "{lat: 30.194085, lng: -97.67108859999999}", "{lat: 32.3598289, lng: -64.7020387}", "{lat: 41.9388735, lng: -72.68603139999999}", "{lat: 13.0765848, lng: -59.4877921}", "{lat: 36.126317, lng: -86.67737129999999}", "{lat: 4.7014128, lng: -74.1444969}", "{lat: 42.3656132, lng: -71.0095602}", "{lat: 18.4953957, lng: -67.1355779}", "{lat: 44.4706939, lng: -73.1516037}", "{lat: 42.9397059, lng: -78.7295067}", "{lat: 34.1983122, lng: -118.3574036}", "{lat: 39.1774042, lng: -76.6683922}", "{lat: 32.8942676, lng: -80.038159}", "{lat: 41.4124339, lng: -81.84799249999999}", "{lat: 35.2144026, lng: -80.9473146}", "{lat: 21.418612, lng: -77.849724}", "{lat: 10.446315, lng: -75.516454}", "{lat: 21.0403409, lng: -86.873564}", "{lat: 12.188463, lng: -68.960945}", "{lat: 29.1807079, lng: -81.0591529}", "{lat: 38.851242, lng: -77.04023149999999}", "{lat: 39.8560963, lng: -104.6737376}", "{lat: 32.8998091, lng: -97.0403352}", "{lat: 42.2161722, lng: -83.3553842}", "{lat: 40.6895314, lng: -74.1744624}", "{lat: 26.0742344, lng: -80.1506022}", "{lat: 19.2962995, lng: -81.357771}", "{lat: 12.004167, lng: -61.78611100000001}", "{lat: 22.9915431, lng: -82.410078}", "{lat: 20.785278, lng: -76.315}", "{lat: 29.6459109, lng: -95.2768859}", "{lat: 41.0683325, lng: -73.7086641}", "{lat: 38.9531162, lng: -77.45653879999999}", "{lat: 30.49407129999999, lng: -81.6879368}", "{lat: 40.6413111, lng: -73.77813909999999}", "{lat: 17.9333852, lng: -76.7796899}", "{lat: 36.0839998, lng: -115.1537389}", "{lat: 33.9415889, lng: -118.40853}", "{lat: 40.7769271, lng: -73.8739659}", "{lat: 33.8197834, lng: -118.1508396}", "{lat: -12.0240527, lng: -77.112036}", "{lat: 10.5943664, lng: -85.5441512}", "{lat: 18.4484458, lng: -68.9118337}", "{lat: 18.5022634, lng: -77.91443439999999}", "{lat: 28.4311577, lng: -81.308083}", "{lat: 6.170763399999999, lng: -75.4276201}", "{lat: 19.4360762, lng: -99.07190829999999}", "{lat: 29.9922012, lng: -90.25901119999999}", "{lat: 41.3894691, lng: -70.6119605}", "{lat: 25.0439288, lng: -77.4655212}", "{lat: 37.7167503, lng: -122.2130475}", "{lat: 41.9741625, lng: -87.9073214}", "{lat: 42.2680227, lng: -71.8735112}", "{lat: 18.5756545, lng: -72.29489339999999}", "{lat: 26.6857475, lng: -80.0928165}", "{lat: 45.58976939999999, lng: -122.5950942}", "{lat: 39.8743959, lng: -75.2424229}", "{lat: 33.4372686, lng: -112.0077881}", "{lat: 40.4957722, lng: -80.24131129999999}", "{lat: 21.7763463, lng: -72.27133400000001}", "{lat: 19.7553589, lng: -70.563822}", "{lat: 10.5976964, lng: -61.339527}", "{lat: 18.0090714, lng: -66.5625743}", "{lat: 33.8303194, lng: -116.5070468}", "{lat: 18.5622845, lng: -68.3683966}", "{lat: 41.7245271, lng: -71.4304062}", "{lat: 43.6464785, lng: -70.30969739999999}", "{lat: 35.88007899999999, lng: -78.7879963}", "{lat: 37.5065795, lng: -77.3208112}", "{lat: 39.4995907, lng: -119.7680951}", "{lat: 43.1225229, lng: -77.66657219999999}", "{lat: 26.5337051, lng: -81.7553083}", "{lat: 32.7338006, lng: -117.1933038}", "{lat: 32.1294267, lng: -81.2018521}", "{lat: 18.4319537, lng: -69.6720974}", "{lat: 47.4502499, lng: -122.3088165}", "{lat: 37.6213129, lng: -122.3789554}", "{lat: 37.3639472, lng: -121.9289375}", "{lat: 9.9979333, lng: -84.2046714}", "{lat: 18.4375849, lng: -66.00398179999999}", "{lat: 40.7899404, lng: -111.9790706}", "{lat: 38.6950854, lng: -121.5900648}", "{lat: 22.492155, lng: -79.943983}", "{lat: 27.3955284, lng: -82.55452389999999}", "{lat: 19.4021334, lng: -70.6019073}", "{lat: 18.3360608, lng: -64.9722726}", "{lat: 17.701287, lng: -64.805797}", "{lat: 41.4985635, lng: -74.1004385}", "{lat: 18.0418698, lng: -63.1130821}", "{lat: 43.1139301, lng: -76.1101888}", "{lat: 27.9834776, lng: -82.5370781}", "{lat: -0.1225875, lng: -78.35855839999999}", "{lat: 13.733375, lng: -60.950289}"]
airportCodes = ["ABQ","ACK","ALB","ANU","ATL","AUA","AUS","BDA","BDL","BGI","BNA","BOG","BOS","BQN","BTV","BUF","BUR","BWI","CHS","CLE","CLT","CMW","CTG","CUN","CUR","DAB","DCA","DEN","DFW","DTW","EWR","FLL","GCM","GND","HAV","HOG","HOU","HPN","IAD","JAX","JFK","KIN","LAS","LAX","LGA","LGB","LIM","LIR","LRM","MBJ","MCO","MDE","MEX","MSY","MVY","NAS","OAK","ORD","ORH","PAP","PBI","PDX","PHL","PHX","PIT","PLS","POP","POS","PSE","PSP","PUJ","PVD","PWM","RDU","RIC","RNO","ROC","RSW","SAN","SAV","SDQ","SEA","SFO","SJC","SJO","SJU","SLC","SMF","SNU","SRQ","STI","STT","STX","SWF","SXM","SYR","TPA","UIO","UVF"]
def getCoordsString(airportCode):
	return coords[airportCodes.index(airportCode)]

def getRandomFlight():
	possibleDeals = getDeals(startDate, endDate)
	possibleFlights = []
	if not len(possibleDeals) < 5:
		for x in range(0,5):
			randIndex = randint(0, len(possibleDeals))
			possibleFlights.append(possibleDeals[randIndex])

	choose = randint(0, len(possibleFlights))

	flight = possibleFlights[choose]
	return flight

print getRandomFlight()
