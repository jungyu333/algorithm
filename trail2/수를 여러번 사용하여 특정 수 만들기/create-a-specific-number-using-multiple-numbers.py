A, B, C = map(int, input().split())

# Please write your code here.

max_count_a = C // A
max_count_b = C // B

max_val = float('-inf')

for a in range(max_count_a + 1):
    for b in range(max_count_b + 1):
        calc = (A * a) + (B * b) 
        if calc <= C:
            max_val = max(max_val, calc)

print(max_val)