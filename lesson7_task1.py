class Matrix:
    def __init__(self, matrix: list):
        self.list = matrix

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.list:
            for el in line:
                return el

    def __str__(self):
        result = ''
        for line in self.list:
            result = result + '| '
            for el in line:
                result = result + str(el) + ' '
            result = result+'|\n'
        return result

    def get_count_col(self):
        return len(self.list[0])  #можно было бы перебрать но мы договаривались что матрицы будут одноразмерными

    def get_element(self, line_position: int, col_position: int):
        try:
            return self.list[line_position][col_position]
        except IndexError:
            return 0

    def __add__(self, other):
        max_line = max(len(self.list), len(other.list))
        max_col = max(self.get_count_col(), other.get_count_col())
        result_matrix = [[0 for j in range(max_col)] for i in range(max_line)]
        for ndx_line, line in enumerate(result_matrix):
            for idx_el, el in enumerate(line):
                result_matrix[ndx_line][idx_el] = self.get_element(ndx_line, idx_el)+other.get_element(ndx_line, idx_el)
        return Matrix(result_matrix)


matrix1 = Matrix([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
matrix2 = Matrix([[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]])
print(matrix1)
print(matrix2)
print(matrix1+matrix2)
