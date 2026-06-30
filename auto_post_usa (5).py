"""
Sweet USA - Auto Post Script
USA ki famous places ki images aur descriptions
Har 1 ghante baad automatically post hoga
"""

import requests
import urllib.parse
import time
import random
from datetime import datetime

# ============================================================
FB_PAGE_ACCESS_TOKEN = "EAAhVgRWi8XUBR1thgZBBKdqMhWrm33G8ZC8rGEVjs0t302LZA3uib913icawWggSICinsDCpQxK0DovurKFGtbcnZBDpEFznjBYiR6JK2JVVgQzE79mbrFzmCUwO8WorrrN7eao4vKh1h7vaNEAIpujqwsLdXZCSziXObmST0v2wqpiiBQQ5FvjIgWFViAsxUKgIFh1clxuurv72aPBZBnLJUYM0nxUpJtDoLApAEZD"
FB_PAGE_ID           = "61591540706915"
POST_INTERVAL_HOURS  = 1
# ============================================================

USA_PLACES = [
    {
        "prompt": "Grand Canyon Arizona USA, breathtaking aerial view, vivid red and orange rock layers, dramatic landscape, golden hour lighting, ultra realistic photo",
        "caption": "🏜️ Grand Canyon, Arizona\n\nOne of the world's greatest natural wonders! Carved by the Colorado River over millions of years, the Grand Canyon stretches 277 miles long and up to 18 miles wide. A must-visit destination in the USA! 🇺🇸\n\n#GrandCanyon #Arizona #USA #Travel #NatureLovers #AmericanWonders"
    },
    {
        "prompt": "Statue of Liberty New York Harbor USA, iconic green statue, blue sky, boats in water, ultra realistic professional photo",
        "caption": "🗽 Statue of Liberty, New York\n\nA symbol of freedom and democracy! Lady Liberty stands 305 feet tall and has welcomed millions of immigrants to America since 1886. One of the most recognizable landmarks in the world! 🇺🇸\n\n#StatueOfLiberty #NewYork #NYC #USA #Travel #Freedom #AmericanIcons"
    },
    {
        "prompt": "Yellowstone National Park USA, colorful hot springs Grand Prismatic Spring, aerial view, vivid blue green yellow colors, steam rising, ultra realistic",
        "caption": "🌋 Yellowstone National Park, Wyoming\n\nAmerica's first national park and one of the most geologically unique places on Earth! Home to the Grand Prismatic Spring — the largest hot spring in the USA with stunning rainbow colors. Simply magical! 🇺🇸\n\n#Yellowstone #NationalPark #Wyoming #USA #Travel #Nature #Geothermal"
    },
    {
        "prompt": "Golden Gate Bridge San Francisco California USA, iconic red bridge, fog rolling in, bay view, sunrise lighting, ultra realistic professional photography",
        "caption": "🌉 Golden Gate Bridge, San Francisco\n\nOne of the most photographed bridges in the world! This iconic suspension bridge spans 1.7 miles across the San Francisco Bay and took 4 years to build. A true engineering masterpiece! 🇺🇸\n\n#GoldenGateBridge #SanFrancisco #California #USA #Travel #Architecture"
    },
    {
        "prompt": "Times Square New York City USA night, bright neon lights, busy streets, yellow taxis, crowds of people, vibrant colors, ultra realistic photo",
        "caption": "✨ Times Square, New York City\n\nThe crossroads of the world! Times Square dazzles with over 40 million visitors every year. With its iconic billboards, Broadway theaters, and electric energy — there's no place quite like it! 🇺🇸\n\n#TimesSquare #NewYork #NYC #USA #Travel #Manhattan #CityLife"
    },
    {
        "prompt": "Niagara Falls USA Canada border, massive waterfall, rainbow in mist, aerial view, dramatic water flow, ultra realistic professional photo",
        "caption": "💧 Niagara Falls, New York\n\nOne of the most powerful waterfalls in North America! Over 3,160 tons of water flows over Niagara Falls every second. The mist creates beautiful rainbows that can be seen for miles! 🇺🇸\n\n#NiagaraFalls #NewYork #USA #Travel #Waterfall #NaturalWonder"
    },
    {
        "prompt": "Mount Rushmore South Dakota USA, four presidents carved in granite mountain, blue sky, American flags, ultra realistic professional photo",
        "caption": "🗿 Mount Rushmore, South Dakota\n\nA monument to American greatness! The faces of Presidents Washington, Jefferson, Roosevelt, and Lincoln are carved into a granite mountain. Standing 60 feet tall each, this took 14 years to complete! 🇺🇸\n\n#MountRushmore #SouthDakota #USA #Travel #AmericanHistory #Presidents"
    },
    {
        "prompt": "Antelope Canyon Arizona USA, narrow slot canyon, beams of light streaming through, orange red rock walls, magical lighting, ultra realistic photo",
        "caption": "🌟 Antelope Canyon, Arizona\n\nNature's own light show! This stunning slot canyon was carved by flash floods over thousands of years. The way sunlight beams through the narrow openings creates an absolutely magical experience! 🇺🇸\n\n#AntelopeCanyon #Arizona #USA #Travel #NaturePhotography #HiddenGem"
    },
    {
        "prompt": "Hawaii beach Waikiki Honolulu sunset, palm trees, crystal clear blue ocean, surfers, volcanic mountains background, ultra realistic professional photo",
        "caption": "🌺 Waikiki Beach, Hawaii\n\nParadise found! Hawaii's most famous beach stretches along the shores of Honolulu with perfect waves for surfing and stunning sunsets over the Pacific Ocean. Truly one of America's most beautiful destinations! 🇺🇸\n\n#Hawaii #Waikiki #Honolulu #USA #Travel #BeachLife #Paradise"
    },
    {
        "prompt": "Las Vegas Strip Nevada USA night, bright casino lights, luxury hotels, Bellagio fountains, desert city skyline, ultra realistic professional photography",
        "caption": "🎰 The Las Vegas Strip, Nevada\n\nThe entertainment capital of the world! The Las Vegas Strip is home to the most spectacular hotels, casinos, and shows on the planet. At night, the dazzling lights can even be seen from space! 🇺🇸\n\n#LasVegas #Nevada #USA #Travel #Entertainment #CityLights #Vegas"
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
    print(f"  USA - Time: {now}")
    print(f"{'='*50}")

    place = random.choice(USA_PLACES)

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

    print(f"\nAgla USA post {POST_INTERVAL_HOURS} ghante baad hoga...\n")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("   Sweet USA - Auto Post Script Shuru Ho Gaya!")
    print("   Har 1 ghante baad USA places post hoga.")
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
