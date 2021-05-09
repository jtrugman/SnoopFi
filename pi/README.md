# Network Scanner 
## What Does It Do? 
This Python script will scan the IP Addresses of devices connected to the same network and provide both the IP and MAC Address data. This data will then be sent to a server which will send an email to an email address of the user's choice. 

## How Does it Work? 
The sending device sends an ARP (Address Resolution Protocol) Request containing the IP Address of the device it wants to communicate with. After receiving the broadcast message, the device with the IP address equal to the IP address in the message will send an ARP Response containing its MAC Adress to the sender. The network scanner will use ARP Request and Response to scan the entire network to find active devices on the network and return their MAC Addresses. 

## Implementing Network Scanner
There are four main modules that need to be imported. The first is argparse which will parse user input for arguments to be called later in the script. The second is scapy which has a built-in function that can be used to find what member variables or fields a class has. The third is json which will allow a simple conversion of a dictionary to a string. The last is requests which will allow for interaction with the server. 

The first function defined is get_args(): which will parse the user input for the IP Address range and desired email address arguments. If the argument is missing the program will quit and ask to try again. 

The second function defined is scan(): which will create an ARP Request, create an Ethernet Frame, place the ARP Request inside the Ethernet Frame, send the combined frame and receive responses, and parse the responses and print the results.

The function display_result(): will display the IP and MAC Addresses in the terminal for the user to see. 

The function get_subject(): will create a subject line for the email to be sent. 

The function format_result(): will take the output data which is a dictionary and convert it to a string so it can be sent via email. 

The final 10 lines of code will connect to the server and send the email. 
