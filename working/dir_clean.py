import os

# File extension list
filetypes = [".mp3", ".wav", ".aac", ".m4a",
             ".opus", ".mp4", ".mov", ".mpeg4",
             ".avi", ".wmv", "mpegps", ".flv",
             ".webm", ".3gpp", ".jpg", ".png",
             ".jpeg", ".gif"]


# Cleanup all downloaded, rendered and converted files.
def clean(root_dir):
    working_dir = os.listdir(root_dir)
    for item in working_dir:
        if item.endswith(tuple(filetypes)):
            os.remove(os.path.join(root_dir, item))
