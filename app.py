from flask import Flask,request,render_template,redirect,url_for,session,flash
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from afinn import Afinn 
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyse',methods=['POST','GET'])
def analyse():  
    if request.method=='POST':
        text=request.form['search']
        analyser = SentimentIntensityAnalyzer()
        score = analyser.polarity_scores(text)
        afn = Afinn(emoticons=True)
        af=afn.score(text)
        
        return "<h1>{}</h1><br>\n\n<h3>VaderSentiment'{}</h3><br>\n\n<h3>Afn Ploarity score:{}<h3>".format(text,score,af)
    return redirect(url_for('home'))


#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("Overall sentiment dictionary is : ", score) 
    print("sentence was rated as ", score['neg']*100, "% Negative") 
    print("sentence was rated as ", score['neu']*100, "% Neutral") 
    print("sentence was rated as ", score['pos']*100, "% Positive") 
  
    print("Sentence Overall Rated As", end = " ") 
  
    # decide sentiment as positive, negative and neutral 
    if score['compound'] >= 0.05 : 
        print("Positive") 
  
    elif score['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral") 
  

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)