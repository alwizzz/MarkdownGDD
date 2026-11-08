# 12. Lokasi File Sumber

[← Kembali ke indeks](00_README.md)

Semua path relatif terhadap folder `teardown/com.newnormalgames.phonecasediy/`.

## Tabel data (CSV/TSV): `tables/TextAsset/`

| Segmen | File |
|---|---|
| Level & pelanggan | `level_rewards.csv`, `vip_customer.csv`, `ReturningClients.csv`, `couple_phone_requests.csv`, `Characters.csv` |
| Item & unlock | `Goods.csv`, `goods_decoration_ids.csv`, `break_screen_items.csv`, `crossbody_strap_items.csv` |
| Studio | `Decorations_Categories.csv`, `Decorations_Items.csv` |
| Gacha skin | `skin_items.csv`, `skin_roll_prices.csv`, `skin_rv_coins.csv` |
| Keychain chest | `keychain_chests.csv`, `keychain_items.csv`, `keychain_settings.csv` |
| Bundle | `Bundles.csv`, `Bundle_Items.csv` |
| Retensi | `DailyLogin.csv`, `leaderboard_names.csv`, `leaderboard_scores.csv` |
| A/B | `UiVariants.csv`, `RuntimeBehaviorVariants.csv`, `Features.csv` |
| Teks | `localization.tsv` (16 bahasa), `emoji.tsv` |

## Config (ScriptableObject): `tables/ScriptableObject/`

| Segmen | Folder |
|---|---|
| Maker | `PouringConfig`, `PouringColorConfig`, `MarblePaintingConfig`, `DippingConfig`, `InjectConfigList`, `AllInjectConfig`, `EveryInject`, `StencilConfig`, `PhoneStencilConfig`, `PopItPhoneConfig`, `PullLevelData`, `StringPullColor`, `GlitterConfig`, `GlitterBGConfig`, `StiringConfig` |
| Device | `PhoneAssetConfig`, `PhoneMapTileConfig` |
| Monetisasi | `StoreItemConfig` |
| Retensi | `DailyMissionData`, `LeaderboardSO` |
| LiveOps | `Liveops.ThematicBundles.BundlesConfig`, `CrazyLabs.Extensions.Database.DatabaseConfig` |

## Kode hasil dekompilasi: `dump/`

| File | Isi |
|---|---|
| `dump/il2cppdumper/dump.cs` | Semua kelas, field, enum, dan signature method |
| `dump/il2cppdumper/stringliteral.json` | Semua string literal di kode |
| `dump/isil_annotated/*.txt` | Isi logika per kelas (1.213 file), sudah diberi nama simbol |

### Kelas penting untuk dicari

| Sistem | Kelas |
|---|---|
| Penilaian bintang & permintaan | `MissionManager` (`GetStarNum`, `InitMission`) |
| Pengaturan global & flag | `GameSettingPrefs` |
| Maker | `enum Maker`, `BrushManager`, `AirPod_Manager` |
| Pelanggan | `enum CustomerType`, `AuctionManager`, `RevengeManger` |
| Gacha skin | `SkinManager` |
| Spin wheel | `SpinWheelBase` |
| Leaderboard | `LeaderBoardData`, `enum ScoreLocation` |
| Idle income | `IdleIncome*` |
| Bundle | `BundleService` |
| Iklan | `RVPlayerManager` |
| Remote config | `DatabaseController` (CrazyLabs) |

## Catatan
- `tables/errors.txt`: 31 MonoBehaviour gagal di-dump. Data inti tidak terdampak.
- Aset visual dan audio belum diekstrak dari `extracted/base/assets/bin/Data/data.unity3d`.
