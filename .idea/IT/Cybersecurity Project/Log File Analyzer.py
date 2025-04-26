from datetime import datetime

log_file = "system_logs.txt"

SUSPICIOUS_HOURS = range(0, 6)

failed_logins = []
odd_hour_logins = []


with open(log_file, 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) != 4:
            continue

        date_str, time_str, status, user = parts

        # timestamp.hour = datetime.strptime(date.string(f"{date_str} {time_str}"), format="%Y-%m-%d %H:%M:%S")
        timestamp = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
        hour = timestamp.hour

        if status == "LOGIN_FAILURE":
            failed_logins.append((timestamp, user))

        if status == "LOGIN_SUCCESS" and hour in SUSPICIOUS_HOURS:
            odd_hour_logins.append((timestamp, user))

print("\n🚨 Failed Login Attempts")
for ts, user in failed_logins:
    print(f"User: {user} at {ts}")

print("\n🌙 Logins During Suspicious Hours (12AM - 6AM)")
for ts, user in odd_hour_logins:
    print(f"User: {user} at {ts}")