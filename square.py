'''
	Tai Warner
	Written 22/05/2020
	Square class for the Royal Game of Ur
'''

class Square:
	def __init__(self, n, r):
		self.name = n
		self.occupied = False
		self.member = []
		self.rosette = r
		self.successor = None

	# never used, lol
	def succ(self):
		return self.successor.name

	def __repr__(self):
		if self.name not in ['starta', 'enda', 'start1', 'end1']: # regular squares are easy
			l1 = '  ^  |\n' if (self.name in ['o', 'q']) else '     |\n'
			if self.rosette:
				l2 = ' \|/ |\n'
				l3 = ' -' + repr(self.member[0]) + '- |\n' if self.occupied else ' -*- |\n'
				l4 = ' /|\ |\n'
			else:
				l2 = '     |\n'
				l3 = '  ' + repr(self.member[0]) + '  |\n' if self.occupied else l2
				l4 = l2
			l5 = '_____|\n'
		else: # now it gets complex
			if self.name in ['starta', 'start1']:
				l1 = '  ^  '
				l2 = '     '
				l3 = '     '
				l4 = '     '
				l5 = '     '
				# making the pieces organize nicely in the start zone
				if len(self.member) >= 3:
					l2 = ' ' + repr(self.member[0]) + repr(self.member[1]) + repr(self.member[2]) + ' '
					if len(self.member) >= 6:
						l3 = ' ' + repr(self.member[3]) + repr(self.member[4]) + repr(self.member[5]) + ' '
						if len(self.member) == 7:
							l4 = '  ' + repr(self.member[6]) + '  '
					elif len(self.member) == 5:
						l3 = ' ' + repr(self.member[3]) + ' ' + repr(self.member[4]) + ' '
					else:
						l3 = '  ' + repr(self.member[3]) + '  ' if len(self.member) == 4 else '     '
				elif len(self.member) == 2:
					l2 = ' ' + repr(self.member[0]) + ' ' + repr(self.member[1]) + ' '
				else:
					l2 = '  ' + repr(self.member[0]) + '  ' if len(self.member) == 1 else '     '
				# draw the fencepost border only for the letters' side
				l1 = l1 + '|\n' if self.name == 'starta' else l1 + ' \n'
				l2 = l2 + '|\n' if self.name == 'starta' else l2 + ' \n'
				l3 = l3 + '|\n' if self.name == 'starta' else l3 + ' \n'
				l4 = l4 + '|\n' if self.name == 'starta' else l4 + ' \n'
				l5 = l5 + '|\n' if self.name == 'starta' else l5 + ' \n'
			else: # if it's an end zone
				# basically arranging the pieces upside down from how they appear in the start zones
				l1 = '     '
				l2 = '     '
				l3 = '     '
				l4 = '     '
				if len(self.member) == 7:
					l2 = '  ' + repr(self.member[6]) + '  '
					l3 = ' ' + repr(self.member[3]) + repr(self.member[4]) + repr(self.member[5]) + ' '
					l4 = ' ' + repr(self.member[0]) + repr(self.member[1]) + repr(self.member[2]) + ' '
				elif len(self.member) > 3:
					if len(self.member) == 6:
						l3 = ' ' + repr(self.member[3]) + repr(self.member[4]) + repr(self.member[5]) + ' '
					else:
						l3 = ' ' + repr(self.member[3]) + ' ' + repr(self.member[4]) + ' ' if len(self.member) == 5 else \
								'  ' + repr(self.member[3]) + '  '
					l4 = ' ' + repr(self.member[0]) + repr(self.member[1]) + repr(self.member[2]) + ' '
				else:
					l3 = '     '
					if len(self.member) == 3:
						l4 = ' ' + repr(self.member[0]) + repr(self.member[1]) + repr(self.member[2]) + ' '
					elif len(self.member) == 2:
						l4 = ' ' + repr(self.member[0]) + ' ' + repr(self.member[1]) + ' '
					else:
						l4 = '  ' + repr(self.member[0]) + '  ' if len(self.member) == 1 else '     '
				# draw the fencepost border only for the letters' side
				l1 = l1 + '|\n' if self.name == 'enda' else l1 + ' \n'
				l2 = l2 + '|\n' if self.name == 'enda' else l2 + ' \n'
				l3 = l3 + '|\n' if self.name == 'enda' else l3 + ' \n'
				l4 = l4 + '|\n' if self.name == 'enda' else l4 + ' \n'
				l5 = '_____|\n' if self.name == 'enda' else '_____\n'
		return l1 + l2 + l3 + l4 + l5
		