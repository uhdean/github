import numpy as np

## 집합
## 중복된 원소 제거하기

a = [1,2,3]
b = [4,5,6]
c = [1,2,3,1,2]
d = [3,3,4,5,6,6,6,7,8,8,9]
print(a)
print(b)
print(d)
print()

new_c = []
for i in c:
    if i not in new_c:
        new_c.append(i)
print(new_c)

new_d = []
for i in d:
    if i not in new_d:
        new_d.append(i)
print(new_d)

print()
print()

### 합집합 구하기
### 1. 겹쳐지는 원소가 없을 경우

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print()

### 2. 겹치는 원소가 있을 경우

e = [1,2,3]
f = [2,3,4,5,6]
k = []
for i in e:
    if i not in f:
        k.append(i)
print(k)
k = k + f
print(k)
print()
# practice 1

A = ['apple','melon','orange']
B = ['chicken','pig','cow']
C = A + B
print(C)
print()
### 교집합 구현하기

a = [1,2,3]
b = [2,3,4,5,6]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)
print()
### 차집합 구현하기 ( c =  a-b )

a = [1,2,3]
b = [2,3,4,5,6]
c = []
for i in a:
    if i not in b:
        c.append(i)
print(c)
print()

### remove 사용하기

a = [1,2,3]
b = [2,3,4,5,6]
c = a + [] # a를 복사
for i in b:
    if i in a:
        c.remove(i)
print(c)
print()

### 여집합 구하기
U = [1,2,3,4,5]
a = [1,2,3]
a_com = []
for i in U:
    if i not in a:
        a_com.append(i)
print(a_com)
print()

U = [1,2,3,4,5]
a = [1,2,3]
rest = U + []
for i in U:
    if i in a:
        rest.remove(i)
print(rest)
print()

######### 소수 알아보기

a = 20
a_prime = True
for i in range(2,a):
    if a % i == 0:
        a_prime = False
if a_prime == True:
    print('%d은(는) 소수입니다.' %a)
else:
    print('%d은(는) 소수가 아닙니다.' %a)
print()

### 약수 찾기

a = 24
b = range(1,a)
factors = []
for i in b:
    if a % i == 0:
        factors.append(i)
factors.append(a)
print(factors)
print()

# 최대공약수 찾기
## 1. 각 수의 약수를 모두 구한다.
## 2. 겹쳐지는 수를 구하여 오름차순으로 정리한다.
## 3. 마지막 숫자가 최대 공약수이다.

a = 24
aa = range(1,a)
a_factors = []
for i in aa:
    if a % i == 0:
        a_factors.append(i)
a_factors.append(a)
print(a_factors)

b = 36
bb = range(1,b)
b_factors = []
for i in bb:
    if b % i == 0:
        b_factors.append(i)
b_factors.append(b)
print(b_factors)

common = []
for i in a_factors:
    if i in b_factors:
        common.append(i)
common.sort()
print(common[-1])
print()

### 최소 공배수 구하기
#### 1. 두 수의 곱을 구한다.
#### 2. 두 수의 최대공약수를 구한다.
#### 3. 두 수의 곱을 최대공약수로 나눈다.

M = a*b
GCD = common[-1]
LCM = M / GCD

print('%d 와 %d의 최소 공배수는 %d이다.' %(a,b,LCM))
