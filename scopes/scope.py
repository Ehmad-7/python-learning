username='ehmad'

def func():
  # username='other'
  print(username)
  
print(username)
func()

x=99

def func2(y):
  z=x+y
  return z

print(func2(1))

a=99

def func3():
  global a
  a=88

func3()
print(a)

# closure

def f1():
  a=88
  def f2():
    print(a)
  f2()
  
f1()

def coder(num):
  def actual(x):
    return x**num
  return actual

f=coder(2)
print(f(3))