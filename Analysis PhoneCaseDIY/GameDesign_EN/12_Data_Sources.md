# 12. Data Sources

[← Back to index](00_README.md)

All paths are relative to the `teardown/com.newnormalgames.phonecasediy/` folder.

## Data tables (CSV/TSV): `tables/TextAsset/`

| Topic | Files |
|---|---|
| Levels & customers | `level_rewards.csv`, `vip_customer.csv`, `ReturningClients.csv`, `couple_phone_requests.csv`, `Characters.csv` |
| Items & unlocks | `Goods.csv`, `goods_decoration_ids.csv`, `break_screen_items.csv`, `crossbody_strap_items.csv` |
| Studio | `Decorations_Categories.csv`, `Decorations_Items.csv` |
| Skin gacha | `skin_items.csv`, `skin_roll_prices.csv`, `skin_rv_coins.csv` |
| Keychain chest | `keychain_chests.csv`, `keychain_items.csv`, `keychain_settings.csv` |
| Bundles | `Bundles.csv`, `Bundle_Items.csv` |
| Retention | `DailyLogin.csv`, `leaderboard_names.csv`, `leaderboard_scores.csv` |
| A/B | `UiVariants.csv`, `RuntimeBehaviorVariants.csv`, `Features.csv` |
| Text | `localization.tsv` (16 languages), `emoji.tsv` |

## Configs (ScriptableObject): `tables/ScriptableObject/`

| Topic | Folders |
|---|---|
| Makers | `PouringConfig`, `PouringColorConfig`, `MarblePaintingConfig`, `DippingConfig`, `InjectConfigList`, `AllInjectConfig`, `EveryInject`, `StencilConfig`, `PhoneStencilConfig`, `PopItPhoneConfig`, `PullLevelData`, `StringPullColor`, `GlitterConfig`, `GlitterBGConfig`, `StiringConfig` |
| Devices | `PhoneAssetConfig`, `PhoneMapTileConfig` |
| Monetization | `StoreItemConfig` |
| Retention | `DailyMissionData`, `LeaderboardSO` |
| LiveOps | `Liveops.ThematicBundles.BundlesConfig`, `CrazyLabs.Extensions.Database.DatabaseConfig` |

## Decompiled code: `dump/`

| File | Contents |
|---|---|
| `dump/il2cppdumper/dump.cs` | All classes, fields, enums and method signatures |
| `dump/il2cppdumper/stringliteral.json` | All string literals in the code |
| `dump/isil_annotated/*.txt` | Method logic per class (1,213 files), annotated with symbol names |

### Key classes to search for

| System | Class |
|---|---|
| Star rating & requests | `MissionManager` (`GetStarNum`, `InitMission`) |
| Global settings & flags | `GameSettingPrefs` |
| Makers | `enum Maker`, `BrushManager`, `AirPod_Manager` |
| Customers | `enum CustomerType`, `AuctionManager`, `RevengeManger` |
| Skin gacha | `SkinManager` |
| Spin wheel | `SpinWheelBase` |
| Leaderboard | `LeaderBoardData`, `enum ScoreLocation` |
| Idle income | `IdleIncome*` |
| Bundles | `BundleService` |
| Ads | `RVPlayerManager` |
| Remote config | `DatabaseController` (CrazyLabs) |

## Notes
- `tables/errors.txt`: 31 MonoBehaviours failed to dump. Core data is not affected.
- Visual and audio assets have not been extracted from `extracted/base/assets/bin/Data/data.unity3d`.
