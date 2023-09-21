
# # # # # # def countSameBitNumbers(N):
# # # # # #     MOD = 10**9 + 7

# # # # # #     # Function to count the number of set bits in an integer
# # # # # #     def countSetBits(n):
# # # # # #         count = 0
# # # # # #         while n:
# # # # # #             count += n & 1
# # # # # #             n >>= 1
# # # # # #         return count

# # # # # #     # Calculate the number of set bits in N
# # # # # #     num_set_bits_N = countSetBits(N)

# # # # # #     # Calculate f(N)
# # # # # #     f_N = N
# # # # # #     if f_N & (f_N + 1) != 0:
# # # # # #         f_N |= (f_N >> 1)

# # # # # #     # Initialize count
# # # # # #     count = 0

# # # # # #     # Iterate through integers from 1 to f(N)
# # # # # #     for i in range(f_N + 1):
# # # # # #         # Count the set bits in i without the need for a function
# # # # # #         set_bits_i = bin(i).count('1')
# # # # # #         if set_bits_i == num_set_bits_N and i != N:
# # # # # #             count += 1

# # # # # #     return count % MOD

# # # # # # # Example usage:
# # # # # # N = 1
# # # # # # result = countSameBitNumbers(N)
# # # # # # print(result)

# # # # # # Measure the execution time of the function/code snippet
# # # # # # execution_time = timeit.timeit(result, number=1)

# # # # # # Print the execution time
# # # # # # print(f"Execution time: {execution_time} seconds")


# # # # # # import time
# # # # # # start_time = time.time()
# # # # # # print(start_time)

# # # # # # def countSameBitNumbers(N):
# # # # # #     MOD = 10**9 + 7

# # # # # #     # Function to count the number of set bits in an integer
# # # # # #     def countSetBits(n):
# # # # # #         count = 0
# # # # # #         while n:
# # # # # #             count += n & 1
# # # # # #             n >>= 1
# # # # # #         return count

# # # # # #     # Calculate the number of set bits in N
# # # # # #     num_set_bits_N = countSetBits(N)

# # # # # #     # Record the start time
# # # # # #     start_time = time.time()

# # # # # #     # Calculate f(N)
# # # # # #     f_N = N
# # # # # #     while (f_N & (f_N + 1)) != 0:
# # # # # #         f_N |= (f_N >> 1)

# # # # # #     # Initialize count
# # # # # #     count = 0

# # # # # #     # Iterate through integers from 1 to f(N)
# # # # # #     for i in range(f_N + 1):
# # # # # #         # Count the set bits in i without the need for a function
# # # # # #         set_bits_i = bin(i).count('1')
# # # # # #         if set_bits_i == num_set_bits_N and i != N:
# # # # # #             count += 1

# # # # # #     # Record the end time


# # # # # #     # Calculate and print the elapsed time
# # # # # #     # print(f"Execution time: {end_time} seconds")

# # # # # #     return count % MOD

# # # # # # # Example usage:
# # # # # # N = 5
# # # # # # result = countSameBitNumbers(N)
# # # # # # print(result)
# # # # # # end_time = time.time()
# # # # # # print(end_time)
# # # # # # microseconds=end_time-start_time
# # # # # # seconds = microseconds / 1000000  # Convert microseconds to seconds
# # # # # # print(f"{microseconds} microseconds is equal to {seconds} seconds")


# # # # # # import timeit
# # # # # # # Define your code as a string inside a function
# # # # # # code_to_measure = """
# # # # # # def countSameBitNumbers(N):
# # # # # #     MOD = 10**9 + 7

# # # # # #     # Function to count the number of set bits in an integer
# # # # # #     def countSetBits(n):
# # # # # #         count = 0
# # # # # #         while n:
# # # # # #             count += n & 1
# # # # # #             n >>= 1
# # # # # #         return count

# # # # # #     # Calculate the number of set bits in N
# # # # # #     num_set_bits_N = countSetBits(N)

# # # # # #     # Calculate f(N)
# # # # # #     f_N = N
# # # # # #     while (f_N & (f_N + 1)) != 0:
# # # # # #         f_N |= (f_N >> 1)

# # # # # #     # Initialize count
# # # # # #     count = 0

# # # # # #     # Iterate through integers from 1 to f(N)
# # # # # #     for i in range(f_N + 1):
# # # # # #         # Count the set bits in i without the need for a function
# # # # # #         set_bits_i = bin(i).count('1')
# # # # # #         if set_bits_i == num_set_bits_N and i != N:
# # # # # #             count += 1

# # # # # #     return count % MOD

# # # # # # # Example usage:
# # # # # # N = 6
# # # # # # result = countSameBitNumbers(N)
# # # # # # """



