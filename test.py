#the trees got scrambled! use the tree name unscrambler to fix the mess

#input from user
#get from file

import re

scrambled_tree_names = "soak biRchwooDoAkdj164spalmjSn3oakD2baobaBbbdacaciasdacacAOAKir"
tree_names = {'birch','acacia','oak','baobab','palm'}

scrambled_tree_names = scrambled_tree_names.lower()
print(scrambled_tree_names.count('oak'))

######## no regex, ineficient approach ##########
found_trees = []
for letter_pos in range(len(scrambled_tree_names)):
	for tree in tree_names:
		if(scrambled_tree_names.startswith(tree,letter_pos)):
			found_trees.append(tree)
print(found_trees)
#################################################


######## regex approach #########################
found_trees = []
for tree in tree_names:
	tree_occurances = re.findall(tree,scrambled_tree_names)
	found_trees += tree_occurances
print("Static string:",found_trees)
#################################################


####### user input + regex ######################
found_trees = []
user_str = input("Enter string:")
user_str = user_str.lower()
for tree in tree_names:
	tree_occurances = re.findall(tree,user_str)
	found_trees += tree_occurances
print("User inputed string:",found_trees)
#################################################


####### str from file + regex ###################
found_trees = []
file = open("scrambled.txt","r")
scrambled_file_text = file.read()
scrambled_file_text = scrambled_file_text.lower()
for tree in tree_names:
	found_trees += re.findall(tree,scrambled_file_text)
print("Trees from file:",found_trees)
file.close()


file = open("unscrambled.txt","w")
for tree in found_trees:
	file.write(tree)
#################################################