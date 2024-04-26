#the trees got scrambled! use the tree name unscrambler to fix the mess

import re

tree_names = {'birch','acacia','oak','baobab','palm'}

def unscramble(scramled_string):
	found_trees = []
	for tree in tree_names:
		found_trees += re.findall(tree,scramled_string.lower())
	return found_trees



scrambled_tree_names = "soak biRchwooDoAkdj164spalmjSn3oakD2baobaBbbdacaciasdacacAOAKir"
######## no regex, ineficient approach ##########

found_trees = []
for letter_pos in range(len(scrambled_tree_names)):
	for tree in tree_names:
		if(scrambled_tree_names.lower().startswith(tree,letter_pos)):
			found_trees.append(tree)
print(f"Static string (no regex): {found_trees}")

#################################################


######## regex approach #########################

found_trees = unscramble(scrambled_tree_names)
print(f"Static string:{found_trees}")

#################################################


####### user input + regex ######################

user_str = input("Enter string:")
print(f"User inputed string: {unscramble(user_str)}")

#################################################


####### str from file + regex ###################

file = open("scrambled.txt","r")
scrambled_file_text = file.read()
file.close()
found_trees = unscramble(scrambled_file_text)
print(f"Trees from file: {found_trees}")

file = open("unscrambled.txt","w")
for tree in found_trees:
	file.write(f"{tree} ")
file.close()

#################################################