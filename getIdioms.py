def main():
	fo = open('idioms.txt','r+')
	a = fo.readlines()
	a = [x for x in a if x!='\n']
	for line in a:
		print line
main()
