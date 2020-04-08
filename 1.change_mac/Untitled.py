from re import *

str = "abcdefghi4k123j4kl12j4lkj1l;324j;132lj4l;231j4l1jkl4jklmnopqrstuvwxyz"
p = '\D' # ditgit
p2= "\d"

# find number from str
result = findall(p, str)

# find char from str
resutl1 = findall('\d', str)

# find 2 number connect 

result2 = findall(p2, str)
print(result2)
result2.group(0)
# result2.group(0)
# print("after group")
# print(result2)
# # print(findall('[a-o]', str))