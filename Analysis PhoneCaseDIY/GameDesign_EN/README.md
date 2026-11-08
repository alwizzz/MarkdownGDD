---
description: readme
---

# Phone Case DIY: Game Design Teardown

Teardown notes for **Phone Case DIY**, split by topic so the development team can jump straight to the section they need.

| | |
|---|---|
| Package | `com.newnormalgames.phonecasediy` v5.2.0.0 (Google Play) |
| Publisher / SDK | CrazyLabs (TTPlugins / CLIK) |
| Engine | Unity 2022.3.62f2, IL2CPP, arm64 |
| Teardown date | 2026-11-04 |

## Contents

| # | File | Covers | Best for |
|---|---|---|---|
| 01 | [Core Loop](01_CoreLoop.md) | Player fantasy, core loop, meta loop | Everyone |
| 02 | [Makers & Decoration](02_Maker_Mechanics.md) | 9 case-making techniques, mini-game steps, decoration, phone shapes | Gameplay programmers, artists |
| 03 | [Customer Types](03_Customers.md) | Normal, VIP, Revenge, Auction, Couple, Cleaning, etc. | Gameplay, level designers |
| 04 | [Level Design & Pacing](04_LevelDesign_Pacing.md) | Day structure, FTUE, rhythm, star rating, difficulty | Level designers |
| 05 | [Economy](05_Economy.md) | Currencies, coin sources, coin sinks, unlock paths | Economy designers |
| 06 | [Gacha & Random Systems](06_Gacha.md) | Skin rolls, spin wheel, keychain chest, auction | Economy designers, programmers |
| 07 | [Monetization](07_Monetization.md) | IAP, interstitials, rewarded video, popup queue | Monetization, programmers |
| 08 | [LiveOps & A/B Testing](08_LiveOps_AB.md) | Thematic bundles, UI variants, remote config | LiveOps, backend |
| 09 | [Retention & Social](09_Retention_Social.md) | Bot leaderboard, daily missions, login, idle income | Product, programmers |
| 10 | [Content List](10_Content.md) | Asset counts per category | Producers, artists |
| 11 | [Takeaways for Our Game](11_Takeaways.md) | Design points worth copying | Everyone |
| 12 | [Data Sources](12_Data_Sources.md) | Map of data files, configs and decompiled code | Programmers |

## Labels

| Label | Meaning |
|---|---|
| **[DATA]** | Value taken directly from a CSV table or ScriptableObject inside the APK. |
| **[CODE ✔]** | Confirmed by reading the method body (Cpp2IL ISIL). |
| **[CODE]** | The class/method exists, but behavior details are inferred from names. |
| **[GUESS]** | Design interpretation, not proven. |

> ⚠️ **All values are defaults.** CrazyLabs can replace entire CSV files from the server (see [08_LiveOps_AB.md](08_LiveOps_AB.md)), so the values live on a player's phone may differ.

## Not covered
- Remote config values currently active on the server.
- Player save data.
- Visual and audio assets (still packed in `data.unity3d`, not yet extracted).
