<p align="center">
  <img src="docs/brand/banner.svg" alt="RavenBlack — GammaHEX-HQ" width="100%">
</p>

# GammaHEX-HQ

**v5.9.5** · **RavenBlack** · Python 3.9+ · Windows (core dashboard is cross-platform) · MIT

GUI and firmware for the Bitaxe Hex (6 ASIC) miner — a live telemetry command center for the Bitaxe / NerdQAxe family. Animated gauges, thermal watch, ntfy.sh alerts, system-tray integration.

The working title **RavenMiner HQ is retired.** This repo and product are **GammaHEX-HQ**, under the **RavenBlack** mark.

Source of truth on GitHub: **[Raven-Black00/GammaHEX-HQ](https://github.com/Raven-Black00/GammaHEX-HQ)**.

It speaks the AxeOS local API (`/api/system/info`) that every board in this lineage still exposes: NerdQAxe, NerdQAxe+ / ++, NerdOCTAXE, Bitaxe Gamma, Bitaxe Hex, and Satoshi-branded cousins. The current build is named for what it grew into:

`Ravenminer_HQ_5_9_5_BitaxeGammaHex_Satoshi_CurrGauge100A.py`

- **5.9.5** — current command-center build
- **BitaxeGammaHex** — first-class Gamma and Hex telemetry
- **Satoshi** — Solo Satoshi / Satoshi-branded hardware in the same API family
- **CurrGauge100A** — 100-amp current needle for high-draw Hex-class rails

---

## Why this exists

Alan (Son of Odin) runs the desk this was forged for. The first boards there were **NerdQAxe** machines — the quad-chip miners that proved multi-ASIC open-source mining was not a stunt. AxeOS (and the NerdQAxePlus firmware fork) already had a browser dashboard. What was missing was a **Windows command center**: always-on gauges, thermal push alerts that survive a closed laptop lid, a tray icon that still shows hashrate, and a celebration when a block actually lands.

GammaHEX-HQ is that layer. It does not replace firmware. It watches the same JSON the miner already publishes, and it grew up in lockstep with the hardware — from the original NerdQAxe through every revision that followed.

Forged by **Selene / Perplexity AI** for Alan.

---

## From NerdQAxe: inception to every change along the way

GammaHEX-HQ is a desktop app. Its *subject* is a decade-compressed hardware story. This is that story, in order, because the dashboard only makes sense if you know which board is talking.

### 0. The two roots (2023)

Two projects, different jobs, same community.

**NerdMiner** (BitMaker) put a lottery miner on an ESP32 with a color screen. Hashrate was tens of kH/s — a teaching toy, not a ticket. In a month, thousands of people had one on a desk. The point was participation.

**Bitaxe** (Skot / skot9000, stewarded by Open Source Miners United) put a real Bitmain ASIC on an open board. Hardware under CERN-OHL-S, firmware (ESP-Miner / AxeOS) under GPL-3.0. That is the first fully open-source Bitcoin ASIC miner.

Chip generations of Bitaxe track Bitmain's own silicon:

| Bitaxe | Chip | Source miner | Stock hashrate |
| --- | --- | --- | --- |
| Max | BM1397 | Antminer S17 | ~400 GH/s |
| Ultra | BM1366 | Antminer S19 XP | ~500 GH/s |
| Supra | BM1368 | Antminer S21 | ~625–775 GH/s |
| Gamma (announced 19 Aug 2024) | BM1370 | Antminer S21 Pro | ~1.0–1.2 TH/s |

OSMU was founded March 2023. Everything below is a fork, a display graft, or a multi-chip scaling of this pair.

### 1. NerdAxe — the graft

**NerdAxe** (BitMaker-hub) put a real BM1366 on the NerdMiner platform: ~500 GH/s, LILYGO color screen, maker DNA intact. Single-chip. The display stayed; the hash became real.

### 2. PiAxe → QAxe — four chips, still open

**PiAxe** (shufps) was a BM1366 Raspberry Pi HAT. **QAxe** scaled it: four BM1366 chips on one board, built on PiAxe + Bitaxe knowledge.

| QAxe rev | What changed | Hashrate |
| --- | --- | --- |
| rev1 | First quad-BM1366, tested | ~1.7 TH/s |
| rev2 | Expected speed after cap work | ~1.8 TH/s avg (330 µF caps wrongly placed) |
| rev3 | Caps corrected; boot switch added | ~1.8 TH/s |

This is the architecture every later quad-chip OSMU miner inherits.

### 3. NerdQAxe — where this dashboard starts

**NerdQAxe** (BitMaker-hub, forked from shufps/qaxe) is QAxe plus the NerdMiner / NerdAxe display. Four BM1366 chips, 1.7–2.4 TH/s, browser AxeOS, 1.9″ LCD. It is the miner that started the quad-chip revolution in this community: before it, open-source solo mining topped out at single-chip hashrates.

GammaHEX-HQ's first job was to sit on the LAN next to a NerdQAxe and poll `/api/system/info` so the fleet did not live in a browser tab.

### 4. QAxe+ / NerdQAxe+ — BM1368, no Pi

Same four-chip idea, next silicon.

**QAxe+** — 4× BM1368, ~2.4 TH/s at ~55 W.

| QAxe+ rev | What changed |
| --- | --- |
| rev4 | Quad BM1368. ASIC reset occasionally odd. 2.4 TH/s @ 55 W measured at 230 V |
| rev4.1 | Three pull-downs on NRSTI pins |

**NerdQAxe+** — QAxe+ with NerdMiner / NerdAxe display, **standalone ESP32, no Raspberry Pi**, Bitaxe firmware as the core. 4× BM1368, ~2.4–2.5 TH/s. Clock and voltage adjustable without reboot. Firmware: [shufps/ESP-Miner-NerdQAxePlus](https://github.com/shufps/ESP-Miner-NerdQAxePlus).

**rev5.0** of NerdQAxe+ shipped as “good to go.”

From this point the API GammaHEX-HQ consumes is the NerdQAxePlus / AxeOS family: power, voltage, current, ASIC temp, VR temp, hashrate, frequency, core voltage, fan, Wi-Fi, shares, best difficulty.

### 5. NerdQAxe++ — four BM1370s

Almost the same board as +, with S21 Pro silicon.

- 4× BM1370
- ~4.8 TH/s at ~76 W (~15.8 J/TH) stock

| ++ revision | Power path | Stock | Overclock | Notes |
| --- | --- | --- | --- | --- |
| Rev 5 | 95472MC three-phase, 8 A barrel jack, mechanical fuse | ~4.8 TH/s, ~87 W, ~18 J/TH | Hardware-limited | Foundation board; most early NQ++ units |
| Rev 5.1 | Same family, production-stable | ~4.8 TH/s @ ~76 W | — | The revision most NQ++ units actually ran |
| Rev 6 / 6.1 | Still 95472MC; **XT30 15 A, fuse-free** | 4.82 TH/s, 70.6 W, 14.66 J/TH | 800 MHz firmware ceiling, 6+ TH/s, ~103 W | Power-path overhaul |
| Rev 7 (ships ~third week of June 2026) | **TPS546D24A two-phase** (same regulator as Bitaxe 801 GT) | 4.80 TH/s, 69.5 W, 14.48 J/TH | **1000 MHz** ceiling, 8.10 TH/s, ~140 W | Fixes VRM blow-ups from long, hard OC |

Confirmed solo blocks on this platform include **#913,272** (5 Sep 2025, NerdQAxe++ via Ocean DATUM) and **#920,440** (27 Oct 2025, a home cluster of six NQ++ units, ~3.141 BTC).

### 6. Eight chips, then Hex, then Gamma Hex

The quad-chip idea kept doubling.

- **NerdOCTAXE-Plus** — 8× BM1368 (Patsch91)
- **NerdOCTAXE-Gamma** — 8× BM1370, per-chip temps in firmware, dual fans (ASIC + VReg)
- **Bitaxe Hex** family — 6-chip boards (Ultra Hex BM1366, Supra Hex BM1368, Gamma Hex BM1370)
- **Bitaxe Gamma Hex 1300** — 6× BM1370, AIO hydro, ~8.4 TH/s at ~140 W stock, near-silent

Satoshi-branded Gamma / Hex units are the same AxeOS citizens. That is why 5.9.5's filename reads **BitaxeGammaHex_Satoshi**. Current on a Hex-class 12 V rail is no longer a toy number, which is why the command center grew a **100 A** needle — headroom for the rail, not a claim that a single board draws 100 A.

### 7. Firmware the dashboard actually speaks

NerdQAxe+ / ++ / OCTAXE run a fork of ESP-Miner. The changes that matter to a telemetry HQ:

| Firmware | What landed |
| --- | --- |
| Dual Pool (v1.0.35 era) | Two pools at once; Bresenham job interleave; stratum settings apply without reboot; graphs switch to **chip hashrate** |
| v1.0.37 (9 May 2026) | New dashboard (temp pills, 3 h history + zoom). **Stratum V2** with Noise. Dual pool mixed SV1+SV2. Independent dual-fan PID (ASIC vs VReg). Internal VReg temp. OCTAXE 8-chip temps. Network difficulty on the info endpoint |
| v1.0.37.x LTS | Bugfix-only line (session stats, SV2 pubkeys, etc.) while 1.1.0 was in flight |
| v1.1.0 (29 Aug 2026) | **Q1373** board (BM1373, 6-phase, Ethernet + CAN). **NerdQAxe++ rev7 (TPS546)** first-class. Solo-mining verification (coinbase payout address). Generic webhook alerts. Unified GitHub updater |

Bitaxe mainline ESP-Miner stayed on its own track (unified `esp-miner.bin` in 2.15.0, native SV2 from 2.14.0). GammaHEX-HQ targets the **common `/api/system/info` surface**, so a Gamma, a Hex, and a NerdQAxe++ can share the same gauges.

---

## How GammaHEX-HQ itself grew

There is no public git history for the early scripts. The 5.9.5 GUI still ships under a fossil filename (`Ravenminer_HQ_…`); the product name is GammaHEX-HQ.

### 1.x — NerdQAxe poller

A Python process on the same LAN. Miner IP in a JSON file. `requests` against `/api/system/info`. Hashrate, temperature, and “is it even up.” This is the inception: stop babysitting the AxeOS tab.

### 2.x — Gauges

Needles instead of labels. Frequency with colour zones (green → orange → red). Fan drawn as a spinning blade locked to reported speed. Dark iron surfaces. The mining-rig look is not decoration — it is how you read a board from across the room.

### 3.x — Alerts that leave the desk

**ntfy.sh** topics for high ASIC temp, high VR temp, low hashrate, miner offline, and **block found**. Thresholds in `ravenminer_alerts.json`. Cooldown plus a 24-hour sent-log (`ravenminer_ntfy_sent.json`) so a restart does not re-page you. Optional startup horn.

### 4.x — Gamma, Hex, Satoshi

Same API, new current and thermal envelopes. Hex-class input current, VR temps that actually move, frequency that wants to live past 800 MHz. The lightning overlay on the OC gauge is the 4.x tell: it intensifies once the board is in the danger-fun zone the NerdQAxe++ 6.x/7.x firmware unlocked.

### 5.x — A real Windows citizen

- System tray via `pystray`, live tooltip (hashrate / temp)
- Compact overlay while minimized
- Windows startup registry, with or without `--minimized`
- Block-found full-screen flash + beep sequence
- PIL-accelerated glow on gauges, radar, and the ping ECG (graceful fallback without Pillow)

### 5.9 — CurrGauge100A

The 100-amp current gauge. Animated needle sweep. Named in the file because it is the feature that made Hex-class current readable at a glance.

### 5.9.5 — this build

Gamma + Hex + Satoshi in one script. Ping **ECG** (three-pass glow). Radar / Wi-Fi sweep. Lightning bolt past 800 MHz. Fan sync. ntfy cooldowns that persist across restarts. Tray overlay. The command center the NerdQAxe desk always wanted.

---

## Features (5.9.5)

### Live telemetry

- Real-time **hashrate, ASIC temp, VR temp, input current / voltage, core voltage** from the Bitaxe / NerdQAxe local API
- **100 A current gauge** with animated needle sweep
- **Frequency / overclock gauge** with dynamic colour zones and a lightning overlay that intensifies past 800 MHz
- **Ping ECG waveform** — heart-rate-style latency graph, 3-pass glow, PIL when available
- **Spinning fan** locked to reported fan speed
- **Radar / Wi-Fi sweep** for signal

### Alerts

- ntfy.sh push: high temp, high VR temp, low hashrate, new block, miner offline
- Thresholds in `ravenminer_alerts.json`
- Cooldown + 24-hour persistence against alert spam
- Optional startup horn (embedded WAV)

### Desktop

- System tray (`pystray`) with live tooltip
- Compact stats overlay when minimized
- Windows Startup registry (`--minimized` optional)
- Block-found celebration: full-screen flash + beep

### Persistence (all local, gitignored)

| File | Role |
| --- | --- |
| `ravenminer_config.json` | Miner IP and general settings |
| `ravenminer_alerts.json` | Thresholds and toggles |
| `ravenminer_ntfy_sent.json` | Cooldown / history |

---

## Quick start

**Needs.** Python 3.9+. A Bitaxe Gamma / Hex / Supra, or a NerdQAxe / + / ++ / OCTAXE, running AxeOS or ESP-Miner-NerdQAxePlus. Windows recommended for tray, startup registry, and `winsound`; the core dashboard runs cross-platform.

```bash
git clone https://github.com/Raven-Black00/GammaHEX-HQ.git
cd GammaHEX-HQ
pip install -r requirements.txt
python Ravenminer_HQ_5_9_5_BitaxeGammaHex_Satoshi_CurrGauge100A.py
```

Launch minimized to tray:

```bash
python Ravenminer_HQ_5_9_5_BitaxeGammaHex_Satoshi_CurrGauge100A.py --minimized
```

**First launch.** HQ writes `ravenminer_config.json` next to the script. Set the miner's LAN IP (placeholder `192.168.68.100`) in Settings. Optionally paste an ntfy.sh topic URL for phone push.

---

## Dependencies

| Package | Purpose | Required |
| --- | --- | --- |
| `requests` | Polls `/api/system/info` | Yes |
| `Pillow` | Glow on gauges, radar, ECG | Recommended (fallback without it) |
| `numpy` | Tray-icon transparency | Optional |
| `pystray` | Tray icon + menu | Optional (Windows / Linux) |
| `winsound` | Horn + block beep | Windows built-in |

```bash
pip install -r requirements.txt
```

---

## Layout

```
GammaHEX-HQ/
├── Ravenminer_HQ_5_9_5_BitaxeGammaHex_Satoshi_CurrGauge100A.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
└── docs/
```

Do not commit the three runtime JSON files. They are gitignored on purpose.

---

## Standalone .exe

PyInstaller:

```powershell
pyinstaller --onefile --windowed --name GammaHEX-HQ `
  --hidden-import=PIL._tkinter_finder --hidden-import=pystray --hidden-import=pystray._win32 `
  --collect-all=PIL Ravenminer_HQ_5_9_5_BitaxeGammaHex_Satoshi_CurrGauge100A.py
```

---

## License

MIT. Hardware and firmware this app talks to are separately licensed (CERN-OHL-S hardware, GPL-3.0 ESP-Miner / NerdQAxePlus). HQ is a client, not a firmware fork.

---

## Credits

- **RavenBlack** — the mark this ships under
- **Alan (Son of Odin)** — the desk this was forged for
- **Selene / Perplexity AI** — the 5.9.5 command center
- **BitMaker** — NerdMiner, NerdAxe, NerdQAxe
- **skot / bitaxeorg / OSMU** — Bitaxe, ESP-Miner, AxeOS
- **shufps** — PiAxe, QAxe, NerdQAxe+, NerdQAxe++, ESP-Miner-NerdQAxePlus
- **Patsch91** — NerdOCTAXE
- **pmaxuw, BitMaker-hub**, and everyone who burned in a rev so the next one did not blow a VRM

May your hashrate burn bright as Sunna's own fire.
