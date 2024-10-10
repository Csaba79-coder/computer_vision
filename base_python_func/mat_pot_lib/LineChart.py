from matplotlib import pyplot as plt

class LineChart:

    def __init__(self):
        """Initialize data and create the line chart."""
        self.x = [1, 2, 3, 4, 5]  # X-axis values
        self.y = [2, 4, 6, 8, 10]  # Y-axis values
        self.create_chart()

    def create_chart(self):
        """Create and display the line chart."""
        plt.plot(self.x, self.y)

        # Set the title and axis labels
        plt.title('Simple Line Chart')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')

        # Display the chart
        plt.show()

# Example usage
if __name__ == "__main__":
    line_chart = LineChart()