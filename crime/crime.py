import requests
import json
from typing import Dict, Any

cookies = {
}

headers = {
    'referer': 'https://spotcrime.com/map?lat=40.6639208097322&lon=-73.9383508819293',
    'spotcrime-api-token': 'SFMyNTY.g2gDbQAAADMxOTUuMTMzLjEyOS4xMDplZTkwNzM3YS1kMDEzLTQ2YzYtYjFmNC0zNDI5MGI0YTM0YjVuBgCzYgm1mQFiAAFRgA.oy-ufAkuAg7ODv7AM7CuqBBdeDowNX8rx5IWjEfXRHk',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.2102659789.1759678852; __eoi=ID=9f2a5bf2ddb84de8:T=1759678852:RT=1759678852:S=AA-AfjbsSkUT5-_1cDjF4HD84XZk; FCNEC=%5B%5B%22AKsRol-2JKudyZGU2LojCcSg8_5XJ5t-u3V6I2rRklxJ5tRjEnAZfsFwYG_mylELOjkkrSHFP31DV7E1r5MRgfqV_BjogXjoVImWa95w3ilPYUsj5mKrxxZLFuBOlRMPAUAEOKalMUxVpoV3-Ixk3mAQUFZYLRZmXw%3D%3D%22%5D%5D; _ga_H6H0H4RXJH=GS2.1.s1759678852$o1$g1$t1759678915$j60$l0$h0',
}

def fetch_crime_data(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Fetch crime data from SpotCrime.

    Required params keys: 'lat', 'lon'. Optional: 'radius' (miles, string or number).
    Returns parsed JSON as a dict.
    """
    resp = requests.get(
        'https://spotcrime.com/crimes.json',
        params=params,
        cookies=cookies,
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


if __name__ == '__main__':
    # Example: Manhattan area (adjust as needed)
    params = {
        'lat': '40.6639208097322',
        'lon': '-73.9383508819293',
        'radius': '0.02',
    }
    data = fetch_crime_data(params)
    crimes = data.get('crimes') or []
    print(f'extracted {len(crimes)} crimes → crime.json')
    with open('crime.json', 'w', encoding='utf-8') as f:
        json.dump(crimes, f)