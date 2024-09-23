import json
# d={
#     'course_name': 'python',
#     'fees':15000
# }

# f=json.dumps(d)
# print(type(f))
# print(f) 


# d='{"cname":"python","fees":12000,"duration":"2months"}'

# x=json.loads(d)
# print(type(x))
# print(x)
# for a in x:
#  print(a,x[a])



file=open("posts.json","r")
x=file.read()
# finaldata=json.loads(x)


# print(finaldata);


finaldata=json.loads(x)

for a in in finaldata:
    print(a['title'],a['userid'])


print(finaldata);