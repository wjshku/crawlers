import requests
from bs4 import BeautifulSoup
import json

def fetch_sohu_profile():
    """
    Fetch Sohu profile page HTML
    """
    cookies = {
        'SUV': '1761456502828odinqfcO',
        'reqtype': 'pc',
        'gidinf': 'x099980107ee1b829c17bac31000396b6596aefaa33b',
        '_dfp': 'tgWd/PeOqyhBKzfqD5Rx5QL5+GI0g1J11Z0srNbBlIk=',
        'clt': '1761456516',
        'cld': '20251026132836',
        't': '1761461385507',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        # 'Cookie': 'SUV=1761456502828odinqfcO; reqtype=pc; gidinf=x099980107ee1b829c17bac31000396b6596aefaa33b; _dfp=tgWd/PeOqyhBKzfqD5Rx5QL5+GI0g1J11Z0srNbBlIk=; clt=1761456516; cld=20251026132836; t=1761461385507',
    }

    response = requests.get('https://mp.sohu.com/profile?xpt=aGFvY2hpYnVueUBzb2h1LmNvbQ==', cookies=cookies, headers=headers)

    return response.text

def parse_sohu_articles(html_content: str) -> list:
    """
    Parse Sohu articles from HTML content - extract only title, description, and article_url
    """
    from sohu_article import fetch_sohu_article, parse_sohu_article_content

    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    # Find all article items
    article_items = soup.find_all('div', class_='TPLImageTextFeedItem')

    for i, item in enumerate(article_items):
        try:
            article_data = {}

            # Extract title
            title_elem = item.find('div', class_='item-text-content-title')
            article_data['title'] = title_elem.get_text(strip=True) if title_elem else "No title"

            # Extract description
            desc_elem = item.find('div', class_='item-text-content-description')
            article_data['description'] = desc_elem.get_text(strip=True) if desc_elem else "No description"

            # Extract article URL
            link_elem = item.find('a', class_='tpl-image-text-feed-item-content')
            if link_elem and link_elem.get('href'):
                article_url = link_elem['href']
                # Convert relative URLs to absolute
                if article_url.startswith('//'):
                    article_url = 'https:' + article_url
                elif article_url.startswith('/'):
                    article_url = 'https://www.sohu.com' + article_url
                article_data['article_url'] = article_url
            else:
                article_data['article_url'] = ""

            # Fetch and parse article content using sohu_article.py
            if article_data['article_url']:
                try:
                    print(f"Fetching content for article {i+1}: {article_data['title'][:50]}...")
                    article_html = fetch_sohu_article(article_data['article_url'])
                    article_content = parse_sohu_article_content(article_html)
                    article_data['content_paragraphs'] = article_content.get('content_paragraphs', [])
                except Exception as e:
                    print(f"Error fetching content for {article_data['article_url']}: {e}")
                    article_data['content_paragraphs'] = []
            else:
                article_data['content_paragraphs'] = []

            articles.append(article_data)

        except Exception as e:
            print(f"Error parsing article: {e}")
            continue

    return articles

if __name__ == "__main__":
    print("Fetching Sohu profile...")
    html = fetch_sohu_profile()

    print("Parsing articles...")
    articles = parse_sohu_articles(html)

    # Save to JSON file
    with open('sohu.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    print(f"Successfully extracted {len(articles)} articles and saved to sohu.json")

    # Print summary
    print("\n=== SOHU ARTICLES SUMMARY ===")
    for i, article in enumerate(articles[:5], 1):  # Show first 5 articles
        print(f"{i}. {article['title'][:50]}...")
        paragraphs_count = len(article.get('content_paragraphs', []))
        print(f"   📄 {paragraphs_count} paragraphs")

    if len(articles) > 5:
        print(f"... and {len(articles) - 5} more articles")