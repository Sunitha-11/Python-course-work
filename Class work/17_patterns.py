
'''Enter The size:12
* * * * * * * * * * * *
*                     *
*                     *
*                     *
*                     *
*                     *
* * * * * * * * * * * *
*                     *
*                     *
*                     *
*                     *
* * * * * * * * * * * *'''

n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2 or col==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  

'''Enter The size:12
* * * * * * * * * * * *
*           *         *
*           *         *
*           *         *
*           *         *
*           *         *
* * * * * * * * * * * *
*           *         *
*           *         *
*           *         *
*           *         *
* * * * * * * * * * * *'''


n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row== n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  

'''Enter The size:12
* * * * * * * * * * * *
                    *
                  *
                *
              *
            *
          *
        *
      *
    *
  *
* * * * * * * * * * * *'''

n = int(input("Enter The size:"))
for row in range(n):
    for col in range(n):
        if row==col or col+row== n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()  

'''Enter The size:14
*                         *
  *                     *
    *                 *
      *             *
        *         *
          *     *
            * *
            * *
          *     *
        *         *
      *             *
    *                 *
  *                     *
*                         *'''



# First half
for i in range(1, 5):
    print((str(i) + ' * ') * (i - 1) + str(i))

# Second half
for i in range(3, 0, -1):
    print((str(i) + ' * ') * (i - 1) + str(i))



size = 7  # Pattern size (must be odd)

for row in range(size):
    for col in range(size):
        if row == col or row + col == size - 1:
            print('.', end=' ')
        else:
            print('*', end=' ')
    print()

size = 7  # Must be odd
mid = size // 2  # Middle index

for row in range(size):
    for col in range(size):
        if col == mid:
            print('.', end=' ')
        elif row == mid:
            print('.', end=' ')
        elif col < abs(mid - row) or col >= size - abs(mid - row):
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()