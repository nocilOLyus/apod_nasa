# apod_nasa
Python script to get (random) images from the Astronomy Picture Of the Day NASA api.

Works only in windows (for now), uses the default image viewer to open images.
Gifs should work too.

Gets hd images if available.
If a video is returned, it gets the thumbnail.

# Files
Saves every image in images\
Saves a log.txt in the same folder as the script, with the title and url of every downloaded images.
If an image has already been downloaded (title present in log file), it requests another image.

# How to  use
Get an api key from https://api.nasa.gov/
On line 4, replace `DEMO_KEY` with your freshly acquired api key (don't forget to save).
Run from anywhere (IDE, console, double click...) and enjoy.
