import re, string

STOPWORDS = set("""a an the and or of for to in on at by with from is are was were be been being
this that these those i you he she it we they them his her my your our their as if then than so
not no do does did doing have has had having can will would should could may might must shall
about above after again against all am because before below between both during each few further
here how into more most off once only other out over own same some such too under until up very
what when where which who whom why""".split())

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+|www\.\S+', ' ', text)
    text = re.sub(r'[#@]\w+', ' ', text)
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = [t for t in text.split() if t not in STOPWORDS and len(t) > 1]
    return ' '.join(tokens)
