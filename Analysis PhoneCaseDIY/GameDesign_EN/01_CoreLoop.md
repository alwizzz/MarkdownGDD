# 01. Core Loop

[← Back to index](00_README.md)

## Genre & Fantasy
- **Genre:** hybrid-casual "DIY / satisfying craft" plus shop simulation.
- **Player fantasy:** "I run a custom phone case workshop. Customers come in, I make cases to order, get paid in coins, then decorate my studio."
- **Experience focus:** self-expression and *satisfying* feel, not challenge. There is no fail state (see [04_LevelDesign_Pacing.md](04_LevelDesign_Pacing.md)).

## Core Loop (1 level = 1 customer)

```
Customer arrives (Normal / VIP / Returning / Couple / Revenge / Auction)
  → choose phone shape
  → choose MAKER (case-making technique: Spray, Acrylic, Stencil, Marble, ...)
  → play the mini-game steps (glue → paint → dry → ...)
  → decorate (2D stickers, 3D stickers, glitter, keychain, strap)
  → result rated 1–3 stars
  → earn coins (+ RV ×2) and a 70% chance of a chest key
  → possible upsell: "CAN YOU DO MY HEADPHONES CASE TOO?" → bonus level
```

| Stage | Detail | Doc |
|---|---|---|
| Customer | 6 active types, each with its own rules | [03_Customers.md](03_Customers.md) |
| Maker & steps | 9 makers, each made of several mini-games | [02_Maker_Mechanics.md](02_Maker_Mechanics.md) |
| Rating | Deterministic star formula, no randomness | [04_LevelDesign_Pacing.md](04_LevelDesign_Pacing.md#star-rating) |
| Reward | Linear coins per customer, RV multipliers | [05_Economy.md](05_Economy.md) |

## Meta Loop

```
Day → each day has 1–6 customers
  → new days unlock makers, phone shapes, stickers and studio categories
  → coins are spent on studio decor and tool skins
  → action points raise the (bot) leaderboard rank → premium spin rewards
  → daily missions, daily login, idle income and bundle timers bring players back
```

| Meta system | Doc |
|---|---|
| Studio (shop decor), tool skins | [05_Economy.md](05_Economy.md), [06_Gacha.md](06_Gacha.md) |
| Leaderboard, daily missions, login, idle | [09_Retention_Social.md](09_Retention_Social.md) |
| Thematic bundles (timers) | [08_LiveOps_AB.md](08_LiveOps_AB.md) |

## Content length
- **25 designed days** (120 customers). After Day 25 the table is clamped to Day 25 and its last 6 customers repeat. Rewards stop growing.
- After onboarding, variety comes from new phone shapes, new stickers, VIP items and special modes (Revenge, Auction, Couple, Cleaning).
