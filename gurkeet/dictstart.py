dy={'pun':'chandigarh','bihar':'patna','maharashtra':'mumbai'}
print(dy['pun'])
del dy['bihar']
print(dy)
man={'gurkeet':349,'manpreet':300,'sarbjotpabla':344,'rajdeep':307,'minakshi':256}
for k in man:
    print(k,man[k])

man['manpreetpabla']=100
print(man)
man['manpreetpabla']=400
print(man)