# --importing external libraries--
from tkinter import *
from tkinter.ttk import Notebook
from tkinter import messagebox
import json
import time
import requests

# --Main Window--
window = Tk()
window.title("COVID-19 Information page")
window.geometry("800x600")


# --Def for Clock to run--
def update():
    clock.config(text=time.strftime('%H:%M:%S %p \n %d %B'))
    clock.after(1000, update)


# --Def for getting Covid cases--
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
    covid_msg = f"Last number of new confirmed cases in {searchcountry}: {newconfirmed}.\nThe total cases are: {totalconfirmed}"
    # Return covid msg to gui
    output_text.set(covid_msg)


def info():
    List = open('txt_files/Info message.txt')
    data = List.read()
    messagebox.showinfo(title="Info!", message=data)


# function for saving text to text file
def save_file():
    stuff = open("Saved_location/Saved_locations.txt", "a")
    if file_name.get() == "":
        messagebox.showerror("")
    else:
        stuff.write(file_name.get())
        stuff.write("\n")
    stuff.close()


def reset_file_entry():
    file_name.delete(0, END)


def update_window():
    tab3.update()


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

img = PhotoImage(file="img/BG1.png")
label = Label(tab1, image=img)
label.place(x=0, y=0)
clock = Label(tab1, bg='lightgrey', foreground='black', font=('arial', 18, 'bold'))
update()
clock.pack(pady=2, anchor='e')
List = open('txt_files/COVID_19.txt')
data = List.read()
text = Label(tab1, text=data, fg="black", font=('arial', 12, 'bold'))
text.pack(padx=30, pady=50, ipadx=30)
List = open('txt_files/Contact_us.txt')
data = List.read()
text2 = Label(tab1, text=data, bg="lightgrey", fg="black", height=3, width=120, font=("ariel", 12))
text2.pack(anchor='sw')

img2 = PhotoImage(file="img/BG2.png")
label2 = Label(tab2, image=img2)
label2.pack()
# Create Label
lbl = Label(tab2, text="Enter Country:", font=("ariel", 15, "bold"))
lbl.pack(padx=5, pady=50, anchor='center')
# Create Entry Field
txt = Entry(tab2, width=40, font=("ariel", 15, "bold"))
txt.pack(padx=5, pady=10, anchor='center')
# Create Button
btn = Button(tab2, text="Get Information", command=get_country_info, font=("ariel", 13, "bold"))
btn.pack(padx=5, pady=10, anchor='center')
# Display Output
output_text = StringVar()
lbl_output = Label(tab2, textvariable=output_text, font=("ariel", 13, "bold"))
lbl_output.pack(padx=5, pady=10, anchor='center')

text = Button(tab2, text="Warning! \n Please press this before searching", fg="black", font=('arial', 18, 'bold'),
              command=info)
text.pack(padx=30, pady=40, ipadx=30)

Grey_bar = Label(tab2, bg="lightgrey", height=5, width=120)
Grey_bar.pack(anchor='s')

img3 = PhotoImage(file="img/BG3.png")
label3 = Label(tab3, image=img3)
label3.pack()
lbl = Label(tab3, text="Enter locations you have visited:", font=("ariel", 15, "bold"))
lbl.pack(padx=5, pady=20, anchor='center')
# create a TextBox for the file name
file_name = Entry(tab3, width=40, font=("ariel", 15, "bold"))
file_name.pack(padx=30, pady=10, anchor='center')
# create a save button which uses the save_file function
save_button = Button(tab3, text="Save", font=("ariel", 13, "bold"), command=lambda: [save_file(), reset_file_entry()])
save_button.pack(padx=30, pady=5, anchor='center')

locations = open("Saved_location/Saved_locations.txt")
display_locations = locations.read()
locations_label = Label(tab3, text=display_locations, height=10, width=90, font=("ariel", 13, "bold"))
locations_label.pack(pady=40)

Grey_bar = Label(tab3, bg="lightgrey", height=5, width=120)
Grey_bar.pack(anchor='s')

List = open('txt_files/Vax.txt')
data = List.read()
text = Label(tab4, text=data, fg="black", height=30, width=90, font=("ariel", 18, "bold"))
text.pack(padx=30, pady=30, anchor='center')

List = open('txt_files/Travel.txt')
data = List.read()
text = Label(tab5, text=data, fg="black", height=30, width=90, font=("ariel", 18, "bold"))
text.pack(padx=30, pady=30, anchor='center')

tab_control.pack(expand=True, fill='both')

window.resizable(False, False)
window.mainloop()
