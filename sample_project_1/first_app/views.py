from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = { 'author' : "Rahim" , "age": 20 ,  'courses' : [
           { 'id' : 1 , 'name' : "python" , 'fee': 2000},
           { 'id' : 2 , 'name' : "Ruby" , 'fee': 3000},
           { 'id' : 3 , 'name' : "C Plus_Plus" , 'fee': 4000},  
    ], "value1" : 4  ,
        'value2' :  'I’m Jubaer' ,
        'value3' :  'jubaer ' ,
        'value4' :  'jubaer mahmud' ,
        'value5' :  'jubaer mahmud sarker' ,
        'value6' :  datetime.datetime.now(),
        'value7' :  '',
        'value8' :  [ {'name' : 'zayed' ,'age': 29 }, 
                       
                        {'name' : 'abul' ,'age': 17 },

                        {'name' : 'babul' ,'age': 33 },
                     ],
        'value9' : 21,
        'value10' : 123456789,
        'value11' :  ['a', 'b' ,'c' ,'d'],
        'value12' :  ['abul', 'babul' ,'cabul'],
        'value13' :  "one\ntwo\nthree\nfour",
        'value14' :  'JUBAER MAHMUD SARKER' ,
        'value15' :  'jubaermahmudsarker' ,
        'value16' :  'jubaermahmudsarker' ,
        'value17' :  'jubaer mahmud sarker' , 
        'value18' :  'jubaer Mahmud sarker' , 
        'value19' :  'jubaer  Mahmud sarker tfdyhtf tghfy ghf hgv' , 
        'value20' :  '<b>I</b> <button>love</button> <span>dogs</span>' , 
        'blog_date' : datetime.datetime(2006, 6, 1, 0, 3) , # Midnight on 1 June 2006
        'comment_date' : datetime.datetime(2006, 6, 1, 8, 0) , # 08:00 on 1 June 2006
         'var' : ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']]
    }
    return render(request , 'home.html' ,d)
