import subprocess
import platform
import requests

system = platform.system()
base_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
parameters = "&count=1&thumbs=true"                                     
                                                                       
restart = 'y'
while restart[0] == 'y':
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

    with open("log.txt", "a") as l:
        log = f"{title}\n\t{image_url}\n"
        l.write(log)

    print(f"-------\n|\tDownloading {filename}...")

    image = requests.get(image_url)
    image_size = int(image.headers["Content-Length"])
    print(f"|\tSize: {round(image_size / 1000, 2)} kB\t{round(image_size / 1_000_000, 2)} MB\n-------")
    
    if system == "Windows":
        with open(f"images\\{filename}", "wb") as f:
            f.write(image.content)
        subprocess.Popen(f"explorer images\\{filename}")
    elif system == "Linux":
        with open(f"images/{filename}", "wb") as f:
            f.write(image.content)
        try:
            subprocess.Popen(["imv", f"images/{filename}"])
        except FileNotFoundError:
            subprocess.Popen(["feh", f"images/{filename}"])

    restart = input(f"\n\nDownload another image ? (Y/n): ").lower()
    if len(restart) == 0 or restart == "\n": restart = 'y'
    
    print()
