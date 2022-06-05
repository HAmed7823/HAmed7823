Pythonbook Page : 511&512  Exercise 11 , answer :
----------------------------------------
11-Consider the following Python code:
class Widget:
def __init__(self, v = 40):
if v >= 40:
self.value = v
else:
self.value = 0
def get(self):
return self.value
def bump(self):
if self.value < 50:
self.value += 1
def main():
w1 = Widget()
w2 = Widget(5)
print(w1.get())
print(w2.get())
w1.bump()
w2.bump()
print(w1.get())
print(w2.get())
for i in range(20):
w1.bump()
w2.bump()
print(w1.get())
print(w2.get())
if __name__ == '__main__':
main()
(a) What does the program print?
Answer:
40
0
41
1
50
21

(b) If wid is a Widget object, what is the minimum value the expression wid.get() can return?40u
(c) If wid is a Widget object, what is the maximum value the expression wid.get() can return?50