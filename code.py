addition_str = "2+5+10+20"
str_list = addition_str.split("+")
int_list = [int(i) for i in str_list]  # list comprehension
sum_val = 0
for j in int_list:
    sum_val = sum_val + j
print(sum_val)

# use for loop to the get same result as list comprehension, cant use Git#
str_list2 = addition_str.split("+")
int_list2 = []
for k in str_list2:
    int_list2.append(int(k))
sum_val2 = 0
for m in int_list2:
    sum_val2 = sum_val2 + m
print(sum_val2)