import requests
import json

def search_huawei_appgallery(keyword, limit=10):
    url = f"https://web-drru.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&serviceType=20&uri=searchApp%2F{keyword}&appid="
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://appgallery.huawei.com/",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://appgallery.huawei.com"
    }

    proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}

    response = requests.get(url, headers=headers, proxies=proxies)

    if response.status_code != 200:
        print(f"❌ Error: Unable to fetch data from Huawei AppGallery (Status Code: {response.status_code})")
        return []

    data = response.json()
    
    apps = []
    if "layoutData" in data:
        app_list = data["layoutData"][0]["dataList"][:limit]
        for app in app_list:
            apps.append({
                "name": app.get("name", "N/A"),
                "app_id": app.get("appid", "N/A"),
                "developer": app.get("developer", "N/A"),
                "category": app.get("kindName", "N/A"),
                "rating": app.get("score", "N/A"),
                "reviews": app.get("commentCount", "N/A"),
                "downloads": app.get("downCountDesc", "N/A"),
                "url": f"https://appgallery.huawei.com/#/app/{app.get('appid', '')}"
            })
    
    return apps

# Example usage
keyword = "payment"
huawei_apps = search_huawei_appgallery(keyword)
print(json.dumps(huawei_apps, indent=4, ensure_ascii=False))
