def perfectsqr(n):
             for i in range(1,n):
                          if i*i==n:
                                       return True
                          elif i*i>n:
                                       return False
var=list(filter(perfectsqr,[1,2,4,16,120,256,49]))
print(var)
                                       
