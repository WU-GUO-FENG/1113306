import requests
import json

def API_fetching():
    # 抓取百變怪的資料
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # 儲存成 JSON 檔案
            with open("pokemon_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("寶可夢資料抓取成功！檔案已儲存為 pokemon_data.json")
        else:
            print(f"抓取失敗，錯誤代碼：{response.status_code}")
    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    API_fetching()