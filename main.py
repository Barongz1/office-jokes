"""One-Line Office Jokes — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: the printer only jams near deadlines — it smells fear and feeds on quarterly reviews.
TEXT = "Our printer only jams when the deadline is near. I think it can smell fear, and it feeds on my quarterly reviews."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
