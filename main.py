#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:30:25 2023

@author: lou
"""

import scrapetube
import re
import itertools
from yt_dlp import YoutubeDL
videos = scrapetube.get_channel("UC4eYXhJI4-7wSWc8UNRwD4A")
videos1, videos2 = itertools.tee(videos)
ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                        }],
                    }
                




import os
root_dir = ""
data_files = os.listdir()
tot = len([j for j in videos2])
print(tot)
count = 0
for video in videos1:
    
    with YoutubeDL(ydl_opts) as ydl:
      info_dict = ydl.extract_info("https://www.youtube.com/watch?v="+video["videoId"], download=False)
      video_url = info_dict.get("url", None)
      video_id = info_dict.get("id", None)
      video_title = info_dict.get('title', None)
      video_desc = info_dict.get('description', None).split()
    i = 0
    tiny = False
    while i< len(video_desc)-1:
        if video_desc[i].lower()=="set" and video_desc[i+1].lower()=="list":
            tiny = True
            count +=1
            break
        i+=1
    already_down = False
    for n in data_files:
        if re.split(":|：",video_title)[0] in re.split(":|：",n)[0]:
            print(n+": Already downloaded")
            already_down=True
            break
    
    
    if tiny and not already_down:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download("https://www.youtube.com/watch?v="+video["videoId"])
    print(str(count)+" concerts already downloaded.")
    print("About "+str(int(100*count/tot))+"% done")
