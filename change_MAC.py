#!/usr/bin/env python3

from subprocess import *
import optparse
import re

# change mac function
def change_mac(interface, newMAC):
    print("[+] change MAC address for",interface,"to",newMAC)
    call(['ifconfig', interface, 'down'])
    call(['ifconfig', interface, 'hw', 'ether', newMAC])
    call(['ifconfig', interface, 'up'])

def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface", dest="interface", help="Interface to change MAC")
    parse.add_option("-m","--mac", dest="new_MAC", help="New MAC Address ")
    (options, arguments) = parse.parse_args()
    if not options.interface:
        options.error("[+] Please specify an interface, use --help for more information")
    elif not options.new_MAC:
        options.error("[+] Please specify a new MAC, use --help for more information")
    return options

def get_mac(interface):
    ifconfig_result = check_output(["ifconfig", interface])
    print(ifconfig_result)
    a = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if a :
        return a.group(0)
    else:
        print("[-] Couldn't read Mac Address")


options = get_arguments()
change_mac(options.interface, options.new_MAC)
# a = get_mac(options.interface)
# print("mac =",a)
#tests


