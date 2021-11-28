num = int(input())
if num<10:
    n = 0
    m = num
else:
    m = num % 10
    n = (num-m)/10
s=0
count = 0
while s != num :
    n = (n + m)%10
    s = 10 * m + n
    count += 1
    m = s%10
    n = ((s-m)/10)
print(count)