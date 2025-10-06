import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

# ✅ Task 1: Move all .jpg files to a new folder
def move_jpg_files():
    source_folder = input("Enter source folder path: ")
    dest_folder = input("Enter destination folder path: ")

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    moved_count = 0
    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder, file))
            moved_count += 1
    print(f"✅ Moved {moved_count} JPG file(s).")


# ✅ Task 2: Extract all emails from a .txt file
def extract_emails():
    input_file = input("Enter input .txt file name: ")
    output_file = input("Enter output .txt file name: ")

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

    with open(output_file, "w", encoding="utf-8") as f:
        for email in set(emails):
            f.write(email + "\n")

    print(f"✅ Extracted {len(set(emails))} unique email(s). Saved to {output_file}")


# ✅ Task 3: Scrape title of a webpage
def scrape_title():
    url = input("Enter webpage URL: ")
    output_file = input("Enter output .txt file name: ")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(title)

    print(f"✅ Title extracted and saved: {title}")


# ✅ Main Menu
def main():
    while True:
        print("\n=== Python Task Automation ===")
        print("1. Move all .jpg files to a new folder")
        print("2. Extract all email addresses from a .txt file")
        print("3. Scrape the title of a webpage and save it")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_title()
        elif choice == "4":
            print("Exiting... Goodbye 👋")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
