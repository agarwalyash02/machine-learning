
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

sample_text = """I loved this movie <br /><br /> since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, nudity/sexuality and some language."""

tokenizer=RegexpTokenizer(r'\w+')
en_stopwords=set(stopwords.words('english'))
ps=PorterStemmer()


def getCleanReview(review):
	review=review.lower()
	review=review.replace("<br /><br />"," ")

	tokens=tokenizer.tokenize(review)
	new_token=[token for token in tokens if token not in en_stopwords or token=='not']
	

	stemmed_tokens=[ps.stem(token) for token in new_token]
	cleaned_review= ' '.join(stemmed_tokens)

	return cleaned_review