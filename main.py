import time
import os
from bilibili.video.download import *
from bilibili.ups import *

path = os.getcwd()
up_id = "1069912452"

ups_video = get_up_video_list(up_id)
for i in ups_video:
    print("Start to download :" + i)
    download_video(i,path)
    time.sleep(1)

