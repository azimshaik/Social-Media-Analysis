# Social-Media-Analysis
## Getting Data from Twitter API
Install python package twython
```python
pip install twython
```
Working with Twitter API
1. https://dev.twitter.com/overview/api
2. Tools & Support -> My apps
3. Create New App
   
![alt text](https://github.com/azimshaik/Social-Media-Analysis/blob/master/Create%20App.png "Logo Title Text 1")
4. Open the App -> Keys and Access Tokens, copy and paste API Key and API Secret into code

Execute the code
```python
python twitterdata.py
```
Saving Data in to a file
```python
python twitterdata.py > tweets.txt
```
------------------------------------------------
## Watson Developer Cloud
Install watson-developer cloud package
```python
pip install --upgrade watson-developer-cloud
```
or 
```python 
easy_install watson-developer-cloud
```
Emotion Tones:
	1.Anger
	2.Disgust
	3.Fear
	4.Joy
	5.Sadness
Language Tones:
	1.Analytical
	2.Confident
	3.Tenatative
Social Tones:
	1.Openness
	2.Conscientiousness
	3.Extraversion
	4.Agreeableness
	5.Emotional Range 
