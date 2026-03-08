import os
import sys
import requests

OUTLOOK_ICS_URL = os.environ.get("OUTLOOK_ICS_URL")
if not OUTLOOK_ICS_URL:
    print("Error: OUTLOOK_ICS_URL environment variable is not set.", file=sys.stderr)
    sys.exit(1)

OUTPUT_PATH = "docs/calendar.ics"

print(f"Fetching ICS feed...")
response = requests.get(OUTLOOK_ICS_URL, timeout=30)
response.raise_for_status()

original = response.text
fixed = original.replace("Pacific Standard Time", "Customized Time Zone")

replacements = original.count("Pacific Standard Time")
print(f"Replaced {replacements} instance(s) of 'Pacific Standard Time' with 'Customized Time Zone'.")

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(fixed)

print(f"Saved corrected ICS to {OUTPUT_PATH}.")
