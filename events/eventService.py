# EventService
from meetup import fetch_events as fetch_meetup, parse_events as parse_meetup
import json

def event_service(lat, lon, category, start_date = "2025-10-12", num_events = 20):
    raw = fetch_meetup(lat, lon, category, num_events, start_date)
    extracted = parse_meetup(raw)
    return extracted

if __name__ == "__main__":
    # Five Categories: Get 20 top events by default
    # Sports & Fitness, Community & Environment, 
    # Identity & Language, Pets & Animals, Social Activities
    extracted = event_service(40.75, -74, "Sports & Fitness", "2025-10-12")
    with open("events.json", "w", encoding="utf-8") as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(extracted)} events → events.json")