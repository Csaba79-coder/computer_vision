import matplotlib.pyplot as plt
class LineChartManager:

    def __init__(self):
        self.set_label()

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