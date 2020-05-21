'''
	Tai Warner
	Written 22/05/2020
	Board class for the Royal Game of Ur
'''

from square import Square
from piece import Piece
import numpy as np

class Board:
	def __init__(self):
		letters = ['A','B','C','D','E','F','G']
		numbers = ['1','2','3','4','5','6','7']
		# init all the squares
		self.a = Square('a', True)
		self.b = Square('b', False)
		self.c = Square('c', True)
		self.d = Square('d', False)
		self.e = Square('e', False)
		self.f = Square('f', False)
		self.g = Square('g', False)
		self.h = Square('h', False)
		self.i = Square('i', False)
		self.j = Square('j', False)
		self.k = Square('k', True)
		self.l = Square('l', False)
		self.m = Square('m', False)
		self.n = Square('n', False)
		self.o = Square('o', True)
		self.p = Square('p', False)
		self.q = Square('q', True)
		self.r = Square('r', False)
		self.s = Square('s', False)
		self.t = Square('t', False)
		self.starta = Square('starta', False)
		self.start1 = Square('start1', False)
		self.enda = Square('enda', False)
		self.end1 = Square('end1', False)

		# assign successors
		self.a.successor = self.b
		self.b.successor = self.e
		self.c.successor = self.b
		self.d.successor = self.a
		self.e.successor = self.h
		self.f.successor = self.c
		self.g.successor = self.d
		self.h.successor = self.k
		self.i.successor = self.f
		self.j.successor = self.g
		self.k.successor = self.m
		self.l.successor = self.i
		self.m.successor = self.n
		self.n.successor = self.p
		self.o.successor = self.enda
		self.p.successor = self.s
		self.q.successor = self.end1
		self.r.successor = self.o
		# self.s is a special case since it is where the shared path splits to individual paths again
		def ssucc(piece):
			if repr(piece) in letters:
				return self.r
			return self.t
		self.s.successor = ssucc
		self.t.successor = self.q
		self.starta.successor = self.j
		self.start1.successor = self.l

		# init each player's pieces
		self.piecesa = [Piece(l) for l in letters]
		self.pieces1 = [Piece(n) for n in numbers]
		for piece in self.piecesa:
			piece.location = self.starta
		for piece in self.pieces1:
			piece.location = self.start1

		# populate the start squares with the players' pieces
		self.starta.member = self.piecesa[:]
		self.start1.member = self.pieces1[:]

		# represent the board the way it is organized spatially
		self.arrangement = np.array([[self.a, self.b, self.c],\
																 [self.d, self.e, self.f],\
																 [self.g, self.h, self.i],\
																 [self.j, self.k, self.l],\
																 [self.starta, self.m, self.start1],\
																 [self.enda, self.n, self.end1],\
																 [self.o, self.p, self.q],\
																 [self.r, self.s, self.t]])

	def __repr__(self):
		b = '___________________\n' # top of the board
		for row in self.arrangement:
			# print([x.name for x in row])
			lines0 = repr(row[0]).split('\n')[:-1] # the last element is always ''
			lines1 = repr(row[1]).split('\n')[:-1]
			lines2 = repr(row[2]).split('\n')[:-1]
			assert len(lines0) == len(lines1) == len(lines2)
			for i in range(len(lines0)):
				# start and end squares are squares in code but not on the real life
				# board, so we don't draw them as such
				b += '|' if row[0].name not in ['starta', 'enda'] else ' '
				b += lines0[i] + lines1[i] + lines2[i] + '\n'
		return b
