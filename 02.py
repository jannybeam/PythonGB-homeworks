num_list = [14, 122, 47, 28, 235, 2, 11, 91, 18]
result = [num_list[i] for i in range(1, len(num_list)) if num_list[i] > num_list[i - 1]]
print(result)