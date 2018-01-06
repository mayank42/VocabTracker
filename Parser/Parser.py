from argparse import ArgumentParser
from Actions import *
#Creating parser object
parser = ArgumentParser(prog='VocabTracker',description='This is a command line tool to help keep track of accumulating subject vocabulary as you learn the subject. You can add,remove or search for words.')

#Adding add option
parser.add_argument('--add','-a',action=AddToDict,nargs=2,metavar=('WORD','MEANING'))

#Adding search option
parser.add_argument('--search','-s',action=SearchInDict,metavar='WORD')

#Adding remove option
parser.add_argument('--remove','-r',action=RemoveFromDict,metavar='WORD')

