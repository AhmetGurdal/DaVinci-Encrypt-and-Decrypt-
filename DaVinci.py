#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp1254 -*-
a = (":#><`$|{[]}@.,;!^+&/()=?_%-* ~abcdefghijklmnopqrstwyzuvxUABCDEFGHIJKLMNOQPRSTWXVYZ1234567890'" + "\\" + "\"" + u"ĞÜŞÇÖİğüşıöç" + u"é£¨æß")
a.split()
key = raw_input(u"Key word:")
word  = raw_input(u"Text:")
que = raw_input("d or c:")
key = unicode(key,"cp857")
word = unicode(word,"cp857")
print ""
	
def cipher():
	last = ""
	i = 0
	for k in word:
		if i >= len(key):
				i = 0
		if a.find(k)+a.find(key[i]) + 1 >= len(a):
			last = last + a[a.find(k) + a.find(key[i]) - len(a)]
		else:
			last = last + a[a.find(k) + a.find(key[i])]
			
		i = i + 1
	print last
	#To write encryted text into a file
	#f = open("..\\Crypted.txt","w")
	#last = last.encode("utf-8","ignore")
	#f.write(last)
	#f.close

def decipher():
	last = ""
	i = 0
	for k in word:
		if i >= len(key):
				i = 0
		if a.find(k) - a.find(key[i]) + 1 < 0:
			last = last + a[a.find(k) - a.find(key[i]) + len(a)]
		else:
			last = last + a[a.find(k) - a.find(key[i])]
		i = i + 1
	print last

	
if que == "d":
	decipher()
elif que == "c":
	cipher()
	
raw_input()
