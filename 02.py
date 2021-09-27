sec = int(input("Enter time in seconds: "))

print(f"{sec // 3600:02}:{sec % 3600 // 60:02}:{sec % 60:02}")

if sec < 60:
    print(f"00:00:{sec}")
elif sec < 360:
    print(f"00:{sec // 60}:{sec % 60}")
else:
    print(f"{sec // 3600:02}:{sec % 3600 // 60:02}:{sec % 60:02}")