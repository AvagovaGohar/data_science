import numpy as np

def min_(a,b,c):
    if a < b:
        if a <= c:
            return a
        else:
            return c
    elif b < c:
            return b
    else:
        return c
        
all_strings = []
file_ = None
try:
    file_ = open("dictionary.txt","r")
    for line in file_:
        line = line.strip("\n")
        if len(line) != 0:
            all_strings.append(line)
    file_.close()
except:
    all_strings = []

def find_matches(string):
    
    if string in all_strings:
        return set()
    
    min = 100
    matches = set()
    init = set()
    len_s = len(string)+1
    tmp = [0]* len_s
    
    for string2 in all_strings:
        if string in string2 or string2 in string:
            init.add(string2)
            continue
        len_i = len(string2)+1
        cur_matrix = np.array([tmp]*len_i)
        a = b = c = i = u = j = 0
        while i < len_i:
            j = 0
            while j < len_s:
                if i == 0:
                    cur_matrix[i][j] = j 
                elif j == 0:
                    cur_matrix[i][j] = i 
                else:
                    u = 0
                    if string[j-1] != string2[i-1]:
                        u = 1
                    a = cur_matrix[i-1][j]
                    b = cur_matrix[i][j-1]
                    c = cur_matrix[i-1][j-1]
                    
                    cur_matrix[i][j] = min_(a,b,c)+u
                j+=1
            i+=1
        if  min >= (cur_matrix[i-1][j-1]*100/len(string2)):
            min = cur_matrix[i-1][j-1]*100/len(string2)
            matches.clear()
            matches.add(string2)
    if len(init)!=0:
        return init
    else:
        return matches
    
print("\nFor exit input: exit() ")
print("If you want to see the dictionary input: all()")
print("If you want delete/add word input del()/add() \"your_word\"\n")
n = input("Input some text: ")
n = n.lower()
while n != "exit()":
    if n == "all()":
        print(all_strings)
    elif "del()" in n:
        t = n.split(" ")
        if t[1] in all_strings:
            print("The word doesn't exist ")
        else:
            all_strings.remove(t[1])
    elif 'add()' in n:
        t = n.split(" ")
        if t[1] in all_strings:
            print("The word already exists ")
        else:
            all_strings.append(t[1])
    else:
        tmp = n.split(" ")
        for i in tmp:
            res = find_matches(i)
            if len(res) != 0:
                print(f"\"{i}\" word is not in the dictionary, maybe you mean {res}.")
                n = input("Do you want to add this word in dictionary?(y/n) ")
                n=n.lower()
                if n == 'y':
                    all_strings.append(i)
    print()
    n = input("Input some text: ")
    n = n.lower()
file_ = open("dictionary.txt","w")
for line in all_strings:
    file_.write(line+'\n')
file_.close()