# # # # # # """
# # # # # # Input: n = 19
# # # # # # Output: true
# # # # # # Explanation:
# # # # # # 12 + 92 = 82
# # # # # # 82 + 22 = 68
# # # # # # 62 + 82 = 100
# # # # # # 12 + 02 + 02 = 1
# # # # # # Example 2:

# # # # # # Input: n = 2
# # # # # # Output: false
# # # # # # """
# # # # # # n=int(input("enter an positive number"))
# # # # # # value=1
# # # # # # count=0
# # # # # # if value<=n:
# # # # # #     for i in str(n):
# # # # # #         a=((int(i)**2))
# # # # # #         print(a)
# # # # # # num = 19
# # # # # # def power(n):
# # # # # #     str_n = str(n)
# # # # # #     result = []
# # # # # #     for i in str_n:
# # # # # #         result.append(int(i)*int(i))
# # # # # #     return sum(result)
    
# # # # # # def func(n):
# # # # # #     new_n = str(n)
# # # # # #     if len(new_n)==1:
# # # # # #         if n==1:
# # # # # #             return True
# # # # # #         else: return False
# # # # # #     else:aa = power(n)
# # # # # #     res = func(aa)
# # # # # #     return res        
# # # # # # print(func(num))

# # # # # # from math import sqrt
# # # # # # num = input("Maximum Number? ")
# # # # # # import pdb;pdb.set_trace()
# # # # # # num = int(num)+1
# # # # # # for a in range(1,num):
# # # # # #     for b in range(a,num):
# # # # # #         c_square = a**2 + b**2
# # # # # #         value = int(sqrt(c_square))
# # # # # #         if ((c_square - value**2) == 0):
# # # # # #             print(a, b, value)

# # # # # # Example 1:
# # # # # # Input: s = "anagram", t = "nagaram"
# # # # # # Output: true

# # # # # # Example 2:
# # # # # # Input: s = "rat", t = "car"
# # # # # # Output: false

# # # # # # str1=str(input("enter first string value:-"))
# # # # # # str2=str(input("enter second string value:-"))
# # # # # # a=str(sorted(str1))
# # # # # # b=str(sorted(str2))
# # # # # # if a==b:
# # # # # #     print("true")
# # # # # # else:
# # # # # #     print("false")
    
# # # # # # strs = ["eat","tea","tan","ate","nat","bat"]
# # # # # # aa=dict()
# # # # # # for i in strs:
# # # # # #     ss = sorted(i) 
# # # # # #     aa[''.join(ss)]= [j for j in strs if sorted(i)==sorted(j)]

# # # # # # print(list(aa.values()))

# # # # # # n=int(input("enter"))
# # # # # # s=n
# # # # # # v=0
# # # # # # while s>0:
# # # # # #     t=s%10
# # # # # #     v=v+t**3
# # # # # #     s=s//10
# # # # # # if n==v:
# # # # # #     print(n,"is an armstrong number")
# # # # # # else:
# # # # # #     print("not armastong")

# # # # # # var="1234abcd"
# # # # # # v=""
# # # # # # for i in var:
# # # # # #     v=i+v
# # # # # # print(v)

# # # # # # var_1="the sky is blue"
# # # # # # v=var_1.split()
# # # # # # v.reverse()
# # # # # # print(v)

# # # # # # num=[1,2,1,3,2,4]
# # # # # # d={}
# # # # # # for i in num:
# # # # # #     s=num.count(i)
# # # # # #     d[i]=s
# # # # # # print(d)

# # # # # # d={"red":1,"green":3}
# # # # # # s=d.items()
# # # # # # print(list(s))

# # # # # # string="aaabc"
# # # # # # for i in string:
# # # # # #     c=string.count(i)
# # # # # #     if c==2:
# # # # # #         print("true")
# # # # # #     else:
# # # # # #         print("false")

# # # # # def numberofSubsequences(N, S, Q, queries):
# # # # #     # Initialize counters for '01' and '10' subsequences
# # # # #     count_01 = 0
# # # # #     count_10 = 0

# # # # #     # Count '01' and '10' subsequences in the original string
# # # # #     for i in range(N - 1):
# # # # #         if S[i:i + 2] == '01':
# # # # #             count_01 += 1
# # # # #         elif S[i:i + 2] == '10':
# # # # #             count_10 += 1

# # # # #     # Process queries
# # # # #     results = []
# # # # #     for query in queries:
# # # # #         index = query - 1  # Adjust for 0-based indexing
# # # # #         if S[index] == '0':
# # # # #             # Flip 0 to 1
# # # # #             if index > 0 and S[index - 1] == '1':
# # # # #                 count_01 -= 1
# # # # #             if index < N - 1 and S[index + 1] == '1':
# # # # #                 count_10 -= 1
# # # # #             S = S[:index] + '1' + S[index + 1:]
# # # # #         else:
# # # # #             # Flip 1 to 0
# # # # #             if index > 0 and S[index - 1] == '0':
# # # # #                 count_10 -= 1
# # # # #             if index < N - 1 and S[index + 1] == '0':
# # # # #                 count_01 -= 1
# # # # #             S = S[:index] + '0' + S[index + 1:]

