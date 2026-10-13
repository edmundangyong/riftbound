import json

input_file = "card_image_urls.json"
output_file = "clean_card_image_urls.json"

# 1. Load the original URLs
with open(input_file, "r", encoding="utf-8") as f:
    urls = json.load(f)

# 2. Strip everything after '?' for every URL
clean_urls = [url.split("?")[0] for url in urls]

# Optional: Deduplicate just in case any duplicates existed
clean_urls = list(dict.fromkeys(clean_urls))

# 3. Save the full-resolution links back to a new file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(clean_urls, f, indent=2)

print(f"Cleaned {len(clean_urls)} URLs!")
print(f"Sample full-res URL:\n{clean_urls[0]}")