import matplotlib.pyplot as plt

class BarChart:

    def __init__(self):
        """Define the data for the bar chart."""
        self.categories = ['A', 'B', 'C', 'D', 'E']  # Categories
        self.values = [15, 28, 24, 20, 18]  # Heights of the bars

        # Create the bar chart
        self.create_bar_chart()

    def create_bar_chart(self):
        """Create and display the bar chart."""
        plt.bar(self.categories, self.values)

        # Set the title and labels
        plt.title('Bar Chart Example')
        plt.xlabel('Categories')
        plt.ylabel('Values')

        # Set y-axis ticks to show desired scale
        plt.yticks(range(0, 31, 5))  # Set y-axis ticks to 0, 5, 10, ..., 30

        # Show the chart
        plt.show()

# Example usage
if __name__ == "__main__":
    bar_chart_manager = BarChart()
