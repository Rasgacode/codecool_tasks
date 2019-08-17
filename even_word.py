s = ['code', 'aaagmnrs', 'anagrams', 'doce', 'ecod', 'nagramsa']

output_list = []
for x in range(len(s)):
    for y in range(len(s)):
        if x != y and sorted(s[x]) == sorted(s[y]):
            temp = sorted([s[x], s[y]])
            if temp[0] not in output_list:
                output_list.append(temp[0])
print(sorted(output_list))


            





