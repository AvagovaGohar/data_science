from dataclasses import replace
from logging import exception
import sys

logic_operators_ = frozenset(['==', '!=', '>', '<', '>=', '<=', '&&', '||'])
arithmetic_operators_ = frozenset(['+', '-', '*', '/', '|', '&', '%'])
assigment_operators = frozenset(
    ['=', '+=', '-=', '*=', '/=', '|=', '&=', '%='])
and_or_operators = frozenset(['&&', '||'])

if_while_bol = []  # if or while should continiue or not
if_while_ind = []  # index from where to continue
if_while_name = []  # if or while
if_while_count = []
main_file = None
variables_ = {}


def ASSIGMENT_(file_name):

    if file_name[0] not in variables_ and file_name[1] not in assigment_operators:
        raise exception("Wrong value ")
        ###############
    val_ = EXPRESSION_(file_name[2:])
    variables_[file_name[0]] = ASSIGMENT_OPERATORS_(
        variables_[file_name[0]], file_name[1], val_)


def ASSIGMENT_OPERATORS_(a, simb, b):
    if simb == '=':
        a = b
    if simb == '+=':
        a += b
    if simb == '-=':
        a -= b
    if simb == '*=':
        a *= b
    if simb == '/=':
        a /= b
    if simb == '|=':
        a |= b
    if simb == '%=':
        a %= b
    if simb == '&=':
        a &= b
    return a


def FIND_VALUE(val_, word_a=0, txt_=" "):
    if type(val_) == type(" ") and val_[-1] == '\n':
        val_ = val_[:-1]
    if val_ == 'true':
        return True
    if val_ == 'false':
        return False
    if val_ in variables_:
        return variables_[val_]
    res = 0
    if '"' in txt_[word_a]:
        scuotes_b = True
        tmp = ""
        txt_[word_a] = txt_[word_a][1:]
        while word_a < len(txt_):
            tmp += txt_[word_a]
            if '"' in txt_[word_a] and txt_[word_a].count('"') == 1:
                scuotes_b = False
                break
            tmp += ' '
            word_a += 1

        tmp = tmp.replace('"', "")
        tmp = tmp.replace('\n', "")
        tmp = tmp.replace('\t', "")
        tmp = tmp.replace(' ', "")
        tmp = tmp.replace('\_', "_")
        tmp = tmp.replace('_', " ")
        if scuotes_b == True:
            raise exception('No "')
        return tmp
    try:
        res = int(val_)

    except:
        raise Exception("Wrong variable")
    return res


def VAR_(file_name):
    if file_name[1] in variables_.keys() or file_name[2] != '=':
        raise Exception("Wrong declaration of variable ")

    variables_[file_name[1]] = EXPRESSION_(file_name[3:])


def LOGIC_OPERATORS_(a, b, simb):

    res = 0
    if b == None:
        b = a
    if a == None:
        a = b
    if simb == None:
        simb = '||'
    if simb == '||':
        res = a or b
    if simb == '&&':
        res = a and b
    if simb == '==':
        res = a == b
    elif simb == '!=':
        res = a != b
    elif simb == '>=':
        res = a >= b

    elif simb == '<=':
        res = a <= b
    elif simb == '>':
        res = a > b
    elif simb == '<':
        res = a < b
    return bool(res)


def ARITHMETIC_OPERATORS_(a, b, simb):
    if type(a) == type(" "):
        if b == None:
            b = ""
        else:
            b = str(b)
    if type(b) == type(" "):
        if a == None:
            a = ""
        else:
            a = str(a)
    if simb == '%':
        return a % b
    if b == None:
        b = 0
    if a == None:
        a = 0
    if simb == '+':
        return a + b
    if simb == '-':
        return a - b
    if simb == '*':
        return a * b
    if simb == '/':
        return a / b
    if simb == '|':
        return a | b
    if simb == '&':
        return a & b


