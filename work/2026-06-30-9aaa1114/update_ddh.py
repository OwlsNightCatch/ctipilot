import json
TODAY="2026-06-30"
with open("state/deep_dive_history.json") as f: d=json.load(f)
d["entries"].append({
    "date":TODAY,
    "category":"ransomware-affiliate",
    "title":"Bumblebee → AdaptixC2 → Akira: SEO-poisoning-to-ransomware kill chain (DFIR Report; Swisscom B2B CSIRT parallel intrusion)",
    "primary_cve":"",
    "brief_path":f"briefs/{TODAY}.md"
})
d["entries"]=d["entries"][-30:]
d["last_updated"]=TODAY
with open("state/deep_dive_history.json","w") as f: json.dump(d,f,indent=2,ensure_ascii=False); f.write("\n")
print("deep_dive_history entries:", len(d["entries"]))
