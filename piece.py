'''
	Tai Warner
	Written 22/05/2020
	Piece class for the Royal Game of Ur
'''

class Piece:
	def __init__(self, name):
		self.name = name
		self.location = None

	def __repr__(self):
		return self.name
