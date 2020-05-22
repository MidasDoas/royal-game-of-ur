'''
	Tai Warner
	Written 22/05/2020
	main code for the Royal Game of Ur
'''

import numpy as np
from random import randint
from square import Square
from board import Board
from time import sleep

# Rolls 4 virtual d2's
def roll4d2():
  return [randint(0,1) for a in range(4)]

# Returns the score (sum) from a roll of 4 d2's
def roll():
	return np.sum(roll4d2())

# Returns the team a piece belongs to
def team(piece):
	letters = ['A','B','C','D','E','F','G']
	numbers = ['1','2','3','4','5','6','7']
	return letters if repr(piece) in letters else numbers

# Returns the square n squares ahead of a given one
def nth_successor(n, sq):
	piece = sq.member[0] if len(sq.member) is not 0 else None
	assert piece is not None
	succ = sq
	for i in range(n):
		succ = succ.successor if succ.name is not 's' else succ.successor(piece) # square s is a special case
		if succ == None:
			return None
	return succ

# Returns whether a given piece can legally move n steps ahead
def can_move(n, piece):
	loc = piece.location
	succ = nth_successor(n, loc)
	if succ is None: # if you can't land exactly on an end square
		return False
	if succ.occupied:
		if succ.name is 'k': # if the safe square is occupied
			return False
		else:
			if succ.member[0].name in team(piece): # if the nth successor is occupied by your own piece
				if succ.name not in ['enda', 'end1']: # except if that square is an end square
					return False
	return True

# Returns the actual Piece object given its name string, case insensitive
def piece_from_name(group, name):
	for piece in group:
		if repr(piece).lower() == name.lower():
			return piece
	return None

def main():
	board = Board()
	print(board)
	turn = 0

	# coin flip to start
	turn += randint(0,1)
	if turn:
		print('Player 1 goes first!')
	else:
		print('Player A goes first!')

	# enter game loop
	while True:
		rosette = True
		while rosette:
			rosette = False
			player = 'Player A' if turn % 2 == 0 else 'Player 1'
			print(player + '\'s turn:')

			# Step 1: roll
			die = roll()
			print(player + ' rolls a ' + str(die))

			# Step 2: determine which pieces can move
			pieces = board.piecesa if turn % 2 == 0 else board.pieces1
			moveable = np.array([piece for piece in pieces if can_move(die, piece)])

			# Step 3: offer choice of pieces from (2)
			if len(moveable) == 0 or die == 0:
				print(player + ' cannot move -- passing turn')
				sleep(2)
			else:
				piece = None
				while piece is None:
					name = input('Choose a piece to move from ' + str(moveable) + ': ')
					piece = piece_from_name(moveable, name)

			# Step 4: move the chosen piece (if possible) and print the board state
				new_loc = nth_successor(die, piece.location)
				old_loc = piece.location
				old_loc.member.remove(piece)
				if len(old_loc.member) == 0: # only do for regular squares
					old_loc.occupied = False
				if new_loc.occupied and new_loc.name not in ['enda', 'end1']: # treat end squares specially
					# boot the enemy piece from a non-end square
					# we know it's an enemy on the square because of how can_move works
					enemy = new_loc.member.pop()
					# bookkeeping to keep enemy Piece and Square data in agreement
					enemy_start = board.start1 if turn % 2 == 0 else board.starta
					enemy_pieces = board.pieces1 if turn % 2 == 0 else board.piecesa
					enemy.location = enemy_start
					enemy_start.member.append(enemy)
				# bookkeeping for the current player's Piece and Square
				piece.location = new_loc
				new_loc.occupied = True
				new_loc.member.append(piece)

			print(board)

			# Step 5: check if either player has won
			if len(board.enda.member) == 7:
				print('Player A has won!')
				exit()
			if len(board.end1.member) == 7:
				print('Player 1 has won!')
				exit()

			# Step 6: check if player landed on a rosette square and repeat if so
			land = new_loc.name if new_loc else None
			if land in ['a','c','k','o','q']:
				rosette = True
				print(player + ' has landed on a rosette! Taking another turn')
			new_loc = None # you don't get another rosette if your rosette roll was a 0
		turn += 1

if __name__=='__main__':
	main()
	