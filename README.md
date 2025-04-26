# 🔐 Log File Analyzer (Python)

This Python script simulates a basic log analysis tool that scans system log files to detect:
- 🚨 Failed login attempts
- 🌙 Successful logins during suspicious hours (12AM–6AM)

It’s a great foundational project for anyone exploring cybersecurity, health IT, or IT support roles.

---

## 📂 Project Files

| File | Description |
|------|-------------|
| `Log File Analyzer.py` | Main Python script that parses logs and flags suspicious behavior |
| `system_logs.txt`      | Sample system log file used for analysis |
| `README.md`            | Project overview and documentation |

---

## 🧠 What It Does

- Reads from a structured text log file
- Parses timestamps and login actions
- Flags:
  - All `LOGIN_FAILURE` events
  - Any `LOGIN_SUCCESS` between 12AM–6AM
- Outputs a clean, human-readable summary report

---

## 🛠️ Sample Log Entry Format

```plaintext
2025-04-25 01:15:23 LOGIN_SUCCESS user1
2025-04-25 02:44:10 LOGIN_FAILURE user2
