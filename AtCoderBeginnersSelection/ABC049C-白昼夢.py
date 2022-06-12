import itertools

st = str(input())
st_tmp = st
arr = ['dreamer','dream','erase','eraser']
leng = len(st)

arr = list(itertools.permutations(arr))
for tmp in arr:
    st_tmp = st
    for tmp2 in tmp:
        if tmp2 in st_tmp:
            st_tmp = st_tmp.replace(tmp2,'')
    if len(st_tmp) == 0:
        leng = len(st_tmp)


if leng == 0:
    print("YES")
else:
    print("NO")