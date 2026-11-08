# 07. Monetization

[← Back to index](00_README.md)

**Business model:** ad-first (hybrid-casual). All IAP products are non-consumable and there is **no premium currency**. IAP only removes ads or unlocks content.

## IAP
[DATA `StoreItemConfig`], default USD prices:

| Product | Price | Removes ads? |
|---|---|---|
| noads | $4.99 | ✔ |
| noadstwo | $3.99 | ✔ |
| keychains (buy all keychains) | $1.99 | |
| premiumdesigns | $1.99 | |
| fullgame | $1.99 | |
| geteverything | $4.99 | ✔ |
| specialoffer | $5.99 | ✔ |
| premiumpack | $7.99 | ✔ |
| allincludedbundle | $12.99 | ✔ |
| unlockmakers / bundle | price from store | |

Permanent idle boosters and thematic bundles can also be bought as IAP (see [05_Economy.md](05_Economy.md), [08_LiveOps_AB.md](08_LiveOps_AB.md#thematic-bundles)).

## Interstitials
[CODE ✔]

- There are **about 75 call sites** in the code.
- Almost **every maker step transition** triggers an interstitial:
  - after glue, paint, dry, acrylic
  - changing stencil
  - switching decoration tabs (×6)
  - injection, pop-it, string pull, crossbody
- Other call sites: end of level, entering Cleaning mode, leaving the leaderboard, accepting an auction bid, declining a revenge RV, "No thanks" on the result screen.
- **The client does not cap frequency** (no level / day / cooldown checks). The only conditions are: NoAds not purchased and an ad is ready.
- So **actual frequency is controlled by the CrazyLabs SDK from the server**. The game deliberately exposes many ad "slots", and the server decides which ones fire.
- The end-of-level ad is skipped if the Rate Us popup is about to show.
- There are also **App Open Ads**.

## Rewarded Video (RV)
[CODE ✔]

| Category | RV placement | Value |
|---|---|---|
| **Reward multipliers** | Claim on the result screen | ×2 (normal), **×4 (VIP)** |
| | Auction Best Offer / Coins Multiplier | highest bid / ×2 |
| **Direct coins** | Earn Coins / Skin panel | 500 + 25×(day−1) |
| | Extra coins, Mystery Box, floating icon | — |
| **Content access** | Start a VIP level | — |
| | Unlock AirPods | — |
| | "TRY ONCE" a locked item | — |
| | Studio items with `price_rv` (33 items) | 1 RV per item |
| | Claim bundle items | 1 RV for 2 items |
| | Repair / break screen | — |
| **Gacha** | Skin reroll / reshuffle | replaces 500 coins |
| | Spin wheel | beyond the free 6-hour spin |
| | +3 chest keys | — |
| **Other** | Daily sign | — |
| | Idle workers & boosters | — |
| | Revenge materials (poop/pepper spray, poison glue/soap) | — |

**Video ticket**: exists in code but is only displayed, never earned or spent (leftover feature).

## Home Popup Queue
Popup priority order:

```
GetEverything → SpecialOrder → No Ads (~every 4 completed levels) → Daily
  → Leaderboard → Auction → Weekly → DailyMission → Bundle
  → StudioCategoryUnlock → RateUs
```

- The "Get Everything" popup and `RvOfferPopup` are **disabled** in this build.
- **Rate Us** gives a free reward after rating.

## Notes for the team
- Different RV multipliers per context (×2 normal, ×4 VIP) make ads feel most "worth it" at special moments.
- RV items are interleaved with coin items in the studio shop, so ads feel like a natural shortcut.
- Interstitial hooks at every transition plus server-side pacing are more flexible for A/B than hardcoded cooldowns.
