# apod_nasa
Python script to get (random) images from the Astronomy Picture Of the Day NASA api.

Windows: uses the default image viewer to open images.

Linux: uses imv by default for image viewing. If imv isn't found, uses feh.
Gifs should work too.


# Files
Gets hd images if available.
If a video is returned, it gets the thumbnail.

If an image has already been downloaded (title present in log file), it requests another image.

Saves every image in the folder `images` (create it in the same folder as the script).

Saves a `log.txt` in the same folder as the script, with the title and url of every downloaded image.

# How to  use
Get an api key from `https://api.nasa.gov/`

On line 4, replace `DEMO_KEY` with your freshly acquired api key (don't forget to save).
