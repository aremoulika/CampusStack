import collections
from datetime import date
from typing import Collection
import smtplib
import random
from unicodedata import name

from flask import Flask, render_template, request, session, redirect
from pymongo import MongoClient


dbClient = MongoClient('mongodb://localhost:27017/')
db = dbClient['stackypane']
c = db['question']

db = dbClient['stackypane']
d = db['register']

db = dbClient['stackypane']
e = db['answer']

f = db['admin']

app = Flask('name')

app.secret_key = '901101'


@app.route('/')
def preloader():
    return render_template('preloader.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/developer')
def developer():
    return render_template('developer.html')


@app.route('/myprofile')
def myprofile():
    return render_template('profile.html')


@app.route('/main')
def main():
  result = d.find()
  data = []
  for i in result:
    data.append(i)
    result = c.find()
    result1 = e.find()
    data = list(result)
    x = list(result1)
    details = d.find_one({'email': i['email']})
    session['name'] = details['name']
    b = 0
    x = []
    finalBox = []
            # print('Moulika',data)
    for a in data:
        dummy1 = []
        dummy1.append(a['name'])
        dummy1.append(a['question'])
        dummy1.append(str(a['_id']))
                # print(a['_id'])
        x = list(e.find())
                # print('Are',x)
        answersBox = []
        for b in x:
                    # print(b,'qid',b['qid'],len(b['qid']),'_id',a['_id'],len(str(a['_id'])))
            if (b['qid'] == str(a['_id'])):
                        # print('hi')
                abc = []
                abc.append(b['name'])
                abc.append(b['answers'])
                        # print(answersBox)
                answersBox.append(abc)
                # print(dummy)
        dummy1.append(answersBox)
        finalBox.append(dummy1)
    print(finalBox)
  return render_template('main.html', fb=reversed(finalBox), c=reversed(data), name=session['name'])

@app.route('/', methods=['post', 'get'])
def getdata():
    result = c.find()
    for i in result:
        data = []
        result = c.find()
        result1 = e.find()

        data = list(result)
        x = list(result1)
        details = d.find_one({'email': i['email']})
        session['name'] = details['name']
        b = 0
        x = []
        finalBox = []
        # print('Moulika',data)
        for a in data:
            dummy1 = []
            dummy1.append(a['name'])
            dummy1.append(a['question'])
            dummy1.append(str(a['_id']))
            # print(a['_id'])
            x = list(e.find())
            # print('Are',x)
            dummy = []
            answersBox = []
            for b in x:
                # print(b,'qid',b['qid'],len(b['qid']),'_id',a['_id'],len(str(a['_id'])))
                if (b['qid'] == str(a['_id'])):
                    # print('hi')
                    abc = []
                    abc.append(b['name'])
                    abc.append(b['answers'])
                    # print(answersBox)
                    answersBox.append(abc)
                # print(dummy)
                    dummy1.append(answersBox)
                    finalBox.append(dummy1)
                    print(finalBox)
        return render_template('1.html', fb=reversed(finalBox), c=reversed(data), name=session['name'])


@app.route('/reg')
def regi():
    return render_template('register.html')

@app.route('/login')
def log():
    return render_template('login.html')

@app.route('/log', methods=['POST', 'GET'])
def login1():
    email = request.form['email']
    psw = request.form['psw']
    result = d.find()
    flag = 0
    for i in result:
        if (i['email'] == email and i['psw'] == psw):
            flag = 1
            data = []
            result = c.find()
            result1 = e.find()
            data = list(result)
            x = list(result1)
            details = d.find_one({'email': i['email']})
            session['name'] = details['name']
            b = 0
            x = []
            finalBox = []
            # print('Moulika',data)
            for a in data:
                dummy1 = []
                dummy1.append(a['name'])
                dummy1.append(a['question'])
                dummy1.append(str(a['_id']))
                # print(a['_id'])
                x = list(e.find())
                # print('Are',x)
                dummy = []
                answersBox = []
                for b in x:
                    # print(b,'qid',b['qid'],len(b['qid']),'_id',a['_id'],len(str(a['_id'])))
                    if (b['qid'] == str(a['_id'])):
                        # print('hi')
                        abc = []
                        abc.append(b['name'])
                        abc.append(b['answers'])
                        # print(answersBox)
                        answersBox.append(abc)
                # print(dummy)
                dummy1.append(answersBox)
                finalBox.append(dummy1)
            #print(finalBox)
    return render_template('1.html', fb=reversed(finalBox), c=reversed(data), name=session['name'])

