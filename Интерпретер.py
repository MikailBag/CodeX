#!/usr/bin/env python
# -*- coding: utf-8 -*-


#CodeX Script Beta 1.2.0 Ultra Full HD Free Download Without SMS And Registration
#Von Sup Studio Production



import math
from colorama import *
import sys
init()

#Check if param can be number
#Проверить, может ли параметр быть числом
def isNum(x):
    try:
        x = int(x)
        return True
    except:
        return False

#Error messages
#Сообщения об ошибках
def ERROR(q):
    print()
    print(Fore.RED + "ERROR: " + q)
    print()
    print(Fore.RED + "[Exiting program]")
    print()
    exit(0);

#Converts list to string
#Переводит список в строку
def list2str(mas):
    s = ''
    for i in mas:
        for j in i:
            if (mas.index(i) == 0) and (i.index(j) == 0) and ((j == "'") or (j == '"')):
                j = j[1:]
            elif (mas.index(i) == len(mas) -1) and (i.index(j) == len(i) -1) and ((j == "'") or (j == '"')):
                j = j[:-1]
            s += j
        s += ' '
    s = s[:-1]
    return s

#Converts string expression to str variable
#Приводит выражение из строк к одной строке
def str_exp(line):
    if ((line[0][0] == "'") and (line[-1][-1] == "'")) or ((line[0][0] == '"') and (line[-1][-1] == '"')):
        line[0] = line[0][1:]
        line[-1] = line[-1][:-1]
    if '*' in line:
        return str_exp([str_exp([line[:line.index('*')]]) * num_exp([line[line.index('*')+1:]])])
    elif '+' in line:
        return str_exp([str_exp([line[:line.index('+')]]) + str_exp([line[line.index('+')+1:]])])
    else:
        if (str(line[0]) in strs.keys()) and (len(line) == 1):
            return strs[line[0]]
        else:
            return list2str(line)

#Converts numerical expression to num variable
#Приводит численное выражение к одному числу
def num_exp(line):
    if len(line) == 1:
        if line[0] in nums.keys():
            return num_exp([nums[line[0]]])
        else:
            try:
                if int(line[0]) == float(line[0]):
                    return int(line[0])
                else:
                    return float(line[0])
            except:
                ERROR('The value of this variable is invalid')
    else:
        if 'fac' in line:
            return num_exp([math.factorial(num_exp([line[line.index('fac') +1]]))])
        elif ('power' in line) or ('root' in line):
            try:
                if line.index('power') < line.index('root'):
                    line[line.index('power') -1] = num_exp([line[line.index('power') +1]]) ** num_exp([line[line.index('power') -1]])
                    del line[line.index('power') +1]
                    del line[line.index('power')]
                    return num_exp(line)
                else:
                    line[line.index('root') -1] = num_exp([line[line.index('root') +1]]) ** (1 / num_exp([line[line.index('root') - 1]]))
                    del line[line.index('root') + 1]
                    del line[line.index('root')]
                    return num_exp(line)
            except:
                if 'power' in line:
                    line[line.index('power') - 1] = num_exp([line[line.index('power') + 1]]) ** num_exp([line[line.index('power') - 1]])
                    del line[line.index('power') + 1]
                    del line[line.index('power')]
                    return num_exp(line)
                else:
                    line[line.index('root') - 1] = num_exp([line[line.index('root') + 1]]) ** (1 / num_exp([line[line.index('root') - 1]]))
                    del line[line.index('root') + 1]
                    del line[line.index('root')]
                    return num_exp(line)
        elif ('*' in line) or ('/' in line):
            try:
                if line.index('*') < line.index('/'):
                    line[line.index('*') -1] = num_exp([line[line.index('*') +1]]) * num_exp([line[line.index('*') -1]])
                    del line[line.index('*') +1]
                    del line[line.index('*')]
                    return num_exp(line)
                else:
                    line[line.index('/') -1] = num_exp([line[line.index('/') -1]]) / num_exp([line[line.index('/') +1]])
                    del line[line.index('/') +1]
                    del line[line.index('/')]
                    return num_exp(line)
            except:
                if '*' in line:
                    line[line.index('*') -1] = num_exp([line[line.index('*') +1]]) * num_exp([line[line.index('*') -1]])
                    del line[line.index('*') +1]
                    del line[line.index('*')]
                    return num_exp(line)
                else:
                    line[line.index('/') -1] = num_exp([line[line.index('/') -1]]) / num_exp([line[line.index('/') +1]])
                    del line[line.index('/') + 1]
                    del line[line.index('/')]
                    return num_exp(line)
        elif ('+' in line) or ('-' in line):
            try:
                if line.index('+') < line.index('-'):
                    line[line.index('+') -1] = num_exp([line[line.index('+') +1]]) + num_exp([line[line.index('+') -1]])
                    del line[line.index('+') +1]
                    del line[line.index('+')]
                    return num_exp(line)
                else:
                    line[line.index('-') -1] = num_exp([line[line.index('-') -1]]) - num_exp([line[line.index('-') +1]])
                    del line[line.index('-') +1]
                    del line[line.index('-')]
                    return num_exp(line)
            except:
                if '+' in line:
                    line[line.index('+') -1] = num_exp([line[line.index('+') +1]]) + num_exp([line[line.index('+') -1]])
                    del line[line.index('+') +1]
                    del line[line.index('+')]
                    return num_exp(line)
                else:
                    line[line.index('-') -1] = num_exp([line[line.index('-') -1]]) - num_exp([line[line.index('-') +1]])
                    del line[line.index('-') + 1]
                    del line[line.index('-')]
                    return num_exp(line)
        elif '%' in line:
            line[line.index('%') - 1] = num_exp([line[line.index('%') - 1]]) % num_exp([line[line.index('%') + 1]])
            del line[line.index('%') + 1]
            del line[line.index('%')]
            return num_exp(line)

