#!usr/bin/python
import sys
text =' '.join(sys.argv[1:])
def func(s):	
	ret = ""
	i = True
	for char in s:
		if i:
			ret += char.upper()
		else:
			ret += char.lower()
		if char!= ' ':
			i = not i
	return ret
print func(text)
