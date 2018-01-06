from argparse import ArgumentParser
from Actions import *
#Creating parser object
parser = ArgumentParser(prog='Network Vocab Dictionary',description='This is a command line tool to help keep track of accumulating network vocabulary as you learn Networking. You can add network terms, add your own custom meanings to them.')

#Adding add option
parser.add_argument('--add','-a',action=AddToDict,nargs=2,metavar=('WORD','MEANING'))

#Adding search option
parser.add_argument('--search','-s',action=SearchInDict,metavar='WORD')

#Adding remove option
parser.add_argument('--remove','-r',action=RemoveFromDict,metavar='WORD')

