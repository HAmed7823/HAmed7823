Pythonbook exercises Page : 459 answer :
----------------------------------------
11- Wrap the following code in a try statement to
defend against any exceptions it can raise. Do not use
a catch-all handler.
lst = [0, 0, 0, 0]
with open('data.txt', 'r') as f:
count = 0
for line in f.readlines():
lst[count] = int(line)
count += 1
--------
answer:
lst = [0, 0, 0, 0]
try :
    with open('data.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            lst[count] = int(line)
            count += 1
except IndentationError:
    print("IndentationError")
----------------------------------------
12-For the next set of questions show what 
each program will print when the user supplies the indicated
input text.
Write *EXCEPTION* if and when the execution will 
generate an exception stack trace for an uncaught exception.
(a) print('Begin')
x = int(input())
print(x)
print('End')
i. User enters 22
ii. User enters ZZ

output when user enters 22:

Begin
22
22
End

output when user enters ZZ :

Begin
zz
Traceback (most recent call last):
  File in <module>
    x = int(input())
ValueError: invalid literal for int() with base 10: 'zz'
--------------------
(b) print('Begin')
try:
x = int(input())
print(x)
except ValueError:
print('Wrong!')
print('End')
i. User enters 22
ii. User enters ZZ

output when user enters 22:

Begin
22
22

output when user enters ZZ :

Begin
zz
Wrong!
End
--------------------
(c) print('Begin')
try:
x = int(input())
print(x)
except IndexError:
print('Wrong!')
print('End')
i. User enters 22
ii. User enters ZZ

output when user enters 22:

Begin
22
22

output when user enters ZZ :

Begin
ZZ
Traceback (most recent call last):
  File in <module>
    x = int(input())
ValueError: invalid literal for int() with base 10: 'ZZ'
--------------------
(d) print('Begin')
try:
x = int(input())
print(x)
except Exception:
print('Wrong!')
print('End')
i. User enters 22
ii. User enters ZZ

output when user enters 22:

Begin
22
22

output when user enters ZZ :

Begin
ZZ
Wrong!
End
--------------------
(e) print('Begin')
try:
x = int(input())
print(x)
except ValueError:
print('Wrong!')
else:
print('Wow')
print('End')
i. User enters 22
ii. User enters ZZ

output when user enters 22:

Begin
22
22
Wow
End

output when user enters ZZ :

Begin
ZZ
Wrong!
--------------------
(f) print('Begin')
try:
x = int(input())
print(x)
except ValueError:
print('Wrong!')
finally:
print('Done')
print('End')
i. User enters 22
ii. User enters ZZ

output when user enters 22:

Begin
22
22
Done
End

output when user enters ZZ :

Begin
ZZ 
Wrong!
Done
End
--------------------
(g) print('Begin')
try:
x = int(input())
print(x)
except ValueError:
print('Wrong!')
else:
print('Wow')
finally:
print('Done')
print('End')
i. User enters 22
ii. User enters ZZ

output when user enters 22:

Begin
22
22
Wow
Done
End

output when user enters ZZ :

Begin
ZZ
Wrong!
Done
End