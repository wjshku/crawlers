import requests
import json

cookies = {
    'PHPSESSID': 'd176f0elv291id3505fj3c9282',
    'user_city_query': 'new+york',
    'user_city': 'New+York',
    '_ae_utm_track': 'utmcsr=(direct)|utmcmd=(none)|utmccn=(not set)',
    '_ae_utm_track_ses': '1',
    '_fbp': 'fb.1.1760280801676.175134991',
    '_gcl_au': '1.1.1383084143.1760280802',
    '_ga': 'GA1.1.372562655.1760280802',
    'FPID': 'FPID2.2.eboPeLs04b9qsXo1MCpRek3XeCf%2F4q7lCGF86c9eaUk%3D.1760280802',
    'FPLC': 'KtVY2CuDw6Csx0Yer1vc7Fg%2Fs9AmHFOgLn1kazUv0kCrr%2FVg%2Fb367xTD8voC3InfoBRGV35T4k7k%2F22EfjfOS0%2Fc6BsxGqP9ljrFXvb1DoNaXCPENU2cp7xViKE5JQ%3D%3D',
    '_pk_id.1.6c4e': '5612c771520fd8de.1760280802.',
    '_pk_ses.1.6c4e': '1',
    'WZRK_G': '7c94fbf954f846f38473692b7653d295',
    'ACTRKID': '32ce9220-a77b-11f0-9a78-990aa495478e',
    '_clck': '13r5dr6%5E2%5Eg03%5E0%5E2111',
    '__gads': 'ID=6d97bbcebeddda1b:T=1760280805:RT=1760280805:S=ALNI_MbPoM9CVYtqMlh7KAImVKNqnm2VDg',
    '__gpi': 'UID=0000129cd25a1276:T=1760280805:RT=1760280805:S=ALNI_MaPwUsYeOEtg_fQB7Vl3y5j92XOtA',
    '__eoi': 'ID=1a27ef43bacb74a9:T=1760280805:RT=1760280805:S=AA-AfjYjArk8Fkfj1QPlfvZgsvxh',
    'current_lat': '1.3051',
    'current_long': '103.8843',
    '__AP_SESSION__': '981cfb3c-0772-4b10-84c6-b87c8f401580',
    '__qca': 'P1-85aae91b-4fe4-41a9-a807-48e7e6fedf09',
    '_cc_id': '9ccebdcd04973499e4ffd47406309e91',
    'panoramaId': 'a0408cbadb6da78f052abedc26cfa9fb927a4cbe50c9effc7ea75cad68ba59f4',
    'panoramaIdType': 'panoDevice',
    'panoramaId_expiry': '1760367220007',
    'fblogin-remind': 'true',
    'fblike-remind': 'true',
    '_ctuid': '79a5ec96-91ca-46ef-ae61-3a28dade00c8',
    'fpestid': '-PaEz__9Gvr0pzQ_allEudems-u9_peRBfEY9vOy28F4zCbE-Mrtrs1Xf-lmKQ8pHAUddA',
    'cto_bundle': 'Sn9SFl9XZzVUQzlRTldqOEUzZSUyQjNJZXFGb1FyQmNEWiUyRkM2NTJmdEdIRGhZMmZtYnlrQlk5YmcxSzh0bVVvODVDUHBUZDZyNUNnV1RSTXU3MzlWT3JkTnEwdm8zd1BpRTFoelo1ZURuMCUyQnhaaDluTUt5RjFwOHlyT053ek1pSDlZMU14JTJGSFU0VmNHV1VGcWFaQ2tmcnlEWTlDVnRZd2QlMkZtTWslMkJpb3FkaWNPSG9qZHdNWlFia2ZXamx3djN3MG8yUjZUeTBlV2NBSmRXRHdsbGFOYVR6TVE2ZWRnJTNEJTNE',
    '_ctpuid': 'b044c2dd-09d3-4480-82f7-858c11fed604',
    '_ctz_opt_out': '_ctz_opt_out_ddu',
    'FPGSID': '1.1760280801.1760280968.G-DZD3QFXNY7.Pb08E2sG8nv5aF4qr6nsfA',
    '_clsk': 'vyjibm%5E1760280969486%5E4%5E1%5Ei.clarity.ms%2Fcollect',
    'FCNEC': '%5B%5B%22AKsRol_svMQ76eAKyCOQBs32J4ljNvBolEy0EhzZn5WABlnz3DeA-srkcqH7hMUN9QP8ND8qlFiXDVusRPGAXZpmF71pqSknxAed7CFYxBi7p-YTqLIkGCsrh_kcomjefACAQWGtUJT-LPnYIEp56yXN08w1SeeOhg%3D%3D%22%5D%5D',
    'g_state': '{"i_l":0,"i_ll":1760280975896,"i_b":"QZrTF5u0IZMEOGHUlUwUAe9s8gtEHUVjtTk/z/PyKDc"}',
    '_visit': '5',
    '_pgrf': '404',
    '_ga_DZD3QFXNY7': 'GS2.1.s1760280801$o1$g1$t1760281010$j22$l0$h1823136172',
    'WZRK_S_69R-556-545Z': '%7B%22p%22%3A6%2C%22s%22%3A1760280802%2C%22t%22%3A1760281010%7D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://allevents.in/new-york/entertainment',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    # 'cookie': 'PHPSESSID=d176f0elv291id3505fj3c9282; user_city_query=new+york; user_city=New+York; _ae_utm_track=utmcsr=(direct)|utmcmd=(none)|utmccn=(not set); _ae_utm_track_ses=1; _fbp=fb.1.1760280801676.175134991; _gcl_au=1.1.1383084143.1760280802; _ga=GA1.1.372562655.1760280802; FPID=FPID2.2.eboPeLs04b9qsXo1MCpRek3XeCf%2F4q7lCGF86c9eaUk%3D.1760280802; FPLC=KtVY2CuDw6Csx0Yer1vc7Fg%2Fs9AmHFOgLn1kazUv0kCrr%2FVg%2Fb367xTD8voC3InfoBRGV35T4k7k%2F22EfjfOS0%2Fc6BsxGqP9ljrFXvb1DoNaXCPENU2cp7xViKE5JQ%3D%3D; _pk_id.1.6c4e=5612c771520fd8de.1760280802.; _pk_ses.1.6c4e=1; WZRK_G=7c94fbf954f846f38473692b7653d295; ACTRKID=32ce9220-a77b-11f0-9a78-990aa495478e; _clck=13r5dr6%5E2%5Eg03%5E0%5E2111; __gads=ID=6d97bbcebeddda1b:T=1760280805:RT=1760280805:S=ALNI_MbPoM9CVYtqMlh7KAImVKNqnm2VDg; __gpi=UID=0000129cd25a1276:T=1760280805:RT=1760280805:S=ALNI_MaPwUsYeOEtg_fQB7Vl3y5j92XOtA; __eoi=ID=1a27ef43bacb74a9:T=1760280805:RT=1760280805:S=AA-AfjYjArk8Fkfj1QPlfvZgsvxh; current_lat=1.3051; current_long=103.8843; __AP_SESSION__=981cfb3c-0772-4b10-84c6-b87c8f401580; __qca=P1-85aae91b-4fe4-41a9-a807-48e7e6fedf09; _cc_id=9ccebdcd04973499e4ffd47406309e91; panoramaId=a0408cbadb6da78f052abedc26cfa9fb927a4cbe50c9effc7ea75cad68ba59f4; panoramaIdType=panoDevice; panoramaId_expiry=1760367220007; fblogin-remind=true; fblike-remind=true; _ctuid=79a5ec96-91ca-46ef-ae61-3a28dade00c8; fpestid=-PaEz__9Gvr0pzQ_allEudems-u9_peRBfEY9vOy28F4zCbE-Mrtrs1Xf-lmKQ8pHAUddA; cto_bundle=Sn9SFl9XZzVUQzlRTldqOEUzZSUyQjNJZXFGb1FyQmNEWiUyRkM2NTJmdEdIRGhZMmZtYnlrQlk5YmcxSzh0bVVvODVDUHBUZDZyNUNnV1RSTXU3MzlWT3JkTnEwdm8zd1BpRTFoelo1ZURuMCUyQnhaaDluTUt5RjFwOHlyT053ek1pSDlZMU14JTJGSFU0VmNHV1VGcWFaQ2tmcnlEWTlDVnRZd2QlMkZtTWslMkJpb3FkaWNPSG9qZHdNWlFia2ZXamx3djN3MG8yUjZUeTBlV2NBSmRXRHdsbGFOYVR6TVE2ZWRnJTNEJTNE; _ctpuid=b044c2dd-09d3-4480-82f7-858c11fed604; _ctz_opt_out=_ctz_opt_out_ddu; FPGSID=1.1760280801.1760280968.G-DZD3QFXNY7.Pb08E2sG8nv5aF4qr6nsfA; _clsk=vyjibm%5E1760280969486%5E4%5E1%5Ei.clarity.ms%2Fcollect; FCNEC=%5B%5B%22AKsRol_svMQ76eAKyCOQBs32J4ljNvBolEy0EhzZn5WABlnz3DeA-srkcqH7hMUN9QP8ND8qlFiXDVusRPGAXZpmF71pqSknxAed7CFYxBi7p-YTqLIkGCsrh_kcomjefACAQWGtUJT-LPnYIEp56yXN08w1SeeOhg%3D%3D%22%5D%5D; g_state={"i_l":0,"i_ll":1760280975896,"i_b":"QZrTF5u0IZMEOGHUlUwUAe9s8gtEHUVjtTk/z/PyKDc"}; _visit=5; _pgrf=404; _ga_DZD3QFXNY7=GS2.1.s1760280801$o1$g1$t1760281010$j22$l0$h1823136172; WZRK_S_69R-556-545Z=%7B%22p%22%3A6%2C%22s%22%3A1760280802%2C%22t%22%3A1760281010%7D',
}

