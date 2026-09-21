#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PNG-график H(B)."""
import csv, os
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FuncFormatter

# Читает dense_for_plot.csv и пишет H_of_B.png рядом со скриптом (портативность).
OUT = str(Path(__file__).resolve().parent)
B, H, HK, HS = [], [], [], []
with open(os.path.join(OUT, 'dense_for_plot.csv')) as fh:
    r = csv.reader(fh, delimiter=';')
    next(r)
    for row in r:
        B.append(int(row[0])); H.append(int(row[1])); HK.append(int(row[2])); HS.append(int(row[3]))

fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
ax.plot(B, H, lw=2.2, color='#b33', drawstyle='steps-post',
        label='H(B): оптимум атакующего (roster / attach, s* оптимизирована)')
ax.plot(B, HK, lw=1.4, ls='--', color='#28a',
        label='Контраст: абсолютный порог K_min=10 (рекомендация №1 прошлого отчёта): max(H,10)')
ax.plot(B, HS, lw=1.2, ls=':', color='#888',
        label='Деградир. summit-вершина (единогласная L0(4)-сестра): только локальный охват')

# изломы/аннотации
ann = [
    (1,    3,      'B=1–3: H=3\n(roster L0(4), quench<4)', (-5, 18), 'left'),
    (4,    3,      'B=4: H=3 (s=m=5)', (3, -16), 'left'),
    (15,   9,      'B=15: s=B не выживает\n(t_min(30)=16>15), s*=16', (6, 12), 'left'),
    (16,   9,      '', (0, 0), 'left'),
    (19,   10,     'B=19: старт γ-режима\ns*<B', (12, 8), 'left'),
    (484,  141,    'B=484: γ·s → κ\n(27–28% B)', (-10, 26), 'right'),
    (17999, 4501,  'ПЛАТО H=4501: B∈[17999..36091]\n(κ=4500 conspiracy floor, §5.4.2/§9)', (-260, 30), 'left'),
    (36092, 4502,  'B≈36·10³: f·B\n(f→5%)', (30, -8), 'left'),
    (10**4, 2571,  'B=10⁴: H=2571\n(vs t_equal=4001)', (-16, -46), 'right'),
    (10**7, 525282, 'B=10⁷: H=525282 (5.25%)', (-150, 12), 'right'),
]
for x, y, txt, (dx, dy), ha in ann:
    if not txt: continue
    ax.annotate(txt, xy=(x, y), xytext=(dx, dy), textcoords='offset points',
                fontsize=8, ha=ha, color='#222',
                arrowprops=dict(arrowstyle='->', color='#555', lw=0.8))

ax.axhline(3, color='#b33', lw=0.6, alpha=0.4)
ax.axhline(4501, color='#960', lw=0.8, ls='-.', alpha=0.6)
ax.text(1.15, 4.0, 'пол цены: H=3 = ⌊4/2⌋+1 (min живой L0, quench<4, §4.3.6/§9)', fontsize=8, color='#960')
ax.text(1.15, 5600, 'conspiracy floor κ=4500 → H=4501', fontsize=8, color='#960')

ax.set_xscale('log'); ax.set_yscale('log')
ax.set_xlim(1, 1.3e7); ax.set_ylim(2, 2e6)
ax.set_xticks([1, 2, 3, 4, 10, 30, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7])
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: ('%g' % x).replace('e+0', 'e')))
ax.set_xlabel('B — число ботов (лог. шкала)')
ax.set_ylabel('H(B) — мин. число людей-соучастников')
ax.set_title('PoSoc v0.13: цена включения B ботов в человеческую сеть\n'
             '(§5.4 f/γ/κ, §5.5 attach+C2, §4.3 roster/quench, §9 параметры; steps-post, лог-лог)')
ax.grid(True, which='major', alpha=0.35, ls='-')
ax.grid(True, which='minor', alpha=0.12, ls=':')
ax.legend(loc='upper left', fontsize=8.5, framealpha=0.95)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'H_of_B.png'))
print('PNG сохранён')
