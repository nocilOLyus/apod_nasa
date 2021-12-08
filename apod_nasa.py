import subprocess
import requests

base_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"       # Replace DEMO_KEY by your api key.
parameters = "&count=1&thumbs=true"                                     # because of the count=1, we get a single dictionary in a list,
                                                                        # but it's necessary to get a random image everytime.
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
    if char in '<>:"/\|?*\r\n ':
        filename += "_"
    elif char not in ",.":
        filename += char
filename += ".jpg"
#print(apod_json)
print(filename)

image = requests.get(image_url)
image_size = int(image.headers["Content-Length"])
print(f"Size: {round(image_size / 1000, 2)} kB\t{round(image_size / 1_000_000, 2)} MB")
with open(f"images\\{filename}", "wb") as f:
    f.write(image.content)

with open("log.txt", "a") as l:
    log = f"{title}\n\t{image_url}\n"
    l.write(log)

subprocess.Popen(f"explorer images\\{filename}")
