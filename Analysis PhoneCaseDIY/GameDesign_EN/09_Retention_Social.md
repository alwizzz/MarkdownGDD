# 09. Retention & Social

[← Back to index](00_README.md)

## Why players come back

| System | Return trigger |
|---|---|
| [Bot leaderboard](#bot-leaderboard) | Rank up, premium spin every 10 ranks |
| [Daily Missions](#daily-missions) | New missions every day |
| [Daily Login](#daily-login) | Rewards grow up to day 7 / 30 |
| [Idle Income](#idle-income) | Coins accumulate offline (5-hour cap) |
| Free spin wheel | Every 6 hours (see [06_Gacha.md](06_Gacha.md#spin-wheel)) |
| Thematic bundles | 2–10 minute timers (see [08_LiveOps_AB.md](08_LiveOps_AB.md#thematic-bundles)) |
| Weekly event | `WeeklyStartPopup` |
| Push notifications | — |
| Photo Album | Every case is saved and shareable (viral loop) |

## Bot Leaderboard
[CODE ✔ `LeaderBoardData.Init`]

- Contains **499 NPCs** with fixed scores: `(500 − rank) × 50`. Rank 1 = 24,950.
- The player starts at **rank 500** and **climbs 1 rank per 50 points**.
- Bot scores never increase, and no weekly reset was found.
- So this is really a **progress bar dressed up as competition**.
- Bot names come from `leaderboard_names.csv` (154 names). There are 4 `LeaderboardSO` variants (50 avatars/flags).
- **Reward:** every 10 ranks (490, 480, …) the player gets a **free Premium spin**.

### Points per action
[DATA `leaderboard_scores.csv`]

| Action | Points |
|---|---|
| Complete VIP level | 400 |
| Complete regular / Revenge / Auction | 200 |
| Choose Glitter / Marble / Injection maker | 200 |
| Choose Pop-It / Stencil maker | 150 |
| Complete Cleaning, Collect key, Place keychain | 100 |
| Upgrade studio (interior / wall / floor) | 80 |
| Choose Spray / Acrylic | 50 |
| Unlock skin | 50 |
| Place sticker / 3D decoration | 20 |

Advanced makers are worth more points so players try new makers, since new makers are expensive content to build.

## Daily Missions
- 27 missions in `DailyMissionData`, with reward groups.
- Rewards of 50–150 coins.
- Examples: "Create 3 Spray cases" (120), "Upgrade your floor once" (50), "Play boxes mini game 2 times" (150).

## Daily Login
- **7 days:** 250, 500, 750, 1,000, 1,250, 1,500, 1,750 (7,000 total per cycle) [DATA `DailyLogin.csv`].
- **30 days** (`ThrityDaySign`, iOS): exclusive items on days 1/2/4/5/7/9 (`daily_bonus_order` in `Goods.csv`).
- Daily sign has an RV option.

## Idle Income
The formula and boosters are in [05_Economy.md](05_Economy.md). For retention, the key points are:
- The **5-hour** offline cap pushes players to open the game several times a day.
- Workers are temporary and obtained via RV, so players need to renew them.
