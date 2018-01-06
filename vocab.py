from Parser import parser
import pickle
from os import path
import sys
#Checking for dictionary
if not path.exists('./VocabDictionary.pkl'):
	with open('VocabDictionary.pkl','wb') as f:
		pickle.dump({},f,protocol=pickle.HIGHEST_PROTOCOL)

if __name__=='__main__':
	parser.parse_args(sys.argv[1:])
