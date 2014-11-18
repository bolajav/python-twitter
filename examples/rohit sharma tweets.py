import twitter
api = twitter.Api()
api = twitter.Api(consumer_key='tXomawmsM47niZF8ZIhDpCmlF',
                   consumer_secret='EtgcUvCQNmn6f3LVOh9oUfnuk2iirRrre9ZNRUlVVnU2rPxX5n',
                   access_token_key='561059839-ebjXZZdysyYXbSogt9Ww17kt84l0p56lmtUDRMB7',
                   access_token_secret='vF0PR43cL2MRqDCfMJjX2ZzcpUy5gXAciGasgMtTUgUID')
search = api.GetSearch(term="Rohit Sharma", lang='en', result_type='recent', count=100, max_id='')



import re

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))',' ',tweet)
    tweet = re.sub('^(rt[\s]+)',' ',tweet)
    tweet = re.sub('(http://)',' ',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+',' ',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end



fo=open("tweets.html","w")
fo.write('<link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />')





fo.write('<table class="table-fill">')
fo.write("<table>")
fo.write('<thead>')
fo.write('<tr>')
fo.write('<th class="text-left">Username</th>')
fo.write('<th class="text-left">Time</th>')
fo.write('<th class="text-left">Tweet</th>')
fo.write('</tr>')
fo.write('</thead>')

for t in search:
	fo.write("<tr>")
	fo.write("<td>"+ t.user.screen_name+"</td>")
	fo.write("<td>"+t.created_at+"</td>")
 #Add the .encode to force encoding
	processedTweet = processTweet(t.text)
    	#print processedTweet
        fo.write("<td>"+processedTweet.encode('UTF-8','ignore')+"<td>")
	fo.write( '')
	fo.write("</tr>")
fo.write("</table>")

 
