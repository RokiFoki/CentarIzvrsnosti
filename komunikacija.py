'''
	VAŽNO: potrebno instalirati dodatak WebSocket pomoću naredbe u cmd.exe
	pip install git+https://github.com/dpallot/simple-websocket-server.git
	
	Referenca: https://github.com/dpallot/simple-websocket-server
'''

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

PORT = 8001

identifikator = 0
klijenti = {}
class Prosljeditelj(WebSocket):
	"""
		razred koji nasljeđuje WebSocket (WebSocket ima sve nužno implementirano) te dodatno 
		definira što ućiniti kad primi poruku, kad se neko spoji i kad se netko odspoji
	"""
	def handleMessage(self):
		"""
			primi poruku proslijedi je svim klijentima osim onome tko je poslao
		"""
		
		print(self, klijenti[self], self.data)
		for klijent in klijenti.keys():
			if klijent != self:
				klijent.sendMessage(klijenti[self] + " " + self.data)

	def handleConnected(self):
		"""
			kad se netko spoji, obavijesti sve klijente da se taj netko spojio te mu dodijeli
			identifikator i doda u listu klijenata
		"""
		
		# omogucivanje -> promjene <- globalnih (zajednickih) varijabli
		global identifikator, klijenti
		
		print(self.address, 'spojen')
		for klijent in klijenti.keys():
			klijent.sendMessage(str(identifikator) + ' spojen')
			
		klijenti[self] = str(identifikator)
		identifikator += 1

	def handleClose(self):
		"""
			kad se netko odspoji, obavijesti sve klijente da se taj netko odspojio te ga
			izbaci iz liste klijenata
		"""
		
		print(self.address, 'odspojen')
		for klijent in klijenti.keys():
			klijent.sendMessage(klijenti[self] + ' odspojen')
			
		klijenti.pop(self, None)

# pokreni obicni web socket server na definiranom portu
server = SimpleWebSocketServer('', PORT, Prosljeditelj)
server.serveforever()