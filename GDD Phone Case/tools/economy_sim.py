"""
Phone Case Gallery - simulasi ekonomi L1-L10 (V1 / MVP)

Cara pakai:  python3 economy_sim.py
Ubah konstanta di bagian CONFIG, jalankan ulang, lalu salin hasil ke 07_Level_Design.md dan 08_Ekonomi.md.

Model (sengaja sederhana):
- Pemain mengerjakan pesanan satu per satu. Bayaran = gaji dasar + bonus sesuai (25%) + bonus cepat (20%).
  Asumsi rata-rata: 90% pesanan sesuai request, 70% pesanan selesai di bawah waktu target.
- Karyawan mengerjakan pesanan paralel: 1 pesanan / EMP_SECONDS, 60% cash, 25% XP.
  (Asumsi: skill karyawan cukup. Upgrade skill/speed/quality TIDAK dihitung sebagai sink di sini.)
- Pemain membeli item tycoon begitu level & cash cukup, lalu dekor varian Basic
  jika masih ada sisa setelah menyisihkan harga tycoon berikutnya.
- Tidak menghitung: AFK income, bonus teman/grup, gamepass, login, Gems.
  Artinya hasil ini adalah jalur PEMAIN GRATIS, SOLO, TANPA BONUS (paling lambat).
"""

# ---------------- CONFIG ----------------
STEP_CASH = {'shape': 4, 'paint': 6, 'smooth': 4, 'pattern': 8, 'sticker': 8, 'glossy': 10, 'clean': 3}  # gaji dasar per langkah
STEP_TIME = {'shape': 4, 'paint': 16, 'smooth': 14, 'pattern': 14, 'sticker': 18, 'glossy': 4, 'clean': 10}  # detik
STEP_PROB = {'shape': 1, 'paint': 1, 'smooth': 1, 'clean': 1, 'pattern': .7, 'sticker': .6, 'glossy': .4}
STEP_UNLOCK = {'shape': 1, 'paint': 1, 'smooth': 1, 'clean': 1, 'pattern': 2, 'sticker': 4, 'glossy': 6}
OVERHEAD_SEC = 18          # jalan ke waiting table, baca order card, kembali ke bench
BONUS_MATCH, BONUS_SPEED = 0.25, 0.20
P_MATCH, P_SPEED = 0.90, 0.70   # peluang rata-rata pemain mendapat masing-masing bonus
PAY_FACTOR = 1 + BONUS_MATCH * P_MATCH + BONUS_SPEED * P_SPEED
DEVICES = {  # cash dasar, faktor waktu
    'aphone': (14, 1.0), 'samsam': (18, 1.0), 'earpod': (10, 0.7), 'tablet': (28, 1.4), 'macbook': (38, 1.7)}
DEVICE_MIX = [  # (dari level, bobot)
    (1, {'aphone': 1}),
    (3, {'aphone': .6, 'samsam': .4}),
    (5, {'aphone': .45, 'samsam': .35, 'earpod': .2}),
    (7, {'aphone': .35, 'samsam': .3, 'earpod': .15, 'tablet': .2}),
    (9, {'aphone': .3, 'samsam': .25, 'earpod': .15, 'tablet': .15, 'macbook': .15})]
CUSTOMERS = {  # cash mult, xp mult
    'normal': (1.0, 1.0), 'fancy': (1.5, 1.3), 'thief': (1.2, 1.2), 'oldclub': (2.6, 1.6), 'rich': (2.0, 1.5)}
CUSTOMER_MIX = [
    (1, {'normal': 1}),
    (3, {'normal': .75, 'fancy': .25}),
    (5, {'normal': .6, 'fancy': .25, 'thief': .15}),
    (7, {'normal': .5, 'fancy': .22, 'thief': .13, 'oldclub': .15}),
    (9, {'normal': .45, 'fancy': .2, 'thief': .12, 'oldclub': .13, 'rich': .1})]
XP_BASE, XP_PER_STEP = 6, 5
XP_TO_NEXT = {1: 50, 2: 120, 3: 220, 4: 350, 5: 500, 6: 680, 7: 880, 8: 1100, 9: 1350}
EMP_SECONDS, EMP_CASH, EMP_XP = 75, 0.60, 0.25
TYCOON = {2: ('Pattern Shelf', 120), 3: ('Employee #1', 350), 4: ('Sticker Stock', 600),
          6: ('Glossy Finish Paint Shelf', 1500), 7: ('Employee #2', 2200),
          8: ('Waiting Room Expand', 3000), 10: ('Employee #3', 6500)}
