import config
import json
from Tone_Category_Class import ToneCategory
from Tone_Category_Class import Tone
from watson_developer_cloud import ToneAnalyzerV3
import time
tone_analyzer = ToneAnalyzerV3(
    username=config.username,
    password=config.password,
    version='2017-06-16')

result =  (json.dumps(tone_analyzer.tone(text='I hate you.'),indent=2))

result2 = tone_analyzer.tone(text='I hate you.')


# for dump in (json.dumps(result2['document_tone']['tone_categories'])):
#     print dump
#print (json.dumps(result2['document_tone']['tone_categories'][0]['category_id']))
#print (json.dumps(result2['document_tone']['tone_categories'][0]['tones']))
length = len(result2['document_tone']['tone_categories'][0]['tones'])
#print length
i=0
# while i<length:
#     #print (json.dumps(result2['document_tone']['tone_categories'][0]['tones'][i]))
#     i+=1
print time.asctime( time.localtime(time.time()) )
print '----------------------------------------------------------'

#looping through tone_categories
toneCatLength = len(result2['document_tone']['tone_categories'])


#print toneCatLength
i=0
toneCategoryArray  = []
while i<toneCatLength:
    #print (result2['document_tone']['tone_categories'][i])
    tonesLength = len(result2['document_tone']['tone_categories'][i]['tones'])
    j=0
    category_name = result2['document_tone']['tone_categories'][i]['category_name']
    category_id = result2['document_tone']['tone_categories'][i]['category_id']
    print 'Tone Category: '+ category_name
    print '-------------------------------'
    tonesArray =  []
    while j<tonesLength:
        #print (result2['document_tone']['tone_categories'][i]['tones'][j])
        tone_Name =  result2['document_tone']['tone_categories'][i]['tones'][j]['tone_name']
        score = result2['document_tone']['tone_categories'][i]['tones'][j]['score']
        tone_Id = result2['document_tone']['tone_categories'][i]['tones'][j]['tone_id']
        print 'Tone Name: ' + tone_Name
        print 'Score%:  ' 
        print score*100
        tone = Tone(tone_Name, score, tone_Id)
        j+=1
        tonesArray.append(tone)
    print '----------------------------------------------------------'
    toneCategory = ToneCategory(category_id,tonesArray, category_name)
    i+=1
    toneCategoryArray.append(toneCategory)

print type(toneCategoryArray[0].category_id)
#print (json.dumps(result2['document_tone']['tone_categories'][2]['category_id']))
# print '----------------------------------------------------------'
# print (json.dumps(result2['document_tone']['tone_categories'][2]['category_id']))
# print type(result2)

tonesArray = []

# tonesArray.append((json.dumps(tone_analyzer.tone(text='I hate you.'),indent=2)))
# tonesArray.append((json.dumps(tone_analyzer.tone(text='I love you.'),indent=2)))
# print tonesArray[1]

