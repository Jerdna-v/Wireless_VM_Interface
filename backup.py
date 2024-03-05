f = open("coding_qual_input.txt", "r")
codes_map={}
for code in f.readlines():
    code=code.strip().split(" ")
    codes_map[int(code[0])]=code[1]
f.close()
codes_sorted=list(codes_map.keys())
codes_sorted.sort()
level = 1
i = 1
print(codes_map.values())
while i*level <= len(codes_sorted):
    print(i*level-level)
    if i*level != len(codes_sorted):
        print(codes_map[codes_sorted[i*level]])
    else:
         print(codes_map[codes_sorted[-1]])
    level+=1
    i+=1