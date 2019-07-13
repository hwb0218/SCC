import requests


print ('hello world')

a = 5
b = 5
c = 5

d = a + b + c

print (d)

# array (배열)
a_list = []
b_list = [1]
c_list = [1,2]

print (a_list)
print (b_list)
print (c_list)

a_list.append(5)
a_list.append(6)
a_list.append([7,8])

print (a_list)

print (a_list[2][1])

a_dict = {}
a_dict = {'name' : 'bob', 'age' : 21}
a_dict ['height'] = 178

print(a_dict)  #객체형(Javascript의 object 형과 동일)

# Dictionary형과 list형의 조합 ( ★★★★★ )

scc = [{'name' : 'woobeen','age' : '27' },{'name' : 'woo','age' : '30'}]

# scc ['a'] = 150
print (scc)

print (scc[0]['age'])

# 함수선언

def a(x):
    y = x * x
    return y

print(a(10))

def isD(x):
    if(x % 2 == 0) :
        print('success')
    return True
isD(10)

# 반복문
def allsum(mylist) :
    sum = 0
    for i in mylist:
        sum = sum + i
    return sum

sth_list = [0,1,2,3,4,5,6,7,8,9]
print (allsum(sth_list))

sth_list_2 = range(10)
print (allsum(sth_list_2))

#조건문 & 반복문 조합
def primenumber(num):
    num = 0
    if num % 2 == 1:
        for i in num:
            if num < 10 :
                ++num
        return True
    else :
        return False
print(primenumber(9))


r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
print (rjson['RealtimeCityAir']['row'][0]['NO2'])

# <data>data</data> >> xml
# {data : [1,2,3,4]} >> json