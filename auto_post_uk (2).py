"""
imanexis - Auto Post Script
UK ki famous places ki images aur descriptions
Har 1 ghante baad automatically post hoga
"""

import requests
import urllib.parse
import time
import random
from datetime import datetime

# ============================================================
FB_PAGE_ACCESS_TOKEN = "EAAhVgRWi8XUBRxHSZCcuLU8sWzuCVX5qInVgzY7c3X1z0ieZCgDbgehJ52Cr14uq29bwlepewIWZBbQqIZA2NOdZCbmSZCpdG25MlPAEUyLVnZC3a1UecAfTvgeHNZAlJsDjOk27b6alZCIPUtZAhFRZADktUFTDyi4xz6PlNUPsNnNO2fSrlD6VaeIFDBfeJEpZApCtZBY14ceOpxxdQY9NGwn8NbzeZCEBxqMlfn08M1DkDKZBNwZD"
FB_PAGE_ID           = "61585489487268"
POST_INTERVAL_HOURS  = 1
# ============================================================

UK_PLACES = [
    {
        "prompt": "Big Ben London UK, iconic clock tower, Westminster Bridge, River Thames, red double decker bus, golden hour lighting, ultra realistic professional photo",
        "caption": "🕰️ Big Ben, London\n\nThe most iconic clock tower in the world! Standing 96 meters tall at the Palace of Westminster, Big Ben has been keeping time for London since 1859. A true symbol of British heritage! 🇬🇧\n\n#BigBen #London #UK #Travel #BritishIcons #Westminster #England"
    },
    {
        "prompt": "Stonehenge Wiltshire England UK, ancient mysterious stone circle, dramatic cloudy sky, green fields, sunrise, ultra realistic professional photo",
        "caption": "🪨 Stonehenge, Wiltshire\n\nOne of the world's greatest mysteries! These massive stones were erected over 4,000 years ago and archaeologists still debate how prehistoric people moved stones weighing up to 25 tons. Truly awe-inspiring! 🇬🇧\n\n#Stonehenge #Wiltshire #England #UK #Travel #AncientHistory #Mystery"
    },
    {
        "prompt": "Edinburgh Castle Scotland UK, dramatic castle on volcanic rock, city skyline below, cloudy dramatic sky, ultra realistic professional photography",
        "caption": "🏰 Edinburgh Castle, Scotland\n\nPerched dramatically on an ancient volcanic rock, Edinburgh Castle has dominated Scotland's capital for over 3,000 years! Home to the Scottish Crown Jewels and one of the most visited attractions in the UK! 🇬🇧\n\n#EdinburghCastle #Edinburgh #Scotland #UK #Travel #Castle #History"
    },
    {
        "prompt": "Tower Bridge London UK, iconic Victorian bridge over River Thames, night reflection in water, illuminated blue, ultra realistic professional photo",
        "caption": "🌉 Tower Bridge, London\n\nLondon's most famous bridge! This magnificent Victorian masterpiece took 8 years to build and opened in 1894. The bridge still opens over 800 times a year to let tall ships pass through the Thames! 🇬🇧\n\n#TowerBridge #London #UK #Travel #Thames #Architecture #England"
    },
    {
        "prompt": "Buckingham Palace London UK, grand royal palace, royal guards in red uniform, golden gates, blue sky, ultra realistic professional photo",
        "caption": "👑 Buckingham Palace, London\n\nThe official residence of the British Royal Family since 1837! With 775 rooms including 19 State rooms, 52 bedrooms, and 92 offices — this magnificent palace is one of the world's most visited landmarks! 🇬🇧\n\n#BuckinghamPalace #London #UK #Travel #RoyalFamily #England #Palace"
    },
    {
        "prompt": "Lake District England UK, stunning mountain lake reflection, green hills, dramatic clouds, peaceful nature landscape, ultra realistic professional photo",
        "caption": "🏔️ Lake District, England\n\nEngland's largest national park and a UNESCO World Heritage Site! With 16 lakes, dramatic mountains, and picturesque villages, the Lake District inspired famous poets like William Wordsworth. Pure natural beauty! 🇬🇧\n\n#LakeDistrict #England #UK #Travel #NationalPark #Nature #UNESCO"
    },
    {
        "prompt": "Oxford University England UK, historic gothic buildings, beautiful architecture, green lawns, cobblestone streets, golden sunlight, ultra realistic photo",
        "caption": "🎓 Oxford University, England\n\nThe oldest university in the English-speaking world! Founded in 1096, Oxford has produced 28 British Prime Ministers, 50 Nobel Prize winners, and countless world leaders. Walking these ancient streets is like stepping back in time! 🇬🇧\n\n#Oxford #OxfordUniversity #England #UK #Travel #Education #History"
    },
    {
        "prompt": "Giant's Causeway Northern Ireland UK, unique hexagonal basalt columns, dramatic ocean waves, stormy sky, ultra realistic professional photography",
        "caption": "🌊 Giant's Causeway, Northern Ireland\n\nA natural wonder unlike anything else on Earth! Around 40,000 interlocking basalt columns formed by ancient volcanic activity 60 million years ago. Legend says it was built by giant Finn McCool! 🇬🇧\n\n#GiantsCauseway #NorthernIreland #UK #Travel #UNESCO #NaturalWonder #Ireland"
    },
    {
        "prompt": "Cotswolds England UK, charming honey stone village, beautiful cottages with flower gardens, green rolling hills, sunny day, ultra realistic professional photo",
        "caption": "🌸 The Cotswolds, England\n\nEngland's most beautiful countryside! These charming honey-coloured stone villages look like they've jumped straight out of a fairytale. With rolling green hills and flower-filled gardens, it's a perfect slice of English paradise! 🇬🇧\n\n#Cotswolds #England #UK #Travel #Countryside #Village #EnglishHeritage"
    },
    {
        "prompt": "Windsor Castle England UK, largest occupied castle world, royal standard flag flying, beautiful gardens, blue sky, ultra realistic professional photo",
        "caption": "🏰 Windsor Castle, England\n\nThe world's oldest and largest occupied castle! Windsor has been the home of British monarchs for over 1,000 years. Covering 13 acres, it's a stunning symbol of the British Royal Family's enduring legacy! 🇬🇧\n\n#WindsorCastle #Windsor #England #UK #Travel #RoyalFamily #Castle #History"
    },
]


