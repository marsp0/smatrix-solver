
class Main(object):

	def __init__(self):

		self.matrix = []
		self.start()

	def start(self):
		while True:
			current_row = raw_input('Please enter the row by separating the entries with a comma. Type "end" to stop: ')
			if current_row.lower() != 'end':
				if len(self.matrix) == 0:
					self.matrix.append(self.get_row(current_row))
				else:
					current_clear_row = self.get_row(current_row)
					if len(current_clear_row) != len(self.matrix[0]):
						while True:
							new_row = raw_input('The row entered is of different size, the size of the row should be {}. Please enter a new row: '.format(len(self.matrix[0])))
							if new_row.lower() == 'end':
								return
							new_clear_row = self.get_row(new_row)
							if len(new_clear_row) != len(self.matrix[0]):
								continue
							self.matrix.append(new_clear_row)
							break
					self.matrix.append(current_clear_row)
			else:
				print self.get_determinant(self.matrix)
				return

	def get_minor(self,matrix, row,column):
		''' this would give us the minor of a given element
		'''
		new_matrix = []
		row = row-1
		column = column-1
		for m_row in xrange(len(matrix)):
			if m_row == row:
				continue
			else:
				new_matrix_row = []
				for m_column in xrange(len(matrix[m_row])):
					if m_column == column:
						continue
					else:
						new_matrix_row.append(matrix[m_row][m_column])
				new_matrix.append(new_matrix_row)
		return new_matrix

	def get_cofactor(self, row, col):
		'''this function returns the cofactor of the element
			Cofactor of a given element is the element multiplied by '-1'^(element_row + element_column) 
		'''
		power = int(row) + int(col+1)
		return pow(-1,power)

	def get_row(self,str_row):
		sep_elements = str_row.split(',')
		clear_row = []
		count_cols = 0
		for item in sep_elements:
			if item.startswith('-'):
				if item[1:].isdigit():
					count_cols += 1
					clear_row.append(int(item))
			else:
				if item.isdigit():
					count_cols += 1
					clear_row.append(int(item))
		if clear_row:
			return clear_row
		else:
			return []

	def get_determinant(self,matrix):
		try:
			det = 0
			if len(matrix) != 2 and len(matrix[0]) != 2:
				for col in xrange(len(matrix[0])):
					minor = self.get_minor(matrix,1,col+1)
					minor_det = self.get_determinant(minor)
					cofactor = self.get_cofactor(1,col)*minor_det
					det +=  cofactor*matrix[0][col]
				return det
			else:
				return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
		except IndexError:
			print 'Couldnt find the determinant'

if __name__=='__main__':
	p = Main()