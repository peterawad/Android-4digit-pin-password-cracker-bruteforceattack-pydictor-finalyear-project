import tkinter as tk
from tkinter import filedialog
import itertools
import pydictor
import subprocess
import AndroidBruteForce as and_br_fo
import pyautogui


def main():
    	# Set up the ADB connection to the Android device over USB
        # Start check server and make kill if running and start again then list devices
        subprocess.run(["adb", "kill-server"])
        subprocess.run(["adb", "start-server"])
        devices = subprocess.run(["adb", "devices"], capture_output=True)
        
        # if device not list we display msg then exit
        if b"device\n" not in devices.stdout:
                print("No device found. Make sure your Android device is connected and USB debugging is enabled.")
                exit()
        else:
                and_br_fo.abf()
                start_program()
                
def start_program():
        # Create a window
        window = tk.Tk()
        window.title("Control your device")
        # Create a label
        label = tk.Label(window, text="Select an action:")

        # Add the label to the window
        label.pack()

        # Create a frame for the buttons
        button_frame = tk.Frame(window)

        # Create 13 buttons with different names and commands run onclick on button
        button_names = ["Open the camera", "Volume up", "Volume down","Make a Call","Answer call", "Cancel call", "Lock ring", "Transfer a file to the device", 
                        "Transfer a file from the device", "Screenshot", "Screen record", "Contacts", "Turn the Android device ON and OFF", 
                        "open Bluetooth "]
        button_functions = [open_camera, volume_up, volume_down, make_call, ANSWER_call, cancel_call, lock_ring, transfer_to_device, transfer_from_device, 
                            take_screenshot, start_screen_record, show_contacts, power_on_off, connect_bluetooth]

        for i, name in enumerate(button_names):
                button = tk.Button(button_frame, text=name, command=button_functions[i])
                button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Add the button frame to the window 
        button_frame.pack()
        
        # Start the main loop
        window.mainloop()

# Define the functions for each button(What is AFTER THE Android brute force)
# functions to start control Androide

# Open Mobile camera 
def open_camera():
    command = f"adb shell input keyevent 27"  
    result2 = subprocess.run(command, shell=True, capture_output=True)
    print("Opening the camera...")

# up volume of device
def volume_up():
    command = f"adb shell input keyevent 24"
    result2 = subprocess.run(command, shell=True, capture_output=True)
    print("Volume up...")

# Down volume of device
def volume_down():
    command = f"adb shell input keyevent 25"
    result2 = subprocess.run(command, shell=True, capture_output=True)
    print("Volume down...")

# Transfer file from your PC to internal storage on device using open dialogue     
def transfer_to_device():
    filepath = filedialog.askopenfilename(initialdir="/home/peter/Desktop",title="Open file okay?",filetypes= (("text files","*.txt"),("Image","*.jpg"), ("All files",".")))
    #window = tk()
    #button = Button(text="Open",command=openFile)
    print(filepath)
    subprocess.Popen(["adb", "push", filepath, "/sdcard/Testscreen"])
    print("Transferring a file to the device...")

# you can take screenshot on andoride device and store in internal storage device 
def take_screenshot():
    command = f"adb shell screencap /sdcard/screen.png"   
    result2 = subprocess.run(command, shell=True, capture_output=True)
    print("Taking a screenshot...")

# open contacts on mobile
def show_contacts():
    command = f"adb shell input keyevent 207"
    result2 = subprocess.run(command, shell=True, capture_output=True)
    print("Showing contacts...")

# make alock for your device
def power_on_off():
    command = f"adb shell input keyevent 26"
    result2 = subprocess.run(command, shell=True, capture_output=True)
    print("Turning the Android device ON and OFF...")

# you can cancel incoming calls
def cancel_call(): 
    command = f"adb shell input keyevent 6" # 
    result2 = subprocess.run(command, shell=True, capture_output=True)
    print("Cancelling the call...")
    
# you can answer incoming call    
def ANSWER_call(): 
    command = f"adb shell input keyevent 79" 
    result2 = subprocess.run(command, shell=True, capture_output=True)
    print("Answer the call...")

# start and stop recording video for 10 second and store in internal storage device
def start_screen_record():
    command = f"adb shell screenrecord --time-limit=10 /sdcard/time.mp4"
    result2 = subprocess.run(command, shell=True, capture_output=True)

# you can take screenshot on andoride device and save it in storage device 
tel_no=""
def calling(tel_no):
        # check if number is valid or not 
        print(tel_no) 
        if not tel_no.isdigit():
                print("invalid phone number")
                return
    
        # write phone number or call screen on andoride then make a call
        command2 = f"adb shell input text {tel_no}"
        result2 = subprocess.run(command2, shell=True, capture_output=True)
        command3 = f"adb shell input keyevent 5"
        result3 = subprocess.run(command3, shell=True, capture_output=True)
         
        print("Making a call...")
        
def make_call():       
        # Create the window.
        command = f"adb shell input keyevent 5 && adb shell input keyevent 5"
        result = subprocess.run(command, shell=True, capture_output=True)
        window = tk.Tk()
        label = tk.Label(window, text="Please Enter phoone number:")
        label.pack()
        # Create the text box.
        text_box = tk.Entry(window)

        # Place the text box in the window.
        text_box.pack()
        tel_no = text_box.get()
        
        button_frame = tk.Frame(window)
        button = tk.Button( window, text="Make a Call", command=lambda: calling(text_box.get()))
        button.pack()
        
        window.mainloop()




# you can set ring off while call still ring 
def lock_ring():
        command = f"adb shell input keyevent 11"
        result2 = subprocess.run(command, shell=True, capture_output=True)
        print("Locking the ring...")






# Transfer file from your  to internal storage on device  to connected pc using open dialogue 
def transfer_from_device():
        command = f"adb pull sdcard/Testscreen/file.txt /home/peter/Desktop/recieve/"
        result = subprocess.run(command, shell=True, capture_output=True)
        print("Transferring a file from the device...")
    
    


# open Bluetooth setting 
def connect_bluetooth():
       
       
        # Open Bluetooth settings
        subprocess.run(["adb", "shell", "am", "start", "-a", "android.settings.BLUETOOTH_SETTINGS"], capture_output=True)

        # Wait for settings to open
        subprocess.run(["adb", "shell", "sleep", "2"], capture_output=True)

        # Check Bluetooth status
        bluetooth_status = subprocess.check_output(["adb", "shell", "settings", "get", "secure", "bluetooth_on"], universal_newlines=True).strip()

        if bluetooth_status == "0":
                # Enable Bluetooth
                subprocess.run(["adb", "shell", "input", "keyevent", "SPACE"], capture_output=True)
                subprocess.run(["adb", "shell", "input", "keyevent", "ENTER"], capture_output=True)
                subprocess.run(["adb", "shell", "input", "keyevent", "BACK"], capture_output=True)


        print("Bluetooth is now enabled")

# calling main to start project
main()       



        


    
""" Another way to use recording screen on or off 
is_recording = False
    global is_recording
    if not is_recording:
        # start recording
        subprocess.call(['adb', 'shell', 'screenrecord', '/sdcard/screen.mp4'])
        is_recording = True
        button.config(text='Stop Recording')
        print("Starting screen recording...")
    else:
        # stop recording
        subprocess.call(['adb', 'shell', 'pkill', 'screenrecord'])
        subprocess.call(['adb', 'pull', '/sdcard/screen.mp4', './screen.mp4'])
        is_recording = False
        button.config(text='start Recording')
"""


