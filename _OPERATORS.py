Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=3
b=5
c=a+b
c
8
k=9
n=0.8
h=k+n
h
9.8
9.78+3.45
13.23
p=9
q=7
z=p-q
z
2
a=54
b=67
a-b
-13
88*1
88
5*3
15
56*0
0
0.9*2
1.8
r= 7
b= 8
r/b
0.875
7/4
1.75
1.751.75
SyntaxError: incomplete input
4/2
2.0
2.0+4
6.0
6//5
1
6//3
2
7//8
0
1//0
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    1//0
ZeroDivisionError: integer division or modulo by zero

6//9
0
5//2
2
4%2
0
5%2
1
7%5
2
8*0
0
c=5
c
5
i=3
i+=1
i
4
i+=3
i
7
i-=4
i
3
i-=5
 i
 
SyntaxError: unexpected indent
i=6
i/=4
i
1.5
i*=5
i
7.5
i/=7.5
i
1.0
n=9
n=-n
n
-9
m=-m
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    m=-m
NameError: name 'm' is not defined
m=8
m=-m
m
-8
a<b
False
a=9
b=8
a<b
False
b>a
False
b<a
True
m=5
n=4
m>n
True
m>=n
True
m<=n
False
a=0
b=1
a!=b
True
a==b
False
c=8
h=8
c==h
True
a=9
b=8
a and b
8















4>6 and 5<8
False
6>3 and 3>2
True
4!=4 and 9>=0
False
3!=3 and 4!=4
False
4=4 and 3>6
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
4==4 and 5<7
True
7>8 or 4<6
True
2<4 or 5!=0
True
9!=0 or 3<4
True
9<6 or 4>2
True
7<3  or 8<3
False
x= True
type(x)
<class 'bool'>
not x
False
not 2==2
False
not 9>6
False
not 0!=1
False
not 2>6
True
4+6*9-3/2
56.5
-5**2+34>66+8/2*3
False
4+6
10
4+9/6*7
14.5
5+10
15
'4'+'6'
'46'
'hi'+1
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    'hi'+1
TypeError: can only concatenate str (not "int") to str
type(eee)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    type(eee)
NameError: name 'eee' is not defined
type (eee)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    type (eee)
NameError: name 'eee' is not defined
eee=1
type(eee)
<class 'int'>
abc= xyz
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    abc= xyz
NameError: name 'xyz' is not defined
abc = 'xyz'
type(abc)
<class 'str'>
  X= 4
  
SyntaxError: unexpected indent
x = 4
type(x)
<class 'int'>
float(x)
4.0
type(4)
<class 'int'>
float(4)
4.0
a = 5
type(a)
<class 'int'>
b = 6
>>> type(b)
<class 'int'>
>>> c= a/b
>>> c
0.8333333333333334
>>> type(c)
<class 'float'>
>>> int('1 2')
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    int('1 2')
ValueError: invalid literal for int() with base 10: '1 2'
>>> int('12')
12
>>> print 'hi' + '123'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print ('hi'+'123')
hi123
>>> print ('bye'*9)
byebyebyebyebyebyebyebyebye
>>> print ("we are "*4)
we are we are we are we are 
