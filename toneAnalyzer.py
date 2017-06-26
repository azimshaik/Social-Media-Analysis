import config
import json
from watson_developer_cloud import ToneAnalyzerV3
tone_analyzer = ToneAnalyzerV3(
    username=config.username,
    password=config.password,
    version='2017-06-16')

print (json.dumps(tone_analyzer.tone(text='I hate you.'),indent=2))