def generate_image(prompt, save_path="generated_image.png"):
    encoded = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true&seed={random.randint(1,99999)}"
    r = requests.get(url, timeout=90)
    r.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(r.content)
    print(f"   Image save ho gayi: {save_path}")
    return save_path


def upload_to_facebook(image_path, caption):
    url = f"https://graph.facebook.com/v25.0/{FB_PAGE_ID}/photos"
    with open(image_path, "rb") as img:
        r = requests.post(url, files={"source": img}, data={"caption": caption, "access_token": FB_PAGE_ACCESS_TOKEN})
    result = r.json()
    if "id" in result:
        print(f"   Facebook pe post ho gaya! Post ID: {result['id']}")
        return True
    else:
        print(f"   Facebook Error: {result}")
        return False


def run_once():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*50}")
    print(f"  UK - Time: {now}")
    print(f"{'='*50}")

    place = random.choice(UK_PLACES)

    print(f"\nStep 1: Image generate ho rahi hai...")
    print(f"   Place: {place['caption'][:40]}...")
    try:
        image_path = generate_image(place["prompt"])
    except Exception as e:
        print(f"   Image error: {e}")
        return

    print(f"\nStep 2: Facebook pe upload...")
    try:
        upload_to_facebook(image_path, place["caption"])
    except Exception as e:
        print(f"   Upload error: {e}")

    print(f"\nAgla UK post {POST_INTERVAL_HOURS} ghante baad hoga...\n")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("   imanexis UK - Auto Post Script Shuru Ho Gaya!")
    print("   Har 1 ghante baad UK places post hoga.")
    print("="*50)

    while True:
        try:
            run_once()
            time.sleep(POST_INTERVAL_HOURS * 3600)
        except KeyboardInterrupt:
            print("\n\nScript band kar di gayi.")
            break
        except Exception as e:
            print(f"\nError: {e}")
            time.sleep(60)
