import requests
import json

cookies = {
    'stableId': 'c1a4e01b-eec8-4b21-87d5-480c9f1204c6',
    'mgrefby': '',
    'guest': 'identifier%3D962a4002-d8b7-4bb2-a5e3-7147aa5f4c56%26a%3D1497%26s%3D4107b7da86213116d63285f1fae37350db161fd1400d4a3cf1e2dcff65684ed9',
    'csrftoken': 'd104f5aaa1ff11f091e53b19e64a90d8',
}

headers = {
    'referer': 'https://www.eventbrite.com/d/ny--new-york/all-events/?page=1&lang=es',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-csrftoken': 'd104f5aaa1ff11f091e53b19e64a90d8',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'stableId=c1a4e01b-eec8-4b21-87d5-480c9f1204c6; mgrefby=; guest=identifier%3D962a4002-d8b7-4bb2-a5e3-7147aa5f4c56%26a%3D1497%26s%3D4107b7da86213116d63285f1fae37350db161fd1400d4a3cf1e2dcff65684ed9; G=v%3D2%26i%3D962a4002-d8b7-4bb2-a5e3-7147aa5f4c56%26a%3D1497%26s%3Dd85e64080b4a00c76a1bad1592500aa7c872e34f; ebEventToTrack=; SS=AE3DLHTRBtVqLU9neD7Tw5bBtFebcyAHqA; eblang=lo%3Den_US%26la%3Den-us; AN=; AS=98044e3d-534b-403f-b72d-0e0e647883f7; mgref=typeins; csrftoken=d104f5aaa1ff11f091e53b19e64a90d8; _gcl_au=1.1.484588827.1759678058; _ga_TQVES5V6SH=GS2.1.s1759678057$o1$g0$t1759678057$j60$l0$h0; _ga=GA1.2.578567404.1759678058; _gid=GA1.2.464945882.1759678058; IR_gbd=eventbrite.com; IR_21676=1759678058083%7C0%7C1759678058083%7C%7C; _hp2_props.1404198904=%7B%7D; __spdt=3a6b9ac9bb894b918947f496231b210c; _fbp=fb.1.1759678058147.345051439546031287; _tt_enable_cookie=1; _ttp=01K6TFRKP13Q098ZA6R9PS3WVT_.tt.1; _uetsid=d347d980a1ff11f0933b67cebf3b1112; _uetvid=d347bb30a1ff11f0b78637602277b13c; _pin_unauth=dWlkPU1EUTNPR1E0TlRJdFptSTBNUzAwWmpaa0xXSXdPV0l0TlRVeVlUUTBZV1JpWkdaaQ; _hp2_ses_props.1404198904=%7B%22ts%22%3A1759678058094%2C%22d%22%3A%22www.eventbrite.com%22%2C%22h%22%3A%22%2Fd%2Fny--new-york%2Fall-events%2F%22%7D; tcm={"purposes":{"SaleOfInfo":"Auto","Functional":"Auto","Analytics":"Auto","Advertising":"Auto"},"timestamp":"2025-10-05T15:27:35.490Z","confirmed":false,"prompted":false,"updated":false}; __hstc=195498867.8f9aa1a8deb28594d3d9010009634a39.1759678077208.1759678077208.1759678077208.1; hubspotutk=8f9aa1a8deb28594d3d9010009634a39; __hssrc=1; __hssc=195498867.1.1759678077208; _cs_c=0; _hp2_id.1404198904=%7B%22userId%22%3A%228862078595695051%22%2C%22pageviewId%22%3A%222631025439180127%22%2C%22sessionId%22%3A%222467973638680402%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _cs_id=e0308b01-fb89-a90b-da3f-4f30c19a5369.1759678077.1.1759678412.1759678077.1751381409.1793842077242.1.x; session=identifier%3D7499e9fb0eb440709c0a950e8b537c37%26issuedTs%3D1759678413%26originalTs%3D1759678054%26s%3D73ae2a70bf4fee1e8ca55649ec7b2d195e1be9b04767ca1e78c8d36791bb1a14; SP=AGQgbbnyeHaFHdZtN9lyuwmIqGn7pbim4DTtHKZyrG-SBZmkG__bk0RlgvqJm5XqTF-8mEhDrswgyZazCYDdEHiHNJjgVM4OYjPuGxDXQQASz48j9-Mu_W3-d0bNleQbG_qlrqadVigEh1kWC3tZ-VvHrC-PCzCjKg2Wki4dz6ia5FajUpP8yCkL25LqVItY_P9Sj68sS7QHt3vWJMvcih68Uwm4w_SVBH3MDCoZqncy6z0UBOd45V8; _cs_s=2.0.U.9.1759680214559; _dd_s=rum=0&expire=1759679317291; ttcsid=1759678058179::45RyRMrYptKWMsCNC8bI.1.1759678417304.0; ttcsid_C3DHGPITO1NMNN16MDBG=1759678058179::qaC5DHOE2WyrAXCTqR09.1.1759678417305.0',
}

