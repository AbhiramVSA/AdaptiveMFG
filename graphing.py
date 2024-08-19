import matplotlib.pyplot as plt

def produce_visual(self):
    selected_option = self.optionmenu_1.get()  # Get the selected option from the menu

    if selected_option == "Bar Graph":
        self.plot_bar_graph()  # Call the function to produce a bar graph
    elif selected_option == "Scatter Plot":
        self.plot_scatter_plot()  # Call the function to produce a scatter plot
    elif selected_option == "Line Graph":
        self.plot_line_graph()  # Call the function to produce a line graph

    
    
def plot_bar_graph(self):
     # Example bar graph plotting code
    data = {'A': 10, 'B': 15, 'C': 7}
    names = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.bar(names, values)
    plt.title('Bar Graph Example')
    plt.show()

def plot_scatter_plot(self):
    # Example scatter plot code
    x = [1, 2, 3, 4, 5]
    y = [5, 7, 8, 5, 3]

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y)
    plt.title('Scatter Plot Example')
    plt.show()

def plot_line_graph(self):
    # Example line graph code
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title('Line Graph Example')
    plt.show()