def EXPRESSION_(txt_):
   # print(txt_)
    all_result = 0
    a = None
    cur_result = 0
    b = None
    ao_sign = '||'  # and or signs
    lo_sign = '||'  # other logic signs
    is_logic_used1 = False
    is_logic_used2 = False
    word_a = 0
    while word_a < len(txt_):

        word_ = txt_[word_a]

        if a == None:
            a = FIND_VALUE(word_, word_a, txt_)
            # print(a,'120')
        elif word_ in arithmetic_operators_:
            # print(121)

            word_a += 1
            b = FIND_VALUE(txt_[word_a], word_a, txt_)
            a = ARITHMETIC_OPERATORS_(a, b, word_)

            b = None
        elif word_ in logic_operators_ and word_ not in and_or_operators:
           # print(126)
            if is_logic_used1 == False:
                cur_result = a
            else:
                raise Exception("Wrong value")
            is_logic_used1 = True
            lo_sign = word_
            a = None
            b = None

        if (word_ in and_or_operators) or (word_a + 1) >= len(txt_):
            # print(137)
            if is_logic_used1 == True:
                # print(139)
                is_logic_used1 = False
                cur_result = LOGIC_OPERATORS_(cur_result, a, lo_sign)
            else:
                # print(143)
                cur_result = a
            if is_logic_used2 == True:
               # print(146)
                all_result = LOGIC_OPERATORS_(all_result, cur_result, ao_sign)

            else:
                # print(150)
                all_result = cur_result
            is_logic_used2 = True
            a = None
            b = None
            ao_sign = word_
        word_a += 1

    return all_result


def PRINT_(file_name):

    print(EXPRESSION_(file_name[1:]), end='')


def IF_(file_name):
    global if_while_bol
    global if_while_ind
    global cur_op

    if file_name[-1] != '{':
        raise exception('No "{" scope ')
    bool_val = EXPRESSION_(file_name[1:-1])
    if bool_val == True:
        if_while_bol[cur_op] = True


def WHILE_(file_name):
    global if_while_bol
    global if_while_ind
    global cur_op

    if file_name[-1] != '{':
        raise exception('No "{" scope ')
    bool_val = EXPRESSION_(file_name[1:-1])
    if bool_val == True:
        if_while_bol[cur_op] = True
    else:
        if_while_bol[cur_op] = False


# START

main_file = ''
try:
    main_file = open(sys.argv[1], mode='r')
    
except IOError:
    raise Exception("File not found or path is incorrect")

cur_count_scopes = 0
cur_op = -1
cur_line_index = 0
line_ = main_file.readline()
while line_:
   # cur_line_index += len(line_)
    length = len(line_)+1
    line_ = line_.replace('\n', "")
    line_ = line_.replace('\t', "")
    line_ = line_.replace('\r\n', "")
    if line_[:2] == '//':
        line_ = main_file.readline()
        continue
    keyword_ = line_.split(" ")
    ind = 0
    while ind < len(keyword_):
        keyword_[ind] = keyword_[ind].replace(" ", "")
        if len(keyword_[ind]) == 0:
            del keyword_[ind]
        else:
            ind += 1
    if keyword_ == "" or len(keyword_) == 0:
        line_ = main_file.readline()
        continue
    if '}' == keyword_[0]:
        if len(keyword_) != 1:
            raise ("After { something else")

        if if_while_bol[cur_op] == True and if_while_name[cur_op] == 'w' and if_while_count[cur_op] == cur_count_scopes:
            main_file.seek(if_while_ind[cur_op])
            #cur_line_index = if_while_ind[cur_op]

        elif if_while_name[cur_op] == 'i' and if_while_count[cur_op] == cur_count_scopes:
            del if_while_bol[-1]
            del if_while_ind[-1]
            del if_while_name[-1]
            del if_while_count[-1]
            cur_count_scopes -= 1
            cur_op -= 1
        elif if_while_name[cur_op] == 'w' and if_while_bol[cur_op] == False and if_while_count[cur_op] == cur_count_scopes:
            del if_while_bol[-1]
            del if_while_ind[-1]
            del if_while_name[-1]
            del if_while_count[-1]
            cur_count_scopes -= 1
            cur_op -= 1
        else:
            cur_count_scopes -= 1

        line_ = main_file.readline()
        continue
    if cur_op >= 0 and if_while_bol[cur_op] == False:
        if '{' in line_:
            cur_count_scopes += 1
        line_ = main_file.readline()
        continue
    if keyword_[0] in variables_:
        ASSIGMENT_(keyword_)
    elif keyword_[0] == 'var':
        VAR_(keyword_)
    elif keyword_[0] == 'print':
        t = True
        PRINT_(keyword_)
    elif keyword_[0] == 'if':
        if_while_ind.append(main_file.tell()-length)
        if_while_bol.append(False)
        if_while_name.append('i')
        cur_count_scopes += 1
        if_while_count.append(cur_count_scopes)

        cur_op += 1
        IF_(keyword_)

    elif keyword_[0] == 'while':
        if len(if_while_ind) == 0 or (len(if_while_ind) > 0 and main_file.tell()-length != if_while_ind[cur_op]):
            if_while_ind.append(main_file.tell()-length)
            cur_count_scopes += 1
            if_while_count.append(cur_count_scopes)
            if_while_bol.append(False)
            if_while_name.append('w')
            cur_op += 1
        WHILE_(keyword_)
    line_ = main_file.readline()
