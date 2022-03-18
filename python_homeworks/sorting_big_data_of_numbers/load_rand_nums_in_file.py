import random as r

m_file = open("my_data",'w')
a = 0
while a < 1_000_000_000:
	m_file.write(str(r.randint(0,121))+'\n')
	a+= 1
m_file.close()
