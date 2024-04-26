#the trees got scrambled! use the tree name unscrambler to fix the mess

#input from user
#get from file

import re

scrambled_tree_names = "soak biRchwooDoAkdj164spalmjSn3oakD2baobaBbbdacaciasdacacAOAKir"
tree_names = {'birch','acacia','oak','baobab','palm'}

scrambled_tree_names = scrambled_tree_names.lower()
#print(scrambled_tree_names.count('oak'))

found_trees = []
######## no regex, ineficient approach ##########
for letter_pos in range(len(scrambled_tree_names)):
	for tree in tree_names:
		if(scrambled_tree_names.startswith(tree,letter_pos)):
			found_trees.append(tree)
#################################################
print(found_trees)
found_trees = []
######## regex approach #########################
for tree in tree_names:
	tree_occurances = re.findall(tree,scrambled_tree_names)
	found_trees += tree_occurances
#################################################
print(found_trees)