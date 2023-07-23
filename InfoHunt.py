import os
from colorama import init, Fore, Back, Style
import time

def print_banner(message):
    # Clear the terminal
    os.system('clear')

    # Define the ANSI escape code for purple color
    purple = '\033[95m'

    # Get the width of the terminal
    terminal_width = os.get_terminal_size().columns

    # Calculate the padding for center alignment
    padding = (terminal_width - len(message)) // 2

    # Print the banner
    print(f"{purple}{' ' * padding}{message}{' ' * padding}")

# Example usage
banner = "▀█▀ █▀▀▄ █▀▀ █▀▀█ ▒█░▒█ █░░█ █▀▀▄ ▀▀█▀▀\n" \
         "▒█░ █░░█ █▀▀ █░░█ ▒█▀▀█ █░░█ █░░█ ░░█░░\n" \
         "▄█▄ ▀░░▀ ▀░░ ▀▀▀▀ ▒█░▒█ ░▀▀▀ ▀░░▀ ░░▀░░"

print_banner(banner)
print("version 1.0")
print(Fore.YELLOW + Style.BRIGHT +  "please choose from the following options : ")
print("======================================================================================>>>")
print(Fore.GREEN + Style.BRIGHT + "1.information gather (phone numbers) [1]")
print(Fore.CYAN+ Style.BRIGHT + "2.information gathering (Ip addresses & websites ) [2]") 
print(Fore.MAGENTA+ "3.About this tool [3]") 
print(Fore.YELLOW + Style.BRIGHT + "=====================================================")
print(Fore.CYAN + Style.BRIGHT + "enter option below ")
option = input(">>> ")

if option == '1':
    #pyth
    import phonenumbers
    from phonenumbers import timezone, geocoder, carrier
    num = input("Enter number with code (e.g. +91123456789) :  ")
    time.sleep(1)
    print("fetching info............")
    time.sleep(3)
    p = phonenumbers.parse(num)
    t = timezone.time_zones_for_number(p)
    c = carrier.name_for_number(p,"en")
    print(Fore.YELLOW + Style.BRIGHT + (f"BASE INFO    : {p}"))
    print(Fore.MAGENTA + Style.BRIGHT + (f"TIMEZONE     : {t}"))
    print(Fore.GREEN + Style.BRIGHT + (f"CARRIER      : {c}"))
    print(Fore.CYAN + Style.BRIGHT + (f"COUNTRY OR STATE: {geocoder.description_for_number(p,'en')}"))
    print("[✓] Done.")

elif option == '2':
    import requests
    import socket

    address = input("Enter IP address or website address to track (website e.g. google.com) : ")
    time.sleep(1)
    print("Fetching info .........")
    time.sleep(3)
    try:
        # Check if the input is a valid IP address
        socket.inet_aton(address)
        ip_address = address  # Use the input as the IP address
    except socket.error:
        # Input is not a valid IP address, resolve the website address to an IP address
        ip_address = socket.gethostbyname(address)

    url = f"http://ip-api.com/json/{ip_address}"

    response = requests.get(url).json()

    print(Fore.RED + Style.BRIGHT + (f"\nIP Address:               {response['query']}"))
    print(Fore.CYAN + Style.BRIGHT + (f"Country:                   {response['country']}"))
    print(Fore.GREEN + Style.BRIGHT + (f"City:                     {response['city']}"))
    print(Fore.MAGENTA + Style.BRIGHT + (f"Region:                 {response['regionName']}"))
    print(Fore.YELLOW + Style.BRIGHT + (f"ISP:                     {response['isp']}"))
    print(Fore.WHITE + Style.BRIGHT + (f"Latitude:                 {response['lat']}"))
    print(Fore.WHITE + Style.BRIGHT + (f"Longitude:                {response['lon']}"))
    print(Fore.GREEN + Style.BRIGHT + (f"Timezone:                 {response['timezone']}"))
    print(Fore.CYAN + Style.BRIGHT + (f"ZIP Code(might not be accurate) :   {response['zip']}"))
    print("""            Done [√].           """)
elif option == '3':
	print("""InfoHunt is a information gathering tool that helps the the user to collect basic information about phone numbers and ip address for more information check the InfoHunt github page .
Thanks for using this tool""")
else:
	print(" No such option [x]")
