import sys

matrix = [list(sys.stdin.readline().replace("\n","")) for x in range(5)]

valid = True
knights = 0
for row_idx, row in enumerate(matrix):
	for col_idx, item in enumerate(row):
		if item == "k":
			knights+=1
			if row_idx+2 < 5 : #Can move down
				if col_idx > 0 and matrix[row_idx+2][col_idx-1] == "k":
					valid = False
					break
				if col_idx < 4 and matrix[row_idx+2][col_idx+1] == "k":
					valid = False
					break
			if row_idx-2 >= 0: #Can move up
				if col_idx > 0 and matrix[row_idx-2][col_idx-1] == "k":
					valid = False
					break
				if col_idx < 4 and matrix[row_idx-2][col_idx+1] == "k":
					valid = False
					break	
			if col_idx+2 < 5 : #Can move right
				if row_idx > 0 and matrix[row_idx-1][col_idx+2] == "k":
					valid = False
					break
				if row_idx < 4 and matrix[row_idx+1][col_idx+2] == "k":
					valid = False
					break
			if col_idx-2 >= 0: #Can move left
				if row_idx > 0 and matrix[row_idx-1][col_idx-2] == "k":
					valid = False
					break
				if row_idx < 4 and matrix[row_idx+1][col_idx-2] == "k":
					valid = False
					break
if valid and knights == 9:
	print("valid")
else:
	print("invalid")