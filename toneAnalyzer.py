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
print (json.dumps(result2['document_tone']['tone_categories'][0]['category_id']))
#print (json.dumps(result2['document_tone']['tone_categories'][0]['tones']))
length = len(result2['document_tone']['tone_categories'][0]['tones'])
#print length
i=0
while i<length:
    print (json.dumps(result2['document_tone']['tone_categories'][0]['tones'][i]))
    i+=1

print '----------------------------------------------------------'
# print (json.dumps(result2['document_tone']['tone_categories'][1]['category_id']))
# print '----------------------------------------------------------'
# print (json.dumps(result2['document_tone']['tone_categories'][2]['category_id']))
# print type(result2)

tonesArray = []

# tonesArray.append((json.dumps(tone_analyzer.tone(text='I hate you.'),indent=2)))
# tonesArray.append((json.dumps(tone_analyzer.tone(text='I love you.'),indent=2)))
# print tonesArray[1]