params = {
    'stable_id': '3eff2ab4-0f8b-48c5-bae5-fa33a68f2342',
}

json_data = {
    'event_search': {
        'dates': 'current_future',
        'dedup': True,
        'places': [
            # '85977539', # For new york
            "85922351", # For palo alto
        ],
        'page': 1,
        'page_size': 20,
        'aggs': [
            'places_borough',
            'places_neighborhood',
        ],
        'online_events_only': False,
        'languages': [
            'es',
        ],
    },
    'expand.destination_event': [
        'primary_venue',
        'image',
        'ticket_availability',
        'saves',
        'event_sales_status',
        'primary_organizer',
        'public_collections',
    ],
    'browse_surface': 'search',
}

def fetch_events():

    response = requests.post(
        'https://www.eventbrite.com/api/v3/destination/search/',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    return response.json()


def _get_address(venue):
    addr = venue.get('address') or {}
    return {
        'address_1': addr.get('address_1'),
        'address_2': addr.get('address_2'),
        'city': addr.get('city'),
        'region': addr.get('region'),
        'postal_code': addr.get('postal_code'),
        'country': addr.get('country'),
        'latitude': addr.get('latitude'),
        'longitude': addr.get('longitude'),
        'display': addr.get('localized_address_display') or addr.get('localized_multi_line_address_display'),
    }


def parse_events(obj):
    events = ((obj.get('events') or {}).get('results')) or []
    normalized = []
    for e in events:
        venue = e.get('primary_venue') or {}
        organizer = e.get('primary_organizer') or {}
        ticket = e.get('ticket_availability') or {}
        image = e.get('image') or {}
        norm = {
            'id': e.get('id') or e.get('eventbrite_event_id'),
            'name': e.get('name'),
            'url': e.get('url'),
            'language': e.get('language'),
            'start_date': e.get('start_date'),
            'start_time': e.get('start_time'),
            'end_date': e.get('end_date'),
            'end_time': e.get('end_time'),
            'timezone': e.get('timezone'),
            'summary': e.get('summary'),
            'organizer': {
                'id': organizer.get('id'),
                'name': organizer.get('name'),
                'url': organizer.get('url'),
                'followers': organizer.get('num_followers'),
            },
            'venue': {
                'id': venue.get('id'),
                'name': venue.get('name'),
                'address': _get_address(venue),
            },
            'ticket': {
                'is_free': ticket.get('is_free'),
                'has_available_tickets': ticket.get('has_available_tickets'),
                'is_sold_out': ticket.get('is_sold_out'),
                'min_price': (ticket.get('minimum_ticket_price') or {}).get('display'),
                'max_price': (ticket.get('maximum_ticket_price') or {}).get('display'),
            },
            'image_url': (image.get('original') or {}).get('url') or image.get('url'),
            'tags': [t.get('display_name') for t in (e.get('tags') or []) if isinstance(t, dict)],
        }
        normalized.append(norm)
    return normalized


if __name__ == '__main__':
    raw = fetch_events()
    extracted = parse_events(raw)
    with open('events.json', 'w', encoding='utf-8') as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(extracted)} events → events.json")
