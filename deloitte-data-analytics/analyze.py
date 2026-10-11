import json
from collections import Counter

with open("daikibo-telemetry-data.json", encoding="utf-8") as f:
    rows = json.load(f)

# Unhealthy = 10 minutes of downtime per unhealthy status message
by_factory = Counter()
by_factory_device = Counter()
for r in rows:
    if r["data"]["status"] == "unhealthy":
        fac = r["location"]["factory"]
        by_factory[fac] += 10
        by_factory_device[(fac, r["deviceType"])] += 10

print("Down Time per Factory (minutes)")
for fac, m in by_factory.most_common():
    print(f"  {fac:28s} {m:6d}")

top = by_factory.most_common(1)[0][0]
print(f"\nDown Time per Device Type @ {top}")
for (fac, dev), m in sorted(by_factory_device.items(), key=lambda x: -x[1]):
    if fac == top:
        print(f"  {dev:20s} {m:6d}")
