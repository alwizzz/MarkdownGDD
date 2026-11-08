# 14. Dokumen Teknis Programmer

[← Kembali ke indeks](00_README.md)

Dokumen ini menerjemahkan desain menjadi arsitektur untuk V1. Angka gameplay **tidak ditulis di kode**. Semuanya ada di modul config (bagian 4) dan bersumber dari [08_Ekonomi.md](08_Ekonomi.md).

---

## 1. Keputusan teknis kunci

| # | Keputusan | Alasan |
|---|---|---|
| 1 | **Case disimpan sebagai *recipe* (data), bukan gambar.** Case = `{device, shape, baseColor, finish, pattern, patternColor, stickers[]}` | Kecil untuk DataStore, bisa dirender ulang di mana saja (bench, rak, tangan avatar, galeri, Hall of Fame), aman dari moderasi UGC karena semua bahan sudah disetujui |
| 2 | **Tanpa `EditableImage` di V1.** Painting memakai grid sel + SurfaceGui sementara, hasil akhir = warna solid + decal | `EditableImage` masih beta, dibatasi memori, dan mewajibkan verifikasi umur/ID [SRC Analisis S23]. Free-paint ditunda |
| 3 | **Server-authoritative untuk ekonomi.** Client hanya mengirim pilihan tiap langkah. Server memvalidasi, **mengukur waktu kerja sendiri**, menghitung bonus, cash, dan XP | Mencegah exploit cash/XP |
| 4 | **Semua angka di ModuleScript config** (`ReplicatedStorage.Shared.Config`) | Prinsip game sumber: semua angka di tabel [SRC 08]. Siap dipindah ke remote config di V1.1 |
| 5 | **NPC divisualkan di client**, logika di server | 8 plot × ±10 NPC = ±80 NPC. Server hanya menyimpan state ringan, client merender model + animasi untuk plot yang dekat |
| 6 | **ProfileStore** untuk data pemain | Session locking, auto-save, aman dari data hilang/duplikasi |
| 7 | **StreamingEnabled aktif** | Device mobile low-end |

---

## 2. Stack & tooling

| Bagian | Pilihan |
|---|---|
| Bahasa | Luau `--!strict` |
| Sinkronisasi file | Rojo + Git |
| Package | Wally: `ProfileStore`, `Signal` (GoodSignal), `Promise`, `t` (validasi tipe remote) |
| UI | React-Lua (`jsdotlua/react`) **atau** Fusion. Pilih satu di awal dan jangan dicampur |
| Test | Jest-Lua / TestEZ untuk modul murni (rumus ekonomi, dispatch, order generator) |
| Lint | Selene + StyLua |

## 3. Struktur folder (Rojo)

```
src/
├─ ReplicatedStorage/Shared/
│  ├─ Config/            -- semua angka desain (bagian 4)
│  ├─ Types.luau         -- tipe Order, CaseRecipe, PlayerData, dll.
│  ├─ Formulas.luau      -- rumus gaji/bonus/XP/AFK (murni, dites)
│  ├─ CaseBuilder.luau   -- recipe → Model case (dipakai client & server)
│  └─ Remotes.luau       -- definisi semua RemoteEvent/Function
├─ ServerScriptService/
│  ├─ Services/
│  │  ├─ DataService        -- ProfileStore, load/save, migrasi skema
│  │  ├─ PlotService        -- assign/reset plot, build tycoon & dekor
│  │  ├─ ShopService        -- customer spawn, kasir, dispatch, waiting table
│  │  ├─ OrderService       -- order generator, validasi craft, reward
│  │  ├─ EmployeeService    -- timer kerja karyawan, upgrade
│  │  ├─ ProgressionService -- XP, level, unlock
│  │  ├─ AfkService         -- Tip Jar, offline income
│  │  ├─ SocialService      -- like, visit, bonus teman/grup/premium
│  │  ├─ GalleryService     -- Best Case of the Week, Hall of Fame
│  │  ├─ MonetizationService-- gamepass, ProcessReceipt, gems
│  │  ├─ QuestService       -- daily login, daily quest, codes
│  │  └─ AnalyticsService   -- wrapper AnalyticsService Roblox
│  └─ Main.server.luau
└─ StarterPlayer/StarterPlayerScripts/
   ├─ Controllers/
   │  ├─ CraftController    -- kamera tetap di Craft Bench, rotasi case per langkah, tray HUD, mini-game
   │  ├─ Steps/             -- ShapeStep, PaintStep, SmoothStep, PatternStep, StickerStep, CleanStep
   │  ├─ NpcController      -- render pelanggan, karyawan, kasir dari state server
   │  ├─ GuideController    -- panah kuning, cincin, tutorial
   │  ├─ InputController    -- PreferredInput, mapping kontrol
   │  └─ AudioController    -- SoundGroup, variasi, ducking
   └─ UI/                   -- HUD, Phone + apps, CraftScreen, Reward, LevelUp
```

