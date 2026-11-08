# 05. Economy

[← Back to index](00_README.md)

The game has **no premium currency**. The economy runs on coins (soft currency), with RV as the main shortcut. Random systems (gacha, spins, chests) are covered separately in [06_Gacha.md](06_Gacha.md).

## Currencies & Resources

| Resource | Source | Used for |
|---|---|---|
| **Coin** (soft) | Level rewards, VIP, missions, login, chests, idle income, RV | Studio decor, tool skin rolls, skipping bundle timers |
| **Key** | **70%** drop per level (`keychain_settings: key_drop_chance_percent=70`) | Opening the keychain chest |
| **Spin Wheel Ticket** | Events / rewards | Spin wheel (`wheelType: free / ticket / rv`) |
| **Video Ticket** | [CODE `RVPlayerManager.videoTicketCount`] | Replaces watching an RV. Only displayed, never earned or spent (leftover feature). |
| **Leaderboard Score** | In-game actions | Rank up (50 points = 1 rank) |
| **Real money (IAP)** | — | No Ads, packs, unlocks (see [07_Monetization.md](07_Monetization.md)) |

## Faucets (coin sources)

### a. Level rewards
Linear per customer, where n = global customer number 1…120 [DATA `level_rewards.csv`].

| Stars | Formula | Customer #1 | Customer #120 |
|---|---|---|---|
| 1★ | `75 + 2(n−1)` | 75 | 313 |
| 2★ | `100 + 3(n−1)` | 100 | 457 |
| 3★ | `125 + 4(n−1)` | 125 | **601** |

**Coins per day** (3★, without ×2, without VIP):

| Day | 1 | 2 | 4 | 6 | 9 | 14 | 20 | 25 |
|---|---|---|---|---|---|---|---|---|
| 3★ coins | 125 | 262 | 447 | 700 | 1,125 | 1,962 | 2,826 | 3,546 |

Total Day 1–25: **43,560** (3★) / 23,280 (1★). With RV ×2 this can approach double.

### b. VIP
- `200 + 30 × (day − 2)` per VIP (Day 25 = 890).
- **×4 with RV**, plus 8–10 emoji × random 10–30 coins.
- 30 VIPs across Day 1–25.

### c. Daily Login
- 7 days: 250, 500, 750 … 1,750 (**7,000** total per cycle).
- 30-day variant (`ThrityDaySign`, iOS) with exclusive items on days 1/2/4/5/7/9 (`daily_bonus_order`).

### d. Daily Missions
27 missions, rewards of **50–150 coins**. Examples: "Create 3 Spray cases" 120, "Upgrade your floor once" 50, "Play boxes mini game 2 times" 150.

### e. Keychain Chest
Random 20–440 coins per tap. Details in [06_Gacha.md](06_Gacha.md#keychain-chest).

### f. Free coin RV
In the Skin panel and the HUD "Earn Coins" button: `500 + 25 × (day − 1)` per view (Day 25 = 1,100) [DATA `skin_rv_coins.csv`].

### g. Idle Income
[CODE ✔]
```
coins = hours × (worker_count × 50 + shop_income) × (DoubleTime ? 2 : 1)
```
- Offline savings are capped at **5 hours** of worker income (15 hours with the *Stretch the Limit* booster).
- Workers are obtained **through RV** and are temporary.

| Booster (RV) | Effect |
|---|---|
| DoubleTime | Income ×2 |
| Stretch the Limit | Offline cap 15 hours |
| Design Discount | Studio decor −30% |

Permanent boosters are sold as IAP. Booster durations could not be read from the code.

### h. Spin Wheel
Rewards of 100–2,000 coins. Details in [06_Gacha.md](06_Gacha.md#spin-wheel).

### i. Auction
Bids of 1.0–3.0 × the 3★ reward. Details in [03_Customers.md](03_Customers.md#auction).

### j. Extra Coins RV
RV coin buttons in the HUD, shop and floating icons (`extra_coins_rv`, `float_skin_rv`, `MysteryBoxRV`).

## Sinks (coin spending)

### a. Studio (shop decor)
10 categories, 125 items [DATA `Decorations_Categories.csv`, `Decorations_Items.csv`].

| Category | Unlock day | Items |
|---|---|---|
| Walls, Floor, Table | 1 | 15 / 15 / 15 |
| Showcase, Chairs | 3 | 10 / 10 |
| Lamp, Sofa | 4 | 15 / 10 |
| Rug | 5 | 15 |
| Plant | 6 | 10 |
| Left Wall Decor | 7 | 10 |

- Breakdown: **35 free (default), 57 coin-priced, 33 RV-only** (1 ad per item).
- Coin prices range 50 → 1,500. **All coin items total 33,400**, about **77%** of total 3★ income for Day 1–25. The sink is tuned so the studio is "almost full" around Day 25.
- Price pattern per category: 2–5 free items → coin items rising gradually → RV items interleaved between coin items (by `order`). Players short on coins see RV as the shortcut.
- Studio upgrades (interior/wall/floor) also give +80 leaderboard points.

### b. Tool Skins (gacha roll)
49,500 coins in total for all skins. Details in [06_Gacha.md](06_Gacha.md#tool-skins).

### c. Bundle timer skip
500–1,000 coins per cycle. Details in [08_LiveOps_AB.md](08_LiveOps_AB.md#thematic-bundles).

## Rough balance, Day 1–25

| | Coins |
|---|---|
| Level faucet at 3★ | ~43,560 |
| + VIP, login, missions, chests, RV, idle | (depends on player behavior) |
| Studio sink | 33,400 |
| Tool skin sink | 49,500 |
| Bundle skip sink | 3 cycles × (500…1,000) per bundle |

Total sinks are well above the level faucet. **This shortfall is what pushes players to watch RVs.** [GUESS]

## Content Unlock Paths
`Goods.csv` separates how each item is unlocked:

| Path | Column | Examples |
|---|---|---|
| 1. Day progress | `unlock_day_gp` / `unlock_day_ios` | Stickers unlock gradually Day 1 → 23 |
| 2. Serving VIPs | `unlock_vip_order` 1…54 | 21 2D stickers, 13 3D stickers, 10 spray, 10 acrylic, 3 glitter. Tagged "VIP ITEM". |
| 3. Chest / daily bonus | `daily_bonus_order`, keychain chest | Keychains via chests, exclusive items via 30-day login |
| 4. Bundles | `Bundle_Items.csv` | See [08_LiveOps_AB.md](08_LiveOps_AB.md) |
| 5. RV "TRY ONCE" | — | Try a locked item once by watching an ad |