# # # # #         results.append(count_01 + count_10)

# # # # #     return results

# # # # # # Input
# # # # # N = 5
# # # # # S = "11011"
# # # # # Q = 1
# # # # # queries = [1]

# # # # # # Call the function and print the results
# # # # # results = numberofSubsequences(N, S, Q, queries)
# # # # # for result in results:
# # # #     # print(result)

# # # # def numberofSubsequences(N, S, Q, queries):
# # # #     # Initialize counters for '01' and '10' subsequences
# # # #     count_01 = 0
# # # #     count_10 = 0
# # # #     # Initialize lists to store the positions of '0' and '1' in the string
# # # #     positions_0 = []
# # # #     positions_1 = []

# # # #     # Helper function to count subsequences containing '01' or '10'
# # # #     def count_subsequences(subsequence_count, positions, flip_index):
# # # #         for pos in positions:
# # # #             if pos < flip_index:
# # # #                 subsequence_count += 1
# # # #             else:
# # # #                 break
# # # #         return subsequence_count

# # # #     # Count initial subsequences
# # # #     for i, char in enumerate(S):
# # # #         if char == '0':
# # # #             count_01 = count_subsequences(count_01, positions_1, i)
# # # #             positions_0.append(i)
# # # #         else:
# # # #             count_10 = count_subsequences(count_10, positions_0, i)
# # # #             positions_1.append(i)

# # # #     # Process queries and print counts
# # # #     for query in queries:
# # # #         flip_index = query
# # # #         if S[flip_index] == '0':
# # # #             count_01 = count_subsequences(count_01, positions_1, flip_index)
# # # #             count_10 = count_subsequences(count_10, positions_0, flip_index)
# # # #             positions_0.remove(flip_index)
# # # #             positions_1.append(flip_index)
# # # #         else:
# # # #             count_01 = count_subsequences(count_01, positions_1, flip_index)
# # # #             count_10 = count_subsequences(count_10, positions_0, flip_index)
# # # #             positions_1.remove(flip_index)
# # # #             positions_0.append(flip_index)

# # # #         print(count_01)
# # # #         print(count_10)

# # # # # Input
# # # # N = 5
# # # # S = "01111"
# # # # Q = 2
# # # # queries = [0, 0]

# # # # # Call the function with the input and print the results
# # # # numberofSubsequences(N, S, Q, queries)
# # # def NumberofSubsequences(N, S, queries, Q):
# # #     results=[]
# # #     new = S

# # #     for i in range(Q):
# # #         if S[queries[i]] == "0":
# # #                 S = S[:queries[i]]+"1"+S[queries[i]+1:]
# # #         else:
# # #                 S = S[:queries[i]]+"0"+S[queries[i]+1:]

# # #     count = 0
# # #     for j in range(N-1):
# # #             if S[j]+S[j+1] in ['10', '01']:
# # #                 count +=1
# # #     results.append(count)   
# # #     for i in results:
# # #         print(i)  
            
# # # 		# Call the function to solve the problem
# # # N=5
# # # S='01111'
# # # Q=2
# # # queries= [0,0]
# # # # output = 0 1

# # # # N=4
# # # # S='01111'
# # # # Q=2
# # # # queries= [0,0]
# # # # output = 0 1
# # # NumberofSubsequences(N, S, queries, Q)


# def NumberofSubsequences(N, S, queries, Q):
#     results = []

#     for i in range(Q):
#         if S[queries[i]] == "0":
#             S = S[:queries[i]] + "1" + S[queries[i] + 1:]
#         else:
#             S = S[:queries[i]] + "0" + S[queries[i] + 1:]

#         count = 0
#         for j in range(N - 1):
#             if S[j] + S[j + 1] in ['10', '01']:
#                 count += 1
#         results.append(count)

#     for i in results:
#         print(i)

# # Call the function to solve the problem
# N = 5
# S = '01111'
# Q = 2
# queries = [0]

# NumberofSubsequences(N, S, queries, Q)


# def recurringStrings(N, N_StringArr, S1):
#     import pdb;pdb.set_trace()
#     count = 0
#     for string in N_StringArr:
#         if len(string) != len(S1):
#             continue  # Skip strings of different lengths
#         can_reframe = True
#         for i in range(len(string)):
#             if ord(string[i]) - ord(S1[i]) == 1:
#                 can_reframe = False
#                 break
#         if can_reframe:
#             count += 1
#     return count

