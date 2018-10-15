import random

class Team:
	def __init__(self,name,efect):
		self.name=name
		self.efect=efect
		self.restart()
		self.champWinned=0

	def darGoles(self):
		return float(random.random())*float(10.0)*float(self.efect)

	def chandePoints(self,pe):
		self.pointsPlayed=self.pointsPlayed+3
		self.pointsEarned=self.pointsEarned+pe

	def changeEfectivity(self):
		self.efect=float(pointsEarned/pointsPlayed)

	def restart(self):
		self.pointsEarned=0
		self.pointsPlayed=0

class Championship:
	def __init__(self,teams):
		self.teams=teams
		self.prepareChampionship()
		print("\nEQUIPOS CARGADOS.")
		self.printTeams()

	def prepareChampionship(self):
		self.auxTeams1=self.teams[:4]
		self.auxTeams2=self.teams[4:8]
		self.auxTeams3=self.teams[8:12]
		self.auxTeams4=self.teams[12:]
		self.journey=0

	def restartTeams(self):
		for i in range(0,len(self.teams)):
			self.teams[i].restart()

	def printTeams(self):
		for i in range(0,len(self.teams)):
			print(self.teams[i].name,end=" - ")
			print(self.teams[i].pointsEarned,end=" - ")
			print(self.teams[i].pointsPlayed)

		print("\n")

	def updateTeams(self):
		pos=0
		for i in range(0,len(self.teams)):
			if(pos==4):
				pos=0

			if(i<4):
				self.teams[i]=self.auxTeams1[pos]
			elif(i>=4 and i<8):
				self.teams[i]=self.auxTeams2[pos]
			elif(i>=8 and i<12):
				self.teams[i]=self.auxTeams3[pos]
			else:
				self.teams[i]=self.auxTeams4[pos]

			pos+=1
		self.teams=sorted(self.teams,key=lambda i: int(i.pointsEarned),reverse=True)

	def moveTeam(self,teams):
		aux1=teams[0]
		aux2=None
		i=0
		while(i<len(teams)):
			aux2=teams[i]
			teams[i]=aux1
			aux1=aux2
			i+=1
		teams[0]=aux1

	def moveTeams3(self):
		self.moveTeam(self.auxTeams1)
		self.moveTeam(self.auxTeams2)
		self.moveTeam(self.auxTeams3)
		self.moveTeam(self.auxTeams4)

	def moveTeams1(self):
		self.moveTeam(self.auxTeams2)
		self.moveTeam(self.auxTeams4)

	def moveTeams2(self):
		self.moveTeam(self.auxTeams1)
		self.moveTeam(self.auxTeams4)

	def playMatch(self,team1,team2):
		#print(team1.name,end=" vs ")
		#print(team2.name)

		if(team1.darGoles()<team2.darGoles()):
			team1.chandePoints(0)
			team2.chandePoints(3)
		elif(team1.darGoles()>team2.darGoles()):
			team1.chandePoints(3)
			team2.chandePoints(0)
		else:
			team1.chandePoints(1)
			team2.chandePoints(1)

	def simJourney(self):
		if(self.journey<4):
			self.moveTeams1()
			for i in range(0,len(self.auxTeams1)):
				self.playMatch(self.auxTeams1[i],self.auxTeams2[i])
				self.playMatch(self.auxTeams3[i],self.auxTeams4[i])
		elif(self.journey>=4 and self.journey<8):
			self.moveTeams1()
			for i in range(0,len(self.auxTeams1)):
				self.playMatch(self.auxTeams1[i],self.auxTeams4[i])
				self.playMatch(self.auxTeams3[i],self.auxTeams2[i])
		elif(self.journey>=8 and self.journey<12):
			self.moveTeams2()
			for i in range(0,len(self.auxTeams1)):
				self.playMatch(self.auxTeams1[i],self.auxTeams3[i])
				self.playMatch(self.auxTeams2[i],self.auxTeams4[i])
		elif(self.journey==12):
			i=0
			while(i<4):
				self.playMatch(self.auxTeams1[i],self.auxTeams1[i+1])
				self.playMatch(self.auxTeams2[i],self.auxTeams2[i+1])
				self.playMatch(self.auxTeams3[i],self.auxTeams3[i+1])
				self.playMatch(self.auxTeams4[i],self.auxTeams4[i+1])
				i+=2

		elif(self.journey==13):
			self.moveTeams3()
			pos=0
			while(pos<4):
				self.playMatch(self.auxTeams1[pos],self.auxTeams1[pos+1])
				self.playMatch(self.auxTeams2[pos],self.auxTeams2[pos+1])
				self.playMatch(self.auxTeams3[pos],self.auxTeams3[pos+1])
				self.playMatch(self.auxTeams4[pos],self.auxTeams4[pos+1])
				pos+=2

		elif(self.journey==14):
			i=0
			pos=0
			while(pos<4):
				self.playMatch(self.auxTeams1[i],self.auxTeams1[i+2])
				self.playMatch(self.auxTeams2[i],self.auxTeams2[i+2])
				self.playMatch(self.auxTeams3[i],self.auxTeams3[i+2])
				self.playMatch(self.auxTeams4[i],self.auxTeams4[i+2])
				i+=1
				pos+=2

		self.journey+=1
		self.updateTeams()

	def simChampionship(self):
		for i in range(0,len(self.teams)-1):
			self.simJourney()

		self.addChampion()

	def validateTeams(teams):
		if(len(teams)<16 or len(teams)>16):
			return False
		else:
			return True

	def addChampion(self):
		self.teams[0].champWinned+=1
		i=1
		while(i<len(self.teams)):
			if(self.teams[i-1].pointsEarned==self.teams[i].pointsEarned):
				self.teams[i].champWinned+=1
			else:
				i=len(self.teams)
			i+=1

	def verifyTotalChampion(self):
		print()
		print("TABLA DE CAMPEONES")
		self.teams=sorted(self.teams,key=lambda i: int(i.champWinned),reverse=True)
		for i in range(0,len(self.teams)):
			print(self.teams[i].name,end=" -> VECES CAMPEÓN: ")
			print(self.teams[i].champWinned)

		champs=[]
		champs.append(self.teams[0])
		i=1
		while(i<len(self.teams)):
			if(self.teams[i-1].champWinned==self.teams[i].champWinned):
				champs.append(self.teams[i])
			else:
				i=len(self.teams)
			i+=1

		print()
		print("CAMPEONES:")
		for i in range(0,len(champs)):
			print(champs[i].name)

class Reader:
	def readTeams(self,path):
		datos=[]
		file=open(path,"r")
		line=file.readline()
		while line:
			arr=line.split(";")
			team=Team(arr[0],arr[1])
			datos.append(team)
			line=file.readline()
		file.close()
		return datos

class Main:
	def __init__(self):
		reader=Reader()
		teams=reader.readTeams("teams.csv")
		if(Championship.validateTeams(teams)):
			ch=Championship(teams)
			simuTimes=int(input("Cantidad de torneos a simular: "))
			print()
			for i in range(0,simuTimes):
				ch.simChampionship()
				ch.restartTeams()
				ch.prepareChampionship()
			ch.verifyTotalChampion()
		else:
			print("Error en la cantidad de equipos")		


main=Main()