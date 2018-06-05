#!/usr/bin/env python
# -*- coding: utf-8 -*-


#CodeX Script Beta 1.0.0 Ultra Full HD Free Download Without SMS And Registration

# Von Sup Studio Production



import math

lines = []
e = ' '
while (e[0] != 'end') and (e[0] != '.'):
    e = input().split(' ')
    lines.append(e)

nums = {}
strs = {}
bools = {}

def list2str(mas):
    s = ''
    for i in mas:
        s += i
        s += ' '
    s = s[:-1]
    return s

def num_exp(line):
    if len(line) == 1:
        if line[0] in nums.keys():
            return num_exp([nums[line[0]]])
        else:
            if int(line[0]) == float(line[0]):
                return int(line[0])
            else:
                return float(line[0])
    else:
        if 'fac' in line:
            return num_exp([math.factorial(num_exp([line[line.index('fac') +1]]))])
        elif ('power' in line) or ('root' in line):
            try:
                if line.index('power') < line.index('root'):
                    line[line.index('power') -1] = num_exp(line[line.index('power') +1]) ** num_exp(line[line.index('power') -1])
                    del line[line.index('power') +1]
                    del line[line.index('power')]
                    return num_exp(line)
                else:
                    line[line.index('root') -1] = num_exp(line[line.index('root') +1]) ** (1 / num_exp(line[line.index('root') - 1]))
                    del line[line.index('root') + 1]
                    del line[line.index('root')]
                    return num_exp(line)
            except:
                if 'power' in line:
                    line[line.index('power') - 1] = num_exp(line[line.index('power') + 1]) ** num_exp(line[line.index('power') - 1])
                    del line[line.index('power') + 1]
                    del line[line.index('power')]
                    return num_exp(line)
                else:
                    line[line.index('root') - 1] = num_exp(line[line.index('root') + 1]) ** (1 / num_exp(line[line.index('root') - 1]))
                    del line[line.index('root') + 1]
                    del line[line.index('root')]
                    return num_exp(line)
        elif ('*' in line) or ('/' in line):
            try:
                if line.index('*') < line.index('/'):
                    line[line.index('*') -1] = num_exp(line[line.index('*') +1]) * num_exp(line[line.index('*') -1])
                    del line[line.index('*') +1]
                    del line[line.index('*')]
                    return num_exp(line)
                else:
                    line[line.index('/') -1] = num_exp(line[line.index('/') -1]) / num_exp(line[line.index('/') +1])
                    del line[line.index('/') +1]
                    del line[line.index('/')]
                    return num_exp(line)
            except:
                if '*' in line:
                    line[line.index('*') -1] = num_exp(line[line.index('*') +1]) * num_exp(line[line.index('power') -1])
                    del line[line.index('*') +1]
                    del line[line.index('*')]
                    return num_exp(line)
                else:
                    line[line.index('/') -1] = num_exp(line[line.index('/') -1]) / num_exp(line[line.index('/') +1])
                    del line[line.index('/') + 1]
                    del line[line.index('/')]
                    return num_exp(line)
        elif ('+' in line) or ('-' in line):
            try:
                if line.index('+') < line.index('-'):
                    line[line.index('+') -1] = num_exp(line[line.index('+') +1]) + num_exp(line[line.index('+') -1])
                    del line[line.index('+') +1]
                    del line[line.index('+')]
                    return num_exp(line)
                else:
                    line[line.index('-') -1] = num_exp(line[line.index('-') -1]) - num_exp(line[line.index('-') +1])
                    del line[line.index('-') +1]
                    del line[line.index('-')]
                    return num_exp(line)
            except:
                if '+' in line:
                    line[line.index('+') -1] = num_exp(line[line.index('+') +1]) + num_exp(line[line.index('+') -1])
                    del line[line.index('+') +1]
                    del line[line.index('+')]
                    return num_exp(line)
                else:
                    line[line.index('-') -1] = num_exp(line[line.index('-') -1]) - num_exp(line[line.index('-') +1])
                    del line[line.index('-') + 1]
                    del line[line.index('-')]
                    return num_exp(line)

def bool_exp(line):
    if len(line) == 1:
        if line[0] in bools.keys():
            return bools[line[0]]
        else:
            if line[0] == 'true':
                return True
            else:
                return False

for l in lines:
    if (l[0] == 'end') or (l[0] == '.'):
        exit()
    elif (l[0] == 'num') or (l[0] == 'number'):
        try:
            nums[l[1]] = num_exp(l[3:])
        except:
            nums[l[1]] = 0
    elif (l[0] == 'str') or (l[0] == 'string'):
        try:
            strs[l[1]] = strs(l[3])
        except:
            strs[l[1]] = list2str(l[3:])
    elif (l[0] == 'bool') or (l[0] == 'boolean'):
        try:
            bools[l[1]] = bool_exp(l[3:])
        except:
            bools[l[1]] = False
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
    elif l[0] == 'print':
        if l[1] in strs.keys():
            print(strs[l[1]])
        elif (l[1] in bools.keys()) or (l[1] == 'true') or (l[1] == 'false'):
            print(bool_exp([l[1:]]))
        else:
            print(num_exp(l[1:]))