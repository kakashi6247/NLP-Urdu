import re
import urduhack
from urduhack.tokenization import sentence_tokenizer

def abc(text):
    sentences = sentence_tokenizer(text)
    #note that the predefined funtion returns a list, for that we have to concatinate the elements of it.
    my_string = "- ".join(sentences) + "- "
    return my_string

def urdu_sentence_segmentation(text):
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Split text into sentences based on Urdu punctuation marks
    sentences = abc(text)
    # Remove extra white spaces from each sentence
    sentences = re.sub(r'\s+', ' ', sentences)
    return sentences

# Example text
text_example = "بے چاری عوام چونکہ ہمیشہ سے دھوکہ کھانے کی عادی رہی ہے اس لئے ‘‘تبدیلی سرکار’’ کی چکنی چپڑی باتوں میں آگئی اور اپنے بہتر مستقبل کے لئے نئی حکومت کو اقتدار کے ایوانوں تک پہنچا دیا"
# Perform sentence segmentation
segmented_sentences = urdu_sentence_segmentation(text_example)
print(segmented_sentences)

#incase you want individual words, we can for loop on segmented sentences