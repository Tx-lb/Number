#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Script by Toxic Dz OFC!!
#I Love Free fire!!
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1

print "  _                                                                              "

print "|thes script by Toxic Dz ofc |insta @toxic_dz_ofc|  999 N scrapper on free fire  |   "

print " |  Toxic Tool |first tool of gettin link on free fire   | FF Try linking my account to Gmail  "

print "  because I lost my Facebook account, my UID is 48571916 ME server, credit Mustafa 404                                                     |                        "

def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print (req_link)


def Credit():
	Space(9); print "#####################################"
	Space(9); print "#    Script by Toxic dz ofc         #"
	Space(9); print "#    instagram @toxic_dz_ofc        #"
	Space(9); print "#####################################"


findAdmin()
