# 08_File_Handling_examples.py

"""
Step-by-step guide to Python File Handling.
Demonstrates context managers, efficient reading, and JSON serialization.
"""

import json
from pathlib import Path

# 1. Writing to a file (Standard Text)
print("--- Writing Data ---")
lines_to_write = [
    "Expert Topic: File Handling\n",
    "Rule #1: Always use context managers.\n",
    "Rule #2: Specify encoding='utf-8'.\n"
]

with open("expert_log.txt", "w", encoding="utf-8") as file:
    file.writelines(lines_to_write)
print("Data written to expert_log.txt")

# 2. Efficient Reading (Line-by-line)
print("\n--- Reading Data (Efficiently) ---")
if Path("expert_log.txt").exists():
    with open("expert_log.txt", "r", encoding="utf-8") as file:
        # Iterating over the file object is memory-efficient for large files
        for i, line in enumerate(file, start=1):
            print(f"L{i}: {line.strip()}")

# 3. JSON Handling (Modern Standards)
print("\n--- JSON Serialization ---")
user_profile = {
    "username": "sriram_dev",
    "skills": ["Python", "Django", "Data Science"],
    "active": True
}

# Writing JSON
with open("profile.json", "w") as f:
    json.dump(user_profile, f, indent=4)
print("Profile saved to profile.json")

# Reading JSON
with open("profile.json", "r") as f:
    loaded_data = json.load(f)
    print(f"Loaded User: {loaded_data['username']}")

# 4. Exclusive Creation (Safety Check)
print("\n--- Safety Mode ('x') ---")
try:
    with open("expert_log.txt", "x") as f:
        f.write("This will fail because the file exists.")
except FileExistsError:
    print("Safety Triggered: Cannot overwrite 'expert_log.txt' in 'x' mode.")
