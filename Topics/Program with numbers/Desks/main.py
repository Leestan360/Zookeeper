# put your python code here
group_1 = int(input())
group_2 = int(input())
group_3 = int(input())

classroom_1_desks = (group_1 // 2) + (group_1 % 2)
classroom_2_desks = (group_2 // 2) + (group_2 % 2)
classroom_3_desks = (group_3 // 2) + (group_3 % 2)

total_desks = (classroom_1_desks + classroom_2_desks + classroom_3_desks)

print(total_desks)
