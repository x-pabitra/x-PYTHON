d={
    'course':'python',
    'fees':8000,
    'duration':'2 months'
}
c=d.get('course')
print(c)



for a in d.keys():
    print(a)
for a in d.values():
    print(a)





for a,b in d .items():
    print(a,b)




del d['fees']
print(d)
 


print(d.pop('duration'))
print(d)