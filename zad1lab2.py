import re
from collections import Counter

STOP_WORDS = set([
    "i", "a", "the", "to", "w", "of", "or", "but", "it",
    "is", "are", "that", "this", "as", "by", "for", "not", "be", "he",
    "she", "they", "we", "you", "me", "him", "them", "my", "his",
    "her", "their", "our", "its", "an", "at", "on", "in", "with"
])

def analyze_text(text):
    paragraphs = text.split('\n')
    num_paragraphs = len([p for p in paragraphs if p.strip() != ""])
    sentences = re.split(r'[.!?]+', text)
    num_sentences = len([s for s in sentences if s.strip() != ""])
    words = re.findall(r'\b\w+\b', text.lower())
    num_words = len(words)

    filtered_words = [word for word in words if word not in STOP_WORDS]
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(10)

    def reverse_if_a(word):
        return word[::-1] if word.startswith('a') or word.startswith('A') else None

    transformed_words = list(filter(None, map(reverse_if_a, words)))

    return {
        "num_words": num_words,
        "num_sentences": num_sentences,
        "num_paragraphs": num_paragraphs,
        "most_common_words": most_common_words,
        "transformed_words": transformed_words
    }

text = """
Suppose that you were sitting down at this table. The napkins are in front of you, which napkin would you take?
The one on your ‘left’? Or the one on your ‘right’? 
The one on your  left  side? Or the  one on your  right side?
Usually you would take the one on your left side.
That is ‘correct’ too. But in a larger sense on society, that is wrong.
Perhaps I could even substitute ‘society’ with the ‘Universe’.
The correct answer is that ‘It is determined by the one who takes his or her own napkin first.’
...Yes?
If the first one takes the napkin to their right, then there’s no choice but for others to also take the ‘right’ napkin.
The same goes for the left. Everyone else will take the napkin to their left, because they have no other option.
This is ‘society’...
Who are the ones that determine the price of land first?
There must have been someone who determined the value of money, first.
The size of the rails on a train track? The magnitude of electricity? Laws and Regulations?
Who was the first to determine these things?
Did we all do it, because this is a Republic? Or was it Arbitrary?
NO!
The one who took the napkin first determined all of these things!
The rules of this world are determined by that same principle of ‘right or left?’!
In a Society like this table, a state of equilibrium, once one makes the first move, everyone must follow!
In every era, this World has been operating by this napkin principle.
And the one who ‘takes the napkin first’ must be someone who is respected by all.
It’s not that anyone can fulfill this role... Those that are despotic or unworthy will be scorned. And those are the ‘losers’.
In the case of this table, the ‘eldest’ or the ‘Master of the party’ will take the napkin first... Because everyone ‘respects’ those individuals.
"""

result = analyze_text(text)
print("Liczba słów:", result["num_words"])
print("Liczba zdań:", result["num_sentences"])
print("Liczba akapitów:", result["num_paragraphs"])
print("Najczęściej występujące słowa:", result["most_common_words"])
print("Przekształcone słowa:", result["transformed_words"])
