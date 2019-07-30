from django.http import HttpResponse
from django.shortcuts import render
import json
import operator
def home(request):
    return render(request,'home.html')
def count(request):
    with open('data.json','r') as file:
        output=json.load(file)
    print(output)
    fulltext=request.GET['fulltext']
    result={}
    tmp=set(fulltext.lower())
    try:
        tmp.remove(' ')
    except KeyError:
        pass
    for i in tmp:
        result.update({i:fulltext.lower().count(i)})
    with open('data.json','w') as file:
        json.dump(result,file)
    result=sorted(result.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'result':result})
def about(request):
    with open('pika3.txt','a') as file:
        file.write('2')
    return render(request,'about.html')
def pika(request):
    return render(request,'pika.html')