#Converts logical expression to bool variable
#Приводит логическое выражение к одному boolean'у
def bool_exp(line):
    if len(line) == 1:
        if str(line[0]) in bools.keys():
            return bools[line[0]]
        else:
            if line[0] == 'true':
                return True
            else:
                return False
    elif '==' in line:
        return num_exp(line[:line.index('==')]) == num_exp(line[line.index('==') +1:])
    elif '!=' in line:
        return num_exp(line[:line.index('!=')]) != num_exp(line[line.index('!=') +1:])
    elif '>' in line:
        return num_exp(line[:line.index('>')]) > num_exp(line[line.index('>') +1:])
    elif '<' in line:
        return num_exp(line[:line.index('<')]) < num_exp(line[line.index('<') +1:])
    elif '>=' in line:
        return num_exp(line[:line.index('>=')]) >= num_exp(line[line.index('>=') +1:])
    elif '<=' in line:
        return num_exp(line[:line.index('<=')]) <= num_exp(line[line.index('<=') +1:])
    elif '&' in line:
        return bool_exp(line[:line.index('&')]) and bool_exp(line[line.index('&') + 1:])
    elif '|' in line:
        return bool_exp(line[:line.index('|')]) or bool_exp(line[line.index('|') + 1:])
    elif '^' in line:
        return bool_exp(line[:line.index('^')]) ^ bool_exp(line[line.index('^') + 1:])
    elif '!' in line:
        return not bool_exp(line[line.index('&&') + 1:])

