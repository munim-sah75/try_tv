import requests
from bs4 import BeautifulSoup
import time

def update_m3u():
    url = "https://raw.githubusercontent.com/Hasanmahmud000/BDStreamHub-/refs/heads/main/index.html"
    keyword = "Jalsha Movies"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error HTTP statuses

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the desired lines
        target_lines = []
        for line in soup.find_all(text=True):
            if keyword in line:
                target_lines.append(line.strip())
                next_line = line.next_sibling.strip()
                target_lines.append(next_line)
                break  # Assuming only one match is needed

        # Update the new.m3u file
        with open("new.m3u", "w") as f:
            f.write("\n".join(target_lines))

        print("new.m3u updated successfully!")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching or parsing the HTML: {e}")

# Schedule the task using a library like schedule
import schedule
import time

def job():
    update_m3u()

schedule.every().day.at("19:04").do(job)  # Run at midnight every day

while True:
    schedule.run_pending()
    time.sleep(1)
