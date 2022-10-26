x = "python" # String
x = 123  # Number
x = "123"  # String
x = [12, 345, 678]  #List
x = (12, 345, 678)  #Tuple
x = {"name":"Yeawon", "age":32}  #Dict
x = True  #Boolean
#print(x)

  #checking data type with type(x) eg.print(type(x))

# Using data on numbers
a = 1 + 1
a = 100 - 1
a = 12 * 12 
a = 3 / 4
# print(a)

# Using data on string/text
a = "Act as though \nIt is impossible to fail"  # insert a new line or triple"
a = """Act as though
It is impossible to fail"""

a = '"Falure is simply the opportunity to begin again\" he says.'  # insert ', " by using \ and "
a = """ "Falure is simply the opportunity to begin again\" he says."""
a = "\"Falure is simply the opportunity to begin again\" he says."

a = "A"  # String combination, 1) A+B = AB, 2) A*3 = AAA 
b = "B"
#print(a+B) or (A*3)

a = "Like new"  # count number of words including space: len()
#print(len(a))

x = "hello  python!"  # 1st letter counts from 0
#print(x[0]) indexing
#print(x[0:5])  # 0 <= x >5 slicing
#print(x[6:])  # [:] whole, [6:] from 6 to end

x = "TitanicJames"
title = x[:7]
director = x[7:]
#print(title, "by", "Director" , director)


#a = ["a", "b", "c", "d", "e"] # List
a = ["a", "b", ["c", "d", "e"]]
b = [1, 2, [3, 4, 5]]
#print(a[1])
#print(a[2])
#print(a[2][1]) : 행렬

t = ("a", "a", "a", "b")      ################### 튜플?? vs 리스트 소괄호 

x = {"key1":"value1", "key2":"value2"}  # Dict. key-value matchs 1 to 1 using ":"(only value can be modified) 
#print(x["key2"])

x = set([1,2,3,4,4,4])
x = set(["1","2","3","4","4","4"])
print(x)