# N = 2
# N_StringArr = ["BAAA", "AAAA"]
# S1 =  "BAAA"

# # Call the function and print the result
# result = recurringStrings(N, N_StringArr, S1)
# print(result)

# def NumberofSubsequences(N, S, queries, Q):
#     results = []

#     for i in range(Q):
#         if S[queries[i]] == "0":
#             S = S[:queries[i]] + "1" + S[queries[i] + 1:]
#         else:
#             S = S[:queries[i]] + "0" + S[queries[i] + 1:]

#         count = 0
#         for j in range(N - 1):
#             if S[j] + S[j + 1] in ['10', '01']:
#                 count += 1
#         results.append(count)

#     for i in results:
#         print(i)

# # Call the function to solve the problem
# N = 5
# S = '01111'
# Q = 2
# queries = [0, 0]

# NumberofSubsequences(N, S, queries, Q)

# def findInterestingPairs(arr, sumVal):
#     count = 0  # Initialize a count variable to keep track of interesting pairs

#     # Iterate through the array
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):  # Start j from i+1 to avoid counting the same pair twice
#             # Calculate the absolute difference and absolute sum
#             diff = abs(arr[i] - arr[j])
#             summ = abs(arr[i] + arr[j])
            
#             # Check if the pair is interesting
#             if diff + summ == sumVal:
#                 count += 1

#     return count

# # Example usage:
# arr = [4, 1, 3, 2,0]
# # sumVal = 2
# # result = findInterestingPairs(arr, sumVal)
# # print(result)  # Output should be 2
# import requests

# def findCountries(keyword, region):
#     result=[]
#     base_url =      f'https://jsonmock.hackerrank.com/api/countries/search/?region={region}&name={keyword}'
#     data = requests.get(base_url)
#     response = data.json()
#     countries = response['data']
#     for country in countries:
#         result.append(f"{country['name']}, {country['population']}")
#     print(result)    
#     return result[::-1]

# keyword = 'ab',
# region = 'Asia',
# keyword = 'de'
# region = 'Europe'
# result = findCountries(keyword, region)


# 3                            number of users n = 3
# Hana                    users [Hana', 'Luca', 'Lev']
# Luca 
# Lev
# 4                              instructions count = 4    
# connect 0 1         instruction 1: connect users [0] (Hana) with
# users[1] (Luca)
# hangup 0 1
# connect 1 2
# hangup 1 2

# Sample Output
# Success: Connection established between Hana and Luca
# Success: Hana and Luca are disconnected
# Success: Connection established between Luca and Lev
# Success: Luca and Lev are disconnected


# from dataclasses import dataclass
# from abc import ABC, abstractmethod

# @dataclass
# class Caller:
#     name: str
# class ConnectionException(Exception):
#     pass
# class CommsHandlerABC(ABC):
    
#     @abstractmethod
#     def connect(self, user1: Caller, user2: Caller) -> str:
#         """Implement connect method"""
#     @abstractmethod
#     def hangup(self, user1: Caller, user2: Caller) -> str:
#         """Implement hangup method"""
#     @abstractmethod
#     def clear_all(self) -> None:
#         """Implement clear_all method"""
        
# class CommsHandler(CommsHandlerABC):
    
#     def __init__(self):
#         self.active_connections = []
#     def connect(self, user1: Caller, user2: Caller) -> str:
#         if user1 == user2:
#             raise ConnectionException(f"{user1.name} cannot connect with {user2.name}")
#         if any(user in self.active_connections for user in [user1, user2]):
#             raise ConnectionException("Connection in use. Please try later")
#         self.active_connections.extend([user1, user2])
#         return f"Connection established between {user1.name} and {user2.name}"
#     def hangup(self, user1: Caller, user2: Caller) -> str:
#         if user1 == user2:
#             raise ConnectionException(f"{user1.name} cannot hangup with {user2.name}")
#         if user1 in self.active_connections and user2 in self.active_connections:
#             self.active_connections.remove(user1)
#             self.active_connections.remove(user2)
#             return f"{user1.name} and {user2.name} are disconnected"
#         raise ConnectionException(f"{user1.name} and {user2.name} not found in the communication channel")
#     def clear_all(self) -> None:
#         self.active_connections.clear()
        
