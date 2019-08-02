#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
import sys
import re


stopwords = ['a','an','the','and','is','are','was','were','what','them','had','some','ca',
                 'why','when','where','who','whose','which','that','off','ever','many','ve',
                 'those','this','those','but','so','thus','again','therefore','its','both',
				     'like','in','on','up','down','under','over','i','we','they','while','okay',
				     'he','them','their','there','us','of','you','your','us','our','mine','mr',
                 'such','am','to','too','for','from','since','until','between','she','own',
                 'my','not','if','as', 'well','youre','hadnt','havent','wont','q','se','ok',
                 'very','have','it','be','been','has','having','his', 'her','never','above',
                 'should','would', 'could','just', 'about','do','doing','does','did','la','ha'
                 'go','going','goes','being','with', 'yes', 'no','how','before','than','d',
                 'after','any','here','out','now','then','got','into','all','cant','or','ya',
                 'despite','beyond','further','wanna', 'want','gonna','isnt', 'at','also','lo',
                 'because','due','heres','try','said','says','will','shall','link','asked',
                 'more','less','often','lol','maybe','perhaps','quite','even','him','by','n',
                 'among','can','may','most','took','during','me','told','might','hi','es','l',
                 'theyll','use','u','whats','couldnt','wouldnt','see','im','dont','x','de',
                 'doesnt','shouldnt', 'hes','thats','let','lets','get','gets','en','co','k',
                 'whats','s','say','via','youll','wed','theyd','youd','w','m','hey','hello',
                 'youve','theyve','weve','theyd','youd','ive','were','ill','yet','b','rt','ahead','exist','happen','called','needed',
                 'id','o','r','z','um','em','seen','didnt','r','e','t','c','y','only','v',
                 'arent','werent','hasnt','mostly','much','ago','wasnt','aint','nope','p',
                 'll','ja','al','el','gt','cs','si','didn','re','f','fo','j','ni','tr','il','make','made','st','1','2'
                 ,'3','4','5','6','7','8','9','0']
