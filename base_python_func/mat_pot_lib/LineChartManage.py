import matplotlib.pyplot as plt

# https://www.javatpoint.com/how-to-set-x-axis-values-in-matplotlib-in-python
class LineChartManager:
    def __init__(self):
        """Initialize the data and create the line chart."""
        # Here, we are giving the x-axis values to be plotted on the graph
        self.x = [1, 2, 3, 4, 5, 6]
        # Here, we are giving the y-axis values to be plotted on the graph
        self.y = [6, 5, 4, 3, 2, 1]
        # Here, we are giving the labels for the x-axis
        self.labels = ['A', 'B', 'C', 'D', 'E', 'F']

        # Create the line chart
        self.create_line_chart()
        self.create_line_chart()

    def create_line_chart(self):
        """Create and display the line chart."""
        # Here, we are plotting x-axis values and y-axis values on the graph
        plt.plot(self.x, self.y)
        # Here, we are naming the x-axis and the y-axis
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        # Here, we are naming the title of the plot to be shown on the graph
        plt.title("Set X-Axis Values in Matplotlib using the xticks() function")
        # Here, we are setting the x-axis values on the graph
        plt.xticks(self.x, self.labels)
        # Here, we are declaring the function to show the plot on the graph
        plt.show()

    def set_label(self):
        # here, we are giving the x-axis values to be plot on the graph
        x = [1, 2, 3, 4, 5, 6]
        # here, we are giving the y-axis values to be plot on the graph
        y = [6, 1, 5, 3, 4, 2]
        # here, we are giving the labels for x-axis
        labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5', 'Label6']
        # here, we are plotting x-axis values and y-axis values on the graph
        plt.plot(x, y)
        # here, we are naming the x-axis and the y-axis
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        # here, we are naming the title of the plot to be shown on the graph
        plt.title("Set X-Axis Values in Matplotlib using the xticks() function")
        # here, we are setting the x-axis values and specifying rotation for the labels in degree
        # here, we are setting the x-axis values on the graph
        plt.xticks(x, labels, rotation=40)
        # here, we are declaring the function to show the plot on the graph
        plt.show()


if __name__ == "__main__":
    line_chart_manager = LineChartManager()