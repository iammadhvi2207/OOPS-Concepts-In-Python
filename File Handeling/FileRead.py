# from pathlib import Path

# path = Path("~/Desktop/Harshy.rtf").expanduser()

# try:
#     with path.open("r", encoding="utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#     print(f"File not found: {path}")
# except Exception as e:
#     print(f"Error reading file: {e}")

with open("/Users/madhvimishra/Desktop/harshit.txt", "r") as f:
    print(f.read())

