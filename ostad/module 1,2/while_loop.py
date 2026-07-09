a = [1, 2, 3, 4, 5]
result = 0

i = 0
n = len(a)
while i<n:
    result += a[i]
    i+=1
print(result)

a = [-10, 2, 19, -3, -5]
# minus gulake 0 korte chacchi
i = 0
while i<len(a):
    if a[i]<0:
        a[i]=0
    i+=1
print(a)