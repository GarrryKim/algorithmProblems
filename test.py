#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

N = int(input())

list_star = []
blank = []

for i in range(N):
    list_star.append("*" * (2*(N-i)-1))
    blank.append(" "*i)
    
for i in range(2*N-1):
    if i < N:
        print(f'{blank[N-i-1]}{list_star[N-i-1]}')
    else:
        print(f'{blank[i-N+1]}{list_star[i-N+1]}')