import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import filedialog
import shutil
import os
import matplotlib.pyplot as plt
import csv
import re
from functions import GraphingFunctions


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure rows and columns to be expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Configure window
        self.title("AdaptiveMFG")
        self.geometry(f"{1100}x{580}")

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="AdaptiveMFG", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.upload_and_save_csv)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter CSV in form: UDI,ProdID,Type,Air,Temp[K],ProcessTemp[K],[rpm],Torque [Nm],Toolwear[min],Target,FailureType")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # Button to process the input
        self.main_button_1 = customtkinter.CTkButton(master=self, text="Append to CSV", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.append_to_csv)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # Create tabview
        self.tabview = customtkinter.CTkTabview(self, width=300)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # Configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # Create option menu
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                        values=["Bar Graph", "Scatter Plot", "Line Graph"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Create GraphingFunctions object and pass the option menu
        self.graphing_functions = GraphingFunctions(option_menu=self.optionmenu_1)
        self.graphing_functions.option_menu = self.optionmenu_1  # Link the option menu to GraphingFunctions

        # Create button
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Produce Visual",
                                                           command=self.graphing_functions.produce_visual)
        self.string_input_button.grid(row=1, column=0, padx=20, pady=(20, 10))

        # Set default values
        self.sidebar_button_1.configure(state="enabled", text="Upload CSV Data of Machine")
        self.sidebar_button_2.configure(state="enabled", text="Failure Prediction")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("Bar Graph")

        self.textbox.insert("0.0", "AdaptiveMFG Overview\n\n" + """
AdaptiveMFG focuses on revolutionizing manufacturing with cutting-edge predictive maintenance solutions. Our prototype app is designed to address unplanned equipment failures by leveraging machine learning and real-time data analysis.

Key Features:
- User-Friendly Interface: Simplified navigation.
- Real-Time Data Processing: Quick detection of anomalies.
- Predictive Analytics: Forecasts failures to enable proactive maintenance.
- Data Visualization: Insights through visual data trends.

Goals:
1. Minimize Downtime: Reduce unexpected failures and costs.
2. Enhance Maintenance Efficiency: Transition to proactive maintenance.
3. Leverage Machine Learning: Provide accurate failure predictions.

Our mission is to optimize manufacturing efficiency and reduce downtime through advanced technology.
"""
)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def upload_and_save_csv(self):
        # Open a file dialog to select a CSV file
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if not file_path:
            return  # If no file was selected, exit the function

        # Define a directory to save the CSV file
        save_directory = os.path.expanduser("~")  # Save to user's home directory or change to desired path

        # Create a new file path for saving
        filename = os.path.basename(file_path)
        new_file_path = os.path.join(save_directory, filename)

        try:
            # Copy the file to the new location
            shutil.copy(file_path, new_file_path)
        
            # Optionally display a message indicating success
            tkinter.messagebox.showinfo("Success", f"File saved as {new_file_path}")

        except Exception as e:
            # Handle exceptions (e.g., file copy errors)
            tkinter.messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

        # Optionally save the new file path for later use
        self.saved_csv_file_path = new_file_path
        
    def append_to_csv(self):
        # Retrieve input from the entry widget
        user_input = self.entry.get()

        # Define the expected CSV format using regex
        pattern = r"^\d+,[A-Za-z0-9]+,[A-Za-z]+,\d+(\.\d+)?,\d+(\.\d+)?,\d+(\.\d+)?,\d+(\.\d+)?,\d+,\d+,(No Failure|Failure)$"

        if re.match(pattern, user_input):
            # Split the input into values
            values = user_input.split(',')

            # Define the CSV file path (use the saved file path)
            csv_file_path = getattr(self, 'saved_csv_file_path', None)

            if csv_file_path:
                # Append to the CSV file
                with open(csv_file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(values)

                # Optionally display a message indicating success
                tkinter.messagebox.showinfo("Success", "Data appended to CSV file.")
            else:
                tkinter.messagebox.showwarning("Warning", "No CSV file selected.")
        else:
            tkinter.messagebox.showwarning("Invalid Input", "Input does not match the required CSV format.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
