
def main():
	one = input().split()
	two  = input().split()
	lenth = len(one)
	print(one)
	print(two)
	iter1 = 1
	for i in range(lenth):
		if ''.join(one[i]+two[i]) not in ['AT','TA','CG','GC']:
			iter1 = iter1 + 1
	print (iter1)
if __name__ == "__main__":
	main()