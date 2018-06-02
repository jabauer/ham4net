#!/usr/bin/python

import itertools
import csv
# Open a file
character_lists = open("ham_co_speakers.csv")
# print "Name of File: ", character_lists.name

lines = character_lists.readlines()
# print lines

# # print lines[0]
# test_lines = lines[0].strip().split(',')
# co_speakers = list(itertools.combinations(test_lines,2))
# print co_speakers

edge_list = []

for co_character_list in lines:
	co_character_list = co_character_list.rstrip()
	co_character_list = co_character_list.split(',')
	# print character_list
	co_characters = list(itertools.combinations(co_character_list,2))
	# print co_characters
	edge_list.extend(co_characters)

# print edge_list

with open('co_singer_edges.csv','wb') as out:
	csv_out=csv.writer(out)
	csv_out.writerow(['character1','character2'])
	for row in edge_list:
		csv_out.writerow(row)
