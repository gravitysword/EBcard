a = """Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding:
gzip, deflate
Accept-Language:
zh-CN,zh;q=0.9
Cache-Control:
max-age=0
Connection:
keep-alive
Cookie:
JSESSIONID=C43CF3B233169498BFE44882E753CD13
Host:
120.27.145.118
If-Modified-Since:
Mon, 11 Dec 2023 07:59:39 GMT
If-None-Match:
"6576c16b-295e"
Upgrade-Insecure-Requests:
1
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"""

i = 1
re = ""
for x in a.split("\n"):
    if i%2 :
        x = x.replace(":","")
        re += "\"" +x+"\":"
    else:
        x = x.replace("\"","\\\"")
        re += "\"" +x+"\",\n"
    i=i+1
print(re)



















