my_file = open("my_data", "r")
arr = [0] * 122
my_sorted_file = open("my_sorted_data","w")

for tmp in my_file:
	try:
		tmp = int(tmp)
	except:
		tmp = -1
	if tmp != -1:
		arr[tmp]+=1

my_file.close()

i = 0
while i < 121:
	while arr[i] != 0:
		my_sorted_file.write(str(i)+"\n")
		arr[i]-=1
	i+=1 
my_sorted_file.close()
