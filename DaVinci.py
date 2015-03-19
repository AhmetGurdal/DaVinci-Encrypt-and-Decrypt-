#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp1254 -*-
a= (":#><`$|{[]}@.,;!^+&/()=?_%-* ~abcdefghijklmnopqrstwyzuvxUABCDEFGHIJKLMNOQPRSTWXVYZ1234567890'"+"\\"+"\""+u"ĞÜŞÇÖİğüşıöç"+ u"é£¨æß")
a.split()
key=raw_input(u"Key word:")
word =raw_input(u"Text:")
que=raw_input("d or c:")
key= unicode(key,"cp857")
word=unicode(word,"cp857")
print ""
	
def cipher():
	son=""
	i=0
	for k in word:
		if i >=len(key):
				i=0
		if a.find(k)+a.find(key[i])+1 >= len(a):
			son=son+a[a.find(k)+a.find(key[i])-len(a)]
		else:
			son=son+a[a.find(k)+a.find(key[i])]
			
		i=i+1
	print son
	f=open("..\\Crypted.txt","w")
	son=son.encode("utf-8","ignore")
	f.write(son)
	f.close

def decipher():
	son=""
	i=0
	for k in word:
		if i >=len(key):
				i=0
		if a.find(k)-a.find(key[i])+1 < 0:
			son=son+a[a.find(k)-a.find(key[i])+len(a)]
		else:
			son=son+a[a.find(k)-a.find(key[i])]
		i=i+1
	print son

	
if que =="d":
	decipher()
elif que =="c":
	cipher()
	
raw_input()