@app.route('/feedback')
def feddback():
    return render_template('feedback.html')


@app.route('/logout')
def logout():
    result = c.find()
    data = []
    for i in result:
        data.append(i)
    return render_template('main.html', c=reversed(data))


@app.route('/post', methods=['post'])
def post():
    question = request.form['question']
    name = session['name']
    result=d.find()
    c.insert_one({
        'name': name,
        'question': question,
        'dislikes': 0,
        'likes': 0
    })
    data = []
    result = c.find()
    for i in result:
         data.append(i)
         result1 = e.find()
         data = list(result)
         x = list(result1)
         b = 0
         x = []
         finalBox = []
    # print('Moulika',data)
         for a in data:
          dummy1 = []
          dummy1.append(a['name'])
          dummy1.append(a['question'])
          dummy1.append(str(a['_id']))
            # print(a['_id'])
          x = list(e.find())
            # print('Are',x)
          answersBox = []
          for b in x:
            # print(b,'qid',b['qid'],len(b['qid']),'_id',a['_id'],len(str(a['_id'])))
            if (b['qid'] == str(a['_id'])):
                # print('hi')
                abc = []
                abc.append(b['name'])
                abc.append(b['answers'])
                # print(answersBox)
                answersBox.append(abc)
                # print(dummy)
          dummy1.append(answersBox)
          finalBox.append(dummy1)
         #print(finalBox)
    return render_template('1.html', fb=reversed(finalBox), c=reversed(data), name=session['name'])


@app.route('/regi', methods=['POST', 'GET'])
def registration():
    name = request.form['name']
    email = request.form['email']
    psw = request.form['psw']
    phno = request.form['phno']
    k = {}
    k['name'] = name
    k['email'] = email
    k['psw'] = psw
    k['phno'] = phno
    result = d.find()
    flag = 0
    for i in result:
        if ((i['email'] == email) and (i['psw'] == psw)):
            flag = 1
            result = c.find()
            data = []
            for i in result:
                data.append(i)
                result1 = e.find()
            data = list(result)
            x = list(result1)
            b = 0
            x = []
            finalBox = []
    # print('Moulika',data)
            for a in data:
                dummy1 = []
            dummy1.append(a['name'])
            dummy1.append(a['question'])
            dummy1.append(str(a['_id']))
            # print(a['_id'])
            x = list(e.find())
            # print('Are',x)
            answersBox = []
            for b in x:
            # print(b,'qid',b['qid'],len(b['qid']),'_id',a['_id'],len(str(a['_id'])))
                if (b['qid'] == str(a['_id'])):
                # print('hi')
                 abc = []
                 abc.append(b['name'])
                 abc.append(b['answers'])
                # print(answersBox)
                 answersBox.append(abc)
                # print(dummy)
                 dummy1.append(answersBox)
                 finalBox.append(dummy1)
                #print(finalBox)
    return render_template('1.html', fb=reversed(finalBox), c=reversed(data), name=session['name'])
    if (flag == 0):
        d.insert_one(k)
        return render_template('main.html', result='Registration Successfull')
    else:
        return render_template('main.html', result='Registration Failed')





