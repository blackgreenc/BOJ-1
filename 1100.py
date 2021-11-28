s=0
count = 0

num = int(input())

if num < 1:
    print("1")

elif 0<num<10:
    n = 0
    m = num

else:
    m = num % 10
    n = (num-m)/10



while True :
    count += 1
    n = (n + m)%10
    s = 10 * m + n
    m = s%10
    n = ((s-m)/10)
    if(s == num):
        break

print(count)