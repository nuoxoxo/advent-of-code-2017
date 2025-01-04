test=1
import re
def getlens(s): return list(map(int,(re.findall(r'\d+', s))))

lens = getlens( open(0).read().strip() )
nums = list(range(256))
if test==1:
    nums = list(range(5))
    lens = getlens('3, 4, 1, 5')
skp = 0
cur = 0
N = len(nums)
assert not any([_ > N for _ in lens])
for ln in lens:
    assert ln
    idx,rev = [],[]
    count = 0
    currpos = nums[cur]
    while count < ln:
        idx.append((currpos + count) % N)
        rev.append(nums[(currpos+count)%N])
        count += 1
    rev = rev[::-1]
    print('nms/',nums)
    print('idx/',idx)
    print('rev/',rev)
    for I,i, in enumerate(idx):
        print('\ti/',i,I)
        nums[I] = rev[i]
    cur = (cur + ln + skp) % N
    skp = (skp + 1) % N
    print('at/',ln,'\ntr/',nums)
