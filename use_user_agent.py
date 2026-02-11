import requests
import pandas as pd
import random

# Load user agents
df = pd.read_excel('mobile_user_agents_500_mobile_only.xlsx')

# Pick random mobile user agent
random_row = df.sample(1).iloc[0]

# Create headers for 100% mobile detection
headers = {
    'User-Agent': random_row['User_Agent_String'],
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?1',              # ← CRITICAL: This tells websites it's MOBILE
    'Sec-Ch-Ua-Platform': '"Android"',     # ← Platform hint
    'Viewport-Width': str(random_row['Viewport_Width']),
    'Viewport-Height': str(random_row['Viewport_Height']),
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'com.android.chrome'  # Android Chrome app
}

# Make request - website will see this as MOBILE ONLY
response = requests.get('https://example.com', headers=headers)
print(response.text)