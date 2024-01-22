import json
import requests
import os

import cv2

def is_video_playable(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return False
    else:
        cap.release()
        return True

def get_video(BV_id):
    try:
        os.makedirs("C:/pythom_EBcard/py_bilibili/video/" + BV_id)
    except:
        pass
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }
    video = requests.get("https://www.bilibili.com/video/" + BV_id + "/", headers=header).text
    start = "window.__playinfo__="
    end = "</script>"
    a = video.find(start)
    video_text = video[a + len(start): video.find(end, a)].replace("window.__playinfo__=", "")
    video_json = json.loads(video_text)
    video_video_url_list = video_json["data"]["dash"]["video"]
    video_audio_url_list = video_json["data"]["dash"]["audio"]
    for i in video_video_url_list:
        video_video_url = i["base_url"]
        video_video = requests.get(video_video_url, headers=header).content
        with open("C:/pythom_EBcard/py_bilibili/video/" + BV_id + "/video.mp4", "wb") as f:
            f.write(video_video)
        if is_video_playable("C:/pythom_EBcard/py_bilibili/video/" + BV_id + "/video.mp4"):
            break
        else:
            continue

    for i in video_audio_url_list:
        video_audio_url = i["base_url"]
        video_audio = requests.get(video_audio_url, headers=header).content
        with open("C:/pythom_EBcard/py_bilibili/video/" + BV_id + "/audio.mp3", "wb") as f:
            f.write(video_audio)
        if is_video_playable("C:/pythom_EBcard/py_bilibili/video/" + BV_id + "/audio.mp3"):
            break
        else:
            continue

    print("下载完成,存储路径：" + "C:/pythom_EBcard/py_bilibili/video/" + BV_id + "\n")
    start = "window.__INITIAL_STATE__="
    end = '''</script>'''
    a = video.find(start) + len(start)
    b = video.find(end, a)
    video_details = json.loads(video[a:b].replace(
        ";(function(){var s;(s=document.currentScript||document.scripts[document.scripts.length-1]).parentNode.removeChild(s);}());",
        ""))

    likes = video_details["videoData"]["stat"]["like"]
    view = video_details["videoData"]["stat"]["view"]
    reply = video_details["videoData"]["stat"]["reply"]
    biji = video_details["videoData"]["stat"]["danmaku"]
    favorite = video_details["videoData"]["stat"]["favorite"]
    coin = video_details["videoData"]["stat"]["coin"]
    share = video_details["videoData"]["stat"]["share"]
    title = video_details["videoData"]["title"]
    tag = video_details["tags"]
    tags = []
    for i in tag:
        tags.append(i["tag_name"])
    author_id = video_details["upData"]["mid"]
    author_name = video_details["upData"]["name"]

    start = "<span class=\"pubdate-text\""
    end = "</span>"
    a = video.find(start) + len(start)
    a = video.find(">", a) + 1
    b = video.find(end, a)
    pub_time = video[a:b].replace(" ", "", 10000).replace("\n", "", 10000)
    arr = {
        "likes": likes,
        "reply": reply,
        "view": view,
        "biji": biji,
        "favorite": favorite,
        "coin": coin,
        "share": share,
        "title": title,
        "author_id": author_id,
        "author_name": author_name,
        "pub_time": pub_time,
        "tags": tags
    }
    return arr


def get_dynamic(BV_id):
    try:
        os.makedirs("/pythom_EBcard/py_bilibili/picture/" + BV_id)
    except:
        pass

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }
    data = {
        "id": BV_id
    }
    dynamic = requests.get("https://api.bilibili.com/x/polymer/web-dynamic/v1/detail", headers=header, params=data).text
    dynamic_json = json.loads(dynamic)

    a1 = dynamic_json["data"]["item"]["modules"]["module_stat"]
    comments = a1["comment"]["count"]
    forwards = a1["forward"]["count"]
    likes = a1["like"]["count"]
    a2 = dynamic_json["data"]["item"]["modules"]["module_dynamic"]
    try:
        text = a2["major"]["opus"]["summary"]["text"]
        title = a2["major"]["opus"]["title"]
    except:
        text = a2["desc"]["text"]
        title = "NULL"

    a3 = dynamic_json["data"]["item"]["modules"]["module_author"]
    author_id = a3["mid"]
    author_name = a3["name"]
    pub_time = a3["pub_time"]

    try:
        pictures = a2["major"]["opus"]["pics"]
        m = 0
        for i in pictures:
            picture_url = i["url"]
            print(picture_url)
            picture_picture = requests.get(picture_url).content

            with open("C:/pythom_EBcard/py_bilibili/picture/" + BV_id + "/" + str(m) + ".jpg", "wb") as f:
                f.write(picture_picture)
                m += 1
    except:
        pictures = a2["major"]["draw"]["items"]
        m = 0
        for i in pictures:
            picture_url = i["src"]
            print(picture_url)
            picture_picture = requests.get(picture_url).content
            with open("C:/pythom_EBcard/py_bilibili/picture/" + BV_id + "/" + str(m) + ".jpg", "wb") as f:
                f.write(picture_picture)
            m += 1

    arr = {
        "likes": likes,
        "comments": comments,
        "forwards": forwards,
        "title": title,
        "text": text,
        "author_id": author_id,
        "author_name": author_name,
        "pub_time": pub_time
    }

    return arr



