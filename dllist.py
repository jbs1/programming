"""Jeremy Schulz"""
import copy


class node(object):
	"""node for the linked list"""
	def __init__(self, item=None, prv=None, nxt=None):
		self.prv = prv
		self.item = item
		self.nxt = nxt

	def __str__(self):
		s=""
		s+="{"
		if self.prv==None:
			s+=str(None)
		else:
			s+=str(self.prv.getItem())
		s+=";"+str(self.item)+";"
		if self.nxt==None:
			s+=str(None)
		else:
			s+=str(self.nxt.getItem())
		s+="}"
		return s 

	def getNxt(self):
		return self.nxt
	def getPrv(self):
		return self.prv
	def getItem(self):
		return self.item
	def setNxt(self,v):
		self.nxt=v
	def setPrv(self,v):
		self.prv=v
	def setItem(self,v):
		self.item=v



class dllist(object):
	"""simple implementation of double linked list"""
	def __init__(self, first=None,last=None):
		self.first=first
		self.last=last

	def insertVal_end(self,val):
		if self.last==None and self.first==None:#empty list case
			n=node(val,None,None)
			self.first=n

		elif self.first!=None and self.last==None:#one elelmente list case
			self.last=node(val,self.first,None)
			self.first.setNxt(self.last)

		else:#rest case
			tmp=self.last
			n=node(val,tmp,None)
			self.last=n
			tmp.setNxt(n)

	def insertVal_start(self,val):
		if self.last==None and self.first==None:#empty list case
			n=node(val,None,None)
			self.first=n

		elif self.first!=None and self.last==None:#one elelmente list case
			self.last=self.first
			self.first=node(val,None,self.last)
			self.last.setPrv(self.first)

		else:#rest case
			tmp=self.first
			n=node(val,None,tmp)
			self.first=n
			tmp.setPrv(n)
	
	def length(self):
		i=0
		tmp=self.first
		while tmp.getNxt() != None:
			i+=1;
			tmp=tmp.getNxt()
		return i

	def __repr__(self):
		"""for debugging"""
		s="["
		tmp=self.first
		while True:
			s+=str(tmp)
			if tmp.getNxt()==None:
				break
			else:
				s+=","

			tmp=tmp.getNxt()
		s+="]"
		return s

	def __str__(self):
		s="["
		tmp=self.first
		while True:
			s+=str(tmp.getItem())
			if tmp.getNxt()==None:
				break
			else:
				s+=","

			tmp=tmp.getNxt()
		s+="]"
		return s


l=dllist()
m=dllist()

for i in range(5):
	l.insertVal_start(i)
	m.insertVal_end(i)

print(l)
print(repr(l))
print(m)
print(repr(m))