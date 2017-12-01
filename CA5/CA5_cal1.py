import itertools

# 1. Addition
def add(first, second):
    return map(lambda x, y: x+y, first, second)	

# 2. Subtraction
def subtract(first, second):
    return map(lambda x, y: x-y, first, second)	
        
# 3. Multiplication	
def multi(first, second):
	return map(lambda x, y: x*float(y) if y!=0 else 'nan', first, second) 
    
# 4. Division	
def div(first, second):
	return map(lambda x, y: x/float(y) if y!=0 else 'nan', first, second) 

# 5. Exponential    
def expo(first, second):
    return map(lambda x, y: x**y, first, second)    
    
# 6. Square Root
def sqrt(values):	
	return map(lambda x : x ** 0.5, values) 
    
# 7. Cube
def cbe(values):	
	return map(lambda x: x*x*x, values)
   
# 8. Remainder
def mod(values):	
	return map(lambda x: x%x, values)

# 9. Cube Root
def cbrt(values):	
	return map(lambda x : x ** 1/3, values)     
    
   
# 10. Permutations
def perm(a,k=0):
   if(k==len(a)):
      print a
   else:
      for i in xrange(k,len(a)):
         a[k],a[i] = a[i],a[k]
         perm(a, k+1)
         a[k],a[i] = a[i],a[k]

        
#Code for calls
print add([4, 5, 11, 14, 15], [1, 9, 16, 21, 24])   
print subtract([4, 6, 11, 12, 15], [1, 7, 15, 21, 26])   
print multi([1, 4, 4, 8, 10], [2, 3, 6, 7, 9])
print div([4, 36, 12],[2, 7, 9])
print expo([3, 6, 12], [2, 3, 5])
print sqrt([2, 6, 9])
print cbe([1, 4, 10])
print mod([12, 5, 32])
print cbrt ([2, 6, 9])
print perm([1,2,3])
print max([27, 9, 46, 13])  
print min([47, 11, 22, 15])

	



