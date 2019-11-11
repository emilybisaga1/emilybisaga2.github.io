import json
with open('JEOPARDY_QUESTIONS1.json','r') as f:
    text = f.read()
    jeopardy=json.loads(text)
#jeopardy is alist of dics

count = 0
for questions in jeopardy:
    category=question['category']
    if category == 'HISTORY':
        count += 1
print('count=', count)
print('fraction=', count/len(jeopardy))
    
#json.loads string -> dict 
#json.dumps dict -> string

#JSON is a file format, like a word document or html document, specifically for
#exchanging data, look very close to python dictionaries( databases for
#storing info) alows to transfer dics

#type is dict
grades = {
    'einstein':90,
    'izbicki':100,
    }

result=json.dumps(grades)
grades2=json.loads(result)

# >>> result = '{"einstein": 90, "izbicki": 100}'
#could save to file, transfer file, load file on other comp to share

# from pprint import pprint, prints the dictionary in a nice wayyy 
