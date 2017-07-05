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
length = len(result2['document_tone']['tone_categories'][0]['tones'])
print time.asctime( time.localtime(time.time()) )
print '----------------------------------------------------------'
#looping through tone_categories
toneCatLength = len(result2['document_tone']['tone_categories'])
i=0
toneCategoryArray  = []
while i<toneCatLength:
    tonesLength = len(result2['document_tone']['tone_categories'][i]['tones'])
    j=0
    category_name = result2['document_tone']['tone_categories'][i]['category_name']
    category_id = result2['document_tone']['tone_categories'][i]['category_id']
    print 'Tone Category: '+ category_name
    print '-------------------------------'
    tonesArray =  []
    while j<tonesLength:
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
tonesArray = []
