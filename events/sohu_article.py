import requests
from bs4 import BeautifulSoup
import json

def fetch_sohu_article(article_url: str) -> str:
    """
    Fetch a single Sohu article page
    """
    cookies = {
        'SUV': '1761456502828odinqfcO',
        'reqtype': 'pc',
        'gidinf': 'x099980107ee1b829c17bac31000396b6596aefaa33b',
        '_dfp': 'tgWd/PeOqyhBKzfqD5Rx5QL5+GI0g1J11Z0srNbBlIk=',
        'clt': '1761456516',
        'cld': '20251026132836',
        '_ga': 'GA1.1.756759890.1761461989',
        '_ym_uid': '1761461990920399414',
        '_ym_uid_cst': 'zix7LPQsHA%3D%3D',
        '_cc_id': '9ccebdcd04973499e4ffd47406309e91',
        'panoramaId_expiry': '1761548407198',
        'panoramaId': 'a0408cbadb6da78f052abedc26cfa9fb927a4cbe50c9effc7ea75cad68ba59f4',
        'panoramaIdType': 'panoDevice',
        't': '1761463759249',
        '_ga_DFBWYFE6Q0': 'GS2.1.s1761461988$o1$g1$t1761463884$j58$l0$h0',
        'cto_bundle': 'cQrn-l9LblkxYmVSJTJCSVdxZ0N2c3pOeWFxU0ptZ2tZZlZZaXl6WnlDWldhZEVWQlF4SUtMVEwweldBYTlMcVRYeGtpS2tNaXRNaHV2dW5USDdVVDFwZ2Q1MjklMkZmcDV1aWR3aWd0ZnVwMXRtTmJDOXd2MjN5c2MxSVkzbW5jYnY5VFZzM0ZHNjUyelhrTzN2TlVBaTB1cDJreGFVMUVCZGdVNHBleURYdVBUV3IyM21nJTNE',
        'cto_bidid': 'h31tIF9hR05xa0UlMkJVb21NdHFIRWdtM3Z4WU1NWFZVaFFHMFdtZkRjaTVFZFdPVDY0JTJGVEVTaTAzUTNXWjZIanJObFc4UGpXeURKWEtXRDlvYTlWT1olMkJZSEZQcTJWY3N3YXcwYVo5V3BLMjZGMWolMkJGVlZqT2NxbU9PekRTUko3M3g5amw4',
        'FCNEC': '%5B%5B%22AKsRol8Li6892--LLWORbIkjImiVqaiEyzYgicIztVjFp8zEU-rUpuce6JRX3CSlGAghoPmN9wtJPBfZo2orHy7n-xN4pbIKKieKGhR_BGxVdIUPHgInSFgsIuzI2s8i1soG-8_aZhrzJ1UFdL2mvTubi1tJRSYe8A%3D%3D%22%5D%5D',
        '__gads': 'ID=e7718b719532a4af:T=1761461966:RT=1761465875:S=ALNI_MZnvEPFpF7W9Y5vH7QYiA191rJ8aQ',
        '__gpi': 'UID=000011a97a2471ad:T=1761461966:RT=1761465875:S=ALNI_MZ5x5IgkO3pzg1A7WnsNP9BPOsGMw',
        '__eoi': 'ID=b8f9bf5436920a17:T=1761461966:RT=1761465875:S=AA-AfjaOMzR33r0eD0tTuWx1aT7r',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://mp.sohu.com/profile?xpt=aGFvY2hpYnVueUBzb2h1LmNvbQ==',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    response = requests.get(article_url, cookies=cookies, headers=headers)
    return response.text

def parse_sohu_article_content(html_content: str) -> dict:
    """
    Parse article content from Sohu article HTML
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    article_data = {}

    # Extract title from meta tag or og:title
    title_meta = soup.find('meta', property='og:title')
    if title_meta and title_meta.get('content'):
        article_data['title'] = title_meta['content']
    else:
        title_tag = soup.find('title')
        article_data['title'] = title_tag.get_text(strip=True) if title_tag else "No title"

    # Extract description from meta tag
    desc_meta = soup.find('meta', {'name': 'description'})
    if desc_meta and desc_meta.get('content'):
        article_data['description'] = desc_meta['content']
    else:
        og_desc = soup.find('meta', property='og:description')
        article_data['description'] = og_desc['content'] if og_desc and og_desc.get('content') else ""

    # Extract publish time from meta tag
    time_meta = soup.find('meta', {'name': 'datePublished'}) or soup.find('meta', property='article:published_time')
    if time_meta and time_meta.get('content'):
        article_data['publish_time'] = time_meta['content']
    else:
        # Try to find from og release date
        release_meta = soup.find('meta', property='og:release_date')
        article_data['publish_time'] = release_meta['content'] if release_meta and release_meta.get('content') else "Unknown"

    # Extract main article content
    article_element = soup.find('article', {'class': 'article', 'id': 'mp-editor'})
    content_paragraphs = []

    if article_element:
        # Extract all paragraphs and images from the article
        for element in article_element.find_all(['p', 'div']):
            # Skip non-content elements
            if element.get('class') and ('lookall' in element.get('class') or 'hidden-content' in element.get('class')):
                continue

            # Extract text from paragraphs
            if element.name == 'p':
                # Extract text content
                text = element.get_text(strip=True)
                if text and not text.startswith('返回搜狐'):  # Skip navigation text
                    content_paragraphs.append(text)

    article_data['content_paragraphs'] = content_paragraphs

    # Extract author info if available
    author_meta = soup.find('meta', {'name': 'author'})
    if author_meta and author_meta.get('content'):
        article_data['author'] = author_meta['content']
    else:
        # Try to find from other meta tags
        media_meta = soup.find('meta', {'name': 'mediaid'})
        article_data['author'] = media_meta['content'] if media_meta and media_meta.get('content') else "Unknown author"

    return article_data

def parse_sohu_article_from_file(html_file_path: str) -> dict:
    """
    Parse article from a local HTML file (useful for testing)
    """
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return parse_sohu_article_content(html_content)

if __name__ == "__main__":
    print("Fetching Sohu article...")

    # Fetch the article
    article_url = 'https://www.sohu.com/a/947318560_570646'
    html = fetch_sohu_article(article_url)

    # Save HTML for debugging
    with open('sohu_article.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Parsing article content...")
    article_data = parse_sohu_article_content(html)

    # Save parsed data to JSON
    with open('sohu_article_content.json', 'w', encoding='utf-8') as f:
        json.dump(article_data, f, ensure_ascii=False, indent=2)

    print("Article content extracted successfully!")
    print(f"Title: {article_data['title']}")
    print(f"Author: {article_data['author']}")
    print(f"Publish Time: {article_data['publish_time']}")
    print(f"Paragraphs: {len(article_data['content_paragraphs'])}")
    print("\nFirst few paragraphs:")
    for i, para in enumerate(article_data['content_paragraphs'][:3], 1):
        print(f"{i}. {para[:100]}...")
    print("\nExtracted content saved to sohu_article_content.json")