def fetch_events():
    location = 'new-york'
    category = 'music'
    response = requests.get(f'https://allevents.in/{location}/{category}', cookies=cookies, headers=headers)

    return response.text

def parse_events(raw):
    """
    Parse AllEvents data from HTML response and extract event information.
    
    Args:
        raw (str): Raw HTML response from AllEvents website
        
    Returns:
        list: List of parsed event dictionaries
    """
    import re
    import json
    from datetime import datetime
    
    events = []
    
    try:
        # Extract the events_data array from the JavaScript code
        # Look for the pattern: _this.events_data = [event_data_array];
        # Use a more specific pattern to find the non-empty array
        pattern = r'_this\.events_data\s*=\s*(\[.*?\]);'
        matches = re.findall(pattern, raw, re.DOTALL)
        
        if not matches:
            print("❌ Could not find events_data in the response")
            return []
        
        # Find the largest match (which should be the actual events data)
        events_json_str = max(matches, key=len)
        
        # Clean up the JSON string - remove any trailing semicolons or other JS syntax
        events_json_str = events_json_str.rstrip(';')
        
        # Parse the JSON array
        events_data = json.loads(events_json_str)
        
        # Process each event
        for event_data in events_data:
            event = {
                'event_id': event_data.get('event_id'),
                'name': event_data.get('eventname'),
                'name_raw': event_data.get('eventname_raw'),
                'start_time': event_data.get('start_time'),
                'start_time_display': event_data.get('start_time_display'),
                'end_time': event_data.get('end_time'),
                'end_time_display': event_data.get('end_time_display'),
                'location': event_data.get('location'),
                'location_raw': event_data.get('location_raw'),
                'label': event_data.get('label'),  # Upcoming, Today, etc.
                'featured': event_data.get('featured'),
                'event_url': event_data.get('event_url'),
                'share_url': event_data.get('share_url'),
                'score': event_data.get('score'),
                'short_description': event_data.get('short_description'),
                'timezone': event_data.get('timezone'),
                'display_day': event_data.get('display_day'),
                'display_month': event_data.get('display_month'),
                'display_end_day': event_data.get('display_end_day'),
                'app_display_time': event_data.get('app_display_time'),
                'display_time_label': event_data.get('display_time_label'),
            }
            
            # Extract image URLs
            event['images'] = {
                'thumb_url': event_data.get('thumb_url'),
                'thumb_url_large': event_data.get('thumb_url_large'),
                'banner_url': event_data.get('banner_url')
            }
            
            # Extract venue information
            venue = event_data.get('venue', {})
            if venue:
                event['venue'] = {
                    'street': venue.get('street'),
                    'city': venue.get('city'),
                    'state': venue.get('state'),
                    'country': venue.get('country'),
                    'latitude': venue.get('latitude'),
                    'longitude': venue.get('longitude'),
                    'full_address': venue.get('full_address')
                }
            
            # Extract organizer information
            organizer = event_data.get('organizer', {})
            if organizer:
                event['organizer'] = {
                    'org_id': organizer.get('org_id'),
                    'name': organizer.get('name')
                }
            
            # Extract categories and tags
            event['categories'] = event_data.get('categories', [])
            event['tags'] = event_data.get('tags', [])
            event['formats'] = event_data.get('formats', [])
            
            # Extract ticket information
            tickets = event_data.get('tickets', {})
            if tickets:
                event['tickets'] = {
                    'has_tickets': tickets.get('has_tickets', False),
                    'ticket_url': tickets.get('ticket_url', ''),
                    'ticket_currency': tickets.get('ticket_currency'),
                    'min_ticket_price': tickets.get('min_ticket_price'),
                    'max_ticket_price': tickets.get('max_ticket_price')
                }
            else:
                event['tickets'] = {
                    'has_tickets': False,
                    'ticket_url': '',
                    'ticket_currency': None,
                    'min_ticket_price': None,
                    'max_ticket_price': None
                }
            
            # Extract custom parameters and additional metadata
            custom_params = event_data.get('custom_params', {})
            if custom_params:
                event['custom_params'] = {
                    'interested_count': custom_params.get('interested_count'),
                    'x_categories': custom_params.get('x_categories', []),
                    'merged_lookup': custom_params.get('merged_lookup', []),
                    'gemma_categories': custom_params.get('gemma_categories', [])
                }
                
                # Extract label type if available
                label_type = custom_params.get('label_type', {})
                if label_type:
                    event['label_type'] = {
                        'text': label_type.get('text'),
                        'label': label_type.get('label'),
                        'icon': label_type.get('icon')
                    }
            
            # Extract price display label
            event['display_price_label'] = event_data.get('display_price_label')
            
            # Convert timestamps to readable format
            if event['start_time']:
                try:
                    start_timestamp = int(event['start_time'])
                    event['start_datetime'] = datetime.fromtimestamp(start_timestamp).isoformat()
                except (ValueError, TypeError):
                    event['start_datetime'] = None
            
            if event['end_time']:
                try:
                    end_timestamp = int(event['end_time'])
                    event['end_datetime'] = datetime.fromtimestamp(end_timestamp).isoformat()
                except (ValueError, TypeError):
                    event['end_datetime'] = None
            
            events.append(event)
            
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        return []
    except Exception as e:
        print(f"❌ Error parsing events: {e}")
        return []
    
    return events

if __name__ == "__main__":
    raw = fetch_events()
    extracted = parse_events(raw)
    with open("allevents.json", "w", encoding="utf-8") as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(extracted)} events → allevents.json")