# # Main code
# def main():
#     comms = CommsHandler()
#     functions = {"connect": comms.connect, "hangup": comms.hangup}
#     # Create users
#     n = int(input().strip())
#     users = []
#     for i in range(n):
#         name = input().strip()
#         u = Caller(name)
#         assert u.name == name
#         users.append(u)
#     # Perform operations
#     result_str = ""
#     instructions_count = int(input().strip())
#     for i in range(instructions_count):
#         instructions = input().strip().split()
#         ul, u2 = map(int, instructions[1:])
#         # import pdb;pdb.set_trace()
#         try:
#             result_str += "Success: " + functions[instructions[0]](users[ul], users[u2]) + "\n"
#             print("-------", result_str)
#         except ConnectionException as ce:
#             result_str += "Error: " + str(ce) + "\n"
#             print("========", result_str)
#     comms.clear_all()
    
# if __name__ == "__main__":
#     main()


# from dataclasses import dataclass
# from abc import ABC, abstractmethod

# @dataclass
# class Caller:
#     name: str

# class ConnectionException(Exception):
#     pass

# class CommsHandlerABC(ABC):
    
#     @abstractmethod
#     def connect(self, user1: Caller, user2: Caller) -> str:
#         """Implement connect method"""
#     @abstractmethod
#     def hangup(self, user1: Caller, user2: Caller) -> str:
#         """Implement hangup method"""
#     @abstractmethod
#     def clear_all(self) -> None:
#         """Implement clear_all method"""
        
# class CommsHandler(CommsHandlerABC):
    
#     def __init__(self):
#         self.active_connections = []
        
#     def connect(self, user1: Caller, user2: Caller) -> str:
#         if user1 == user2:
#             raise ConnectionException(f"{user1.name} cannot connect with {user2.name}")
#         if any(user in self.active_connections for user in [user1, user2]):
#             raise ConnectionException("Connection in use. Please try later")
#         self.active_connections.extend([user1, user2])
#         return f"Connection established between {user1.name} and {user2.name}"
    
#     def hangup(self, user1: Caller, user2: Caller) -> str:
#         if user1 == user2:
#             raise ConnectionException(f"{user1.name} cannot hangup with {user2.name}")
#         if user1 in self.active_connections and user2 in self.active_connections:
#             self.active_connections.remove(user1)
#             self.active_connections.remove(user2)
#             return f"{user1.name} and {user2.name} are disconnected"
#         raise ConnectionException(f"{user1.name} and {user2.name} not found in the communication channel")
    
#     def clear_all(self) -> None:
#         self.active_connections.clear()
        
# # Main code
# def main():
#     comms = CommsHandler()
#     functions = {"connect": comms.connect, "hangup": comms.hangup}
#     n = int(input().strip())
#     users = []
#     for _ in range(n):
#         name = input().strip()
#         u = Caller(name)
#         assert u.name == name
#         users.append(u)
    
#     result_str = ""
#     instructions_count = int(input().strip())

#     for _ in range(instructions_count):
#         instructions = input().strip().split()
#         ul, u2 = map(int, instructions[1:])
    
#         try:
#             result_str +=(
#  "Success: " + functions[instructions[0]](users[ul], users[u2]) + "\n"
# )
            
#         except ConnectionException as ce:
#             result_str += "Error: " + str(ce) + "\n"
          
#     comms.clear_all()
    
# if __name__ == "__main__":
#     main()

# def countMinimumOperations(arr):
#     n = len(arr)
    
#     # Find the index of 1 in the array
#     idx_1 = arr.index(1)
    
#     # Initialize the number of operations
#     operations = 0
    
#     # Iterate through the elements from idx_1 to the end of the array
#     for idx in range(idx_1, n):
#         if arr[idx] == 1:
#             idx_1 += 1  # Cyclic shift
#         else:
#             operations += 1  # Swap operation
    
#     return operations

# # Example usage:
# arr = [3, 1, 2]
# result = countMinimumOperations(arr)
# print(result)  # Output should be 1

# l1=[5,6,[],3,[],[],9]
# l2=[]
# for i in l1:
#     if i!=[]:
#         l2.append(i)
#     else:
#         pass
# print(l2)

# l1=[5,6,[],3,[],[],9]
# l2=[ele for ele in l1 if ele!=[]]
# print(l2)

# l1=[5,6,[],3,[],[],9]
# for i in l1:
#     if i ==[]:
#         pass
#     else:
#         print(i)

# def func1(input_list):
#     l1=[]
#     for i in input_list:
#         if i:
#             l1.append(i)
#     print(l1)
#     return l1
# input_list=[5,6,[],3,[],[],9]
# func1(input_list)


# def func2(l1):
#     c1=[]
#     for i in l1:
#         if i>len(l1):
#             c1.append(i)
#     print(c1)
#     return c1           
# l1=[10,23,532,4,1313,4232]
# func2(l1)

# test_list = ["Gfg", 3, "is", 8]
# key_list = ["name", "id"] 
# # Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}] 
# d1={}
# d2={}
# for i in test_list:
#     d1[key_list[0]]=i
#     print(d1)

