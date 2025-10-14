import requests
from typing import List, Dict, Optional
import json
import os

try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # pragma: no cover
    BeautifulSoup = None  # type: ignore
    
def trustpilot_reviews(pages = 10, business_unit = 'nextdoor.com') -> List[Dict[str, object]]:
    cookies = {
        'TP.uuid': '9c93394e-0dec-4d00-956a-d97ccba70024',
    }
    all_reviews: List[Dict[str, object]] = []
    for page in range(1, pages + 1):
        if page == 1:
            url = f'https://www.trustpilot.com/review/{business_unit}'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            }
            params = {
                'stars': '1',
            }
        else:
            url = f'https://www.trustpilot.com/review/{business_unit}'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'referer': f'https://www.trustpilot.com/review/{business_unit}?stars=1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
            }
            params = {
                'page': str(page),
                'stars': '1',
            }
        response = requests.get(url, params=params, cookies=cookies, headers=headers)
        reviews_for_page = parse_reviews_from_html(response.text)
        all_reviews.extend(reviews_for_page)
    return all_reviews

def parse_reviews_from_html(html_text: str) -> List[Dict[str, object]]:
    """Extract reviews from Trustpilot HTML."""
    def _get_parser(html: str):
        if BeautifulSoup is None:
            raise RuntimeError("BeautifulSoup (bs4) is required to parse HTML. Please install with `pip install beautifulsoup4 lxml`.\n")
        try:
            return BeautifulSoup(html, 'lxml')
        except Exception:
            return BeautifulSoup(html, 'html.parser')

    def _text_or_none(node) -> Optional[str]:
        if not node:
            return None
        text = node.get_text(" ", strip=True)
        if not text:
            return None
        return text.replace('See more', '').strip() or None

    def _extract_rating(article) -> Optional[int]:
        img = article.select_one('img[alt$="stars"]')
        if img and img.has_attr('alt'):
            for token in img['alt'].split():
                if token.isdigit():
                    return int(token)
        meta = article.select_one('meta[itemprop="ratingValue"]')
        if meta and meta.has_attr('content') and meta['content'].isdigit():
            return int(meta['content'])
        star_container = article.select_one('[aria-label*="Rated "]')
        if star_container and star_container.has_attr('aria-label'):
            for token in star_container['aria-label'].split():
                if token.isdigit():
                    return int(token)
        return None

    def _extract_author(article) -> Optional[str]:
        aside = article.select_one('aside[aria-label]')
        if aside and aside.has_attr('aria-label'):
            label = aside['aria-label']
            if label.lower().startswith('info for '):
                return label[9:].strip() or None
        link = article.select_one('a[name="consumer-profile"], a[rel="nofollow"][name="consumer-profile"]')
        return _text_or_none(link)

    def _extract_title(article) -> Optional[str]:
        header = article.select_one('h2, h3')
        return _text_or_none(header)

    def _extract_date(article) -> Optional[str]:
        time_el = article.select_one('time[datetime]')
        if time_el and time_el.has_attr('datetime'):
            return time_el['datetime']
        if time_el:
            txt = _text_or_none(time_el)
            if txt:
                return txt
        span_dt = article.select_one('span[datetime]')
        if span_dt and span_dt.has_attr('datetime'):
            return span_dt['datetime']
        return None

    def _extract_text(article) -> Optional[str]:
        body_container = (
            article.select_one('[data-service-review-text-typography]')
            or article.select_one('[data-review-content]')
            or article
        )
        for sel in ['button', 'a', 'span[class*="seeMore"]']:
            for node in body_container.select(sel):
                try:
                    node.decompose()
                except Exception:
                    pass
        paragraphs = [_text_or_none(p) for p in body_container.select('p')]
        paragraphs = [p for p in paragraphs if p]
        if paragraphs:
            return ' '.join(paragraphs)
        return _text_or_none(body_container)

    soup = _get_parser(html_text)
    articles = soup.select('article[data-service-review-card-paper="true"], article[data-review-item-id]')
    results: List[Dict[str, object]] = []
    for article in articles:
        author = _extract_author(article)
        rating = _extract_rating(article)
        date = _extract_date(article)
        title = _extract_title(article)
        text = _extract_text(article)
        if not (author or rating or title or text):
            continue
        results.append({
            'author': author,
            'rating': rating,
            'date': date,
            'title': title,
            'text': text,
        })
    return results

def parse_reviews_from_next_data(json_text: str) -> List[Dict[str, object]]:
    """Extract reviews from Trustpilot Next.js data (response1.json contents)."""
    try:
        data = json.loads(json_text)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON input provided to parse_reviews_from_next_data")

    page_props = data.get('pageProps') or {}
    reviews = page_props.get('reviews') or []

    normalized: List[Dict[str, object]] = []
    for r in reviews:
        consumer = r.get('consumer') or {}
        dates = r.get('dates') or {}
        normalized.append({
            'id': r.get('id'),
            'title': r.get('title'),
            'text': r.get('text'),
            'rating': r.get('rating'),
            'likes': r.get('likes'),
            'language': r.get('language'),
            'location': r.get('location'),
            'consumer_displayName': consumer.get('displayName'),
            'consumer_countryCode': consumer.get('countryCode'),
            'consumer_numReviews': consumer.get('numberOfReviews'),
            'publishedDate': dates.get('publishedDate'),
            'experiencedDate': dates.get('experiencedDate'),
            'updatedDate': dates.get('updatedDate'),
            'source': r.get('source'),
            'isVerified': ((r.get('labels') or {}).get('verification') or {}).get('isVerified'),
        })

    return normalized

if __name__ == "__main__":
    # Fetch Next.js JSON and parse in-memory; only persist extracted results
    business_unit = 'neighbor.com'
    reviews = trustpilot_reviews(pages=20, business_unit=business_unit)
    out_path = f'reviews_{business_unit.replace(".", "_")}.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(reviews)} reviews → {out_path}")
    