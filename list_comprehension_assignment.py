import os

def items_in_dir():
	dir = str(input('Give Dir'))
	item_list = os.listdir(dir)
	items = []
	items = [os.path.abspath(item) for item in item_list]
	print ('Absolute Path of Items in a directory:\n',items)

def items_exc_dir():
	dir = (input('Give Dir'))
	item_list = []
	item_list = os.listdir(dir)
	print (item_list)
	item_list = [os.path.abspath(item) for item in item_list]
	print(item_list)
	items = []
	items = [item for item in item_list if os.path.isfile(item)]
	print ('Absolute path of items excluding directories:\n',items)
def print_imgs():
	dir = str((input('Give Dir')))
	item_list = []
	item_list = os.listdir(dir)
	print(item_list)
	items= []
	items = [item for item in item_list if '.png' in item or '.jpg' in item]
	print ('Only Images:',items)

def count_spaces():
	string = str((input('enter string')))
	count = 0
	char =[cha for cha in string]
	char.count(' ')
	print ('Number of spaces:',char.count(' '))
def rem_vowel():
	string=str((input('Enter string')))
	newstr = [str for str in string ]
	newstr = [ char for char in newstr if char not in ('a','e','i','o','u')]
	new =''.join(newstr)
	print ('String without vowels:',new)
def word_count():
	string=str((input('Enter string')))
	newstr = [str for str in string ]
	print ('Number of words:',newstr.count(' ')+1)
def word_l4_count():
	string=str((input('Enter string')))
	newlist = list(string.split(' '))
	newlist = [ word for word in newlist if len(word)<4]
	print('Words with less than 4 letters:',newlist)

def all_word_len():
	string=str((input('Enter string')))
	newlist = list(string.split(' '))
	newlist = [len(word) for word in newlist]
	print ('Length of each word:', newlist)

def main():
	items_in_dir()
	items_exc_dir()
	print_imgs()
	count_spaces()
	rem_vowel()
	word_l4_count()
	all_word_len()
	
main()