# 43th github project --> Time Zone Converter
print('----------Time Zone Converter----------')
from datetime import datetime
from zoneinfo import ZoneInfo


def main():
    print("TIME ZONE CONVERTER")
    print("Example zones: America/New_York, Europe/London, Asia/Tokyo\n")

    try:
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        hour = int(input("Hour (0-23): "))
        minute = int(input("Minute: "))
    except ValueError:
        print("Enter valid numbers.")
        return

    from_zone = input("From time zone: ").strip()
    to_zone = input("To time zone: ").strip()

    try:
        source_tz = ZoneInfo(from_zone)
        target_tz = ZoneInfo(to_zone)
    except Exception:
        print("Invalid time zone name.")
        return

    dt = datetime(year, month, day, hour, minute, tzinfo=source_tz)
    converted = dt.astimezone(target_tz)

    print(f"\n{dt.strftime('%Y-%m-%d %H:%M %Z')} ({from_zone})")
    print(f"= {converted.strftime('%Y-%m-%d %H:%M %Z')} ({to_zone})")



main()