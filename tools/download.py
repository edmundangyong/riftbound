import json
import os
import urllib.request
from pathlib import Path

# Configuration
INPUT_JSON = "clean_card_image_urls.json"  # or "card_image_urls.json"
OUTPUT_DIR = Path("images")

def download_images():
    OUTPUT_DIR.mkdir(exist_ok=True)

    if not os.path.exists(INPUT_JSON):
        print(f"Error: Could not find {INPUT_JSON}. Make sure it is in the same folder.")
        return

    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        urls = json.load(f)

    # Clean query parameters on the fly just in case
    clean_urls = list(dict.fromkeys([u.split("?")[0] for u in urls]))
    total = len(clean_urls)
    print(f"Found {total} unique images to download.")

    for index, url in enumerate(clean_urls, start=1):
        filename = url.split("/")[-1]
        dest_path = OUTPUT_DIR / filename

        # Skip if already downloaded
        if dest_path.exists():
            print(f"[{index}/{total}] Already exists: {filename}")
            continue

        try:
            # Provide standard browser headers so the CDN doesn't block the request
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            )
            with urllib.request.urlopen(req) as response, open(dest_path, "wb") as out_file:
                out_file.write(response.read())
            print(f"[{index}/{total}] Downloaded: {filename}")
        except Exception as e:
            print(f"[{index}/{total}] Failed to download {filename}: {e}")

    print("\nDownload complete! Images are saved in the 'images/' folder.")

if __name__ == "__main__":
    download_images()