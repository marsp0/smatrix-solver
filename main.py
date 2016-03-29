
class Main(object):

	def __init__(self):

		self.matrix = []
		self.matrix_rows = None
		self.matrix_cols = None
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
								print self.matrix
								return
							new_clear_row = self.get_row(new_row)
							if len(new_clear_row) != len(self.matrix[0]):
								continue
							self.matrix.append(new_clear_row)
							break
					self.matrix.append(current_clear_row)
			else:
				print self.matrix
				print self.get_minor(self.matrix,2,1)
				return

	def get_minor(self,matrix, row,column):
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

	def get_row(self,str_row):
		sep_elements = str_row.split(',')
		clear_row = []
		count_cols = 0
		for item in sep_elements:
			if item.isdigit():
				count_cols += 1
				clear_row.append(int(item))
		if clear_row:
			return clear_row
		else:
			return []

if __name__=='__main__':
	p = Main()