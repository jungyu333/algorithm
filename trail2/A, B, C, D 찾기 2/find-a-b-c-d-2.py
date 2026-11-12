nums = list(map(int, input().split()))

# Please write your code here.

def calc(a, b, c, d):

    return [a, b, c, d, a + b, b + c, c + d, d + a, a + c, b + d, a + b + c, a + b + d, a + c + d, b + c + d, a + b + c + d]

for i in range(1, 41):
    for j in range(i, 41):
        for k in range(j, 41):
            for l in range(k, 41):

                calc_list = calc(i, j ,k ,l)

                if sorted(calc_list) == sorted(nums):
                    print(i, j, k, l)
                