# Hashtag Extraction
import re

s = input("enter social media post: ")

hashtags = re.findall(r"#[a-zA-Z0-9_]+",s)

print("hashtags =",hashtags)
