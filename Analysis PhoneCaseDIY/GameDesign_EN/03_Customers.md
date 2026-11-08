# 03. Customer Types

[← Back to index](00_README.md)

Sources: `enum CustomerType` [CODE], `level_rewards.csv`, `vip_customer.csv`, `ReturningClients.csv`, `couple_phone_requests.csv` [DATA].

## Summary

| Type | Status | Frequency | Leaderboard points |
|---|---|---|---|
| Normal | Active | Default | 200 |
| VIP | Active | Every 3rd customer from Day 2 | 400 |
| Revenge | Active | Replaces the VIP slot (with conditions) | 200 |
| Auction | Active | After a VIP level | 200 |
| Returning (Cleaning) | Active | 13 events, Day 2–15 | 100 |
| Couple | Active | 8 orders | — |
| Headphone/AirPods upsell | Active | After a case is finished | — |
| Boss / "Picky Boss" | **Disabled** | — | — |
| Unhappy customer | **Disabled** | — | — |

## Normal
Regular order. Rewards follow `level_rewards.csv` (see [05_Economy.md](05_Economy.md#a-level-rewards)).

## VIP
- Appears **every 3rd customer** starting Day 2 (`vip_interval=3`, `first_appear_day=2`).
- The VIP reward **replaces** the star reward with a fixed daily amount: **200 + 30 × (day − 2)**, so Day 25 = 890.
- The RV "Claim" multiplies it **×4** (`magnification`) [CODE ✔]. This is the most valuable RV moment in the game.
- 8–10 tappable emoji, each giving a random 10–30 coins.
- Serving VIPs **unlocks VIP items** (`unlock_vip_order` 1…54). See [05_Economy.md](05_Economy.md#content-unlock-paths).
- The VIP level is started through an RV (`VipStart`) and can be skipped.
- 30 VIPs in total across Day 1–25.

## Revenge
- **Replaces the VIP slot** if that level is not an auction / couple / cleaning / weekly level and the revenge has not been completed [CODE ✔ `LevelRevengeEnable`].
- 4 villain customers, e.g. "I STOLE THIS PHONE…", "MAKE ME A CASE, BUT I'M NOT PAYING!".
- Prank materials:
  - poop spray & pepper spray → RV "TRY IT"
  - poison glue & poison soap → RV popup, declining = interstitial
- The paint color automatically becomes a mandatory request.

## Auction
- Appears **after finishing a VIP level** (can be skipped).
- **4 bidders.** Each bid = `random(1.0–3.0) × that slot's 3★ reward`, and all bids are made distinct [CODE ✔].
- RV "Best Offer" = take the highest bid immediately.
- RV "Coins Multiplier" = accepted bid ×2.
- 25 praise words (AMAZING … WONDROUS) for flavor.

## Returning Client (Cleaning)
- 13 events, Day 2–15 (`ReturningClients.csv`).
- Modes: clean a **dirty case** or a **charging port**.
- Short stories, e.g. "dropped the phone in mud", "found it in the dog's food bowl".
- Serves as a short "breather" level.

## Couple
- 8 couple orders (`couple_phone_requests.csv`).
- Make **2 matching cases**, each with a set combination of 1–3 makers.

## Headphone / AirPods upsell
- After the case is done the customer asks "CAN YOU DO MY HEADPHONES CASE TOO?".
- Leads to a bonus Earbuds / Headphones level. Unlocking AirPods uses an RV.

## Disabled features
| Feature | Evidence |
|---|---|
| Boss / "Picky Boss" | Code and text exist, but there are no Boss rows in the table [CODE ✔] |
| Unhappy customer | `isUnhappy` is always `false` [CODE ✔] |
