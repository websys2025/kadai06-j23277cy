# kadai6-2.py

# PokéAPI
# API概要：
#   ポケモンの名前、種族値をJSON形式で取得できます。
# エンドポイント（GET, JSON形式）：
#   https://pokeapi.co/api/v2/pokemon/<ポケモン名またはID>

# 機能：
# 好きなポケモン名を指定して、タイプや種族値を表示します。

# 使い方：
#   $ python kadai6-2.py pikachu
#   → ピカチュウのタイプや種族値を出力
# 英語で指定する。

import sys
import requests

def get_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    resp = requests.get(url)
    if resp.status_code != 200:
        print("ポケモンが見つかりませんでした。")
        return

    data = resp.json()
    print(f"=== {data['name'].title()} の情報 ===")
    types = [t['type']['name'] for t in data['types']]
    print("タイプ：", ", ".join(types))

    print("\n--- 種族値 ---")
    for stat in data['stats']:
        print(f"{stat['stat']['name'].title()}: {stat['base_stat']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python kadai6-2.py <ポケモン名>")
    else:
        get_pokemon_info(sys.argv[1])
