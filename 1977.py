n = int(input())
m = int(input())
i = 1
sum = 0
count = 0
while i*i <= m:
    if n <= i*i:
        sum += i*i
        count = count + 1
        if count == 1:
            mini = i*i
    i = i + 1

if sum == 0:
    print(-1) 
elif sum > 0:
    print(sum)
    print(mini)
        