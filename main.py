#Names:
# Brenden Toussant
#
#
#

import nmap #Imports nmap library, allowing access to nmap functions
#!!!Figure out how to set up nmap to function and form ASM for our environment

nm = nmap.PortScanner() #Intializes the port scanner
nm.scan ('168.28.186.188','22-443') #('IP of local host','Range of port numbers')
nm.command_line()

# This is a sample Python script.