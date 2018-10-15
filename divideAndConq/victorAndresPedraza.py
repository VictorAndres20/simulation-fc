import random

class Team:
	def __init__(self,name,efect):
		self.name=name
		self.efect=efect
		self.restart()
		self.champWinned=0

	def darGoles(self):
		return float(random.random())*float(10.0)*float(self.efect)

	def changePoints(self,pe):
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
		print("\nEQUIPOS CARGADOS.")
		self.printTeams()

	def validateTeams(teams):
		if(len(teams)<16 or len(teams)>16):
			return False
		else:
			return True

	def restartTeams(self):
		for i in range(0,len(self.teams)):
			self.teams[i].restart()

	def printTeams(self):
		for i in range(0,len(self.teams)):
			print(i+1,end=". ")
			print(self.teams[i].name,end=" - ")
			print(self.teams[i].pointsEarned)
		print("\n")

	def playMatch(self,team1,team2):
		g1=team1.darGoles()
		g2=team2.darGoles()
		print(team1.name,end=": ")
		print(g1,end=" - ")
		print(team2.name,end=": ")
		print(g2)
		if(g1<g2):
			team1.changePoints(0)
			team2.changePoints(3)
			return team2
		elif(g1>g2):
			team1.changePoints(3)
			team2.changePoints(0)
			return team2
		else:
			return playMatch(team1,team2)

	def organizeTable(self):
		self.teams=sorted(self.teams,key=lambda team: int(team.pointsEarned),reverse=True)

	def simuchampionship(self,teams):
		if(len(teams)==2):
			return self.playMatch(teams[0],teams[1])
		else:
			return self.playMatch(self.simuchampionship(teams[:int(len(teams)/2)]),self.simuchampionship(teams[int(len(teams)/2):]))

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
			ch.simuchampionship(ch.teams)
			ch.organizeTable()
			ch.printTeams()
		else:
			print("Error en la cantidad de equipos")		


main=Main()