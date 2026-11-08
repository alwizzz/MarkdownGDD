# 04. Level Design & Pacing

[← Back to index](00_README.md)

Main sources: `level_rewards.csv` [DATA], `MissionManager` [CODE ✔].

## Day Structure
- Progress is split into **Days**. Day 1–25 are hand-authored, **120 customers** in total.
- **After Day 25 the table is clamped to Day 25** [CODE ✔ `GameSettingPrefs.get_GLDDayIndex = min(day, 25)`]. Every later day replays Day 25's 6 rows (3★ rewards 581–601, VIP in slot 4). The endgame no longer raises rewards.

### Customers per day

| Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9–13 | 14–25 |
|---|---|---|---|---|---|---|---|---|---|---|
| Customers | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 4 | 5 | 6 |

### Per-customer columns in `level_rewards.csv`

| Column | Purpose |
|---|---|
| `phone_type_source` | Phone shape used |
| `prepare_type` | Main maker (Spray 63×, Acrylic 56×, Marble 1×) |
| `lock_type` | Feature introduced that day |
| `item_require_count` | Number of customer requests |
| `one/two/three_star_reward` | Coin reward per star count |
| `customer_type` | Normal / VIP / etc. |
| `vip_emoji_face_min/max` | VIP emoji count |

## New Phone Shapes & Features Schedule

| Day | New phone shape | Feature introduced (`lock_type`) |
|---|---|---|
| 1 | Normal | — (Spray tutorial) |
| 2 | Bunny | Chain (keychain) |
| 3 | — | Acrylic |
| 4 | — | Decoration (stickers) |
| 5 | Among-us-like | Glitter |
| 6 | — | Marble (forced once) |
| 8 | Unicorn | |
| 11 | Pineapple | |
| 15 | Cola | |
| 20 | "StarBucks" | |
| 23 | Foot | |
| 25 | Cactus | |

## Onboarding Curve (FTUE)

| Day | Customers | What's new |
|---|---|---|
| 1 | 1 | Spray, Normal phone. No choices, so the player gets it right away. |
| 2 | 2 | First VIP, keychain, Bunny phone, Bundles, first Cleaning customer, Acrylic unlocked (GP) |
| 3 | 2 | First Acrylic order, Pop-It, Showcase & Chairs studio categories |
| 4 | 3 | Stencil, Decoration (stickers), Lamp & Sofa |
| 5 | 3 | Glitter, Marble, Rug |
| 6 | 4 | Injection, Liquid Glitter, Plant |
| 7 | 4 | Left Wall Decor (last studio category) |
| 8–25 | 4→6 | New phone shape roughly every 3–5 days, new stickers every 2–3 days |

**Pattern:** up to Day 7, almost **every day unlocks something** (a maker or a studio category). After that, novelty comes from new phone shapes, new stickers, VIP items and special modes (see [03_Customers.md](03_Customers.md)).

## Rhythm Within a Day
- A VIP every 3 customers, so almost every day has 1–2 "special" moments.
- `prepare_type` alternates Spray / Acrylic so the maker keeps changing.
- Returning / Cleaning levels are slotted in as short "breather" levels (100 leaderboard points instead of 200).

## Star Rating
[CODE ✔ `MissionManager.GetStarNum`]

```
stars = (Day <= 3 ? 2 : 1)
      + (all requests fulfilled ? 1 : 0)
      + (any decoration / marker used ? 1 : 0)
if maker = Injection / LiquidGlitter / PopIt / StringPull → stars = 3
max 3
```

- No randomness.
- Day 1–3 guarantee at least 2★.
- Premium makers **always give 3★**.
- Worst result is 1★. There is no fail state.

### Customer requests (`InitMission`)
- Picked at random from {paint color, glitter, 2D sticker, 3D sticker, marker, acrylic}, then filtered by maker and day.
- The count comes from `item_require_count`:

| Value | Meaning |
|---|---|
| −1 | No requests |
| 1 | One request |
| 0 | Random 1…N |

- **Matching check:** colors must match **exactly** (RGBA). Requested stickers must actually be placed.

### Result
- 1★ / 2★ / 3★ pays the matching reward column.
- **RV "Claim"** = coins ×2 for normal customers, ×4 for VIPs.
- "No thanks" pays the base coins, then shows an interstitial.

## Difficulty
- **There is no fail state at all** [CODE ✔]. Boss and Unhappy customer features are disabled.
- The only "penalty" is fewer stars, and only if the player ignores requested colors/stickers or does not decorate.
- **Hidden incentive:** premium makers always give 3★ and more leaderboard points, which pushes players to try new makers.
