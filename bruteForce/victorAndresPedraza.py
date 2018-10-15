import random

class Team:
	def __init__(self,name,efect):
		self.name=name
		self.efect=efect
		self.pointsPlayed=0.0
		self.pointsEarned=0.0
		self.teamsPlayed=[]
		self.active=True

	def darGoles(self):
		return float(random.random())*float(10.0)*float(self.efect)

	def chandePoints(self,pe):
		self.pointsPlayed=self.pointsPlayed+3
		self.pointsEarned=self.pointsEarned+pe

	def changeEfectivity(self):
		self.efect=float(pointsEarned/pointsPlayed)

class Championship:
	def __init__(self,teams):
		self.teams=teams
		self.auxTeams=teams.copy()
		self.pos=1
		self.partidos=[]
		print("\nEQUIPOS CARGADOS.")
		for i in range(0,len(self.teams)):
			print(self.teams[i].name)

	def moveTeams(self):
		aux1=self.auxTeams[0]
		aux2=None
		i=0
		while(i<len(self.auxTeams)):
			aux2=self.auxTeams[i]
			self.auxTeams[i]=aux1
			aux1=aux2
			i+=1
		self.auxTeams[0]=aux1

	def playMatch(self,team1,team2):
		if(team1.darGoles()<team2.darGoles()):
			team2.chandePoints(3)
		elif(team1.darGoles()>team2.darGoles()):
			team1.chandePoints(3)
		else:
			team1.chandePoints(1)
			team2.chandePoints(1)

	def simJourney(self):
		self.partidos=[]
		self.moveTeams()
		print()
		for i in range(0,len(self.teams)):
			print(self.teams[i].name)
			print(self.auxTeams[i].name)
			self.playMatch(self.teams[i],self.auxTeams[i])
		print()

	def simChampionship(self):
		for i in range(0,len(self.teams)-1):
			self.simJourney()

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
		ch=Championship(teams)
		ch.simChampionship()
		


main=Main()