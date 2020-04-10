# new column contain lenght of <tweet> column...................train['char_count'] = train['tweet'].str.len()
#=====================================================
# Average words len in each cell in particuler column
def avg_word(sentence):  
	words = sentence.split()  
	return (sum(len(word) for word in words)/len(words))


train['avg_word'] = train['tweet'].apply(lambda x: avg_word(x))
#=====================================================
# Qty of stopwords in each cell in particuler column
from nltk.corpus import stopwords
stop = stopwords.words('english')
train['stopwords'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x in stop]))
#=====================================================
# Qty of words starts with <#> in each cell in particuler column
train['hastags'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))
#=====================================================
# Qty of numeric in each cell in particuler column
train['numerics'] = train['tweet'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
#=====================================================
# remove punctuation .................. train['tweet'] = train['tweet'].str.replace('[^\w\s]','')
#=====================================================
# remove stop words:
from nltk.corpus import stopwords
stop = stopwords.words('english')
train['tweet'] = train['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
#=====================================================
# Common word removal
freq = pd.Series(' '.join(train['tweet']).split()).value_counts()[:10]
freq = list(freq.index)
train['tweet'] = train['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
#=====================================================
# Rare words removal
freq = pd.Series(' '.join(train['tweet']).split()).value_counts()[-10:]
freq = list(freq.index)
train['tweet'] = train['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
#=====================================================
# Spelling correction
from textblob import TextBlob
train['tweet'][:5].apply(lambda x: str(TextBlob(x).correct()))