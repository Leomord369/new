number_of_pcplayer=int(input())
finallist=[]
for body in range(number_of_pcplayer):
    pcplayer=input()
    pcplayer=pcplayer.split('.')
    index2=pcplayer[1]
    index2=index2.lower()
    index2=index2[0].upper()+index2[1:]
   
    pcplayer[1]=index2

    pcplayer=' '.join(pcplayer)
    finallist.append(pcplayer)
finallistsorted=sorted(finallist,key=lambda x: (x[0],x[2]))    
for i in finallistsorted:
    print(i)

    
 