stopwords_2 = ["a","about","above","after","again","against","ain","all","am","an","and","any","are","aren","aren't","as","at","be",
"because","been","before","being","below","between","both","but","by","can","couldn","couldn't","d","did","didn","didn't","do","does",
"doesn","doesn't","doing","don","don't","down","during","each","few","for","from","further","had","hadn","hadn't","has","hasn","hasn't",
"have","haven","haven't","having","he","her","here","hers","herself","him","himself","his","how","i","if","in","into","is","isn","isn't",
"it","it's","its","itself","just","ll","m","ma","me","mightn","mightn't","more","most","mustn","mustn't","my","myself","needn","needn't",
"no","nor","not","now","o","of","off","on","once","only","or","other","our","ours","ourselves","out","over","own","re","s","same","shan",
"shan't","she","she's","should","should've","shouldn","shouldn't","so","some","such","t","than","that","that'll","the","their","theirs",
"them","themselves","then","there","these","they","this","those","through","to","too","under","until","up","ve","very","was","wasn",
"wasn't","we","were","weren","weren't","what","when","where","which","while","who","whom","why","will","with","won","won't","wouldn",
"wouldn't","y","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","could","he'd","he'll","he's","here's",
"how's","i'd","i'll","i'm","i've","let's","ought","she'd","she'll","that's","there's","they'd","they'll","they're","they've","we'd","we'll",
"we're","we've","what's","when's","where's","who's","why's","would","able","abst","accordance","according","accordingly","across","act",
"actually","added","adj","affected","affecting","affects","afterwards","ah","almost","alone","along","already","also","although","always",
"among","amongst","announce","another","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently",
"approximately","arent","arise","around","aside","ask","asking","auth","available","away","awfully","b","back","became","become","becomes",
"becoming","beforehand","begin","beginning","beginnings","begins","behind","believe","beside","besides","beyond","biol","brief","briefly",
"c","ca","came","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains",
"couldnt","date","different","done","downwards","due","e","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end",
"ending","enough","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far",
"ff","fifth","first","five","fix","followed","following","follows","former","formerly","forth","found","four","furthermore","g","gave",
"get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","happens","hardly","hed","hence","hereafter",
"hereby","herein","heres","hereupon","hes","hi","hid","hither","home","howbeit","however","hundred","id","ie","im","immediate","immediately",
"importance","important","inc","indeed","index","information","instead","invention","inward","itd","it'll","j","k","keep","keeps","kept",
"kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like",
"liked","likely","line","little","'ll","look","looking","looks","ltd","made","mainly","make","makes","many","may","maybe","mean","means",
"meantime","meanwhile","merely","mg","might","million","miss","ml","moreover","mostly","mr","mrs","much","mug","must","n","na","name",
"namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety",
"nobody","non","none","nonetheless","noone","normally","nos","noted","nothing","nowhere","obtain","obtained","obviously","often","oh","ok",
"okay","old","omitted","one","ones","onto","ord","others","otherwise","outside","overall","owing","p","page","pages","part","particular",
"particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present",
"previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","readily",
"really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted",
"resulting","results","right","run","said","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems",
"seen","self","selves","sent","seven","several","shall","shed","shes","show","showed","shown","showns","shows","significant","significantly",
"similar","similarly","since","six","slightly","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat",
"somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully",
"sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","thank","thanks","thanx","thats","that've","thence",
"thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","theyd",
"theyre","think","thou","though","thoughh","thousand","throug","throughout","thru","thus","til","tip","together","took","toward","towards",
"tried","tries","truly","try","trying","ts","twice","two","u","un","unfortunately","unless","unlike","unlikely","unto","upon","ups","us",
"use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","via","viz","vol","vols","vs","w","want",
"wants","wasnt","way","wed","welcome","went","werent","whatever","what'll","whats","whence","whenever","whereafter","whereas","whereby",
"wherein","wheres","whereupon","wherever","whether","whim","whither","whod","whoever","whole","who'll","whomever","whos","whose","widely",
"willing","wish","within","without","wont","words","world","wouldnt","www","x","yes","yet","youd","youre","z","zero","a's","ain't","allow",
"allows","apart","appear","appreciate","appropriate","associated","best","better","c'mon","c's","cant","changes","clearly","concerning",
"consequently","consider","considering","corresponding","course","currently","definitely","described","despite","entirely","exactly",
"example","going","greetings","hello","help","hopefully","ignored","inasmuch","indicate","indicated","indicates","inner","insofar","it'd",
"keep","keeps","novel","presumably","reasonably","second","secondly","sensible","serious","seriously","sure","t's","third","thorough",
"thoroughly","three","well","wonder"]

#Top 10 words found in twitter data
#top_words = ['golf','baseball','nba','tennis','football','game','team','tiger','play','win']
#top_words = ['game','season','players','year','team','league','time','baseball','play','woods']
#top_words = ['game','season','players','year','team','league','time','baseball','play','golf']
top_words = ['golf','women','augusta','woods','year','national','play','game','communities','week']

#The context for the co occurrence is twitter data is tweet. Each tweet is there in separate line.
for line in sys.stdin:
	line = line.strip()
	line = re.sub("<.*>|<|!|\.|@|#|\$|\*|:|%|\+|…|\\\\|\/|«|»|···|\||\•|\?|\(|\)|=|-|&|;|\_|—|~|¯|\{|\}|\[|\]|£|€|¥|¿|–", "", line)
	line = re.sub("\“|\”|\‘|\’|\"|,|'", " ", line)
	line = re.sub("[0-9]+|http[a-zA-Z0-9]+", " ", line)
	line = line.lower()
	line = re.sub(" [a-z] |aa+[a-z]* | ab | aba | abc | ac | acc | acq | az | ba | baa* | ca | czq | czt | da | daca  | ec | ed | rt | co | fx | xa | xf | xe | xb | fxa |ixe | x*", " ", line)
	line = re.sub(" amp | get | pi | marc | someon | talking | speaking | ever | done | less | fx | xa ", " ", line)
	line = line.strip()
	if(line == ''):
		continue
	words = line.split()
        temp = []
   #Remove stop words
	for word in words:
		if word not in stopwords and word not in stopwords_2:
			temp.append(word)
	words = list(filter(None, temp))
	
   #Emit co-occurance pairs if any word in the pair is part of top_words
   	for i in range(len(words)):
   		for j  in range(i+1, len(words)):
   			if words[i] == words[j]: 
   				continue
   			if words[i] in top_words or words[j] in top_words and words[j]:		
   				print ('%s\t%s' % (words[i]+','+words[j], 1))
   		
	