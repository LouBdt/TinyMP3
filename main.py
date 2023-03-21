#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:30:25 2023

@author: lou
"""

import scrapetube
from yt_dlp import YoutubeDL
videos = scrapetube.get_channel("UC4eYXhJI4-7wSWc8UNRwD4A")

ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                        }],
                    }
                
 for video in videos:
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
            break
        i+=1
    if tiny:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download("https://www.youtube.com/watch?v="+video["videoId"])