# list_method
# l1=[]
# for i in range(50):
#     l1.append(i)
# print(l1)
# aa=l1.count(10)
# print(aa)
# bb=l1.extend(['orange','banana','cherry','pineapple'])
# print(l1)
# cc=l1.insert(9,["first",'second','third','fourth','fifth'])
# print(l1)
# dd=l1.insert(0,(100,200,300,400,500,600,700))
# print(l1)
# l1.remove(1)
# print(l1)
# ff=l1.pop()
# print(ff)
# l1.reverse()

# def my_func():
#     pass
# result=my_func()
# print(result)

# def another_func():
#     return None

# print(another_func())

# def findInterestingPairs(arr, sumVal):
#     count = 0
#     element_count = {}
    
#     for num in arr:
#         diff1 = num - sumVal
#         diff2 = num + sumVal
#         count += element_count.get(diff1, 0)
#         count += element_count.get(diff2, 0)
#         element_count[num] = element_count.get(num, 0) + 1
#     return count

# # Example usage:
# arr = [1, 4, -1, 2]
# sumVal = 4
# result = findInterestingPairs(arr, sumVal)
# print(result)  # Output should be 2

# arr = [1,3,2,0]
# sumVal = 2
# c = 0
# b = sumVal//2
# for i in range(len(arr)):
#     if arr[i]!=b and abs(arr[i]+b)+abs(arr[i]-b)==sumVal:
#         c+=1
# print(c) 

# arr =[1,3,2,0]
# sumVal = 2
# c = 0
# b = sumVal//2
# for i in range(len(arr)):
#     if arr[i]!=b and abs(arr[i]+b)+abs(arr[i]-b)==sumVal:
#         c+=1
# print(c)

# def countMinimumOperations(arr):
#     import pdb;pdb.set_trace()
#     num = len(arr)
#     out_of_place = 0

#     for i in range(num):
#         if arr[i] != i + 1:
#             out_of_place += 1

#     if out_of_place == 0:
#         return 0
#     elif out_of_place == 1:
#         return 1
#     else:
#         return 2

# # Example usage:
# arr = [3,1,2]#--->[3,2,1,4,5]--->[1,2,3,4,5]
# result = countMinimumOperations(arr)
# print(result)  # Output should be 2

# def countMinimumOperations(arr):
#     n = len(arr)
#     operations = 0

#     for i in range(n):
#         if arr[i] != i + 1:
#             # Find the correct index for the current element
#             correct_index = arr.index(i + 1)
            
#             # Swap the current element with the element at correct_index
#             arr[i], arr[correct_index] = arr[correct_index], arr[i]
            
#             # Increment the operations count
#             operations += 1
            
#             # Perform a cyclic shift to the left by (correct_index - 1) positions
#             arr = arr[correct_index - 1:] + arr[:correct_index - 1]

#     return operations

# # Example usage:
# arr = [5, 3, 2, 1, 4]
# result = countMinimumOperations(arr)
# print(result)  # Output should be 2

# l1=[1,3,5,7,7]
# print(type(l1))
# l1=[10,20,30,40,50]
# l1.extend([1000,200,300])
# l1.insert(4,"hello")
# print(l1)
# l1.remove(1000)
# l1.clear()
# print(l1)
# l2=[10,10,30,30,30,100,100,100,100]
# print(l2.count(100))
# l3=[2]
# print(l3.index(2))
# l4=[20,30,10,40,60,80]
# l4.sort()
# print(l4)
# l4.reverse()
# print(l4)

# from collections import deque
# # queue=deque(["Eric","john","Michael"])
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham") 
# print(queue)
# print(queue.popleft())
# print(queue.popleft())
# print(queue)

# square=[]
# for i in range(1,10):
#     square.append(i**2)
# print(square)

# ls1=[x**2 for x in range(1,10) if x%2==0]
# print(ls1)

# ls2=list(map(lambda x:x**2 ,range(10)))
# print(ls2)

# combs=[]
# for i in range(10):
#     for k in range(20):
#         if i!=k:
#             combs.append((i,k))
# print(i,k)

# combs1=[(x,y) for x in range(10) for y in range(20) if x!=y]
# print(combs1)

# def func1(item):
#     return item**2

# l1=[10,20,30,40,50]
# result=map(func1,l1)
# print(result)

# s1="the sky  is blue"
# s2=s1[::-1]
# print(s2)

# def func(item):
#     return item**2

# l1=[10,20,30,40]
# result=map(func,l1)
# print(list(result))


# l1=[10,20,30,40]
# result=list(map(lambda x:x**2,l1))
# print(result)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# l1=[[row[i] for row in matrix] for i in range(4)]
# print(l1)

# l1=[]
# for i in range(4):
#     l1.append([row[i] for row in matrix])
# print(l1)

