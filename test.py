array_row_column = []
temp_row = []
array_row_max = []
array_row_max_index = []

max_row = 0
max_column = 0

for i in range(9):
    temp_row = list(map(int,input().split()))
    array_row_column.append(temp_row)
    
    array_row_max.append(max(temp_row))
    
    temp_row = []
    
max_row = max(*array_row_max)
max_row_index = array_row_max.index(max_row)
max_column_index = array_row_column[max_row_index].index(max_row)

print(max_row)
print(f'{max_row_index+1} {max_column_index+1}')