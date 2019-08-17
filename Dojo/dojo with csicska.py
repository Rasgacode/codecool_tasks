import math

sum_square_root = 0
with open('100.txt') as text_file:
    nums = "".join(text_file.readlines()).replace("\n", ",").split(",")
for i in range(0, len(nums), 3):
    first_num = int(nums[i])
    second_num = int(nums[i + 1])
    third_num = int(nums[i + 2])
    sum_square_root += math.sqrt(first_num + second_num + third_num)
print(sum_square_root)
'''
    for a in f:
        p = ''
        for b in a:
            a_s = a.strip()
            if b != ',':
                p += b
            else:
                if a_s not in d:
                    d[a_s] = int(p)
                else:
                    d[a_s] += int(p)
                p = ''
        if a_s not in d:
            d[a_s] = int(p)
        else:
            d[a_s] += int(p)

s += math.sqrt(d['23,21,5'])
s += math.sqrt(d['342,2,5'])
s += math.sqrt(d['32,1,777'])
s += math.sqrt(d['234,645,223'])
s += math.sqrt(d['243,646,2342'])
s += math.sqrt(d['6346,3434,222'])
s += math.sqrt(d['3,6,2'])

print(s)
'''