@app.route('/', methods=['post', 'get'])
def getdata1():
    result = c.find()
    for i in result:
        data = []
        result = c.find()
        result1 = e.find()

        data = list(result)
        x = list(result1)
        details = d.find_one({'email': i['email']})
        session['name'] = details['name']
        b = 0
        x = []
        finalBox = []
        # print('Moulika',data)
        for a in data:
            dummy1 = []
            dummy1.append(a['name'])
            dummy1.append(a['question'])
            dummy1.append(str(a['_id']))
            # print(a['_id'])
            x = list(e.find())
            # print('Are',x)
            dummy = []
            answersBox = []
            for b in x:
                # print(b,'qid',b['qid'],len(b['qid']),'_id',a['_id'],len(str(a['_id'])))
                if (b['qid'] == str(a['_id'])):
                    # print('hi')
                    abc = []
                    abc.append(b['name'])
                    abc.append(b['answers'])
                    # print(answersBox)
                    answersBox.append(abc)
                # print(dummy)
                    dummy1.append(answersBox)
                    finalBox.append(dummy1)
                    print(finalBox)
                return render_template('1.html', fb=reversed(finalBox), c=reversed(data), name=session['name'])


@app.route('/collect', methods=['post', 'get'])
def collect():
    question = request.form['question']
    k = {}
    k['question'] = question
    c.insert_one(k)
    for i in result:
      result = c.find()
    
      result = c.find()
      result1 = e.find()
      data = list(result)
      x = list(result1)
      details = d.find_one({'email': i['email']})
      session['name'] = details['name']
      b = 0
      x = []
      finalBox = []
    # print('Moulika',data)
      for a in data:
        dummy1 = []
        dummy1.append(a['name'])
        dummy1.append(a['question'])
        dummy1.append(str(a['_id']))
        # print(a['_id'])
        x = list(e.find())
        # print('Are',x)
        dummy = []
        answersBox = []
        for b in x:
            # print(b,'qid',b['qid'],len(b['qid']),'_id',a['_id'],len(str(a['_id'])))
            if (b['qid'] == str(a['_id'])):
                # print('hi')
                abc = []
                abc.append(b['name'])
                abc.append(b['answers'])
                # print(answersBox)
                answersBox.append(abc)
                # print(dummy)
                dummy1.append(answersBox)
                finalBox.append(dummy1)
                print(finalBox)
        return render_template('1.html', fb=reversed(finalBox), c=reversed(data), name=session['name'])


@app.route('/answer/<id>', methods=['post', 'get'])
def answer(id):
    answers = request.form['answers']
    name = session['name']
    print(answers)
    e.insert_one({
        'name': name,
        'qid': id,
        'answers': answers,
        'dislikes': 0,
        'likes': 0
    })
    result = c.find()
    data = []
    for i in result:
        data.append(i)
        b = 0
        x = []
        finalBox = []
        # print('Moulika',data)
        for a in data:
            dummy1 = []
            dummy1.append(a['name'])
            dummy1.append(a['question'])
            dummy1.append(str(a['_id']))
            # print(a['_id'])
            x = list(e.find())
            # print('Are',x)
            dummy = []
            answersBox = []
            for b in x:
                # print(b,'qid',b['qid'],len(b['qid']),'_id',a['_id'],len(str(a['_id'])))
                if (b['qid'] == str(a['_id'])):
                    # print('hi')
                    abc = []
                    abc.append(b['name'])
                    abc.append(b['answers'])
                    # print(answersBox)
                    answersBox.append(abc)
                # print(dummy)
            dummy1.append(answersBox)
            finalBox.append(dummy1)
        print(finalBox)
    return render_template('1.html', fb=reversed(finalBox), c=reversed(data), name=session['name'])


@app.route('/guidelines')
def guidelines():
    return render_template('guidelines.html')

@app.route('/submit',methods=['POST','GET'])
def collectdata():
    choice=request.form['choice']
    res=request.form['res']
    sug=request.form['sug']
    k={}
    k['choice']=choice
    k['res']=res
    k['sug']=sug
    c.insert_one(k)
    return render_template('abc.html',choice=k['choice'],res=k['res'],sug=k['sug'])

@app.route('/login',methods=['POST','GET'])
def login():
    email=request.form['email']
    psw=request.form['psw']
    result=f.find()
    flag=0
    for i in result:
        if (i['email']==email and i['psw']==psw):
            flag=1
            return render_template('abc.html')
    if(flag==0):
        return render_template('alert.html')


if __name__ == "__main__":
    app.run(debug=True)
