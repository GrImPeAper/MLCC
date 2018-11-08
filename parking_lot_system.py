from abc import ABC, abstractmethod
#Assumed that 1-10 are small lots, 11-17 are medium lots and 18-20 are large lots
class parking:
	def __init__(self):
		self.__occupied=0
		self.id=-1
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
	def __init__(self,vid):
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
	def __init__(self,vid):
		self.type='bike'   #m for motorbike
		print('Motorcycle initialized')
		self.vid=vid
class car(vehicle):
	def __init__(self,vid):
		self.type='car' #c for car
		self.vid = vid
		print('Car initialized')
	
class bus(vehicle):
	def __init__(self,vid):
		self.type='bus' #b for bus
		self.vid = vid
		print('Bus initialized')
		
#initialization of parking lots
sp = [smalpark(i) for i in range(1,11)]
mp = [medpark(i) for i in range(11,18)]
lp = [largepark(i) for i in range(18,21)]

nv=int(input('Enter the number of vehicles'))
buses = []
cars = []
motorcycles = []
for i in range(0,nv):
	a=str(input('Enter vehicle type (m/c/b)'))
	a=a.lower()
	if a == 'm':
		vid=int(input(('Enter bike ID')))
		b=bike(vid)
		motorcycles.append(b)
		
	elif a == 'c':
		vid=int(input(('Enter car ID')))
		cars.append(car(vid))
	elif a == 'b':
		vid=int(input(('Enter bus ID')))
		buses.append(bus(vid))
print('Enter vehicle ids for all vehicles')
for motorcycle in motorcycles:
	occ=0
	for slot in sp:
		if not slot.getslot():
			motorcycle.occupiedslot = int(slot.occupyslot())
			motorcycle.printticket()
			occ=1
			break
	if occ == 0:
		for slot in mp:
			if not slot.getslot():
				motorcycle.occupiedslot = int(slot.occupyslot())
				motorcycle.printticket()
				occ=1
				break
	if occ == 0:
		for slot in lp:
			if not slot.getslot():
				motorcycle.occupiedslot = int(slot.occupyslot())
				motorcycle.printticket()
				occ=1
				break
	if occ == 0:
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
	if occ == 0:
		for slot in lp:
			if not slot.getslot():
				carr.occupiedslot = int(slot.occupyslot())
				carr.printticket()
				occ=1
				break
	if occ == 0:
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
	if occ == 0:
		print('Cant find free space')
		break