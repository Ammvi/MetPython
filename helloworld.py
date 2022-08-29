from os import system
system("cls")
# print ("hello world")
# print ("hello world".title())
# print ("hello world".upper())
# print ("Hello World".lower())

# # python中的字符串 拼接采用 “+” 
# print (1+1)
# print ("1"+"1")
# print ("1"+"\n"+"2"+"\t"+"3")

# print (" python  ".rstrip())
# print (" python  ".lstrip())
# print (" python  ".strip()) 
# print ('\'')  #\转义字符标识

# age = 23
# message = "Happy " + str(age) +"rd Birthday!"
# print (message)

# a = "1"
# b =2 
# print (int(a)+b)


#python 列表类同与C的数组
# names =['zhangsan','lisi','wangwu','zhaoliu']
# print (names)
# print (names[0])
# print (names[-1])
# print (names[-2])
# names[0]='qianer'
# print (names)

# names.append('zhouqi')
# print (names)
# names.insert(1,"yangliu")
# print (names)
# del names[0]
# print (names)

# name1 = names.pop()
# print (name1)
# print (names)

# name2 = names.pop(2)
# print (name2)
# print (names)

# names.remove('zhaoliu')
# print(names)

# names.append('zhaoliu')
# names.append('zhaoliu')
# print (names)
# names.remove('zhaoliu')
# print (names)

# 列表排序
# cars = ['bmw','audi','toyota','honda','haval','geely']
# nums = [3,2,5,6,7,9,1]
# cars.sort()
# print (cars)
# nums.sort()
# print (nums)

# cars = ['bmw','audi','toyota','honda','haval','geely']
# nums = [3,2,5,6,7,9,1]
# cars.sort(reverse=True) # sort 改变原列表顺序
# print (cars)
# nums.sort(reverse=True)
# print (nums)

# cars = ['bmw','audi','toyota','honda','haval','geely']
# nums = [3,2,5,6,7,9,1]
# print (sorted(cars))  # sort 改变不原列表顺序
# print (sorted(nums))

# cars = ['bmw','audi','toyota','honda','haval','geely']
# cars.reverse()  # reverse 反转列表，永久改变
# print (cars)

# print (len(cars)) # len 统计列表长度

# for 循环遍历列表
# cars = ['bmw','audi','toyota','honda','haval','geely']
# for index in cars:
#     print (index)
# nums = list(range(1,11,2))
# for num in nums:
#     print(num)
# nums = []
# for value in list(range(1,11)):
#     nums.append(value*value)
# print (nums)

# nums = [value*value for value in range(1,11)]  # 正则表达式创建列表
# print (nums)
# print (max(nums))
# print (min(nums))
# print (sum(nums))

# 列表切片
# names = ['张三','李四','王五','赵六','小李','小高','小韩']
# print (names[2:6])
# print (names[:6])
# print (names[2:])
# print (names[-3:])
# for name in names[2:6]:
#     print (name)
# namesTwo = [name for name in names[2:5]]
# print (namesTwo)

# my_foods = ['pizza','carrot','falafel','cake']
# friend_foods = my_foods[:]   # 切片赋值后内容确定，不会随原列表变更
# my_foods.append("jianbing")
# print (my_foods)
# print (friend_foods)

# my_foods = ['pizza','carrot','falafel','cake']
# friend_foods = my_foods
# my_foods.append("jianbing")
# print (my_foods)
# print (friend_foods)



# 元祖 ，python中将不可修改的列表定义为元组

# dimensions = (200,50)
# print (dimensions[0])
# print (dimensions[1])
# for d in dimensions:
#     print(d)

# dimensions =(300,100)  #元祖内容虽然不可修改，但是元祖可以修改
# print (dimensions) 
# 
# cars = ['bmw','audi','toyota','honda','haval','geely'] 
# for car in cars:
#     if car == 'audi':
#         print ('有奥迪汽车')
#     else:
#         pass

# car = 'Bmw'
# print (car != 'bmw')

# age = 17
# if age >= 18:
#     print ("成年人")
# else:
#     print("未成年")

# porson = [1.5,13]
# if porson[0] < 1.2:
#     print("免费")
# elif porson[0] > 1.2 and porson[1] < 16:
#     print("半价")
# else:
#     print("全价")

# car = 12
# if car <= 4.5:
#     print("A")
# elif car > 4.5 and car <= 5.0:
#     print("B")
# elif car > 5.0 and car <= 6.0:
#     print("C")
# elif car > 6.8 and car <= 8.0:
#     print ("D")
# else:
#     print ("E")


# 给函数传递任意函数的实参

# def makePizza(size,*toppings):   #创建时会自动产生一个名称为toppings的空元祖
#     print ('要制作一个'+str(size)+'的pizza，配料为：')
#     for topping in toppings:
#         print(topping)


# makePizza(16,'洋葱')
# makePizza(22,'洋葱','香肠')

# def buildProfile(first,last,**userInfo):
#     profile = {}
#     profile['firstName'] = first
#     profile['lastName'] = last
#     for key,value in userInfo.items():
#         profile[key] = value
#     return profile

# user_profile = buildProfile('zhang','san', sex = '男', age = 18, stature = 180)
# print(user_profile)


from buildProfile import buildProfile

user_profile = buildProfile('zhang','san', sex = '男', age = 18, stature = 180)
print(user_profile)