DECOR = {2: ('Stool', 60), 4: ('Table', 180), 5: ('Sofa', 400), 6: ('Plant Pot', 300),
         7: ('Trash Bin', 250), 8: ('Statue', 900), 10: ('Fish Tank', 2000)}
AFK_RATE_PER_MIN, AFK_SLOTS, AFK_CAP_MIN = 0.02, 4, 180
# ----------------------------------------


def mix_at(table, level):
    cur = table[0][1]
    for lv, m in table:
        if level >= lv:
            cur = m
    return cur


def order_stats(level):
    steps = [s for s, lv in STEP_UNLOCK.items() if level >= lv]
    step_cash = sum(STEP_CASH[s] * STEP_PROB[s] for s in steps)
    step_time = sum(STEP_TIME[s] * STEP_PROB[s] for s in steps)
    n_steps = sum(STEP_PROB[s] for s in steps if s != 'glossy')
    dm, cm = mix_at(DEVICE_MIX, level), mix_at(CUSTOMER_MIX, level)
    dev_cash = sum(DEVICES[d][0] * w for d, w in dm.items())
    dev_time = sum(DEVICES[d][1] * w for d, w in dm.items())
    c_mult = sum(CUSTOMERS[c][0] * w for c, w in cm.items())
    x_mult = sum(CUSTOMERS[c][1] * w for c, w in cm.items())
    cash = (dev_cash + step_cash) * c_mult * PAY_FACTOR
    xp = (XP_BASE + XP_PER_STEP * n_steps) * x_mult
    sec = step_time * dev_time + OVERHEAD_SEC
    return cash, xp, sec, n_steps


def afk_3h(level):
    steps = [s for s, lv in STEP_UNLOCK.items() if level >= lv]
    best_dev = max((DEVICES[d][0] for d in mix_at(DEVICE_MIX, level)))
    value = (best_dev + sum(STEP_CASH[s] for s in steps)) * (1 + BONUS_MATCH + BONUS_SPEED)  # case terbaik, bayaran penuh
    return value, value * AFK_RATE_PER_MIN * AFK_SLOTS * AFK_CAP_MIN


def run():
    level, xp, cash, t, emps = 1, 0.0, 0.0, 0.0, 0
    owned, log = set(), []
    while level < 10:
        c, x, sec, _ = order_stats(level)
        t += sec
        cash += c
        xp += x
        emp_orders = emps * sec / EMP_SECONDS
        cash += emp_orders * c * EMP_CASH
        xp += emp_orders * x * EMP_XP
        for lv, (name, cost) in sorted(TYCOON.items()):
            if lv <= level and name not in owned and cash >= cost:
                cash -= cost
                owned.add(name)
                log.append((t / 60, level, 'TYCOON', name, cost))
                if name.startswith('Employee'):
                    emps += 1
        pending = [cost for lv, (n, cost) in TYCOON.items() if lv <= level and n not in owned]
        reserve = min(pending) if pending else 0
        for lv, (name, cost) in sorted(DECOR.items()):
            if lv <= level and name not in owned and cash >= cost + reserve:
                cash -= cost
                owned.add(name)
                log.append((t / 60, level, 'DECOR', name, cost))
        if xp >= XP_TO_NEXT[level]:
            xp -= XP_TO_NEXT[level]
            level += 1
            log.append((t / 60, level, 'LEVEL UP', f'cash {cash:.0f}', ''))
    return log, cash, t


if __name__ == '__main__':
    print('=== Per level: rata-rata satu pesanan pemain ===')
    print('Lv | cash/order | xp/order | detik | langkah | cash/menit | xp/menit | AFK nilai case | AFK 3 jam (4 slot)')
    for lv in range(1, 11):
        c, x, s, n = order_stats(lv)
        v, afk = afk_3h(lv)
        print(f'{lv:>2} | {c:>10.0f} | {x:>8.1f} | {s:>5.0f} | {n:>7.1f} | {c*60/s:>10.0f} | {x*60/s:>8.1f} | {v:>14.0f} | {afk:>8.0f}')
    print('\n=== Timeline pemain gratis solo ===')
    log, cash, t = run()
    for m, lv, kind, a, b in log:
        print(f'{m:6.1f} min | L{lv:<2} | {kind:<8} | {a} {b}')
    print(f'\nL10 tercapai di {t/60:.0f} menit main aktif, sisa cash {cash:.0f}')
