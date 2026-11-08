# 11. Takeaways for Our Game

[← Back to index](00_README.md)

## Gameplay Design
1. **One fantasy, many "makers".** The core loop stays fixed (order → make → rate → coins), and variety comes from *how* the case is made. Each maker is a separate satisfying mini-game. This is a cheap way to add content. → [02](02_Maker_Mechanics.md)
2. **A special customer every 3 levels** (VIP) keeps attention up without raising difficulty. → [03](03_Customers.md)
3. **No fail state.** For a "satisfying" genre, fewer stars is enough of a penalty. → [04](04_LevelDesign_Pacing.md)
4. **The endgame is clamped at Day 25**, and rewards stop growing. For our game, plan a content loop or events for after the main content runs out. → [04](04_LevelDesign_Pacing.md)

## Economy
5. **Linear rewards + calculated sinks.** Rewards rise +4 coins per customer, and the total studio price (33.4k) is set at about 77% of 25 days of income. Use simple formulas that are easy to tune in a spreadsheet. → [05](05_Economy.md)
6. **Three unlock paths** (days, VIPs, chests) give every type of activity its own unique rewards. → [05](05_Economy.md#content-unlock-paths)
7. **Gacha with a rising price (+200/roll)** is an unlimited sink that feels fair because players never get duplicates. → [06](06_Gacha.md)

## Monetization
8. **RV items interleaved with coin items** in the shop make ads look like a natural shortcut. → [05](05_Economy.md#a-studio-shop-decor)
9. **Many ad slots in the client, frequency set by the server.** Put interstitial hooks at every transition, then control pacing remotely. More flexible for A/B than hardcoded cooldowns. → [07](07_Monetization.md)
10. **Different RV multipliers per context** (normal ×2, VIP ×4, auction ×2 + best offer) make ads most "worth it" at special moments. → [07](07_Monetization.md)

## Retention & LiveOps
11. **An action-based bot leaderboard** gives a sense of competition without a multiplayer backend, while steering behavior (more points for new makers). → [09](09_Retention_Social.md)
12. **A linear fake leaderboard** (50 points = 1 rank, reward every 10 ranks) is the cheapest progression system that still feels social. → [09](09_Retention_Social.md)
13. **All numbers in CSV tables + remote flags**, so designers can A/B pacing without a new release. → [08](08_LiveOps_AB.md)

## Warning
14. ⚠️ **Avoid third-party IP.** This game uses "Among-us" and "StarBucks" shapes. Our game should use original designs instead.
