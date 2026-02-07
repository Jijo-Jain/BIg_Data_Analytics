import sys
import json

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        obj = json.loads(line)
    except Exception:
        continue

    for playlist in obj.get("playlists", []):
        for track in playlist.get("tracks", []):
            uri = track.get("track_uri")
            if uri:
                print(f"{uri}\t1")
