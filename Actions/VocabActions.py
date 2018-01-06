from argparse import Action
import pickle
class AddToDict(Action):
	def __call__(self,parser,namespace,values,option_string=None):
		with open('VocabDictionary.pkl','rb') as f:
			vocab=pickle.load(f)
		vocab[values[0]] = values[1]
		with open('VocabDictionary.pkl','wb') as f:
			pickle.dump(vocab,f,protocol=pickle.HIGHEST_PROTOCOL)

class SearchInDict(Action):
	def __call__(self,parser,namespace,values,option_string=None):
		with open('VocabDictionary.pkl','rb') as f:
			vocab=pickle.load(f)
		if values in vocab:
			print('{0} - {1}'.format(values,vocab[values]))
		else:
			print('Word not found in dictionary.')
class RemoveFromDict(Action):
	def __call__(self,parser,namespace,values,option_string=None):
		with open('VocabDictionary.pkl','rb') as f:
			vocab=pickle.load(f)
		if values in vocab:
			del vocab[values]
			with open('VocabDictionary.pkl','wb') as f:
				pickle.dump(vocab,f,protocol=pickle.HIGHEST_PROTOCOL)
		else:
			print('Word not found in dictionary.')