---

## 4. Config modules

| Modul | Isi | Sumber |
|---|---|---|
| `Levels` | `xpToNext`, unlock per level (customer, device, decor, tycoon, colors, patterns, stickers, shapes), gems level-up | [07](07_Level_Design.md#2-tabel-level-lengkap-v1) |
| `Devices` | id, nama tampil, `baseCash`, `timeFactor`, daftar `shapes` | [06](06_Pelanggan_Device.md#2-device) |
| `Steps` | id, `cash`, `unlockLevel`, `minDurationSec`, kata konfirmasi, skill karyawan | [04](04_Mekanik_HandsOn.md), [08](08_Ekonomi.md#nilai-komponen) |
| `Customers` | id, `cashMult`, `xpMult`, bobot per level, jumlah elemen request, aturan khusus | [06](06_Pelanggan_Device.md) |
| `Colors` / `Patterns` / `Stickers` / `Shapes` | id, nama, hex/aset, `unlockLevel`, `premiumGems?` | [07](07_Level_Design.md), [15](15_Konten_Aset_MVP.md) |
| `Tycoon` | id, level, harga, efek | [05](05_Toko_Tycoon_Karyawan.md#4-tycoon-fungsional-v1) |
| `Decor` | slot, varian (Basic/Cute/Premium), harga, level | [05](05_Toko_Tycoon_Karyawan.md#5-dekorasi-kosmetik) |
| `Employees` | harga rekrut, skill & biaya, tabel Speed & Quality | [05](05_Toko_Tycoon_Karyawan.md#3-karyawan-employee) |
| `Economy` | bonus kesesuaian (0,25) & kecepatan (0,20), pengali target L1–2 (1,5), bonus sosial, AFK rate & cap, harga Instant Finish/Rush, login, quest | [08](08_Ekonomi.md) |
| `Monetization` | GamePassId, ProductId, isi produk | [09](09_Monetisasi.md) |

Contoh:
```lua
-- Config/Steps.luau
return {
  -- cash = gaji dasar langkah, target = detik untuk bonus kecepatan, minSec = batas anti-exploit
  shape   = { cash = 4,  target = 5,  unlock = 1, minSec = 1.0, word = "PERFECT FIT!", skill = "shape"   },
  paint   = { cash = 6,  target = 18, unlock = 1, minSec = 3.0, word = "COLORFUL!",    skill = "paint"   },
  smooth  = { cash = 4,  target = 16, unlock = 1, minSec = 3.0, word = "SMOOTH!",      skill = "smooth"  },
  glossy  = { cash = 10, target = 6,  unlock = 6, minSec = 1.5, word = "SHINY!",       skill = "glossy", sub = true },
  pattern = { cash = 8,  target = 16, unlock = 2, minSec = 2.0, word = "SPARKLY!",     skill = "pattern" },
  sticker = { cash = 8,  target = 22, unlock = 4, minSec = 1.0, word = "CUTE!",        skill = "sticker" },
  clean   = { cash = 3,  target = 12, unlock = 1, minSec = 2.0, word = "SPOTLESS!",    skill = "clean"   },
}
```

---

## 5. Model data

### 5a. CaseRecipe
```lua
export type CaseRecipe = {
  v: number,                 -- versi skema recipe
  device: string,            -- "aphone" | "samsam" | "earpod" | "tablet" | "macbook"
  shape: string,
  baseColor: string,         -- id warna (bukan RGB)
  finish: "matte" | "glossy",
  pattern: string?, patternColor: string?,
  stickers: { { id: string, u: number, v: number, s: number, r: number } }, -- u,v 0..1; s 0.6..1.4; r derajat
}
```
Ukuran ±150–300 byte (JSON). Album 30 case ≈ 9 KB.

### 5b. Order
```lua
export type Order = {
  id: string, plotId: number,
  customerType: string, device: string,
  steps: { string },                  -- urutan langkah wajib, mis. {"shape","paint","smooth","pattern","clean"}
  request: { shape: string?, baseColor: string?, pattern: string?, patternColor: string?,
             sticker: string?, finish: string? },
  pairIndex: number?,                 -- Old Club: 1 atau 2
  baseSalary: number,                 -- gaji dasar, dihitung server saat order dibuat
  targetSec: number,                  -- waktu target bonus kecepatan
  activeSec: number,                  -- waktu kerja terukur server (tidak termasuk PUT DOWN)
  state: OrderState, assignee: number?, -- userId pemain atau index karyawan
  createdAt: number, startedAt: number?,
}
```

### 5c. PlayerData (ProfileStore, skema v1)
```lua
{
  schema = 1,
  level = 1, xp = 0, prestige = 0,
  cash = 0, gems = 0,
  tycoon = { patternShelf = false, emp1 = false, stickerStock = false, glossyShelf = false,
             emp2 = false, waitingExpand = false, emp3 = false },
  decor = { stool = "basic", table = nil, ... , wallPaint = "cream", floor = "checker_pink", ... },
  ownedDecorVariants = { ["stool.cute"] = true, ... },
  employees = { { name = "Jules", skills = {pattern=true}, speed = 1, quality = 1 }, ... },
  album = { CaseRecipe },            -- maks 30, FIFO
  display = { albumIndex | nil x8 }, -- slot rak
  equipped = albumIndex?,
  tipJar = { amount = 0, lastTick = os.time() },
  premiumOwned = { holoGlitter = true, ... },
  daily = { loginDay = 0, lastLoginDay = 0, quests = {...}, questDay = 0 },
  gallery = { week = 202645, submitted = albumIndex?, pendingRewards = {...} },
  likesGivenToday = 0, likeDay = 0,
  badges = {}, codes = {},
  stats = { casesCrafted = 0, thievesCaught = 0, ... },
  receipts = { [purchaseId] = true },  -- untuk idempotensi (simpan 100 terakhir)
  flags = { ftueStep = 0 },
}
```
Setiap perubahan skema menaikkan `schema` dan menambah fungsi migrasi di `DataService`.

---

## 6. State machine

### 6a. Pelanggan
```
SPAWN → WALK_TO_CASHIER → AT_CASHIER ──dispatch──► (EMPLOYEE | WAITING_TABLE | BACKLOG_SEAT)
   BACKLOG_SEAT ──slot/karyawan tersedia──► (EMPLOYEE | WAITING_TABLE)
   (order selesai, sudah dibayar) → WALK_TO_BENCH → PICKUP (reaksi) → [THIEF_RUN?] → LEAVE → DESPAWN
```

### 6b. Order
```
CREATED → ASSIGNED_EMPLOYEE → EMPLOYEE_WORKING → PAID (langsung saat selesai) → PICKUP (visual)
CREATED → ON_WAITING_TABLE → TAKEN_BY_PLAYER → CRAFTING ⇄ PUT_DOWN_ON_BENCH
                                         → PAID (langsung saat langkah terakhir selesai) → PICKUP (visual)
CREATED → BACKLOG → (ASSIGNED_EMPLOYEE | ON_WAITING_TABLE)
```

### 6c. Karyawan
```
IDLE → (ShopService.assign) → WALK_TO_BENCH → WORKING(durasi = Speed) → PAID (roll bonus Quality & Speed) → IDLE
```

### 6d. Dispatch (ShopService)
```lua
local function canDo(emp, order)
  for _, step in order.steps do
    if not (BASE_SKILLS[step] or emp.skills[step]) then return false end
  end
  return true
end

function ShopService.onCustomerAtCashier(plot, order)
  -- karyawan idle yang mampu, pilih yang skill-nya paling sedikit
  local best, bestCount = nil, math.huge
  for i, emp in plot.employees do
    if emp.state == "IDLE" and canDo(emp, order) then
      local n = countSkills(emp)
      if n < bestCount then best, bestCount = i, n end
    end
  end
  if best then return assignToEmployee(plot, best, order) end
  if #plot.waitingTable < Config.Shop.waitingTableCap(plot) then
    return putOnWaitingTable(plot, order)
  end
  return putInBacklog(plot, order)
end

function ShopService.onEmployeeIdle(plot, empIndex)
  local order = firstInBacklog(plot, function(o) return canDo(plot.employees[empIndex], o) end)
  if order then assignToEmployee(plot, empIndex, order) end
end

function ShopService.onWaitingTableSlotFreed(plot)
  local order = popBacklogForTable(plot) or spawnNewCustomer(plot) -- "auto create new antrian"
  if order then putOnWaitingTable(plot, order) end
end
```
Spawner: setiap 6–10 detik, jika `customersInStore < seats + 1`, spawn pelanggan baru.

---

## 7. Alur craft client ↔ server

```
Client                                   Server
──────                                   ──────
[E] Take Order ───── TakeOrder(orderId) ─► validasi: order ON_WAITING_TABLE di plot pemain,
                                           bench kosong → state TAKEN_BY_PLAYER
            ◄──── OrderTaken(order) ─────
StartCraft(orderId) ─────────────────────► server mulai menghitung activeSec (os.clock)
(mini-game langkah demi langkah, lokal)
setiap langkah selesai:
  StepDone(orderId, step, choice) ───────► validasi:
                                           - step = langkah berikutnya yang benar
                                           - choice sudah dimiliki (warna/pola/stiker/bentuk)
                                           - jeda sejak langkah sebelumnya ≥ Steps[step].minSec × faktor gamepass
                                           simpan ke order.progress
  StepDone langkah TERAKHIR ─────────────► pesanan selesai (tanpa DELIVER):
                                           hentikan timer, cek request (bonus 25%),
                                           activeSec ≤ targetSec (bonus 20%),
                                           hitung cash & XP (Formulas.luau), bayar,
                                           simpan recipe ke Album, pelanggan PICKUP
            ◄──── Reward(payload) ───────  rincian: gaji dasar, bonus sesuai, bonus cepat, bonus sosial
```
- **Client tidak pernah mengirim jumlah cash/XP.** Server menghitung dari `order.baseSalary`, pilihan yang tervalidasi, dan **waktu yang diukur server**. Client tidak mengirim durasi, jadi bonus kecepatan tidak bisa dipalsukan.
- `durationSec` minimum mencegah auto-clicker menyelesaikan pesanan dalam 1 detik. Jika gagal validasi, langkah ditolak (bukan kick). Catat ke analytics `exploit_suspect`.
- Progres pesanan di bench disimpan di server, jadi PUT DOWN / disconnect tidak kehilangan pesanan selama sesi. Timer server berhenti saat PUT DOWN dan lanjut saat Resume.

### Implementasi mini-game (client)
| Langkah | Teknik |
|---|---|
| Shape | List bentuk di tray HUD (filter: device pesanan + sudah terbuka). Tap → `StepDone(shape, shapeId)` → case polos di-spawn dengan tween bounce. Tanpa mini-game |
| Paint / Smoothing | Raycast dari layar ke MeshPart case → posisi lokal di bidang belakang → indeks sel grid 8×16. Visual: `SurfaceGui` dengan 128 `Frame` (warna/transparansi per sel). Setelah selesai, SurfaceGui dihapus dan `Color`/`Material` case diset |
| Glossy | Deteksi 3 drag vertikal panjang (≥ 60% tinggi case) |
| Pattern (glitter) | Hitung goyangan (perubahan arah drag / tap), +8% per goyangan. Decal pola fade-in |
| Pattern (roller) | 3 drag horizontal, `UIGradient` sebagai mask reveal pada decal |
| Sticker | Decal/`ImageLabel` di SurfaceGui pada sisi belakang. Posisi `u,v` di-clamp keluar dari area kamera (`Devices[d].cameraRect`) |
| Clean | 4–6 noda sebagai `ImageLabel`. Setiap noda punya HP 1–2. Drag di atas noda mengurangi HP |

---

## 8. CaseBuilder (shared)

`CaseBuilder.build(recipe, lod)` → Model.

| LOD | Dipakai di | Isi |
|---|---|---|
| `full` | Bench, turntable, Gallery app | Mesh case + warna + finish + pola + stiker + partikel glitter |
| `medium` | Display rack, tangan avatar, bingkai Gallery Square | Tanpa partikel |
| `low` | Toko pemain lain yang jauh, Hall of Fame jauh | Mesh + warna saja |

Cache Model per hash recipe di client supaya rak yang sama tidak dibangun berulang.

---

## 9. Remotes

| Remote | Arah | Payload | Rate limit |
|---|---|---|---|
| `TakeOrder` | C→S | orderId | 2/dtk |
| `StartCraft` | C→S | orderId | 2/dtk |
| `StepDone` | C→S | orderId, step, choice | 5/dtk |
| `PutDown` / `Resume` | C→S | orderId | 2/dtk |
| `StopThief` | C→S | orderId | 5/dtk |
| `RichKidHaggle` / `RichKidAccept` | C→S | orderId | 2/dtk |
| `BuildTycoon` | C→S | tycoonId | 2/dtk |
| `SetDecor` / `BuyDecor` | C→S | slot, variantId | 4/dtk |
| `EmployeeUpgrade` | C→S | empIndex, kind | 2/dtk |
| `SetDisplay` / `EquipCase` | C→S | slot, albumIndex | 4/dtk |
| `CollectTipJar` | C→S | — | 1/dtk |
| `Like` | C→S | targetType, targetId | 2/dtk |
| `GallerySubmit` | C→S | albumIndex | 1/10dtk |
| `RedeemCode` | C→S | string (≤ 20 char) | 1/2dtk |
| `UseGems` | C→S | action (instant/rush/boost/premium), targetId | 2/dtk |
| `PlotState` | S→C | snapshot/delta: pelanggan, order, karyawan | 4–10 Hz delta |
| `PlayerState` | S→C | cash, gems, xp, level, bonus | saat berubah |
| `Reward`, `LevelUp`, `Toast`, `ServerFeed` | S→C | payload UI | — |

Semua payload C→S divalidasi dengan `t` dan rate limit per pemain. Pelanggaran → abaikan + log.

---

## 10. Plot

- 8 plot sebagai Model di Workspace dengan `CFrame` tetap. Saat pemain join → plot kosong pertama, bangun ulang toko dari `PlayerData.tycoon/decor`.
- Saat pemain keluar → simpan data, kosongkan plot (animasi tutup toko di client lain).
- Item tycoon/dekor = template di `ServerStorage.Templates`, di-clone ke slot plot.
- Hologram hanya dibuat di client pemilik (pemain lain tidak perlu melihat hologram orang lain).

## 11. AFK

```lua
function AfkService.tick(data, now)
  local perMin = Formulas.displayIncomePerMin(data)          -- Σ nilai_case × 0.02
  local cap = perMin * (owns(NightShift) and 480 or 180)
  local mins = (now - data.tipJar.lastTick) / 60
  data.tipJar.amount = math.min(cap, data.tipJar.amount + perMin * mins)
  data.tipJar.lastTick = now
end
```
Dipanggil saat join (menghitung offline), setiap 30 detik saat online, dan saat isi rak berubah (supaya rate lama dihitung dulu). `lastTick` memakai `os.time()` server.

## 12. Gallery (Best Case of the Week)

| Data | Penyimpanan |
|---|---|
| Entri minggu ini (recipe + pembuat) | DataStore `Gallery_<week>` key = userId |
| Jumlah like per entri | OrderedDataStore `GalleryLikes_<week>` key = userId. Update dengan `UpdateAsync` (increment), dibatch per server setiap 30 detik |
| Pool entri acak untuk app Gallery | MemoryStore SortedMap `GalleryPool_<week>` (key = userId, value = recipe ringkas), TTL 8 hari |
| Siapa sudah like apa | MemoryStore HashMap `GalleryVoted_<week>_<voterId>`, juga di profile `likesGivenToday` |
| Hall of Fame | Dihitung server saat minggu berganti: `GetSortedAsync(false, 8)` → simpan ke DataStore `HallOfFame_<week>` |
| Hadiah | Saat login, pemain cek peringkatnya di minggu lalu (`GetSortedAsync` halaman + cache) → `pendingRewards` |

`week` = format `YYYYWW` (ISO week, UTC).

## 13. Monetisasi & ProcessReceipt

```lua
MarketplaceService.ProcessReceipt = function(info)
  local profile = DataService.waitForProfile(info.PlayerId)
  if not profile then return Enum.ProductPurchaseDecision.NotProcessedYet end
  if profile.Data.receipts[info.PurchaseId] then
    return Enum.ProductPurchaseDecision.PurchaseGranted          -- sudah diberikan
  end
  local ok = Products.grant(profile, info.ProductId)             -- gems / boost / party / starter
  if not ok then return Enum.ProductPurchaseDecision.NotProcessedYet end
  profile.Data.receipts[info.PurchaseId] = true
  trimReceipts(profile.Data.receipts, 100)
  -- simpan segera supaya grant tidak hilang
  profile:Save()
  return Enum.ProductPurchaseDecision.PurchaseGranted
end
```
- Gamepass dicek dengan `UserOwnsGamePassAsync` saat join (cache) + `PromptGamePassPurchaseFinished` untuk aktivasi langsung.
- **Cash Party** disimpan sebagai boost server di memori server (`partyEndsAt`). Pemain yang join belakangan juga mendapat efek sampai waktu habis.

## 14. Analytics

Pakai `AnalyticsService` Roblox:

| Jenis | Event |
|---|---|
| Funnel FTUE (`LogOnboardingFunnelStepEvent`) | 1 spawn → 2 take_first_order → 3 first_paint → 4 first_order_complete → 5 level2 → 6 build_pattern_shelf → 7 level3 → 8 hire_employee → 9 level5 → 10 display_first_case |
| Progression (`LogProgressionEvent`) | level_up (level, menit main) |
| Economy (`LogEconomyEvent`) | Setiap source/sink cash & gems dengan `itemSku` (contoh `tycoon.glossyShelf`, `order.fancy`) |
| Custom (`LogCustomEvent`) | order_complete (bonus_match, bonus_speed, activeSec, targetSec, langkah, device, customerType), thief_result, haggle_result, gallery_submit, like_given, visit_shop, instant_finish, exploit_suspect |

## 15. Performa & batas

| Item | Target |
|---|---|
| FPS | ≥ 30 di Android low-end (2 GB RAM), ≥ 60 di PC |
| Memori client | ≤ 900 MB di mobile |
| Server heartbeat | ≥ 55 Hz dengan 8 plot penuh |
| NPC | Model NPC hanya di client. `AnimationController` + jalur waypoint tetap (tanpa PathfindingService). Plot > 120 stud: NPC disembunyikan |
| Replikasi plot | Delta state 4–10 Hz, hanya untuk plot dalam radius streaming |
| DataStore | Auto-save ProfileStore (default) + save segera setelah pembelian Robux |

## 16. Testing

| Tes | Cara |
|---|---|
| `Formulas` | Unit test: cocokkan contoh hitungan di [08](08_Ekonomi.md#contoh-hitungan) |
| Paritas simulasi | Script test memanggil `Formulas` dengan input yang sama seperti [tools/economy_sim.py](tools/economy_sim.py), hasil harus identik |
| Dispatch | Unit test skenario: karyawan sibuk, skill kurang, table penuh, backlog |
| Order generator | 10.000 order per level → cek bobot tipe/device dan bahwa semua request bisa dipenuhi |
| Exploit | Kirim `StepDone` beruntun lebih cepat dari `minSec`, choice belum dimiliki, order milik plot lain → semua ditolak |
| Multi-device | Uji di HP Android murah, iPhone, PC, gamepad |
| Load | Server 8 pemain bot (Studio "Start Server, 8 players") 30 menit |
