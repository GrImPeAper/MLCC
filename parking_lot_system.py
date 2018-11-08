from abc import ABC, abstractmethod

class parking:
	def __init__(self):
		self.__occupied=0
		self.id=-1
	#def getslotid(self):
	#	return self.id
	def occupyslot(self):
		self.__occupied=1
		return self.id
	def getslot(self):
		return self.__occupied


class smalpark(parking):
	def __init__(self,id):
		super().__init__()
		self.id=id
		
		
class medpark(parking):
	def __init__(self,id):
		super().__init__()
		self.id=id
		
		
class largepark(parking):
	def __init__(self,id):
		super().__init__()
		self.id=id
		


class vehicle:
	type='d'
	@abstractmethod
	def __init__(self):
		self.vid = -1
		self.occupiedslot=-1
		pass
	def occupylot(self,v):
		v.occupylot()
	def givid(self,vid):
		self.vid=vid
	def printticket(self):
		print ('\t\t\tTicket\n')
		print ('Vehicle type:' + self.type)
		print ('Vehicle ID:' + str(self.vid))
		print ('Parking slot:' +  str(self.occupiedslot))


class bike(vehicle):
	def __init__(self):
		self.type='m'   #m for motorbike
		print('Motorcycle initialized')
class car(vehicle):
	def __init__(self):
		self.type='c' #c for car
		print('Car initialized')
	
class bus(vehicle):
	def __init__(self):
		self.type='b' #b for bus
		print('Bus initialized')
		
#initialization of parking lots
sp = [smalpark(i) for i in range(1,11)]
mp = [medpark(i) for i in range(11,18)]
lp = [largepark(i) for i in range(18,21)]

nc=int(input('Enter the number of cars'))
nm=int(input('Enter the number of motorcycles'))
nb=int(input('Enter the number of buses'))

motorcycles = [ bike() for i in range (0,nm)]
cars = [ car() for i in  range(0,nc)]
buses = [ bus() for i in range(0,nb)]
print('Enter vehicle ids for all vehicles')
for i in cars:
	c = int(input('Enter Car ID'))
	i.givid(c)
for i in motorcycles:
	c = int(input('Enter motorcycle ID'))
	i.givid(c)
for i in buses:
	c = int(input('Enter bus ID'))
	i.givid(c)

for motorcycle in motorcycles:
	occ=0
	for slot in sp:
		if not slot.getslot():
			motorcycle.occupiedslot = int(slot.occupyslot())
			motorcycle.printticket()
			occ=1
			break
	if occ is 0:
		for slot in mp:
			if not slot.getslot():
				motorcycle.occupiedslot = int(slot.occupyslot())
				motorcycle.printticket()
				occ=1
				break
	if occ is 0:
		for slot in lp:
			if not slot.getslot():
				motorcycle.occupiedslot = int(slot.occupyslot())
				motorcycle.printticket()
				occ=1
				break
	if occ is 0:
		print('Cant find free slots')
		break

for carr in cars:
	occ=0
	for slot in mp:
		if not slot.getslot():
			carr.occupiedslot = int(slot.occupyslot())
			carr.printticket()
			occ=1
			break
	if occ is 0:
		for slot in lp:
			if not slot.getslot():
				carr.occupiedslot = int(slot.occupyslot())
				carr.printticket()
				occ=1
				break
	if occ is 0:
		print('Cant find freespace')
		break

for buss in buses:
	occ=0
	for slot in lp:
		if not slot.getslot():
			buss.occupiedslot = int(slot.occupyslot())
			buss.printticket()
			occ=1
			break
	if occ is 0:
		print('Cant find free space')
		break