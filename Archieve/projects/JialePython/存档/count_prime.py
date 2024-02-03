a = 10000
b = 20000
x = 0
def isprime(ha):
  for i in range (2 , ha):
    if ha % i == 0:
      return 0  
  return 1
for i in range(1 , 101):
  for j in range(a , b+1):
    if(isprime(j) == 1):
      x = x + 1
  print(a,"~",b," ",x,"\n")
  a = a + 10000
  b = b + 10000
  x = 0