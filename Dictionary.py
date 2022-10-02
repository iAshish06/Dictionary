import json
import difflib  #python library to compare text
from difflib import SequenceMatcher as sm   #For comparing text in case of user enter wrong text
from difflib import get_close_matches as gcm 

data_file=open('data.json')
data1 = json.load(data_file)    #Loading Json file and it can be written as data=json.load(open(filepath.json)) as well
def translate(word):    #Translation
    word=word.lower()      #Since Dictionary contains words in only lower format so we have to transform user input in lower case as well
    if word in data1:
        return data1[word]
    elif len(gcm(word,data1.keys()))>0:
        yn=input('Did you mean %s instead? Enter Y if yes or N if no' % gcm(word,data1.keys())[0])      # if user mistakenly entred wrong word
        if yn =='Y':
            return data1[gcm(word,data1.keys())[0]]     #If yes then print the meaning of right word
        elif yn=='N':
            return ('Word not found')
        else:
            return('We did not understood your query. Try again.')
    else:
        return ('word not found')   #If word not found 
    

word = input('Enter word: ')
output = translate(word)
if output == list:
    for item in output:     #For loop to get output without commas and brackets as it is stored in json file like that
        print(item)
else:
    print(output)
