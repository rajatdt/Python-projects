import sys
'''print sys.__doc__'''

file = open('tut2.py').readlines()
def file_ops():
    for item in file:
        if (not item.startswith('p') and not item.startswith('P')):
            print item
print "these statements do not have print in them"
