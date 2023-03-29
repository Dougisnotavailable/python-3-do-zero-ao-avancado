
rows = 5 
columns = 5

row = 1 

while row <= rows:
    column = 1
    print(row)

    while column <= columns:
        print(f'{row=}{column=}')
        column += 1
    row += 1

print('Acabou')