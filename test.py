import customtkinter
from functions import GraphingFunctions

customtkinter.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.graphing_functions = GraphingFunctions()  # Create an instance of GraphingFunctions

        # Configure window
        self.title("Graphing App")
        self.geometry("500x300")

        # Create buttons and link them to methods
        self.bar_button = customtkinter.CTkButton(self, text="Plot Bar Graph", command=self.graphing_functions.plot_bar_graph)
        self.bar_button.pack(pady=10)

        self.scatter_button = customtkinter.CTkButton(self, text="Plot Scatter Plot", command=self.graphing_functions.plot_scatter_plot)
        self.scatter_button.pack(pady=10)

        self.line_button = customtkinter.CTkButton(self, text="Plot Line Graph", command=self.graphing_functions.plot_line_graph)
        self.line_button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
