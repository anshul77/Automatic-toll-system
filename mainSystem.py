import detect as getVehicleNumber
import databaseHandler as databaseHandler
import Tkinter as tk
import tkMessageBox
import tkFileDialog
from PIL import ImageTk, Image


filepath = ''
panelA = None
panelB = None

#Let assume the sceneio where only a fixed amount of the tax would be paid
#otherwise for the real scenerio it has to be decided more efficiently
taxFare = 100

root = tk.Tk()
root.title("Toll Checker ")
root.geometry()

frame_1 = tk.LabelFrame(root, bg="gray", text="Recent Image..", borderwidth=1, width=500, height=400)
frame_1.grid_propagate(0)
frame_1.grid(row=0, column=0,  padx=10, pady=10 )

frame_3 = tk.LabelFrame(root, fg="black", text="Result..", borderwidth=2, width=500, height=400)
frame_3.grid_propagate(0)
frame_3.grid(row=0, column=1, padx=10, pady=10)

resultVehicleNumber = tk.Label(frame_3,text='image not selected...', font=("Helvetica", 16), padx=10, pady=10)
resultVehicleNumber.grid(row=0, column=0)
resultVehicleOwnerName = tk.Label(frame_3, text='', font=("Helvetica", 12), padx=10, pady=10)
resultVehicleOwnerName.grid(row=2, column=0)
resultVehicleOwnerMobile = tk.Label(frame_3, text='', font=("Helvetica", 12), padx=10, pady=10)
resultVehicleOwnerMobile.grid(row=3, column=0)
resultVehicleOwnerAddress = tk.Label(frame_3, text='', font=("Helvetica", 12), padx=10, pady=10)
resultVehicleOwnerAddress.grid(row=4, column=0)

resultVehicleBalance = tk.Label(frame_3, text='', font=("Helvetica", 12), padx=10, pady=10)
resultVehicleBalance.grid(row=1, column=0)

resultVehicleAlert = tk.Label(frame_3, fg = "red", text='', font=("Helvetica", 16), padx=10, pady=10)
resultVehicleAlert.grid(row=5, column=0)




# function definitions

def exit_command():
    try:
        result = tkMessageBox.askyesno("Exit the editor..", "Do you really want to quit.")
        if result == True:
            root.destroy()
        else:
            print
            # do nothing.
    except:
        tkMessageBox.showinfo("Editor not been quit..", "oops! some error occur\nplease check your functionality..")


def select_image():
    global panelA, panelB, filepath

    # open a file chooser dialog and allow the user to select an input
    path = tkFileDialog.askopenfilename()
    filepath = path
    # tkMessageBox.showinfo("filepath",filepath)
    # ensure a file path was selected
    if len(path) > 0:
        image = ImageTk.PhotoImage(Image.open(path))
        if panelA is None or panelB is None:
            panelA = tk.Label(frame_1, image=image, width=500, height=400)
            panelA.image = image
            panelA.grid(row=0, column=0)
        # otherwise, update the image panels
        else:
            panelA.configure(image=image)
            panelA.image = image
    clearDetails()

def clearDetails():
    resultVehicleNumber.config(text = "image not selected...")
    resultVehicleBalance.config(text = "")
    resultVehicleOwnerName.config(text = "")
    resultVehicleOwnerMobile.config(text = "")
    resultVehicleOwnerAddress.config(text = "")
    resultVehicleAlert.config(text = "")

def clear():
    global panelA
    panelA = None
    clearDetails()

def processing():
    global panelA, panelB, filepath
    # here to execute the getVehicleNumber.detectVehicleNumber
    vehicleNumber = getVehicleNumber.detectVehicleNumber(filepath )
    print vehicleNumber

    vehicleDetails = databaseHandler.getVehicleDetails(vehicleNumber)
    print vehicleDetails[0][0]
    # Initialising the vehicle details according to the result fetched by database handler

    # vehicleType = vehicleDetails[1]
    balance = int(vehicleDetails[0][2])-taxFare
    vehicleAlertstatus = vehicleDetails[0][3]
    vehicleOwnerName = vehicleDetails[0][4]
    vehicleOwnerMobile = vehicleDetails[0][5]
    vehicleOwnerAddress = vehicleDetails[0][6]
    databaseHandler.updatebalance(vehicleNumber,balance)
    # Setting the vehicle details to the interface
    resultVehicleNumber.config(text = "Vehicle Number = " + vehicleNumber)
    resultVehicleBalance.config(text = "Vehicle balance = " + str(balance))
    resultVehicleOwnerName.config(text="Onwer Name = " + vehicleOwnerName)
    resultVehicleOwnerMobile.config(text="Onwer Mobile = " + vehicleOwnerMobile)
    resultVehicleOwnerAddress.config(text="Owner Address = " + vehicleOwnerAddress)

    if (vehicleAlertstatus == True):
        resultVehicleAlert.config(text = "Alert !! The Vehicle is under police search")







frame_2 = tk.LabelFrame(root, fg="black", text="Functionality..", borderwidth=1, width=600, height=60)
frame_2.grid_propagate(0)
frame_2.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="N")

button_find = tk.Button(frame_2, text="Select Image", padx=10, command=select_image)
button_find.grid(row=0, column=0, padx=10, pady=10)

button_apply = tk.Button(frame_2, text="Apply ", padx=10, command = processing)
button_apply.grid(row=0, column=1, padx=10, pady=10)

button_clear = tk.Button(frame_2, text="Clear ", padx=10, command = clear)
button_clear.grid(row=0, column=2, padx=10, pady=10)

# ------------------

label_footer = tk.Label(root, text="@ designed by software engineers", padx=100, pady=5)
label_footer.grid_propagate(0)
label_footer.grid(row=3, column=0, columnspan=2)

# -----------------

root.resizable(True, True)
root.protocol("WM_DELETE_WINDOW", exit_command)
root.mainloop()




