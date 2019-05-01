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

