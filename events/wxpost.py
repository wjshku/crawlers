import requests
from bs4 import BeautifulSoup
import json
import re

def parse_wechat_post(html_content: str) -> dict:
    """
    Extract post content from WeChat HTML
    """

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title
    title_element = soup.find('h1', id='activity-name')
    title = title_element.get_text(strip=True) if title_element else "No title found"

    # Extract author/publisher info
    author_element = soup.find('span', class_='rich_media_meta rich_media_meta_text')
    author = author_element.get_text(strip=True) if author_element else "Unknown author"

    # Extract publish time from JavaScript variable
    publish_time = "Unknown"
    # Look for createTime variable in script tags
    create_time_pattern = r"var createTime = ['\"]([^'\"]*)['\"]"
    create_time_match = re.search(create_time_pattern, html_content)
    if create_time_match:
        publish_time = create_time_match.group(1)

    # Extract nick name and description from JavaScript object
    nick_name = "Unknown"
    description = "Unknown"

    # Look for nick_name in JavaScript
    nick_name_pattern = r"nick_name: JsDecode\('([^']*)'\)"
    nick_name_match = re.search(nick_name_pattern, html_content)
    if nick_name_match:
        nick_name = nick_name_match.group(1)

    # Look for desc in JavaScript
    desc_pattern = r"desc: JsDecode\('([^']*)'\)"
    desc_match = re.search(desc_pattern, html_content)
    if desc_match:
        description = desc_match.group(1)

    # Extract main content
    content_element = soup.find('div', id='js_content')
    content_text = ""

    if content_element:
        # Get clean text content
        content_text = content_element.get_text(strip=True)

        # Remove excessive whitespace
        content_text = re.sub(r'\s+', ' ', content_text).strip()

    # Create structured data
    post_data = {
        'title': title,
        'author': author,
        'nick_name': nick_name,
        'description': description,
        'publish_time': publish_time,
        'content_text': content_text,
    }

    return post_data

# For fetching the content (original functionality)
def fetch_wechat_post(url: str) -> str:
    cookies = {
        'rewardsn': '',
        'wxtokenkey': '777',
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        # 'cookie': 'rewardsn=; wxtokenkey=777',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    
    print("WeChat post fetched")

    return response.text

if __name__ == "__main__":
    url = 'https://mp.weixin.qq.com/s/XttBih5mQ_NA5WxC7uyWwg'
    raw = fetch_wechat_post(url)
    parsed = parse_wechat_post(raw)
    parsed['url'] = url
    with open("wxpost.json", "w", encoding="utf-8") as f:
        json.dump(parsed, f, ensure_ascii=False, indent=2)
    print(f"Parsed {url} → wxpost.json")