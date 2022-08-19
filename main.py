# Importing external libraries
from tkinter import *
from tkinter.ttk import Notebook
from tkinter import messagebox
import json
import time
import requests

# Main Window
window = Tk()
window.title("COVID-19 Information page")
window.geometry("800x600")


# Def for Clock to run
def update():
    clock.config(text=time.strftime('%H:%M:%S %p \n %d %B'))
    clock.after(1000, update)


# Def for getting Covid cases
def get_country_info():
    url = "https://api.covid19api.com/summary"
    response = requests.request("GET", url)
    # Get Data from API and store in json
    data = json.loads(response.text)
    # Get Index for Country
    searchcountry = txt.get().lower()

    def get_country_index(country):
        for index, item in enumerate(data["Countries"]):
            if item["Slug"] == country:
                txt.delete(0, END)
                return index

    countryid = get_country_index(searchcountry)
    # Get New Confirmed & Total Confirmed
    newconfirmed = data["Countries"][countryid]["NewConfirmed"]
    totalconfirmed = data["Countries"][countryid]["TotalConfirmed"]
    covid_msg = f"Last number of new confirmed cases in {searchcountry}:" \
                f"{newconfirmed}.\nThe total cases are:{totalconfirmed}"
    # Return covid msg to gui
    output_text.set(covid_msg)


# Info message on the cases country
def info():
    info_message = open('txt_files/Info message.txt')
    data = info_message.read()
    messagebox.showinfo(title="Info!", message=data)


# Function for saving text to text file
def save_file():
    locations = open("Saved_location/Saved_locations.txt", "a")
    if file_name.get() == "":
        messagebox.showerror("")
    else:
        locations.write(file_name.get())
        locations.write("\n")
    locations.close()


# Delete the entry field after you press button
def reset_file_entry():
    file_name.delete(0, END)


# All the tabs show in window
tab_control = Notebook(window)

tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)
tab4 = Frame(tab_control)
tab5 = Frame(tab_control)

tab_control.add(tab1, text='What is COVID-19?')
tab_control.add(tab2, text='Current cases')
tab_control.add(tab3, text='Tracing')
tab_control.add(tab4, text='Vaccination')
tab_control.add(tab5, text='Travelling')

# Tab1 started here
top_img1 = PhotoImage(file="img/BG1.png")
img1 = Label(tab1, image=top_img1)
img1.place(x=0, y=0)
# Code for the clock
clock = Label(tab1, bg='lightgrey', foreground='black',
              font=('arial', 18, 'bold'))
update()
clock.pack(pady=2, anchor='e')
# Main page covid19 info
covid_info = open('txt_files/COVID_19.txt')
data = covid_info.read()
covid = Label(tab1, text=data, fg="black", font=('arial', 12, 'bold'))
covid.pack(padx=30, pady=50, ipadx=30)
# Details of contact
contact_us = open('txt_files/Contact_us.txt')
data = contact_us.read()
details = Label(tab1, text=data, bg="lightgrey", fg="black", height=3, width=120,
                font=("ariel", 12))
details.pack(anchor='sw')

# Tab2 started here
top_img2 = PhotoImage(file="img/BG2.png")
img2 = Label(tab2, image=top_img2)
img2.pack()
# Create Label
lbl = Label(tab2, text="Enter Country:", font=("ariel", 15, "bold"))
lbl.pack(padx=5, pady=50, anchor='center')
# Create Entry Field
txt = Entry(tab2, width=40, font=("ariel", 15, "bold"))
txt.pack(padx=5, pady=10, anchor='center')
# Create Button
btn = Button(tab2, text="Get Information", command=get_country_info,
             font=("ariel", 13, "bold"))
btn.pack(padx=5, pady=10, anchor='center')
# Display Output for covid19 cases def up above
output_text = StringVar()
lbl_output = Label(tab2, textvariable=output_text, font=("ariel", 13, "bold"))
lbl_output.pack(padx=5, pady=10, anchor='center')

# Warning before user try to find the cases
text = Button(tab2, text="Warning! \n Please press this before searching",
              fg="black", font=('arial', 18, 'bold'), command=info)
text.pack(padx=30, pady=40, ipadx=30)

# Grey bar under for overall interface
Grey_bar = Label(tab2, bg="lightgrey", height=5, width=120)
Grey_bar.pack(anchor='s')

# Tab3 started here
img3 = PhotoImage(file="img/BG3.png")
label3 = Label(tab3, image=img3)
label3.pack()
lbl = Label(tab3, text="Enter locations you have visited:",
            font=("ariel", 15, "bold"))
lbl.pack(padx=5, pady=20, anchor='center')
# Create a TextBox for the file name
file_name = Entry(tab3, width=40, font=("ariel", 15, "bold"))
file_name.pack(padx=30, pady=10, anchor='center')
# Create a save button which uses the save_file function
save_button = Button(tab3, text="Save", font=("ariel", 13, "bold"),
                     command=lambda: [save_file(), reset_file_entry()])
save_button.pack(padx=30, pady=5, anchor='center')
# Display saved location that user input
locations = open("Saved_location/Saved_locations.txt")
display_locations = locations.read()
locations_label = Label(tab3, text=display_locations, height=10, width=90,
                        font=("ariel", 13, "bold"))
locations_label.pack(pady=40)
# Trey bar under for overall interface
Grey_bar = Label(tab3, bg="lightgrey", height=5, width=120)
Grey_bar.pack(anchor='s')

# Tab4 started here (under construction)
List = open('txt_files/Vax.txt')
data = List.read()
text = Label(tab4, text=data, fg="black", height=30, width=90,
             font=("ariel", 18, "bold"))
text.pack(padx=30, pady=30, anchor='center')

# Tab5 started here (under construction)
List = open('txt_files/Travel.txt')
data = List.read()
text = Label(tab5, text=data, fg="black", height=30, width=90,
             font=("ariel", 18, "bold"))
text.pack(padx=30, pady=30, anchor='center')

tab_control.pack(expand=True, fill='both')

# This used to stop user resizing the whole window
window.resizable(False, False)
# This is to run the window
window.mainloop()