# l1=[]
# for i in range(4):
#     l2=[]
#     for row in matrix:
#         l2.append(row[i])
#     l1.append(l2)
# print(l1)
# for i in range(1,10):
#     print(i)
    
# l1=["hello","how","are","you"]
# l2=[10,20,30,40,50]
# z1=zip(l1,l2)
# print(z1)

# lst=['hello','my','name','rahul']
# del lst[2:4]
# print(lst)

# t1=("name",)
# # print(type(t1))

# t=1234,43434,"hello!"
# print(t[0])

# # t[0]="this"
# # print(t)
# l1=list(t)
# print(l1)
# l1[2]="its me"
# print(tuple(l1))
# l2=len(t)
# print(l2)

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket) 
# print('orange' in basket)
# print('pear' is basket)
# l1=[10,20,30,4,10,12,12,13,15]
# s1=set(l1)
# print(s1)
# length=len(s1)
# print(length)

# a={x for x in range(10) if x%2==0}
# print(a)

# tel={'jack':100,'sape':200}
# print(tel['jack'])
# print(tel['sape'])
# tel['guido']=1000
# print(tel)
# del tel['sape']
# print(tel)
# l1=list(tel)
# print(l1)
# l2='guido' in tel
# print(l2)
# l3="sape" in tel
# print(l3)

# d1=dict([('first',100),('second',200),('third',300)])
# print(d1)

# d2={x:x**2 for x in range(1,10) if x%2!=0}
# print(d2)

# d3=dict(indore=53662532,bhopal=21212,gwalior=323232)
# print(d3)

# for k,v in d3.items():
#     l1=[]
#     l1.append([k,v])
#     print(k,v)
    
# for i,v in enumerate([100,'indore','bhopal','gwalior']):
#     print(i,v)
    
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))
    
# for i in reversed(range(1,10)):
#     print(i)
    
# basket=['apple','banana','apple','orange']
# for i in sorted(basket):
#     print(i)
    
# basket=['apple','banana','apple','cherry','nuts']
# for i in set(sorted(basket)):
#     print(i)
    
# l1=[100,200,300,400,500]
# for i in l1:
#     if i in l1:
#         print(i**2)
#     else:
#         print("if this value in not a list")
        
# l1=(1,2,3)
# l2=(1,2,4)
# if l1>l2:
#     print(True)
# else:
#     print(False)

# x=int(input("enter a x value"))
# if x<0:
#     x=0
#     print("negative value will changed with zero")

# elif x<1:
#     print("zero value will be assign")
    
# elif x==1:
#     print("single value will be assign") 

# else:
# #     print("more than 1 value  assign in this part")
# from typing import List
# import ast

# def solution(k: List[int]) -> int:
#     n = len(k)
#     total_sum = 0

#     for i in range(n):
#         for j in range(i + 2, n + 2):
#             subset = k[i:j]
#             if len(subset) % 2 == 0:
#                 total_sum += sum(subset)

#     return total_sum

# if __name__ == "__main__":
#     k_str = input("Enter a list of numbers as a string (e.g., '[4, 1, 2, 5]'): ").strip()
#     k = ast.literal_eval(k_str)
#     print(solution(k))


# from typing import List
# def solution(k: List[int]) -> int:
#     def is_even(num):
#         return num % 2 == 0
#     n = len(k)
#     total_sum = 0
#     # Generate all possible subsets
#     for i in range(n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum += k[j]
#             if is_even(j - i + 1):
#                 total_sum += current_sum
#     return total_sum
# # Test case
# k = [1, 3, 2, 5]
# print(solution(k))
# # Output: 30
# if __name__=='__main__':
#     line = input()
#     k=line.strip().split() 
#     print(solution (k))


# def solution(A,K,L):
#     ans1  = find_maximum_apples_imp(A,K,L)
#     ans2 = find_maximum_apples_imp(A,L,K)
#     return max(ans1, ans2)

# def find_maximum_apples_imp(A,K,L):
#     if K+L > len(A):
#         return -1
#     _sum = [0] * 1000
#     _sum[0] = A[0]
#     for i in range(1,len(A)):
#         _sum[i] = _sum[i-1]+A[i]
#     max_apples = -1
#     x,y = 0,0
#     for a in range(len(A)-K+1):
#         if a>0:
#             x = _sum[a+K-1] - _sum[a-1]
#         else:
#             x = _sum[a+K-1]
#         for b in range(a+K,len(A)-L+1):
#             if b>0:
#                 y = _sum[b+L-1] - _sum[b-1]
#             else:
#                 y = _sum[b+L-1]
#             if x+y > max_apples:
#                 max_apples = x+y
#     print(max_apples)           
#     return max_apples

# def NumberofSubsequences(N, S, queries, Q):
#     results = []

