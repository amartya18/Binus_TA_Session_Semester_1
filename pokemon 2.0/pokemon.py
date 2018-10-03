import random
import sys

playerx = 0
playery = 0

#the map being loaded
file = open("map.txt","r")
temp = file.read().split("\n")
tile = ["" for i in range(len(temp))]
file.close()

file = open("playerposition.txt","r")
temp1 = file.read().split(",")
file.close()

for i in range(0,2):
	temp1[i] = int(temp1[i])

print("")
for row in range(len(temp)):
	tile[row] = list(temp[row])
	for col in range(len(tile[row])):
		if row == temp1[1] and col == temp1[0]:
			print("x",end=" ")
			playerx = col
			playery = row
		else:
			if tile[row][col] == "0":
				print("o",end=" ")
	
			if tile[row][col] == "2":
				print("#",end=" ")
		
	print("")
	col = col
	row = row


#save and exit
def save():
	file = open("playerposition.txt","w")
	temp = ""
	temp += str(playerx) + "," + str(playery)
	file.write(temp)
	file.close()
	sys.exit()

#The menu
print('''
-------------------
Lets Play Pokemon!
-------------------
[w] Move UP
[a] Move LEFT
[s] Move DOWN
[d] Move RIGHT
[1] Save and Exit
------------------
	''')

#player movement
while True:

	if tile[playerx][playery] == "2":
		chance = random.randint(0,5)
		if chance == 0:
			print('''You encountered a pokemon :D''')
			catch = input("You are catching the pokemon! ")
			chance2  = random.randint(0,3)
			if chance2 == 0:
				print("you catched a pokemon! :D")	
			else:
				print("better luck next time!")		

	option = input("Input your choice... ")
	if option == "w":
		if playery - 1 >= 0:
			playery -= 1
	elif option == "a":
		if playerx - 1 >= 0:
			playerx -= 1
	elif option == "s":
		if playery + 1 <= row:
			playery += 1
	elif option == "d":
		if playerx + 1 <= col:
			playerx += 1
	elif option == "1":
		save()

	#map after movement
	for x in range(0, row):
		for y in range (0, col):
			if y == playerx and x == playery:
				print("x",end=" ")
			else:
				if tile[x][y] == "0":
					print("o",end=" ")
				elif tile[x][y] == "2":
					print("#",end=" ")
				elif tile[x][y] == "1":
					print("o",end=" ")
		print("")

	