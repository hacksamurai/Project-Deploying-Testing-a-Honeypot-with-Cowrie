import json
from collections import Counter
ip_counter = Counter()
with open("/home/honeypot/cowrie/var/log/cowrie", "r") as file:
    for line in file:
        try:
            log = json.loads(line)
            if "src_ip" in log:
                ip_counter[log["src_ip"]] += 1
        except json.JSONDecodeError:
            continue  # Skip lines that are not valid JSON
# Display the most common attacker IPs
print("Attacker IPs (Sorted by Frequency):")
for ip, count in ip_counter.most_common():
    print(f"{ip}: {count} times")