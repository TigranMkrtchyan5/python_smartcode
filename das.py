# def gumarum(a,b):
    
#     return a + b

# def hanum(a,b):
    
#     return a - b

# def bazmapatkum(a,b):
    
#     return a * b

# def bajanum(a,b):
    
#     return a / b

# print(f'gumarum:{gumarum(4,7)},hanum:{hanum(4,7)},bazmapatkum:{bazmapatkum(4,7)},bajanum:{bajanum(4,7)}')
# ------------------------------------------------------------------------------------------------------
# def qanak(text):
#     count_tiv = 0
#     count_tar = 0
#     for i in text:
#         if i.isdigit():
#             count_tiv += 1
#         elif i.isalpha():
#             count_tar += 1
#             return f'tareri_qanak = {count_tar}  tveri qanak = {count_tiv}'

# print(qanak('aloazizi'))
# --------------------------------------------------------------------------------
#
# 
# ----------------------------------leeson 18----------------------------------------
# def parz_tiv(tiv):

#     for i in range(2,int(tiv **  0.5)+ 1):
#         if tiv % i == 0:
#             print('parz che')
#             break
#     else:
#         print('parz')

# parz_tiv(97)
# split
# ==========================lesson 19 ===leetcode=====================
# num1 = [1,2,3,0,0,0] 
# m = 3
# num2= [2,5,6] 
# n = 3 
# num1[m:m+n] = num2[:n]
# num1.sort()
# print(num1)
# ---------------------------------------------------------------------------------
# def function(nums):

#     val = 3 
#     while val in nums:
#         nums.remove(val)
#     return(nums)

# print(function([3,2,2,3]))
# --------------------------------------------------------------------------------------
# nums = [0,0,1,1,1,1,1,1,1,1,1,1,2,2,3,3,4]
# for i in nums[::-1]:
#     if nums.count(i) > 1:
#         nums.remove(i)
# print(nums)
# --------------------------------------------------------------------------------------
# nums = [3,2,3]
# nums.sort()
# print(nums[len(nums) // 2])
# ----------------------------------------------------------------------------------------
# s = "hello world"
# print(len(s.split(' ')[-1]))
# -------------------------------------------------------------------------------------------
# nums = [11,15,2,7,4,5,]
# target = 9
# for i in range(0,len(nums) - 1): 
#     if nums[i] + nums[i+1] == target:
#         print(f'stacvec',{i},{i+1})
#     else:
#         print('chstacvec')
# ---------------------------------------------------------------------------------------------
# strs = ["flower","flow","flight"]
# strs.sort(key=len)
# index = 0
# while index < len(strs):
#     if strs[0] == strs[index][:len(strs[0])]:
#         index += 1
#     else:
#         strs[0] = strs[0][:-1]
#         print(strs[0])




# def func():
#     count = 0
#     while True:
#         n = int(input('greq tivy: '))
#         if n == 0:
#             break
#         else:
#             count += n 
#             print(count)

# func()

# --------------------------------------code wars-----------------------------
