def sorted_to(s):
    return s[1]

a = [[2,3],
     [1,2],
     [3,1]]


print(sorted(a, key = sorted_to))
