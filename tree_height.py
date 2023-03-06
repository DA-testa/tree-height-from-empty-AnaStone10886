# python3

import sys
import threading


class Nodes:
    def __init__(self):
        #self.val = val
        self.children = []

    def __str__(self, level=0, height=0):
        if height == 0:
            height = self.getHeight()
        ret = "\t" * level + repr(self.val) + ("____" * height) + "\n"
        for child in self.children:
            if child is None:
                ret += ("\t" * (level+1)) + "|\n"
            else:
                ret += child.__str__(level + 1, height-1)
        return ret
    def children():
        children = []
    
    def __repr__(self):
        return '<tree node representation>'
    
    def getHeight(self):
        h = 1
        if self.children is None:
            return h
        for c in self.children: 
            if c is not None: 
                h = max(h, c.getHeight()+1)
        return h

def compute_height(n, parents):
    root = []
    t = Nodes = []
    for i in parents:
        if i == -1:
            root = parents.index(i)
            t.append(root)
        if i != -1:
            t.children.append(parents.index(i))
            
            
    # Write this function
    max_height = 0
    max_height = Nodes.__str__()
    
    # Your code here
    return max_height


def main():
    str = input()
   
    if "I" in str:
        n = int(input())
        # print(n, type(n))
        parents = list(map(int,input().split()))
        compute_height(n, parents)
       
    elif "F" in str:
        fileName = "./test/"+ input()
        
        if "a" in fileName:
            print ("wrong file name")
        else:
            file = open(fileName, "r")
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))
            compute_height(n, parents)
    
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()