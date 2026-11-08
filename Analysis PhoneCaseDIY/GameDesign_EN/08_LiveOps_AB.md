# 08. LiveOps & A/B Testing

[← Back to index](00_README.md)

## Thematic Bundles
[DATA `Bundles.csv`, `Bundle_Items.csv`] [CODE ✔ `BundleService`]

| Bundle | Cycle timer | Coin skip price / cycle | Contents (3 cycles × 2 items) |
|---|---|---|---|
| Cat | 2 min | 500 | case, spray, 2D sticker ×2, 3D, charm |
| Anime | 5 min | 600 | case, spray, 2D, 3D, charm, strap |
| Robot | 5 min | 700 | case, spray, 2D, 3D, charm, strap |
| Cloud | 10 min | 800 | case, 2D, 3D, glitter, charm, strap |
| Spaceship | 10 min | 900 | case, spray, 3D, glitter, charm, strap |
| Narwhal | 10 min | 1,000 | case, spray, 2D, 3D, glitter, strap |

### Flow
```
Unlocks on Day 2
  → cycle timer runs
  → timer ends: next 2 items become "claimable" → claim with 1 RV (for both items)
  → or pay 500–1,000 coins to skip the timer
  → or buy the whole bundle via IAP
  → 3 cycles done → move to the next bundle
```

- `coins_per_cycle` is the **skip price**, not a reward.
- There are RVs per item category (`bundle_case_rv`, `bundle_glitter_rv`, …).
- Flag `bundle_timer_reset_on_relaunch=1`: the timer resets when the app is relaunched (remotely configurable).
- Design purpose: the timer brings players back (repeat sessions).

## Weekly Event
`WeeklyStartPopup` and the `weeklyEvent` keychain [CODE]. Event contents are not in the tables.

## A/B Testing
The game is built as an **A/B testing machine**.

| Mechanism | Contents |
|---|---|
| `UiVariants.csv` | 89 swappable UI prefabs (`_V2`, `ResultPanel_V430`, `phoneOrder_440`, …) |
| `RuntimeBehaviorVariants.csv` | 23 behavior flags |
| iOS vs GP unlock days | Different pacing per platform |
| `LeaderboardSO_V470_*` | 4 leaderboard content variants |
| `Features.csv` | Feature on/off |

### Example behavior flags
- `all_decoration_tools_unlocked_early`
- `makers_day_lock_removed`
- `phone_selection_available_from_first_day`
- `break_screen_rewarded_unlock`
- `between_level_flow_rework`

### iOS vs Google Play pacing

| Maker | iOS | GP |
|---|---|---|
| Acrylic | Day 4 | Day 2 |
| Stencil | Day 2 | Day 4 |
| Marble | Day 7 | Day 5 |

## Remote Config
[CODE ✔ `CrazyLabs DatabaseController`]

- The game does **not** read remote keys one by one.
- **Entire CSV files can be replaced from the server** (`fileConfig_*`), or just specific cells.
- So every value in these docs (rewards, prices, unlock days, drop rates) is a *default* that can be A/B tested without an app update.

### Legacy flags hardcoded in `GameSettingPrefs`

| Flag | Value |
|---|---|
| Revenge | ON, replaces VIP |
| Auction | ON, skippable |
| IAP NoAds | ON |
| RV-unlock-offers | OFF |

## Notes for the team
- Keep all design numbers in tables (CSV / spreadsheet), not in code.
- Build a pipeline to replace tables from the server. This lets designers tune pacing and economy without a new release.
