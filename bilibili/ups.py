import json
import requests

from bilibili import video
import time


def get_up_video_text(up_id, pn):
    url = "https://api.bilibili.com/x/space/wbi/arc/search"

    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "buvid3=365F5C66-7C06-8AF2-A81F-CB7A87538FAA65905infoc; b_nut=1700582865; i-wanna-go-back=-1; b_ut=7; _uuid=B6A228D9-D4F3-9922-C5C5-21B3DBA9E16869325infoc; buvid_fp=22ac2391d6212751b37014b34b798cfd; buvid4=DDB3F8BD-72A3-C549-4E5B-F749F5C4C04F67051-023112116-; enable_web_push=DISABLE; SESSDATA=d89212b5%2C1716134903%2Ce0755%2Ab1CjDct1V3-FZV1zttjhweFPI1nj1sxUYmzPysU8qHr_VGMR-gpGuxIkHwHUcSfQAqWRUSVmg2ZUdpRjUzbUlrNHM5VVpDOWdkQWJWOVQ5Z00xRTdqdWZacTlfRnQwQ00wRDNsZDd2X05ad3lWb19nM1dGbjFTR3hITGZzak1aMXZ1cG5PckJTQV9BIIEC; bili_jct=b125838bcb66dad570b05fa6a915ba01; DedeUserID=3546562785446755; DedeUserID__ckMd5=484a172bad164c0f; CURRENT_FNVAL=4048; rpdid=0zbfVHg6N0|yvXuDsf2|1hN|3w1R5tja; header_theme_version=CLOSE; hit-dyn-v2=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDEwNjY1ODUsImlhdCI6MTcwMDgwNzMyNSwicGx0IjotMX0.Ybmpj4oVaK4vmKjB6FI4beFT7C-YsifgBvyCSwUzGak; bili_ticket_expires=1701066525; home_feed_column=5; browser_resolution=1536-835; bp_video_offset_3546562785446755=867454480352804882; PVID=3; b_lsid=6A37A39A_18C01A47C6B; sid=7o8qx2jo",
        "Origin": "https://space.bilibili.com",
        "Referer": "https://space.bilibili.com/413276548/video",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",

    }
    data  ={
        "mid": up_id,
        "ps": "30",
        "tid": "0",
        "pn": pn,
        "keyword": "",
        "order": " pubdate",
        "platform": " web",
        "web_location": "hello Bzhan",
        "order_avoided": " true",
        "dm_img_list": " []",
        "dm_img_str": "hello Bzhan",
        "dm_cover_img_str": "hello Bzhan",
        "w_rid": "hello Bzhan",
        "wts": "hello Bzhan",

    }
    up = requests.get(url=url, headers=header,params=data).text
    up_json = json.loads(up)
    return up_json


def get_up_video_list(up_id):
    list = []
    x = get_up_video_text(up_id, 1)
    pn = int(x["data"]["page"]["count"] / x["data"]["page"]["ps"] + 1)
    for pni in range(1, pn + 1):
        print(pni)
        x = get_up_video_text(up_id, pni)
        video_list = x["data"]["list"]["vlist"]
        for j in video_list:
            list.append(j["bvid"])
    return list