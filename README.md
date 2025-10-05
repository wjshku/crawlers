## Crawlers - Quick Start

### Prerequisites
- Python 3.9+
- Install deps:
```bash
pip3 install requests
```

### Crime data (SpotCrime) — `crime.py`
- Function: `fetch_crime_data(params: Dict[str, Any]) -> Dict[str, Any]`
  - **Required params**: `lat`, `lon`
  - **Optional**: `radius` (miles)
- Example (as script):
```bash
python3 crime.py
```
- Example (as library):
```python
from crime import fetch_crime_data

data = fetch_crime_data({
    'lat': '40.6639208097322',
    'lon': '-73.9383508819293',
    'radius': '0.05',
})
crimes = data.get('crimes', [])
```
- Output when run as script:
  - Writes `crime.json` containing a list of crimes
  - Prints `extracted <N> crimes → crime.json`

Notes:
- Headers include an API token; replace if needed.
- SpotCrime may rate limit; keep requests reasonable.

### Events (Eventbrite) — `events.py`
- Configure search in `json_data['event_search']`:
  - `places`: geo IDs (e.g., `85977539` for New York, `85922351` for Palo Alto)
  - `languages`, `page`, `page_size`, etc.
- Functions:
  - `fetch_events() -> dict`: calls Eventbrite search API
  - `parse_events(obj: dict) -> list[dict]`: normalizes events
- Example (as script):
```bash
python3 events.py
```
- Output when run as script:
  - Writes normalized events to `events.json`
  - Each event includes: `id, name, url, language, start_date, start_time, end_date, end_time, timezone, summary, organizer, venue(address), ticket, image_url, tags`
  - Prints `Extracted <N> events → events.json`

Notes:
- Some headers/cookies are captured from browser; refresh if API stops responding.
- Respect Eventbrite terms; avoid high-frequency scraping.

### Tips
- Use virtualenv/pyenv to isolate deps.
- Prefer saving raw API responses during development for reproducibility.

