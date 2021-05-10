import scapy.all as scapy
import argparse
import json
import requests


    #setup code for parsing
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '-- receiver', dest='email', help='Receiver Email Address')
    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
    options = parser.parse_args()

    #Check for errors
    #Quit the program if the argument is missing
    if not options.target:
        #Display error message
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
    return options
    #Code to scan IP Adress/Adresses
def scan(ip):
    #Create Arp Request
    arp_req = scapy.ARP(pdst = ip)
    #Create ethernet frame and place ARP request in ethernet frame
    broadcast_ether = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")

    broadcast_ether_arp_req = broadcast_ether / arp_req
    #Send combined frame and receive responses
    #Parse responses and print result
    answer_list = scapy.srp(broadcast_ether_arp_req, timeout = 1, verbose = False)[0]
    result = []
    for i in range(0,len(answer_list)):
        client_dict = {"ip" : answer_list[i][1].psrc, "mac" : answer_list[i][1].hwsrc}
        result.append(client_dict)

    return result
    #Displays IP and Mac Addresses in Terminal
def display_result(result):
    print("-----------------------------------\nIP Address\tMAC Address\n-----------------------------------")
    for i in result:
        print("{}\t{}".format(i["ip"], i["mac"]))

def get_subject(tar):
        return "Network Scan Data From" + " " + tar
    #Converts from dictionary list to string
def format_result(result):

    # return string
    return str(result)

options = get_args()
scanned_output = scan(options.target)
display_result(scanned_output)
subject = get_subject(options.target)
output = format_result(scanned_output)

#Connects to Server and sends email with data
url = "http://localhost:3000/network"

payload="{\n    \"to\" : \"" + options.email + "\",\n    \"subject\": \"" + subject + "\",\n    \"net_data\" : \"" + output + "\"\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
