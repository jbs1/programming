"""Jeremy Schulz"""

def insertionsort(L,n=None):
	"""implementation of insertionsort with my double-linked list"""
	if n==None:
		n=len(L)
	for x in range(1,n):
		key = L.get_i(x).getItem()
		i=x-1
		while i>=0 and L.get_i(i).getItem()>key:
			L.set_i(i+1,L.get_i(i).getItem())
			i-=1
		L.set_i(i+1,key)
