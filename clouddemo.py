#Print fibonacci series using dp
def fibo(n):
  if n==1 :
    return 0
  if n==0 : 
    return 1

  return fibo(n-1) + fibo(n-2)


a=fibo(10)
print(a)
