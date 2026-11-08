# 02. Makers & Decoration

[← Back to index](00_README.md)

A **maker** is a case-making technique. Each maker is really a separate *satisfying* mini-game, and makers are the main source of gameplay variety.

Sources: `enum Maker` in `dump.cs` [CODE], Feature column in `Goods.csv` [DATA].

## Makers

Unlock days are for Google Play. iOS differs slightly because pacing is A/B tested (see [08_LiveOps_AB.md](08_LiveOps_AB.md)).

| Maker | Unlock (GP) | Steps / core mechanic | Leaderboard points |
|---|---|---|---|
| **Spray** | Day 1 | Glue → spray paint (drag) → hair dryer. 25 colors. | 50 |
| **Marker / BrushPen** | Day 1 | 15 marker colors for free drawing. | — |
| **Acrylic** | Day 2 | Acrylic paint pouring (`PouringConfig`). 25 colors + 25 pouring palettes + bundle palettes. | 50 |
| **Pop-It** | Day 3 | Paint → dry → play the pop-it (tap bubbles). | 150 |
| **Stencil** | Day 4 | Pick a stencil (donut, panda, goldfish, pizza, unicorn, butterfly, heart) → spray over it. | 150 |
| **Marble** | Day 5 | Fluid simulation (resolution 256, `stirForce 500`) → swirl paint in water → dip the phone (`DippingConfig`, 5-second dip). | 200 |
| **Injection** | Day 6 | "HOLD TO INJECT": fill shaped cavities (star, lightning, candy, pineapple, water, gem) with colored liquid. Configured per phone shape. | 200 |
| **Liquid Glitter** | Day 6 | Pick a background → fill with water + glitter. | 200 |
| **String Pull** | ? | Lay strings → pull (patterns in `PullLevelConfig`, 20 levels) → palette → heater → open the cover. | — |
| **ComingSoon** | — | "Coming soon" card to build curiosity. | — |

> **Premium makers** (Injection, Liquid Glitter, Pop-It, String Pull) **always give 3★** (see [04_LevelDesign_Pacing.md](04_LevelDesign_Pacing.md#star-rating)).

## Supporting steps
From `UiVariants.csv`:

| Step | Purpose |
|---|---|
| `step_vip_select` | VIP-specific selection |
| `step_break_screen` / `step_repair_screen` | Repair a cracked screen (unlocked via RV) |
| `step_clean_dirty` | Clean a dirty case (Cleaning customers) |
| `step_clean_charing` | Clean the charging port |
| `step_clean_inside` | Clean the inside |
| `step_crossbody` | Attach a crossbody strap |
| `step_glitter` | Sprinkle glitter |

**Ad note:** almost every transition between steps triggers an interstitial. See [07_Monetization.md](07_Monetization.md#interstitials).

## Decoration

| Type | Count | Notes |
|---|---|---|
| 2D stickers | 81 | Includes 8 holographic "laser" stickers. Themes: Superhero, Kpop, Princess, Creatures. |
| 3D stickers | 37 | |
| Glitter | 15 | |
| Keychains | 12 | Earned from chests (see [06_Gacha.md](06_Gacha.md#keychain-chest)) |
| Crossbody straps | 8 | `crossbody_strap_items.csv`, some are RV |
| Emoji / text | — | |

- Interaction: drag & drop and scaling [CODE `MoveSticker2d`].
- Painting uses P3D Paint with undo / redo / clear [CODE `P3dButtonUndoAll`].

## Phone Shapes & Devices [DATA]

| Type | List |
|---|---|
| Base phones | Normal, Bunny, Among-us-like, Unicorn, Pineapple, Cola, "StarBucks", Foot, Cactus |
| Variants | Flip & Fold (Normal / Bunny) |
| From bundles | Cat, Anime, Robot, Cloud, Spaceship, Narwhal |
| Other devices | AirPods case, Earbuds, Headphones (own flow, `HeadSetType`) |

- Phone models differ by platform: `PhoneAssetConfig_iPhone` and `PhoneAssetConfig_Android`, so the in-game phone looks like the player's own.
- The schedule for new phone shapes is in [04_LevelDesign_Pacing.md](04_LevelDesign_Pacing.md).

> ⚠️ The "Among-us" and "StarBucks" shapes use third-party IP. Do not copy them in our game.

## Related technical configs
All in `tables/ScriptableObject/`:
`PouringConfig`, `PouringColorConfig`, `MarblePaintingConfig`, `DippingConfig`, `InjectConfigList`, `AllInjectConfig`, `EveryInject`, `StencilConfig`, `PhoneStencilConfig`, `PopItPhoneConfig`, `PullLevelData`, `StringPullColor`, `GlitterConfig`, `GlitterBGConfig`, `StiringConfig`, `PhoneAssetConfig`.
