import sys
sys.setrecursionlimit(1500)
_200meg = 6214400
_max_value = 9223372036854775807



def min_ind(list_):
    ind = 0
    i = 0
    while i < len(list_):

        if list_[i] != _max_value and list_[i] < list_[ind]:
            ind = i
        i+= 1
    return ind

def merge2(lst_, big_file_):
    big_file_ = open(big_file_,"w")
    not_none_count = len(lst_)
    lst_ind = [0] * len(lst_)
    i = 0
    lst___ = []
    while i < len(lst_):
        lst_[i] = open(lst_[i], "r")
        tmp = lst_[i].readline()
        lst_ind[i] = int(tmp)
        i+=1
    while not_none_count !=0:
        ind = min_ind(lst_ind)
        big_file_.write(str(lst_ind[ind]) + "\n")
        tmp = lst_[ind].readline()
        if tmp != "":
            lst_ind[ind] = int(tmp)
        else:
            lst_ind[ind] = _max_value
            not_none_count-=1
    i = 0
    while i < len(lst_):
        lst_[i].close()
        i+= 1
    big_file_.close()

def merge(lst_, start=0, end=0, mid=0):
    i = 0
    j = 0
    k = start
    lst_1 = lst_[start:mid]
    lst_2 = lst_[mid: end]
    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] <= lst_2[j]:
            lst_[k] = lst_1[i]
            i += 1
        else:
            lst_[k] = lst_2[j]
            j += 1
        k += 1

    while i < len(lst_1):
        lst_[k] = lst_1[i]
        i += 1
        k += 1

    while j < len(lst_2):
        lst_[k] = lst_2[j]
        j += 1
        k += 1

def merge_sort(lst_, start, end):
    if start + 1 != end:
        mid = int((start+end) / 2)
        merge_sort(lst_, start, mid)
        merge_sort(lst_, mid, end)
        merge(lst_, start, end, mid)

big_file = open("big_file1.txt", "r")
lst_of_fnames = []
cur_fname = "0f.txt"
count_l = 0
cur_lst_ind = 0
cur_list = []

last_ind_fname = 0
number = "f"
while True:
    if number == "" and count_l == 0:
        break
    number = big_file.readline()
    if number != "":
        number = int(number)
        cur_list.append(number)
    count_l+= 1
    if count_l == 1:
        lst_of_fnames.append(cur_fname)
    elif count_l == _200meg or number == "":
        count_l = 0
        cur_lst_ind+=1
        merge_sort(cur_list,0,len(cur_list))
        f = open(cur_fname,'w')
        for tmp in cur_list:
            f.write(str(tmp)+"\n")
        cur_fname = str(cur_lst_ind) + cur_fname[1:]
        cur_list = []
        f.close()
    if number == "":
        break
merge2(lst_of_fnames, "big_file2.txt")    
big_file.close()
