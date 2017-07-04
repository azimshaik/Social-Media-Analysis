import config
import json
from Tone_Category_Class import ToneCategory
from watson_developer_cloud import ToneAnalyzerV3
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

print '----------------------------------------------------------'

#looping through tone_categories
toneCatLength = len(result2['document_tone']['tone_categories'])

#print toneCatLength
i=0
while i<toneCatLength:
    #print (result2['document_tone']['tone_categories'][i])
    tonesLength = len(result2['document_tone']['tone_categories'][i]['tones'])
    j=0
    print result2['document_tone']['tone_categories'][i]['category_name']
    while j<tonesLength:
        #print (result2['document_tone']['tone_categories'][i]['tones'][j])
        print 'Tone Name: ' + result2['document_tone']['tone_categories'][i]['tones'][j]['tone_name']
        print 'Score:  ' 
        print result2['document_tone']['tone_categories'][i]['tones'][j]['score']
        j+=1
    print '----------------------------------------------------------'
    i+=1
#print (json.dumps(result2['document_tone']['tone_categories'][2]['category_id']))
# print '----------------------------------------------------------'
# print (json.dumps(result2['document_tone']['tone_categories'][2]['category_id']))
# print type(result2)

tonesArray = []

# tonesArray.append((json.dumps(tone_analyzer.tone(text='I hate you.'),indent=2)))
# tonesArray.append((json.dumps(tone_analyzer.tone(text='I love you.'),indent=2)))
# print tonesArray[1]

