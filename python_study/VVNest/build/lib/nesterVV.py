"""This is a fucntion that can print nested list"""
"""This fucntion need one values as its variable"""
movies=["The holy grail",1975,"Terrys",91,["Graham",["Mike","John","Eric"]]]
def print_lol(the_list):
	for item in the_list:
		if isinstance(item,list):
			print_lol(item)
		else:
			print(item)
