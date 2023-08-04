# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})', end = ' ')


# i,j = 5,5-------------- F shape using loop
for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 3:
            print('X ', end ='')
        else:
            if j <= 2:
                print('X ', end = '')
    print('\n')
