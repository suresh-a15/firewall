#NOTE: uses python3

import csv
from trie import Trie
from ipaddress import IPv4Address, summarize_address_range

#HELPER FUNCS

#given a string with two values separated by a hyphen, return both (as strings)
#if one value, return it twice 
def return_range(string):
    ind = string.find("-")
    if ind == -1:
        return string, string
    else:
        lower = string[:ind]
        upper = string[ind + 1:]
        return lower, upper

#given either a single ip as a string or a range of ips, insert into trie with a tuple of other params 
def insert_ips(ips, trie, tup):
    lower, upper = return_range(ips)

    #if one ip:
    if lower == upper:
        #convert ip to binary before inserting
        toInsert = str(bin(int(IPv4Address(ips))))[2:]
        trie.insert(toInsert, tup)
        
    else:
        lower = IPv4Address(lower)
        upper = IPv4Address(upper)
        #returns set of cidr address prefixes that encompass full range
        iterator = summarize_address_range(lower, upper)

        #for each entry in the iterator 
        for addr in iterator:
            #convert network prefix to binary, only insert length of prefix 
            #note that all entries within that match cidr prefix will be identical in binary to prefixlen chars of prefix
            #then insert 
            toInsert = str(bin(int(addr.network_address)))[2:addr.prefixlen + 2]
            trie.insert(toInsert, tup)



#Firewall Class
class Firewall:

    #to initialize:
    def __init__(self, filename):

        #create trie 
        self.ip_trie = Trie()

        #for each line in csv file, separate params 
        with open(filename, 'rt') as csvfile:

            rule_list = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in rule_list:
                direction = row[0]
                protocol = row[1]
                ports = row[2]
                ips = row[3]

                #insert into trie: ip range, and tuple consisting of direction, protocol, port range 
                lower, upper = return_range(ports)
                insert_ips(ips, self.ip_trie, (direction, protocol, int(lower), int(upper)))

        #self.ip_trie.display()

    #accept packet function
    def accept_packet(self, direction, protocol, port, ip_address):

        #convert given ip to binary
        bin_ip = str(bin(int(IPv4Address(ip_address))))[2:]

        #search for ip address in trie, see if tuple matches 
        return self.ip_trie.search(bin_ip, (direction, protocol, port))




                
