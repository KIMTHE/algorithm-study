
import sys
input = sys.stdin.readline

class unit:
	def __init__(self,num,si):
		self.num = num
		self.si = si
		self.ei = 0
		self.leng = 0

st,paint = input().split()
paint = int(paint)

num_unit = [[] for _ in range(10)]

now_check = 0
for i in range(len(st)):
	if now_check == 1 and st[i-1] != st[i]:
		tmp.ei = i-1
		tmp.leng = tmp.ei-tmp.si+1
		num_unit[num-1].append(tmp)
		now_check = 0
	
	if now_check == 0:
		num = int(st[i])
		tmp = unit(num,i)
		now_check = 1
		
if now_check == 1:
		tmp.ei = i
		tmp.leng = tmp.ei-tmp.si+1
		num_unit[num-1].append(tmp)
		now_check = 0

most_len = 0
tmp_len = 0

for i in range(10):
	tmp_pa = paint
	if len(num_unit[i]) >= 1:
		tmp_len =  num_unit[i][0].leng
	for j in range(len(num_unit[i])-1):
		if (num_unit[i][j+1].si-num_unit[i][j].ei-1) <= tmp_pa:
			tmp_pa -= (num_unit[i][j+1].si-num_unit[i][j].ei+1)
			tmp_len += num_unit[i][j+1].leng + (num_unit[i][j+1].si-num_unit[i][j].ei+1)
		else:
			if tmp_len > most_len :most_len = tmp_len
			tmp_len =  num_unit[i][j+1].leng
	if tmp_len > most_len : most_len = tmp_len
	
print(most_len)