#!/usr/bin/python

import itertools 
# Open a file

author_lists = open("ham_co-speakers.csv")
# author_lists = open("BM_co-author_network.csv")
#print "Name of File: ", author_lists.name

issues = author_lists.readlines()
# print issues

# print issues[0]
# test_issue = issues[0].rstrip()
# test_issue = test_issue.split(',')
# print test_issue
# print list(itertools.combinations(test_issue,2))

edge_list = []

for author_list in issues:
	author_list = author_list.rstrip()
	author_list = author_list.split(',')
	# print author_list
	co_authors = list(itertools.combinations(author_list,2))
	print co_authors
# 	edge_list.extend(co_authors)

# print edge_list
