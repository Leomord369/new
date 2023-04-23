import collections
number_=int(input())
tedadzhanr=collections.OrderedDict()
tedadzhanr={'Horror':0, 'Romance' :0, 'Comedy':0, 'History':0 , 'Adventure' :0 , 'Action':0}
for i in range(number_):
    input_=input()
    listin=input_.split()

    for j in listin[1:]:
        tedadzhanr[j]=tedadzhanr.get(j,0)+1
tedadzhanr=sorted(tedadzhanr.items(),key=lambda x: (-x[1],x[0]))

for zhanr in tedadzhanr:
    
          print(zhanr[0],":",zhanr[1])