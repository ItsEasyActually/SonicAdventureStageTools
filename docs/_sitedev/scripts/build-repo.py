from nt import mkdir
from pathlib import Path
import requests

extensions_dir = Path("docs\\extensions")
asset_name = "SonicAdventureStageTools.zip"
repo = "https://api.github.com/repos/ItsEasyActually/SonicAdventureStageTools"
releases = f"{repo}/releases"

def get_releases():
    response = requests.get(releases)
    if response.status_code == 200:
        data = response.json()
        stable = None
        dev = None
        for r in data:
            if r['tag_name'].__contains__("beta"):
                dev = r
                break

        return stable, dev

def download_asset(release = None):
    if release != None:
        for asset in release['assets']:
            if asset['name'] == asset_name:
                headers = {"Accept": "application/octet-stream"}
                response = requests.get(asset['url'], headers=headers, stream=True, timeout=60)
                filepath = extensions_dir / asset_name
                with filepath.open("wb") as f:
                    f.write(response.content)

def main() -> None:
    stable, dev = get_releases()
    if extensions_dir.exists() == False:
        extensions_dir.mkdir(parents=True, exist_ok=True)
    download_asset(dev)

if __name__ == "__main__":
    main()