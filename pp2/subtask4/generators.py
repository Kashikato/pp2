# def generate_squares(n):
#     for i in range(1, n+1):
#         yield i * i
# N = int(input())
# for j in generate_squares(N):
#     print(j)

        
# def even_nums(n):
#     for i in range(0,n+1,2):
#         yield i
# N=int(input())
# print(*even_nums(N),sep=",")


# def div34(n):
#     for i in range(0,n+1):
#         if(i%3==0 and i%4==0):
#             yield i
# n=int(input())
# for j in div34(n):
#     print(j)


# def squares(a,b):
#     for i in range(a,b+1):
#         yield i*i
# a=int(input())
# b=int(input())
# for i in squares(a,b):
#     print(i)


def down(n):
    for i in range(n,-1,-1):
        yield i 
n=int(input())
for i in down(n):
    print(i)

