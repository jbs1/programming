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

	def ins_tl(self,val):
		"""insert value at tail"""
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

	def ins_hd(self,val):
		"""insert value at head"""
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

	def ins_i(self,val,index):
		"""insert value at index"""
		if index < 0 or index > len(self):
			print("Wrong index!")
			return False

		elif index == 0:
			self.ins_hd(val)

		elif index == len(self):
			self.ins_tl(val)

		else:
			i=0
			tmpnode=node(val,None,None)
			tmp=self.first
			while i<index:
				tmp=tmp.getNxt()
				i+=1

			tmp.getPrv().setNxt(tmpnode)
			tmpnode.setPrv(tmp.getPrv())
			tmpnode.setNxt(tmp)
			tmp.setPrv(tmpnode)
		return True

	def del_hd(self):
		"""delete element from head"""
		if self.__len__()==0:
			return False
		
		self.first=self.first.getNxt()
		self.first.setPrv(None)

		if self.first==None:#in case the last element is delted also set last=0
			self.last=None
		return True;

	def del_tl(self):
		"""delete element from tail"""
		if self.__len__()==0:
			return False
		
		self.last=self.last.getPrv()
		self.last.setNxt(None)

		if self.last==None:#in case the last element is delted also set first=0
			self.first=None
		return True;

	def del_i(self,index):
		"""delete value at index"""
		if index < 0 or index > len(self):
			print("Wrong index!")
			return False

		elif index == 0:
			self.del_hd()

		elif index == len(self):
			self.del_tl()

		else:
			i=0
			tmp=self.first
			while i<index:
				tmp=tmp.getNxt()
				i+=1

			tmp.getPrv().setNxt(tmp.getNxt())
			tmp.getNxt().setPrv(tmp.getPrv())
		return True
	
	def __len__(self):
		i=0
		tmp=self.first
		while tmp != None:
			i+=1
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



l=dllist();

for i in range(5):
	l.ins_tl(i)

print(repr(l))
l.ins_i(99,2)
print(repr(l))
l.del_i(2)
l.del_i(2)
print(repr(l))