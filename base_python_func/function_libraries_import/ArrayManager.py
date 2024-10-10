import numpy as np

class ArrayManager:

    def __init__(self):
        """Initialize the NumPy array and display its contents."""
        self.arr = self.create_array()
        print("NumPy tömb létrehozása:")
        print(self.arr)
        self.display_array_info()
        self.perform_array_operations()
        self.select_array_elements()
        self.perform_mathematical_operations()
        self.create_array_with_sequence()
        self.create_array_with_zeros_and_ones()

    def create_array(self):
        """Create and return a NumPy array."""
        return np.array([1, 2, 3, 4, 5])

    def display_array_info(self):
        """Display basic information about the NumPy array."""
        print("\nTömb mérete és típusa:")
        print("Méret:", self.arr.shape)
        print("Típus:", self.arr.dtype)

    def perform_array_operations(self):
        """Perform basic operations with another NumPy array."""
        arr2 = np.array([6, 7, 8, 9, 10])
        print("\nTömb műveletek:")
        print("Összeadás:", self.arr + arr2)
        print("Kivonás:", self.arr - arr2)
        print("Szorzás:", self.arr * arr2)
        print("Osztás:", self.arr / arr2)

    def select_array_elements(self):
        """Select and print specific elements from the array."""
        print("\nTömb elemeinek kiválasztása:")
        print("Első elem:", self.arr[0])  # Access the first element
        print("Tartomány kiválasztása:", self.arr[1:4])  # Access a range of elements (index 1 to 3)

    def perform_mathematical_operations(self):
        """Perform mathematical operations on the NumPy array."""
        print("\nMatematikai műveletek tömbön:")
        print("Átlag:", np.mean(self.arr))
        print("Szórás:", np.std(self.arr))
        print("Legnagyobb elem:", np.max(self.arr))
        print("Legkisebb elem:", np.min(self.arr))

    def create_array_with_sequence(self):
        """Create and display a NumPy array using a sequence."""
        seq = np.arange(1, 11)  # Creates an array with values from 1 to 10
        print("\nTömb létrehozása szekvenciával:")
        print(seq)

    def create_array_with_zeros_and_ones(self):
        """Create and display NumPy arrays filled with zeros and ones."""
        zeros = np.zeros(5)  # Creates an array of zeros with size 5
        ones = np.ones(5)    # Creates an array of ones with size 5
        print("\nTömb létrehozása nullákkal vagy egyekkel:")
        print("Nullák:", zeros)
        print("Egyek:", ones)

# Example usage
if __name__ == "__main__":
    array_manager = ArrayManager()