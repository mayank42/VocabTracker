from Parser import parser
import pickle
from os import path

#Checking for dictionary
if not path.exists('./VocabDictionary.pkl'):
	with open('VocabDictionary.pkl','wb') as f:
		pickle.dump({},f,protocol=pickle.HIGHEST_PROTOCOL)
#Testing
parser.parse_args('--add mayank best'.split())
parser.parse_args('--search mayank'.split())
parser.parse_args('--remove mayank'.split())
parser.parse_args('--search mayank'.split())
