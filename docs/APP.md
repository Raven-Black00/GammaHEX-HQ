# App — GammaHEX-HQ 1.0.0

**Starting version:** `1.0.0`  
**File name:** `GammaHEX_HQ.py`  
**Mark:** RavenBlack  
**Engine:** GammaHex1300 / RavenMiner HQ 5.9.3.11 (retired name)

## Run

```bash
pip install -r requirements.txt
python GammaHEX_HQ.py
```

`assets/` must sit next to the script (startup horn, raven marks, lightning frames).

Version is the constant `_APP_VER` inside the script, also written in the repo root `VERSION` file. Do not put the version in the filename.

Runtime config stays `ravenminer_config.json` / `ravenminer_alerts.json` / `ravenminer_ntfy_sent.json` so existing desks keep their settings.
