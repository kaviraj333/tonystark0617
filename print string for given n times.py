def printv(val,n):
	for i in range(n):
		print(val)

def main():
	try :
		v=input()
		n=int(input())
		printv(v,n)
	except:
		print('invalid input')
main()
