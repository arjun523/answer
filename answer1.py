#<----- Pattern 1 ------->
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
for row in range(5):
    for column in range(5):
        if(row + column >= 4):
            print("* ",end=' ')
        else:
            print("  ",end=' ')
    print()

#<----- Pattern 2 ------->
# A
# B C
# D E F
# G H I J
# K L M N O
count=0
for row in range(5):
    for column in range(5):
        if(row >= column):
            print(chr(65 + count),end='  ')
            count += 1
        else:
            print("  ",end=' ')
    print()
    
