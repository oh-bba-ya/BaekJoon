result = []
for i in range(9):
    num = int(input())
    result.append(num)
max_result = max(result)
index_result = int(result.index(max_result))+1
print(max_result)
print(index_result)
