#strings
# 1. strip, lstrip, rstrip
a = '   python is simple'
python is simple
python is simple   
   python is simple

# 2. replace
a = 'python is simple, python is easy, python is allrounder'
b = a.replace('python', 'java')
print(a)
print(b)
python is simple, python is easy, python is allrounder
java is simple, java is easy, java is allrounder

# 3. upper, lower, swapcase, title, capitalize
a = 'PYTHON is siMPle'
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.title())
print(a.capitalize())
python is simple
PYTHON IS SIMPLE
python IS SiMPLE
Python Is Simple
Python is simple

# 4. count, startswith, endswith
a = 'abacad'
b = a.startswith('a')
c = a.startswith('ad')
d = a.endswith('d')
e = a.endswith('de')
f = a.count('a')
g = a.count('ad')
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
True
False
True
False
3
1

# 5. find, rfind, index, rindex
s = 'abacada'
print(s.find('a'))
print(s.find('a', 3))
print(s.find('a', 4, 8))
print(s.rfind('a'))
print(s.rfind('a', 3))
print(s.rfind('a', 4, 8))
print(s.index('a'))
print(s.index('a', 3))
print(s.index('a', 4, 8))
0
4
4
6
6
6
0
4
4
0
4
4

# 6. is-methods
a = ' '
b = ' a'
print(a.isspace())
print(b.isspace())
a = 'aBcD'
print(a.isalpha())
b = 'aBcD1'
print(b.isalpha())
c = 'aBc@D'
print(c.isalpha())  # fixed typo (was isapha)
a = '13'
print(a.isdigit())
b = '12a'  # fixed missing closing quote
print(b.isdigit())

a = 'AbC123'
print(a.isalnum())
b = 'Ab#C2'
print(b.isalnum())
a = '23$U'
print(a.isupper())
b = '23%Ua'
print(b.isupper())
a = '23$u'
print(a.islower())
b = '23%uA'
print(b.islower())

isspace()
True
False

isalpha()
True
False
False

isdigit()
True
False

isalnum()
True
False

isupper()
True
False

islower()
True
False

# split
a = 'badac'
print(a.split('a'))
b = '   '
print(b.split(' '))
print(b.split(' '))
print(b.split(' '))

b = '   '  # 3 spaces
print(b.split(' '))
['', '', '', '']
c = 'abaca'
print(c.split('a'))
['', 'b', 'c', '']
d = 'iam a good person'
print(d.split())
d = 'iam a good person'
print(d.split())

# join
a = '@'
l = [1, 2, 3]
t = (1, 2, 3)
s = {1, 2, 3}
d = {3: 1, 2: 3, 3: 1}  # duplicate key 3 collapses -> {3: 1, 2: 3}
print(d)

# join() needs an iterable of strings, so convert each item first
print(a.join(str(x) for x in l))
print(a.join(str(x) for x in t))
print(a.join(str(x) for x in s))
print(a.join(str(x) for x in d))
a = '@'
l = [1,2,3]
t = (1,2,3)
print(a.join(l))