#     for i in range(Q):
#         if S[queries[i]] == "0":
#             S = S[:queries[i]] + "1" + S[queries[i] + 1:]
#         else:
#             S = S[:queries[i]] + "0" + S[queries[i] + 1:]

#         count = 0
#         for j in range(N - 1):
#             if S[j] + S[j + 1] in ['10', '01']:
#                 count += 1
#         results.append(count)

#     for i in results:
#         print(i)

# # Call the function to solve the problem
# N = 5
# S = '01111'
# Q = 2
# queries = [0, 0]
# NumberofSubsequences(N,S,queries,Q)


# def NumberofSubsequences(N, S, queries, Q):
#         results=[]
#         new = S

#         for i in range(Q):
#             if S[queries[i]] == "0":
#                     S = S[:queries[i]]+"1"+S[queries[i]+1:]
#             else:
#                     S = S[:queries[i]]+"0"+S[queries[i]+1:]

#         count = 0
#         for j in range(N-1):
#                 if S[j]+S[j+1] in ['10', '01']:
#                     count +=1
#         results.append(count)   
#         for i in results:
#             print(i) 

# def count_groups(documents):
#     tata = True
#     data = 0
#     import pdb;pdb.set_trace()
#     for i in range(len(documents)-1):
#         if documents[i] == documents[i+1] :
#             data+=1
#             tata = False
#         elif documents[i] != documents[i+1] :
#             tata = True
#     if data == 1:
#         data+=1
#         return data
#     if data == 0:
#         return 1
#     return data

# documents = [4,1,1,2,2] #out put 2
# documents = [987,650,239,987,650] #get out 1
# documents = [1,1,2,3,5,9] # get 1

# groups = count_groups(documents)
# print("output :", groups)

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for user,status in users.copy().items():
#     if status=="inactive":
#         del users[user]
        
# print(users)

# active_user={}
# for user,status in users.copy().items():
#     if status=='active':
#         active_user[user]=status
# print(active_user)

# l1=[6372,3232,2121,3131,212,121,3233]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1)
# left=0
# right=len(l1)-1
# while left<right:
#     l1[left],l1[right]=l1[right],l1[left]
#     left+=1
#     right-=1
# print(l1)

# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]<l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1)

# l1=[10,20,30,40,50,60]
# for i in range(0,len(l1)):
#     print(l1[i])
    
# l1=["hello",'run',100,200,300,400,1000]
# for i in range(0,len(l1),2):
#     print(l1[i])
    
# l2=["my","name","is","shri",1000,2000,3000,4000]
# for i in range(-(len(l2)),-8,1):
#     print(l1[i])
# l1=[]   
# for i in range(-10,-100,-20):
#     l1.append(i)
# print(l1)

# l1=["mary","had","a","little","lamb"]
# for i in range(len(l1)):
#     print(i,l1[i])
    
# sum=0
# for i in range(0,20):
#     print(i)
#     sum+=i
# print(sum)

# for n in range(2,100):
#     for j in range(2,n):
#         if n%2==0:
#             print(n,"equals",j,"x",n//j)
#             break
#     else:
#         print(n,"is prime numbers")
        
# for i in range(0,10):
#     if i%2==0:
#         print("this is even number")
#         continue
#     else:
#         print("this is odd numbers")
        
# for i in range(0,10):
#     if i%2==0:
#         break
#     print(i)


# def func(n):
#     a,b=0,1
#     while a<n:
#         a,b=b,a+b
#         print(a,end=",")
# print(func(2000))


# a='1111111'
# b='1111111'
# print(list(zip(set(a),set(b)))[0][1])

# def func2(N):
#     result=[]
#     a,b=0,1
#     while a<N:
#         a,b=b,a+b
#         result.append(a)
#     return result
# print(func2(2000))

# while True:
#     user_input = input("Enter 'q' to quit: ")
#     if user_input == 'q':
#         break  # Exit the loop if the user enters 'q'
#     else:
#         print("You entered:", user_input)


# def is_power_of_two(item):
#     import pdb;pdb.set_trace()
#     if item <= 0:
#         return False
#     return (item & (item - 1)) == 0

# # Input a number to check
# number = int(input("Enter a number: "))

# if is_power_of_two(number):
#     print(f"{number} is a power of two: True")
# else:
#     print(f"{number} is a power of two: False")

   
# aa = ['aannnff','dgsga','gdgasdg','trrres','zzzz']
# aa.sort(key=len)
# print(aa)

# def isUgly(self, n: int) -> bool:
#         if n<=0:
#             return False
#         while n%2==0 :
#             n//=2
#         while n%3==0:
#             n//=3
#         while n%5==0 :
#             n//=5
#         return n==1
# isUgly()