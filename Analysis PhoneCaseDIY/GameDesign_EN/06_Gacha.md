# 06. Gacha & Random Systems

[← Back to index](00_README.md)

The game has four random systems. All of them are **player-friendly**: no duplicates, a pity counter, or a rigged first result.

| System | Paid with | Rewards | Protection |
|---|---|---|---|
| [Tool Skins](#tool-skins) | Coins (500 +200/roll) | Cosmetic skins | No duplicates |
| [Spin Wheel](#spin-wheel) | Free every 6h / RV / ticket | Coins, stickers, 3D, keychain | First premium spin is rigged |
| [Keychain Chest](#keychain-chest) | Keys (70% drop) | Random coins + keychain | Pity via `default_count` |
| [Auction](#auction) | — | 1.0–3.0× coins | RV "Best Offer" |

---

## Tool Skins
[DATA `skin_items.csv`, `skin_roll_prices.csv`] [CODE ✔ `SkinManager`]

### Contents
- 3 tool types: **Table, Glue, Hair Dryer**.
- 12 skins each: 6 Common, 3 Rare, 3 Legendary. 36 skins total.

### Price
- "UNLOCK RANDOM" button: starts at **500**, rises **+200 per roll** [CODE ✔ `SkinManager.GetCostCoin`].

```
roll_price(k) = 500 + 200 × k     (k = rolls already done for that tool)
```

| Roll # | 1 | 2 | 3 | … | 11 |
|---|---|---|---|---|---|
| Price | 500 | 700 | 900 | … | 2,500 |

- A full set (11 rolls, 1 default skin) = **16,500 coins**. All three tools = **49,500 coins**.

### Randomness rules
- **No duplicates, no rarity weighting.** Skins are picked *uniformly at random* from the ones still locked [CODE ✔].
- Common / Rare / Legendary labels are **cosmetic only** and do not affect odds.
- The "spin" animation cycles 4–9 times before stopping, purely for effect.

### Reshuffle
- The "RESHUFFLE CHOICES" popup (`PopSkinPanel`) uses a shuffle bag without repeats.
- Reshuffle cost: **500 coins or 1 RV**.

### Purpose
Cosmetic, plus +50 leaderboard points per skin.

---

## Spin Wheel
[CODE ✔ `SpinWheelBase`]

| | Regular | Premium |
|---|---|---|
| Segments | 6 | 6 |
| Rewards | 3D, sticker, 100 / 150 / 250 / 300 coins | keychain, sticker, 3D, 1,000 / 1,500 / 2,000 coins |
| How to get | Free every **6 hours**, otherwise RV | IAP or leaderboard reward (every 10 ranks) |

- `wheelType`: free / ticket / rv.
- **The first premium spin is *rigged*** to a top prize (roll forced to 96) to make a good first impression.

---

## Keychain Chest
[DATA `keychain_chests.csv`, `keychain_settings.csv`] [CODE ✔]

### Flow
```
Finish a level → 70% chance of 1 key (only while locked keychains remain)
  → max 3 keys → chest opens when keys are full
  → 1 tap = 1 key → random coins min_coin–max_coin
  → after default_count opens (pity) → the keychain is awarded
```

| Parameter | Value |
|---|---|
| Key drop per level | 70% |
| Key capacity | 3 |
| Coins per tap | 20–240 (first chest) up to 120–440 (last chest) |
| Number of chests | 11 (for 12 keychains) |
| RV | +3 keys |
| IAP | "keychains" $1.99 = buy all keychains |

- Leaderboard points: collect key 100, place keychain 100.

---

## Auction
See [03_Customers.md](03_Customers.md#auction). In short: 4 random bids of `1.0–3.0 × 3★ reward`; RV Best Offer takes the highest bid instantly; RV Multiplier ×2.

---

## Notes for the team
- All these random systems **can be tuned from the server**, since their configs live in CSVs that can be replaced remotely.
- A gacha price that rises linearly (+200) makes an unlimited sink that still feels fair, because there are no duplicates.
