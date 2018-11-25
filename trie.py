#INSPIRATION FROM: https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python

class Trie:
    
    #init trie as empty dict 
    def __init__(self):
        self.root = {}

    #insert ip in binary into trie, with metadata (allowed ports, protocol, direction) stored at "end" 
    def insert(self, bin_ip, metadata):
        node = self.root
        for char in bin_ip:
            node = node.setdefault(char, {})

        #if ip prefix is already in trie, append tuple to list
        if "end" in node:
            node["end"].append(metadata)
        #else create list with tuple
        else:
            node["end"] = [metadata]


    #search trie for ip, check if tuple is at end
    #if so, ret True, else, ret False 
    def search(self, bin_ip, tup):

        #INNER HELPER FUNCS 

        #given a tuple stored in the trie and a given tuple, check if given tuple falls within allowed params 
        #i.e. if direction and protocol are equal, and port falls within allowed range
        #if so ret True, else, ret False 
        def compare(saved, check):
            print(saved, check)
            if saved[0] == check[0] and saved[1] == check[1] and saved[2] <= check[2] and check[2] <= saved[3]:
                return True
            else:
                return False

        #for given node, return True if "end" is in node and given tuple matches stored metadata
        #else ret False 
        def check_finish(node):
            if "end" in node:
                allowed_lst = node["end"]
                for metadata in allowed_lst:
                    if (compare(metadata, tup)):
                        return True
            return False 


        node = self.root

        #find given ip in tree 
        for char in bin_ip:
            #if existing portion of ip matches, return True
            if "end" in node:
                if check_finish(node):
                    return True
            
            #otherwise, find next character in trie 
            if char in node:
                node = node[char]
            else:
                return False


        #at end of ip, run check for matching "end"
        return check_finish(node)


    #print dict for debugging purposes 
    def display(self):
        print (self.root)
