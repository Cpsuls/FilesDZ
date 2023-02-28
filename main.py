import json
import pickle
import pandas as pd
from bs4 import BeautifulSoup
import lxml
# 1
# with open("addres-book.json", "r") as read_file:
#     data = json.load(read_file)
# lst=[data[i]['email'] for i in range(len(data))]
# print(*lst)
#2
# lst=[data[i]['phones'] for i in range(len(data))]
# print(*lst)
#3
# lst=[]
# with open('addres-book-q.xml') as f:
#     ab=BeautifulSoup(f,'xml')
# for el in ab.address_book.find_all('address'):
#     x=[x.next for x in el.phones.find_all('phone')]
#     lst.append({el.find('name').next:x})
# print(lst)



# 1.1
with open("contributors_sample.json", "r") as read_file:
    data = json.loads(read_file.read())
    # print(*data[0:3])
# 1.2
# lst=[]
# for i in range(len(data)):
#     x=data[i]['mail']
#     x=x.split('@')
#     lst.append(x[1])
# print(set(lst))
# 1.3
# def name(username):
#     for i in range(len(data)):
#         x = data[i]['username']
#         if username==x:
#             print(data[i])
#             break
#         else:
#             continue
#     else:
#         raise ValueError
# name('ashot')
# 1.4
# lstf=[data[i]['sex'] for i in range(len(data)) if data[i]['sex']=='F']
# lstm=[data[i]['sex'] for i in range(len(data)) if data[i]['sex']=='M']
# print(len(lstf))
# print(len(lstm))
# 1.5
# lst1=[]
# for i in range(len(data)):
#         lst = [[], [], []]
#         x,y,z = data[i]['username'],data[i]['id'],data[i]['sex']
#         lst[0],lst[1],lst[2]=x,y,z
#         lst1.append(lst)
# contributers=pd.DataFrame(lst1,columns=['name','id','sex'])
# # 1.6
# recipes = pd.read_csv("recipes_sample.csv",sep=',',header=0)
# recipes=pd.concat([recipes,contributers])
# recipes=recipes.dropna(subset='id')
# print(recipes)
# 2.1
# lst1={}
# lst0={}
# lst_job=[data[i]['jobs'] for i in range(len(data))]
# lst_names=[data[i]['username'] for i in range(len(data))]
# st=[data[i]['jobs'] for i in range(len(data))]
# for i in range(len(st)):
#     for j in range(len(st[i])):
#         x=[]
#         for k in range(len(data)):
#             if st[i][j] in data[k]['jobs']:
#                 x.append(data[k]['username'])
#                 lst0={st[i][j]:x}
#                 lst1.update(lst0)
# print(lst1)
# 2.2
# with open('job_people.pickle','wb') as w:
#     pickle.dump(lst1,w)
# with open('job_people.json','w') as w1:
#     json.dump(lst1,w1)
# # 2.3
# with open('job_people.pickle','rb') as r:
#     data_new=pickle.load(r)
#     print(data_new)
# 3.1
# with open('steps_sample.xml') as f:
#     ab=BeautifulSoup(f,'xml')
# res=list()
# print(ab.steps)
# for el in ab.find_all('recipe'):
#     steps=el.steps.text
#     steps=steps.split('\n')
#     res.append({el.find('id').next:steps[1:3]})
# with open('steps_sample.json','w') as w:
#     json.dump(res,w)
# # 3.2
# with open('steps_sample.xml') as f:
#     ab=BeautifulSoup(f,'xml')
# res=list()
# dtc={}
# dtc0={}
# l=[len(el.steps.text.split('\n'))-1 for el in ab.find_all('recipe')]
# x=ab.find_all('recipe')
# for j in range(len(l)):
#     lst1=[]
#     for i in range(len(x)):
#             steps = x[i].steps.text
#             steps_lght=len(steps.split('\n'))-1
#             if steps_lght==l[j]:
#                 lst1.append(x[i].find('id').next)
#     dtc0={steps_lght:lst1}
#     dtc.update(dtc0)
# print(dtc)
# 3.3
# lst=[]
# with open('steps_sample.xml') as f:
#     ab=BeautifulSoup(f,'xml')
# for el in ab.find_all('recipe'):
#     x=list(el.step.parent)
#     for el1 in x:
#         el1=str(el1)
#         if '<step has_minutes="1">' in el1:
#             lst.append(el)
# 3.4
# with open('steps_sample.xml') as f:
#     ab=BeautifulSoup(f,'xml')
# l=[len(el.steps.text.split('\n'))-1 for el in ab.find_all('recipe')]
# recipe=pd.read_csv('recipes_sample.csv')
# # print(recipe)
# recipe.n_steps = recipe.n_steps.fillna('XXXX')
# for i in range(len(recipe['n_steps'])):
#     if recipe['n_steps'][i]== 'XXXX':
#         recipe['n_steps'][i]=l[i]
# #     print(recipe['n_steps'][i])
# 3.5
# print(recipe.n_steps.isna().sum())
# recipe.n_steps=recipe.n_steps.astype(float)
# recipe=recipe.to_csv('recipes_sample_with_filled_nsteps.csv')









