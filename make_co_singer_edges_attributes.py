#!/usr/bin/python

import itertools
import csv
# Open a file
character_lists = open("Ham4NetLibretto_001.tsv")
# print "Name of File: ", character_lists.name

lines = character_lists.readlines()[1:]
# print lines

edge_list = []

for data in lines:
	data = data.rstrip().split('\t')
	lyric = data[1].rstrip()
	song = data[2].rstrip()
	act = data[3].rstrip()
	attributes = [lyric,song,act]
	# print attributes
	singers = data[0].rstrip().split(',')
	co_singers = list(itertools.combinations(singers,2))
	# print co_singers
	# edge_list.extend(co_singers)
	for duo in co_singers:
		edge_list.append(list(duo) + attributes)


print edge_list

with open('co_singer_edges_acts.csv','wb') as out:
	csv_out=csv.writer(out)
	csv_out.writerow(['character1','character2','lyric','song','act'])
	for row in edge_list:
		csv_out.writerow(row)
