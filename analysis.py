import json
import re
from collections import Counter
from typing import List, Dict, Tuple


def load_reviews(path: str) -> List[Dict[str, object]]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def normalize_text(text: str) -> str:
    # Lowercase and normalize whitespace
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# Basic English stopwords (no external dependency)
STOPWORDS = {
    'a','an','the','and','or','but','if','then','else','when','while','of','to','for','in','on','at','by','with','from','as','is','are','was','were','be','been','being','it','its','this','that','these','those','i','you','he','she','they','we','me','him','her','them','my','your','his','their','our','ours','yours','mine','not','no','so','too','very','can','could','should','would','will','just','about','into','over','under','again','once','only','than','such','both','through','because','what','which','who','whom','where','why','how','all','any','each','few','more','most','other','some','own','same','s','t','d','ll','m','o','re','ve','y','don','doesn','didn','won','weren','couldn','shouldn','isn','aren','has','have','had','do','does','did','having','been','being','up','out','off','down','before','after','during','between','against','further','under','above','below'
}

# Domain-specific noise terms to drop
DOMAIN_STOPWORDS = {
    'nextdoor','next','door','app','site','platform','account','accounts','post','posts','posting','posted','comment','comments','moderator','moderators','lead','leads','review','reviews','reviewer','reviewers','people','person','someone','something','anything','everything','nothing','thing','things','one','two','three','u','im','ive','nd','dont','didnt','doesnt','cant','wont','ok','okay','etc','use','used','using','get','got','getting','make','made','makes','also','even','still'
}


def tokenize(text: str) -> List[str]:
    # Keep alphabetic tokens length >=3
    tokens = re.findall(r"[a-z][a-z]+", text)
    return [t for t in tokens if len(t) >= 3]


def filter_tokens(tokens: List[str]) -> List[str]:
    return [t for t in tokens if t not in STOPWORDS and t not in DOMAIN_STOPWORDS]


def count_unigrams_and_bigrams(texts: List[str]) -> Tuple[Counter, Counter]:
    unigram_counter: Counter = Counter()
    bigram_counter: Counter = Counter()
    for txt in texts:
        norm = normalize_text(txt)
        tokens = tokenize(norm)
        tokens = filter_tokens(tokens)
        if not tokens:
            continue
        unigram_counter.update(tokens)
        # bigrams of filtered tokens
        bigrams = [f"{tokens[i]} {tokens[i+1]}" for i in range(len(tokens)-1)]
        # filter bigrams that contain stopwords (already filtered tokens, but be safe)
        bigrams = [bg for bg in bigrams if all(w not in STOPWORDS and w not in DOMAIN_STOPWORDS for w in bg.split())]
        bigram_counter.update(bigrams)
    return unigram_counter, bigram_counter


def aggregate_texts(reviews: List[Dict[str, object]], max_rating: int = 2) -> List[str]:
    texts: List[str] = []
    for r in reviews:
        if not isinstance(r, dict):
            continue
        rating = r.get('rating')
        try:
            rating_value = int(rating) if rating is not None else None
        except Exception:
            rating_value = None
        # keep reviews with rating < 3 (i.e., 1 or 2)
        if rating_value is None or rating_value > max_rating:
            continue
        title = (r.get('title') or '')
        body = (r.get('text') or '')
        combined = f"{title}\n{body}".strip()
        if combined:
            texts.append(combined)
    return texts


def analyze(path: str, top_n: int = 50) -> Dict[str, object]:
    reviews = load_reviews(path)
    texts = aggregate_texts(reviews, max_rating=2)
    unigrams, bigrams = count_unigrams_and_bigrams(texts)
    top_unigrams = unigrams.most_common(top_n)
    top_bigrams = bigrams.most_common(top_n)
    return {
        'total_reviews': len(reviews),
        'filtered_reviews_lt_3': sum(1 for r in reviews if isinstance(r, dict) and isinstance(r.get('rating'), (int, float)) and r.get('rating') < 3),
        'top_unigrams': [{'term': t, 'count': c} for t, c in top_unigrams],
        'top_bigrams': [{'term': t, 'count': c} for t, c in top_bigrams],
    }


if __name__ == '__main__':
    business_unit = 'neighbor.com'
    input_path = f'reviews_{business_unit.replace(".", "_")}.json'
    results = analyze(input_path, top_n=50)
    out_path = f'analysis_{business_unit.replace(".", "_")}.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Analyzed {results['total_reviews']} reviews → {out_path}")
    # Quick preview
    print('Top 10 needs-related unigrams:')
    for item in results['top_unigrams'][:10]:
        print(f"- {item['term']}: {item['count']}")

