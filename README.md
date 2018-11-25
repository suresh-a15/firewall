a. Testing: I tested my code on only a small amount of input rules - with more time, I'd programmatically add a mass amount to a csv file to check whether this would significantly slow down my code. In addition, I realized in retrospect that most of my test cases involved examples that were meant to return true rather than false; I would balance these out given more time as well. 

b. Algorithmic Decisions: The general gist of my algorithm involves a trie to store IP addresses, which has a linear insertion runtime dependent on the number of words to be inserted, and a constant runtime for search, since the alphabet size is fixed at 2 and the length of an IP address is 32 at max. I took a significant amount of functional help from the standard python library ipaddr - using it in particular to turn an ip address range into a set of cidr addresses with specified prefix lengths. These prefixes I inserted into the trie, such that the first [prefixlen] characters of any given ip will match that entry in the trie. If there is a match, the direction, port, and protocol are checked against allowed possibilities, and the function returns True if allowed, and otherwise continues down the trie. I chose this implementation over a more conventional dictionary primarily for space efficiency, though direct lookup via ip address would have been easier with this sort of dictionary.

c. Future Implementation Changes: With more time, I'd change my trie implementation to something less generic and more efficient - my current version used a series of nested dictionaries, and could have been better planned, perhaps with a custom node design. 

d. I would say that of the three areas, I am most interested in Policy and Data. 



SOURCES:
for the ipaddr library:
https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address

for trie creation:
https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
