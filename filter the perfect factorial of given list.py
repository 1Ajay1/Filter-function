def perfectfact(n,fact=1):
             for i in range(1,n+1):
                          fact=fact*i
                          if fact==n:
                                       return True
                          elif fact>n:
                                       return False
var=list(filter(perfectfact,[1,2,4,6,8,10,12,120,720,24]))
print(var)
                                       
