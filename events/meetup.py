import requests
import json

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"operationName":"recommendedEventsWithSeries","variables":{"first":12,"lat":40.75,"lon":-73.98999786376953,"topicCategoryId":"652","startDateRange":"2025-10-12T04:13:02-04:00[US/Eastern]","numberOfEventsForSeries":5,"seriesStartDate":"2025-10-12","sortField":"RELEVANCE","doConsolidateEvents":true,"doPromotePaypalEvents":false,"indexAlias":"\\"{\\\\\\"filterOutWrongLanguage\\\\\\": \\\\\\"true\\\\\\",\\\\\\"modelVersion\\\\\\": \\\\\\"split_offline_online\\\\\\"}\\"","dataConfiguration":"{\\"isSimplifiedSearchEnabled\\": true, \\"include_events_from_user_chapters\\": true}"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"41c4ab255edd3c793ee394cfaeec3f4e823eab251620360e4705032be0f949a1"}}}'
# response = requests.post('https://www.meetup.com/gql2', cookies=cookies, headers=headers, data=data)


def get_category_id(category):
    return {
        "Indentity & Language": "622",
        "Pets & Animals": "701",
        "Social Activities": "652",
        "Sports & Fitness": "482",
        "Community & Environment": "604",
    }[category]

def fetch_events(lat = 40.75, lon = -73.98999786376953, 
            category = "Community & Environment",
            num_events = 15,
            start_date = "2025-10-12"):

    category_id = get_category_id(category)
    # —————— 配置你的 Meetup 会话信息 ——————
    cookies = {
    }

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        "x-meetup-view-id": "baad2164-31b8-4662-9b82-a4f961a79327",
    }

    json_data = {
        "operationName": "recommendedEventsWithSeries",
        "variables": {
            "first": num_events,
            "lat": lat,
            "lon": lon,
            "topicCategoryId": category_id,
            # "startDateRange": "2025-10-12T04:13:02-04:00[US/Eastern]",
            'eventType': 'PHYSICAL',
            "numberOfEventsForSeries": 5,
            "seriesStartDate": start_date,
            "sortField": "RELEVANCE",
            "doConsolidateEvents": True,
            "doPromotePaypalEvents": False,
            "indexAlias": '"{\\"filterOutWrongLanguage\\": \\"true\\",\\"modelVersion\\": \\"split_offline_online\\"}"',
            "dataConfiguration": '{"isSimplifiedSearchEnabled": true, "include_events_from_user_chapters": true}',
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "41c4ab255edd3c793ee394cfaeec3f4e823eab251620360e4705032be0f949a1",
            },
        },
    }

    response = requests.post(
        "https://www.meetup.com/gql2", cookies=cookies, headers=headers, json=json_data
    )

    return response.json()


def parse_events(raw):
    """
    Parse Meetup events from GraphQL response and extract relevant information.
    
    Args:
        raw (dict): Raw JSON response from Meetup GraphQL API
        
    Returns:
        list: List of parsed event dictionaries
    """
    events = []
    
    try:
        # Navigate to the events data
        edges = raw.get('data', {}).get('result', {}).get('edges', [])
        
        for edge in edges:
            node = edge.get('node', {})
            
            # Extract basic event information
            event = {
                'id': node.get('id'),
                'title': node.get('title'),
                'dateTime': node.get('dateTime'),
                'description': node.get('description'),
                'eventType': node.get('eventType'),  # PHYSICAL, ONLINE, etc.
                'eventUrl': node.get('eventUrl'),
                'isAttending': node.get('isAttending'),
                'isSaved': node.get('isSaved'),
                'maxTickets': node.get('maxTickets'),
                'rsvpState': node.get('rsvpState'),  # JOIN_OPEN, etc.
            }
            
            # Extract featured photo information
            featured_photo = node.get('featuredEventPhoto', {})
            if featured_photo:
                event['featured_photo'] = {
                    'id': featured_photo.get('id'),
                    'high_res_url': featured_photo.get('highResUrl'),
                    'base_url': featured_photo.get('baseUrl')
                }
            
            # Extract fee information
            fee_settings = node.get('feeSettings')
            if fee_settings:
                event['fee'] = {
                    'amount': fee_settings.get('amount'),
                    'currency': fee_settings.get('currency'),
                    'label': fee_settings.get('label')
                }
            else:
                event['fee'] = None
            
            # Extract group information
            group = node.get('group', {})
            if group:
                event['group'] = {
                    'id': group.get('id'),
                    'name': group.get('name'),
                    'urlname': group.get('urlname'),
                    'timezone': group.get('timezone')
                }
                
                # Extract group photo
                group_photo = group.get('keyGroupPhoto', {})
                if group_photo:
                    event['group']['photo'] = {
                        'id': group_photo.get('id'),
                        'high_res_url': group_photo.get('highResUrl'),
                        'base_url': group_photo.get('baseUrl')
                    }
                
                # Extract group stats
                stats = group.get('stats', {})
                if stats:
                    event_ratings = stats.get('eventRatings', {})
                    if event_ratings:
                        event['group']['ratings'] = {
                            'average': event_ratings.get('average'),
                            'total_ratings': event_ratings.get('totalRatings')
                        }
            
            # Extract RSVP information
            rsvps = node.get('rsvps', {})
            if rsvps:
                event['rsvps'] = {
                    'total_count': rsvps.get('totalCount'),
                    'attendees': []
                }
                
                # Extract attendee information
                rsvp_edges = rsvps.get('edges', [])
                for rsvp_edge in rsvp_edges:
                    rsvp_node = rsvp_edge.get('node', {})
                    user = rsvp_node.get('user', {})
                    
                    attendee = {
                        'is_host': rsvp_node.get('isHost'),
                        'user_id': user.get('id'),
                        'name': user.get('name')
                    }
                    
                    # Extract member photo
                    member_photo = user.get('memberPhoto', {})
                    if member_photo:
                        attendee['photo'] = {
                            'id': member_photo.get('id'),
                            'source': member_photo.get('source'),
                            'base_url': member_photo.get('baseUrl')
                        }
                    
                    event['rsvps']['attendees'].append(attendee)
            
            # Extract series information if available
            series = node.get('series')
            if series:
                event['series'] = {
                    'id': series.get('id'),
                    'name': series.get('name'),
                    'description': series.get('description')
                }
            
            events.append(event)
            
    except Exception as e:
        print(f"Error parsing events: {e}")
        return []
    
    return events

if __name__ == "__main__":
    raw = fetch_events(
        lat = 40.75, 
        lon = -74, 
        category = "Sports & Fitness",
        num_events = 15,
        start_date = "2025-10-12"
    )
    extracted = parse_events(raw)
    print(extracted)
    with open("meetup.json", "w", encoding="utf-8") as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(extracted)} events → meetup.json")