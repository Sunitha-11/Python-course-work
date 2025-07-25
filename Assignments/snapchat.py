# App info (str, float, bool, NoneType)
app_name = "Snapchat"
version = 2.5
user_name = "Sunithasunisweety"
is_snapchat_plus = True
last_backup = None  # NoneType

# Snap score and average snaps (int, float)
snap_score = 15320
avg_daily_snaps = 75.6

# Friend streaks (tuple of tuples)
friend_streaks = (
    ("Bestie 💛", 145),
    ("BFF ❤", 212),
    ("Snap queen 👸", 300)
)

# Filters used (list + set)
filters_used = ["Dog Face 🐶", "Anime 😎", "VHS 🎥", "Dog Face 🐶"]
unique_filters = set(filters_used)

# Usage data (dict)
snap_usage = {
    "Stories": 34,
    "Snaps Sent": 89,
    "Snaps Received": 78,
    "Video Calls": 6
}

# Header using f-string
print(f"\n👋 Hello {user_name}, welcome to {app_name} v{version}")
print(f"📦 Snapchat+ User: {'Yes' if is_snapchat_plus else 'No'}")
print(f"📁 Last Cloud Backup: {last_backup}")

# Score using % formatting
print("\n📊 Snap Score Summary")
print(" - Snap Score: %d" % snap_score)
print(" - Avg Daily Snaps: %.1f" % avg_daily_snaps)

# Friend Streaks using .format()
print("\n🔥 Streaks:")
for name, days in friend_streaks:
    print(" - {:<15} : {} days".format(name, days))

# Filter usage using f-string and set
print("\n🎭 Filters You've Used:")
for filter_name in filters_used:
    print(f" - {filter_name}")

print(f"\n✅ Unique Filters Used: {', '.join(unique_filters)}")

# Usage stats using .format()
print("\n📈 Snap Activity Summary:")
for feature, count in snap_usage.items():
    print(" - {:<15}: {} times".format(feature, count))

# Combining all formatting styles
total_snaps = snap_usage["Snaps Sent"] + snap_usage["Snaps Received"]
print("\n📬 Total Snaps Exchanged: %d" % total_snaps)
print(f"🧮 Engagement Score: {total_snaps * avg_daily_snaps:.2f}")
