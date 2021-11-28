import subprocess
import requests

base_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"       # Replace DEMO_KEY with your api key.
parameters = "&count=1&thumbs=true"                                     # (because of the count=1, we get a single dictionary in a list,
                                                                        # but it's necessary to get a random image everytime.)
media = filename = image_url = ""
while True:
    while media != "image":
        request = requests.get(base_url + parameters)
        apod_json = request.json()
        media = apod_json[0]["media_type"]

    if "hdurl" in apod_json[0]: key = "hdurl"
    else: key = "url"
    image_url = apod_json[0][key]
    with open("log.txt", "r") as l:
        if image_url in l:
            continue
        else:
            break

title = apod_json[0]["title"]
for char in title:
    if char in '<>:"/\|?* ':
        filename += "_"
    elif char != ",.":
        filename += char
filename += ".jpg"
print(f"{apod_json}\n{filename}")

image = requests.get(image_url)
with open(f"images\\{filename}", "wb") as f:
    f.write(image.content)

with open("log.txt", "a") as l:
    log = f"{title}\n\t{image_url}\n"
    l.write(log)

subprocess.Popen(f"explorer images\\{filename}")