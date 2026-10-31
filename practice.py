n = [1,2,3,4,5,6]
total = 0
maximum = n[0]
for x in n:
  total += x
  if x >  maximum :
    maximum = x
print(total)
print(maximum)