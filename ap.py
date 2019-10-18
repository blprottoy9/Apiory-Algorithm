f1=open('table.txt').read().split('\n')
p=['I1','I2','I3','I4','I5']
sup_count=int(input("support count:"))
#n=int(input("Max combination:"))
ls=[0,0,0,0,0]
del f1[len(f1)-1]
print(f1)
for i in f1:
	
	#print(a)
	if 'I1' in i:
		ls[0]+=1
	if 'I2' in i:
		ls[1]+=1
	
	if 'I3' in i:
		ls[2]+=1
	if 'I4' in i:
		ls[3]+=1
	if 'I5' in i:
		ls[4]+=1
	
#print('i1:',i1,' i2',i2,' i3:',i3,' i4:',i4,' i5:',i5)


print(ls)
i=0
a=len(ls)
while i <a:
	#print(ls[i])
	if ls[int(i)]<sup_count:
		ls.pop(i)
		p.pop(i)
		a-=1
	else:
		i+=1

#while find_com!=0:
	#print(i)
ppp=[]
llls=[]
for i in range(len(p)):
	ppp.append(p[i])
	llls.append(ls[i])
i=0
print(p)
print(ls)

p1=p
p=[]
ls1=ls
ls=[]
while i<a:
	j=i+1
	while j<a:

		p.append(p1[i]+','+p1[j])
		ls.append(0)
		j+=1
	i+=1
m=0
i=0
print(p)
print(ls)


while m<len(p):
	a1=p[m].split(',')
	for i1 in f1:
		if a1[0] in i1 and a1[1] in i1:
			ls[m]+=1
		#print(a1)
	m+=1
		

print(p)
print(ls)
i=0
a=len(ls)
while i <a:
	#print(ls[i])
	if ls[int(i)]<sup_count:
		ls.pop(i)
		p.pop(i)
		a-=1
	else:
		i+=1			
		
for i in range(len(p)):
	ppp.append(p[i])
	llls.append(ls[i])
print(p)
print(ls)

find_com=len(ls)
tt_len=3
while find_com!=0:
	
	p1=p
	p=[]
	ls1=ls
	ls=[]
	i=0
	a1=[]
	while i<len(p1):
		flag=0
		a1.append(p1[i].split(','))
		j=0
		
		i+=1 
	m=1
	while m<len(p1):
		flag=0
		j=m-1
		while j<len(a1):
			for r in a1[j]:

				if r in p1[m] and m!=j:
					s=set(a1[m])|set(a1[j])
					s=list(s)
					s.sort()
					#print(len(s),"total len",tt_len)
					if s not in p and tt_len==len(s):
						p.append(s)
						ls.append(0)
			'''if a1[j] in p1[m]:
				flag=1

			elif flag==1:
				stor=p1[m]+','+a1[j]
				if stor not in p:
					p.append(stor)
					ls.append(0)'''
			#print(j,p)			
			j+=1
			
		m+=1
	m=0
	i=0
	#print(p)
	#print(ls)
	pk=[]
	if len(p)==0:
		break
	else:
		l=len(p[0])
		tt_len=l+1
	'''for line in p:
		a=''
		l=len(line)
		for line1 in range(len(line)):
			a+=line[line1]
			
			if line1!=len(line)-1:
				a+=', '
		
		pk.append(a)
	p=pk'''
	m=0
	i=0
	while m<len(p):
		a1=p[m]
		flg=0
		for i1 in f1:
			flg=0
			i=0
			while i<len(a1):
				if a1[i] in i1:
					flg+=1
					#ls[m]+=1
				i+=1
			#print(flg)
			if flg==l:
				ls[m]+=1
				#print(a1)
		m+=1	
	for line in p:
		a=''
		l=len(line)
		for line1 in range(len(line)):
			a+=line[line1]
			
			if line1!=len(line)-1:
				a+=','
		
		pk.append(a)
	p=pk	
	i=0
	a=len(ls)
	while i <a:
		#print(ls[i])
		if ls[int(i)]<sup_count:
			ls.pop(i)
			p.pop(i)
			a-=1
		else:
			i+=1
	for i in range(len(p)):
		ppp.append(p[i])
		llls.append(ls[i])	
	print(p)

	print(ls)	
	find_com=len(p)	
print(ppp)
print(llls)
take_a=str(input("A:"))
take_b=str(input("B:"))
take_a_u_take_b=take_a+','+take_b
i=0
while i<len(ppp):
	if(take_a == ppp[i]):
		print(ppp[i])
		tk_v_a=llls[i]
	if(take_a_u_take_b == ppp[i]):
		tk_v_abu=llls[i]	
	i+=1
print(tk_v_abu,' ',tk_v_a,' ',tk_v_abu/tk_v_a)


