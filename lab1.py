import csv
with open ('./enjoysport1.csv','r') as f:
    reader = csv.reader(f)
    data = list(reader)

for row in data:
    print (row)

aL=len(data[0])-1
h=aL*['0']
print (h)
k=0

for row in data:
    if row[-1] == 'yes':
        j=0
        for col in row:
            if col != "yes":
                if col!=h[j] and h[j]=='0':
                    h[j]=col
                elif col!=h[j] and h[j]!='0':
                    h[j]='?'
            j=j+1
    print('h',k,h)
    k=k+1
print ('h',k-1,h)
