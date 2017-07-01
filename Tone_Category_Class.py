class Tone():
    def __init__(self,tone_name, score, tone_id):
        self.tone_name = tone_name
        self.score = score
        self.tone_id = tone_id
#Array of tones 
toneArray = []

class ToneCategory():
    def __init__(self, category_id, toneArray, category_name):
        self.category_id = category_id
        self.tones = toneArray
        self.category_name = category_name

toneCategoryArray = []

toneArray.append(Tone('Anger',0.80,'anger'))
toneArray.append(Tone('Happy',0.90,'happy'))
toneCategoryArray.append(ToneCategory('emotion_tone',toneArray,'Emotion Tone'))

for toneCat in toneCategoryArray:
    print toneCat.tones[1].tone_name