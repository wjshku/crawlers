import requests
from bs4 import BeautifulSoup
import json

def fetch_posts():
    cookies = {
        'acw_tc': '0a00ded117614568773295832e2ee6a3366f1a96afa4ab028b5018b71e2ecf',
        'abRequestId': '1af2143c-3c49-537b-9d46-603b6bea6a9b',
        'a1': '19a1f02f2d3wnbrjkz3p4sxdupamxng7kdo6j7nt230000291018',
        'webId': '7df658e86745cf8d5268ee635e700633',
        'websectiga': 'cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c',
        'sec_poison_id': 'a79e8e59-6a38-463a-abdf-74d98d2bc36c',
        'gid': 'yj0yi8qyKST0yj0yi8JiJfWIfqEIDFVTuqU4l9JMCf7U0Kq86CIkWV888Jjy8yY8yKJijd8d',
        'webBuild': '4.83.1',
        'xsecappid': 'xhs-pc-web',
        'unread': '{%22ub%22:%2264bdfccf000000000800d5ef%22%2C%22ue%22:%2264c4c1360000000010030404%22%2C%22uc%22:20}',
        'web_session': '040069b46dd8005b691454fbc83a4bad727f77',
        'loadts': '1761456989900',
    }

    headers = {
        'referer': 'https://www.xiaohongshu.com/explore/68eeea6500000000070360ca?xsec_token=ABDgHR4CJzOQ-FbeGECgpD1E0i1zGO6DMc-x3Fe6n0OU8=&xsec_source=pc_search&source=web_search_result_notes',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        # 'cookie': 'acw_tc=0a00ded117614568773295832e2ee6a3366f1a96afa4ab028b5018b71e2ecf; abRequestId=1af2143c-3c49-537b-9d46-603b6bea6a9b; a1=19a1f02f2d3wnbrjkz3p4sxdupamxng7kdo6j7nt230000291018; webId=7df658e86745cf8d5268ee635e700633; websectiga=cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c; sec_poison_id=a79e8e59-6a38-463a-abdf-74d98d2bc36c; gid=yj0yi8qyKST0yj0yi8JiJfWIfqEIDFVTuqU4l9JMCf7U0Kq86CIkWV888Jjy8yY8yKJijd8d; webBuild=4.83.1; xsecappid=xhs-pc-web; unread={%22ub%22:%2264bdfccf000000000800d5ef%22%2C%22ue%22:%2264c4c1360000000010030404%22%2C%22uc%22:20}; web_session=040069b46dd8005b691454fbc83a4bad727f77; loadts=1761456989900',
    }

    response = requests.get(
        'https://www.xiaohongshu.com/user/profile/5cabd8e80000000016030a4d?xsec_token=AB51j2YuWDvmCaBaFUq1QZ0ePtFm_YtRSmUtSNfTc5ceo=&xsec_source=pc_note',
        cookies=cookies,
        headers=headers,
    )
    return response.text

def parse_posts(html_content: str) -> list:
    """
    Parse Xiaohongshu posts from HTML content
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    posts = []

    # Find all note items (posts)
    note_items = soup.find_all('section', class_='note-item')

    for note_item in note_items:
        try:
            post_data = {}

            # Extract title
            title_elem = note_item.find('span', {'data-v-51ec0135': True})
            post_data['title'] = title_elem.get_text(strip=True) if title_elem else "No title"

            # Extract author name
            author_elem = note_item.find('span', class_='name')
            post_data['author'] = author_elem.get_text(strip=True) if author_elem else "Unknown author"

            # Extract like count
            like_elem = note_item.find('span', {'selected-disabled-search': True})
            like_count = like_elem.get_text(strip=True) if like_elem else "0"
            # Remove any non-numeric characters and convert to int
            like_count = ''.join(filter(str.isdigit, like_count))
            post_data['likes'] = int(like_count) if like_count else 0

            # Extract image URL
            img_elem = note_item.find('img')
            if img_elem:
                img_url = img_elem.get('src', '')
                # Clean up the URL if it has parameters
                if img_url and 'http' in img_url:
                    post_data['image_url'] = img_url
                else:
                    post_data['image_url'] = ""
            else:
                post_data['image_url'] = ""

            # Extract post URL
            link_elem = note_item.find('a', href=lambda x: x and '/explore/' in x)
            if link_elem:
                post_url = link_elem.get('href', '')
                # Convert relative URL to full URL
                if post_url.startswith('/'):
                    post_url = f"https://www.xiaohongshu.com{post_url}"
                post_data['post_url'] = post_url
            else:
                post_data['post_url'] = ""

            # Extract additional metadata if available
            # Check if it's a video post (has play icon)
            play_icon = note_item.find('span', class_='play-icon')
            post_data['is_video'] = play_icon is not None

            # Extract dimensions if available
            note_div = note_item.find('div', {'data-v-a264b01a': True})
            if note_div:
                width = note_div.get('data-width')
                height = note_div.get('data-height')
                if width and height:
                    post_data['dimensions'] = f"{width}x{height}"

            posts.append(post_data)

        except Exception as e:
            print(f"Error parsing post: {e}")
            continue

    return posts

def parse_posts_from_file(html_file_path: str) -> list:
    """
    Parse posts from a local HTML file (useful for testing)
    """
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return parse_posts(html_content)

if __name__ == "__main__":
    print("Fetching Xiaohongshu posts...")
    html = fetch_posts()
    print("Parsing posts...")
    posts = parse_posts(html)

    # Save to JSON file
    with open('xhs.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f"Successfully extracted {len(posts)} posts and saved to xhs_posts.json")

    # Print summary
    print("\n=== XIAOHONGSHU POSTS SUMMARY ===")
    for i, post in enumerate(posts[:5], 1):  # Show first 5 posts
        print(f"{i}. {post['title'][:50]}... by {post['author']} ({post['likes']} likes)")
        if post['is_video']:
            print("   📹 Video post")
        else:
            print("   🖼️  Image post")

    if len(posts) > 5:
        print(f"... and {len(posts) - 5} more posts")