#Processing code
#Обрабатывает код построчно
def work(ls):
    for l in ls:
        if l[0][0] == '#':
            continue
        elif (l[0] == 'end') or (l[0] == '.'):
            exit()

        #Defining variables
        #Объявление переменных
        elif (l[0] == 'num') or (l[0] == 'number'):
            if isNum(l[1]):
                ERROR("The variable name "+l[1]+" is invalid")
            else:
                try:
                    nums[l[1]] = num_exp(l[3:])
                except:
                    nums[l[1]] = 0
        elif (l[0] == 'str') or (l[0] == 'string'):
            if isNum(l[1]):
                ERROR("The variable name "+l[1]+" is invalid")
            else:
                try:
                    if l[2] == '=':
                        strs[l[1]] = str_exp(l[3:])
                    else:
                        strs[l[1]] = str_exp(l[1:])
                except:
                    strs[l[1]] = ''
        elif (l[0] == 'bool') or (l[0] == 'boolean'):
            if isNum(l[1]):
                ERROR("The variable name "+l[1]+" is invalid")
            else:
                try:
                    bools[l[1]] = bool_exp(l[3:])
                except:
                    bools[l[1]] = False

        #Setting variables values
        #Присваивание значений переменных
        elif l[0] == 'set':
            if l[1] in nums.keys():
                if l[2] == '=':
                    nums[l[1]] = num_exp(l[3:])
                else:
                    nums[l[1]] = num_exp(l[1:])
            elif l[1] in strs.keys():
                if l[3] in strs.keys():
                    strs[l[1]] = strs[l[3]]
                else:
                    strs[l[1]] = list2str(l[3:])
            elif l[1] in bools.keys():
                strs[l[1]] = ''

        #Output
        #Печать (выведение) информации
        elif l[0] == 'print':
            if (l[1] in strs.keys()) or ((l[1][0] == "'") and (l[-1][-1] == "'")) or ((l[1][0] == '"') and (l[1][-1] == '"')):
                print(str_exp(l[1:]))
            elif (l[1] in bools.keys()) or (l[1] == 'true') or (l[1] == 'false'):
                print(bool_exp(l[1:]))
            else:
                print(num_exp(l[1:]))

        #Conditional operators
        #Условные операторы
        elif l[0] == 'if':
            condition = bool_exp(l[1:-1])
            if condition:
                i = ls.index(l)
                ifls = ls[i:]
                ifls = ifls[1:ifls.index(['}'])]
                work(ifls)
            i = ls.index(l)
            while ls[i] != ['}']:
                del ls[i]
        elif l[0] == 'else':
            if condition == 'nothing':
                ERROR("The condition is not defined")
            elif not condition:
                i = ls.index(l)
                ifls = ls[i:]
                ifls = ifls[1:ifls.index(['}'])]
                work(ifls)
            i = ls.index(l)
            while ls[i] != ['}']:
                del ls[i]

        #while loop
        #Цикл while
        elif l[0] == 'while':
            while bool_exp(l[1:-1]):
                i = ls.index(l)
                ifls = ls[i:]
                ifls = ifls[1:ifls.index(['}'])]
                work(ifls)
            i = ls.index(l)
            while ls[i] != ['}']:
                del ls[i]

        #Data input during script
        #Ввод данных в процессе выполнения скрипта
        elif l[0] == 'input':
            if l[1] in nums.keys():
                nums[l[1]] = num_exp([input()])
            elif l[1] in strs.keys():
                print()
                strs[l[1]] = input()
            elif l[1] in bools.keys():
                print()
                bools[l[1]] = bool_exp([input()])
            else:
                ERROR("Variable '" + l[1] + "' does not exist")

        elif l[0] == '}':
            pass

        else:
            ERROR("Command '" + list2str(l) + "' does not exist")

#Data input from console
#Принимает данные из консоли
lines = []
nums = {}
strs = {}
bools = {}
condition = 'nothing'
e = [' ']
if len(sys.argv) >= 2:
    with open(sys.argv[1]) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for i in content:
            e = str(i).split()
            if (e[0] != 'end') and (e[0] != '.'):
                if e == ['']:
                    e = [' ']
                else:
                    lines.append(e)
                    while '' in lines[len(lines) - 1]:
                        lines[len(lines) - 1].remove('')
            else:
                break
else:
    while (e[0] != 'end') and (e[0] != '.'):
        e = input('>>> ').split(' ')
        if e == ['']:
            e = [' ']
        else:
            lines.append(e)
            while '' in lines[len(lines) - 1]:
                lines[len(lines) - 1].remove('')
work(lines)

