import numpy as np

class MatrixManager:

    def __init__(self):
        """Initialize the matrix and display it."""
        self.matrix = self.create_matrix()
        self.display_matrix_info(self.matrix)
        self.matrix_operations()
        self.select_matrix_elements()
        self.perform_matrix_operations()
        self.create_zero_and_one_matrices()
        self.create_and_multiply_matrices()
        self.transpose_matrix()
        self.calculate_determinant()

    def create_matrix(self):
        """Create and display a matrix."""
        matrix = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])
        print("Mátrix létrehozása:")
        print(matrix)
        return matrix

    def display_matrix_info(self, matrix):
        """Display the size and type of the matrix."""
        print("\nMátrix mérete és típusa:")
        print("Méret:", matrix.shape)
        print("Típus:", matrix.dtype)

    def matrix_operations(self):
        """Perform various operations between two matrices."""
        matrix2 = np.array([[9, 8, 7],
                            [6, 5, 4],
                            [3, 2, 1]])
        print("\nMátrix műveletek:")
        print("Összeadás:")
        print(self.matrix + matrix2)
        print("Kivonás:")
        print(self.matrix - matrix2)
        print("Szorzás (elemenkénti):")
        print(self.matrix * matrix2)
        print("Mátrix szorzás:")
        print(np.dot(self.matrix, matrix2))

    def select_matrix_elements(self):
        """Select specific elements, rows, and columns from the matrix."""
        print("\nMátrix elemeinek kiválasztása:")
        print("Egy adott elem (1, 1):", self.matrix[1, 1])
        print("Egy sor kiválasztása (első sor):")
        print(self.matrix[0, :])
        print("Egy oszlop kiválasztása (harmadik oszlop):")
        print(self.matrix[:, 2])

    def perform_matrix_operations(self):
        """Perform various operations on the matrix."""
        print("\nMátrix műveletek:")
        print("Transzponálás:")
        print(np.transpose(self.matrix))
        print("Determináns számítása:")
        determinant = np.linalg.det(self.matrix)
        print(determinant)
        print("Inverz számítása:")
        if determinant == 0:
            print("A mátrix szinguláris, nincs inverze.")
        else:
            inverse_matrix = np.linalg.inv(self.matrix)
            print("Mátrix inverze:")
            print(inverse_matrix)

    def create_zero_and_one_matrices(self):
        """Create matrices filled with zeros and ones."""
        zeros_matrix = np.zeros((3, 3))
        ones_matrix = np.ones((3, 3))
        print("\nMátrix létrehozása nullákkal vagy egyekkel:")
        print("Nulla mátrix:")
        print(zeros_matrix)
        print("Egységmátrix:")
        print(ones_matrix)

    def create_and_multiply_matrices(self):
        """Create two matrices and perform matrix multiplication."""
        matrix_A = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])

        matrix_B = np.array([[9, 8, 7],
                             [6, 5, 4],
                             [3, 2, 1]])

        # Matrix multiplication
        result_matrix = np.dot(matrix_A, matrix_B)
        print("Mátrixszorzás eredménye:")
        print(result_matrix)

    def transpose_matrix(self):
        """Transpose matrix A and display the result."""
        matrix_A = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])

        transposed_matrix_A = np.transpose(matrix_A)
        print("\nMátrix A transzponáltja:")
        print(transposed_matrix_A)

    def calculate_determinant(self):
        """Calculate and display the determinant of matrix A."""
        matrix_A = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])

        determinant_A = np.linalg.det(matrix_A)
        print("\nMátrix A determinánsa:")
        print(determinant_A)

if __name__ == "__main__":
    matrix_manager = MatrixManager()