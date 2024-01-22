a = """mid: 413276548
ps: 30
tid: 0
pn: 1
keyword: 
order: pubdate
platform: web
web_location: 1550101
order_avoided: true
dm_img_list: []
dm_img_str: V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ
dm_cover_img_str: QU5HTEUgKEludGVsLCBJbnRlbChSKSBVSEQgR3JhcGhpY3MgKDB4MDAwMDQ2OEIpIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpR29vZ2xlIEluYy4gKEludGVsKQ
w_rid: 622e097f9779116698d6eeef18d89548
wts: 1700834613"""

i = 1
re = ""
for x in a.split("\n"):
    re += "\""+x.replace(":","\":\"")+"\",\n"
print(re)








