## 13. GLOSSARY

<a id="glos-13"></a>

<a id="glos-notation"></a>

- **Нотация** — **G** — любая группа; **L0** — группа 0 уровня (базовая); **GH** — группа уровня выше L0 (иерархическое сообщество), идентификатор $ID_{GH}$; **P** — подписант записи; **X** — любой ключ; **O** (other) — любой ключ, кроме подписанта; служебные: $S$ — bootstrap-множество, $H(\cdot)$ — функция хеширования (не путать с GH) ([ARCH-2.1](concept.md#arch-2.1), [FMT-2.8](implementation.md#fmt-2.8)).

**Records**

<a id="glos-consent-object"></a>

- **Consent object** — TTL-запись с автопродлением и мгновенным revoke; два типа: `FRIEND`, `MEMBER_OF` ([ARCH-2.3](concept.md#arch-2.3)).

<a id="glos-action"></a>

- **Action** — запись с мгновенным эффектом, без TTL ([ARCH-2.3](concept.md#arch-2.3)).

<a id="glos-x-revoke"></a>

- **`X_REVOKE`** — паттерн именования: action, отзывающий consent object типа X; подписант revoke совпадает с подписантом объекта ([ARCH-2.3](concept.md#arch-2.3)).

<a id="glos-friend"></a>

- **`FRIEND`** — consent object пары ключей; обе подписи ([LINK-3.1](concept.md#link-3.1)).

<a id="glos-friend-revoke"></a>

- **`FRIEND_REVOKE`** — односторонний разрыв: terminирует instance, создаёт poison mark против контрагента ([LINK-3.2](concept.md#link-3.2)).

<a id="glos-key-loss"></a>

- **`KEY_LOSS`** — отзыв (смерть) ключа: action, подписант — сам ключ; все consent-записи ключа невалидны от $t_{sign}$, новые невалидны по умолчанию; без poison marks и штрафов ([ARCH-2.3.2](concept.md#arch-2.3.2)).

<a id="glos-member-of"></a>

- **`MEMBER_OF(X,G)`** — подтверждение членства «X member of G»: подписант = $X$ — само-членство (для сообществ $ID_{GH}$ — заявление о членстве, голос в C1-quorum); подписант ≠ $X$ — подтверждение другого ([L0-4.2](concept.md#l0-4.2), [HIER-5.2](concept.md#hier-5.2)).

<a id="glos-member-of-revoke"></a>

- **`MEMBER_OF_REVOKE(X,G)`** — отзыв подтверждения членства: подписант $X$ — выход (для сообществ — отзыв заявления); подписант-подтверждающий — отзыв своего подтверждения; quorum отзывов = исключение ([L0-4.2](concept.md#l0-4.2), [HIER-5.2](concept.md#hier-5.2)).

<a id="glos-l0-genesis"></a>

- **`L0_GENESIS`** — адрес L0; без привилегий ([L0-4.5](concept.md#l0-4.5)).

**Time & state**

<a id="glos-t-sign"></a>

- **$t_{sign}$** — подписанное автором время записи; единственный источник времени ([ARCH-2.4.1](concept.md#arch-2.4.1)).

<a id="glos-now"></a>

- **$now()$** — субъективные часы узла ([ARCH-2.4.1](concept.md#arch-2.4.1)).

<a id="glos-future-rule"></a>

- **Future rule / $\Delta$** — $t_{sign} > now+\Delta$: discard с пере-оценкой; в коридоре: deferred ([ARCH-2.4.2](concept.md#arch-2.4.2)).

<a id="glos-lww"></a>

- **LWW** — для записей одного назначения действует max $t_{sign}$; замещение при строго большем; равные → меньший $H(\mathrm{record})$ ([ARCH-2.4.4](concept.md#arch-2.4.4)).

<a id="glos-designation"></a>

- **Designation** — identity записи для конфликтов: тип + ключевые поля (для парных — включая направление) ([ARCH-2.4.4](concept.md#arch-2.4.4)).

<a id="glos-reconstruction"></a>

- **Reconstruction** — нормативное вычисление: сортировка по $(t_{sign}, H(\mathrm{record}))$, последовательное применение ([ARCH-2.4.6](concept.md#arch-2.4.6)).

<a id="glos-stored-record-set"></a>

- **Stored record set** — хранимое множество записей; аргумент функции состояния ([ARCH-2.4.8](concept.md#arch-2.4.8)).

<a id="glos-re-publish"></a>

- **Re-publish** — повторная публикация живых `MEMBER_OF` при изменении membership-статуса ([ARCH-2.4.9](concept.md#arch-2.4.9)).

**Links**

<a id="glos-instance"></a>

- **Instance** — текущий `FRIEND` пары; замещается более свежим ([LINK-3.1](concept.md#link-3.1)).

<a id="glos-binding"></a>

- **Binding** — привязка `FRIEND_REVOKE` к последнему instance с $t_c \le t_{sign}$ ([LINK-3.2.2](concept.md#link-3.2.2)).

<a id="glos-winning-revoke"></a>

- **Winning revoke** — действующий revoke направления: max $t_{sign}$ на instance ([LINK-3.2.3](concept.md#link-3.2.3)).

<a id="glos-mutual-revoke"></a>

- **Mutual revoke** — revoke обоих направлений одной пары; не конфликтуют; обе стороны помечены ([LINK-3.2.3](concept.md#link-3.2.3)).

<a id="glos-poison-mark"></a>

- **Poison mark** — активна на $[t_b, \min(t_c+T_{life}, t_{relink}))$; ≤1 на пару-направление, ≤2 на пару ([LINK-3.2.4](concept.md#link-3.2.4)).

<a id="glos-clamp"></a>

- **Clamp** — $t_b = \min(t_{sign},\ t_c + T_{life})$: разрыв зажат в базовое окно instance ([LINK-3.2.4](concept.md#link-3.2.4)).

<a id="glos-n-x"></a>

- **$N_X$** — число активных marks против $X$; $N_X \le \deg(X)$ ([LINK-3.2](concept.md#link-3.2)).

<a id="glos-window-decay"></a>

- **Window / decay** — $W = T_{life}/(1+N_P+N_O)$; $d(\ell)$ — момент распада; необратимость — относительно текущего множества записей ([LINK-3.3](concept.md#link-3.3)).

<a id="glos-truce"></a>

- **Truce** — свежий `FRIEND` пары: усекает marks обоих направлений, расширяет окна выживающих связей ([LINK-3.2](concept.md#link-3.2), св. 3).

<a id="glos-gc-horizon"></a>

- **GC horizon** — записи пары хранятся до $t_{last}+2T_{life}$; дальше — не влияют ни на что ([ARCH-2.2.5](implementation.md#arch-2.2.5), [LINK-3.4.1](concept.md#link-3.4.1)).

**L0**

<a id="glos-candidate"></a>

- **Candidate** — ключ с живым само-членством `MEMBER_OF` ([L0-4.3.1](concept.md#l0-4.3.1)).

<a id="glos-materialization"></a>

- **Materialization** — вхождение кандидата в активный roster ([L0-4.4](concept.md#l0-4.4)).

<a id="glos-active-member"></a>

- **Active member** — участник, прошедший rounds ([L0-4.3](concept.md#l0-4.3)).

<a id="glos-vouch-quorum"></a>

- **Кворум подтверждений (member-of-quorum)** — $\lfloor |M|/2 \rfloor + 1$ живых `MEMBER_OF` от текущих членов ([L0-4.3.4-a](concept.md#l0-4.3.4-a)).

<a id="glos-cohesion"></a>

- **Cohesion** — $\lfloor |M|/2 \rfloor + 1$ активных связей с активными членами ([L0-4.3.4-b](concept.md#l0-4.3.4-b)).

<a id="glos-synchronous-rounds"></a>

- **Synchronous rounds** — одновременное удаление нарушителей до фикс-точки; sound, не maximal ([L0-4.3.4](concept.md#l0-4.3.4)).

<a id="glos-growth-priority"></a>

- **Growth priority** — начальный roster включает всех кандидатов; присоединение никогда не блокируется ([L0-4.3.3](concept.md#l0-4.3.3)).

<a id="glos-squeeze-out"></a>

- **Squeeze-out** — вытеснение incumbents укрупнёнными порогами; принятая семантика ([L0-4.3.3](concept.md#l0-4.3.3), [LIM-10.16](concept.md#lim-10.16)).

<a id="glos-cap-30"></a>

- **Cap-30** — отбор кандидатов: счёт подтверждений → $t_{sign}$ → pk ([L0-4.3.2](concept.md#l0-4.3.2)).

<a id="glos-freshness-tie-break"></a>

- **Freshness tie-break** — при равных притязаниях выбирается fresher $t_{sign}$ ([L0-4.3.5](concept.md#l0-4.3.5)).

<a id="glos-quench"></a>

- **Quench** — $|M_{act}| < 4$: roster пуст, edges отваливаются каскадом ([L0-4.3.6](concept.md#l0-4.3.6)).

**Hierarchy**

<a id="glos-isolate"></a>

- **Isolate** — 0 живых детей; $R_{str} = \varnothing$; привязывается только bootstrap ([HIER-5.5](concept.md#hier-5.5), [HIER-5.6.2](concept.md#hier-5.6.2)).

<a id="glos-vertex"></a>

- **Vertex** — 2 живых ребёнка — предел бинарности ([HIER-5.5](concept.md#hier-5.5), [HIER-5.5.15](concept.md#hier-5.5.15)).

<a id="glos-free-group"></a>

- **Free group** — 1 живой ребёнок; edge грандфатерится; общие правила ([HIER-5.5](concept.md#hier-5.5), [HIER-5.6.2](concept.md#hier-5.6.2)).

<a id="glos-edge"></a>

- **Edge / child / parent / sister** — привязка $G \to GH$; $G$ — child, $GH$ — parent; другие дети $GH$ — sisters ([HIER-5.5](concept.md#hier-5.5)).

<a id="glos-c1"></a>

- **C1** — quorum живых `MEMBER_OF(P, GH)` ([HIER-5.5](concept.md#hier-5.5)).

<a id="glos-c2"></a>

- **C2 (corroboration)** — пара с единственной живой сестрой; детей у сообщества ≤ 2 ([HIER-5.5](concept.md#hier-5.5), [HIER-5.5.15](concept.md#hier-5.5.15)).

<a id="glos-c3"></a>

- **C3** — acyclicity ([HIER-5.5](concept.md#hier-5.5)).

<a id="glos-hold-window"></a>

- **Hold window ($T_{hold}$)** — непрерывное выполнение условий перед активацией ([HIER-5.5](concept.md#hier-5.5)).

<a id="glos-freeze"></a>

- **Freeze ($T_f$)** — блокировка новых активаций вверх после `L0_GENESIS` и bootstrap; параллелен hold window ([HIER-5.5](concept.md#hier-5.5)).

<a id="glos-bootstrap"></a>

- **Bootstrap / S-set** — совместная активация ровно 2 рёбер к пустой группе (бинарность); все пары внутри $S$; окно на фиксированном $S$; выбор: ранний старт → лексикографический минимум ([HIER-5.5](concept.md#hier-5.5), [HIER-5.5.15](concept.md#hier-5.5.15)).

<a id="glos-attach-detach"></a>

- **Attach / detach** — присоединение к живой группе / мгновенный отрыв (провал C1 или любой пары — оба edge) ([HIER-5.5](concept.md#hier-5.5)–[HIER-5.6](concept.md#hier-5.6)).

<a id="glos-demotion"></a>

- **Demotion** — vertex → free group (1 ребёнок) → isolate (0) с отвалом восходящих edges тем же пересчётом ([HIER-5.6.2](concept.md#hier-5.6.2)).

<a id="glos-grandfathered-edge"></a>

- **Grandfathered edge** — edge свободной группы, сохранённый при понижении ([HIER-5.6.2](concept.md#hier-5.6.2)).

<a id="glos-r-str"></a>

- **$R_{str}$ / $R_{decl}$** — структурный roster (союз живых детей; задаёт численности) / roster заявлений `MEMBER_OF(P, GH)` (не носитель доверия) ([HIER-5.3](concept.md#hier-5.3)).

<a id="glos-level"></a>

- **Level ($L$)** — $1 + \max$ по живым детям; метаданные ([HIER-5.6.3](concept.md#hier-5.6.3)).

<a id="glos-multi-parenting"></a>

- **Multi-parenting** — группа может быть ребёнком любого числа родителей; это штатное состояние DAG ([HIER-5.6.4](concept.md#hier-5.6.4)).

<a id="glos-disjoint-count"></a>

- **Disjoint count ($U$)** — corroboration только во внешнюю часть контрагента ([HIER-5.4.1](concept.md#hier-5.4.1)).

<a id="glos-f-curve"></a>

- **$f$-curve / $\gamma$ / $\kappa$ (conspiracy floor)** — пороговая арифметика пар ([HIER-5.4.2](concept.md#hier-5.4.2)).

**Network**

<a id="glos-neighbor"></a>

- **Neighbor** — узел с активной FRIEND; транспорт совпадает с графом доверения ([ARCH-2.2.1](implementation.md#arch-2.2.1)).

<a id="glos-sync-queue"></a>

- **Sync queue** — исходящий буфер ретрансляции ([ARCH-2.2-impl](implementation.md#arch-2.2-impl)).

<a id="glos-anti-entropy"></a>

- **Anti-entropy** — периодическая сверка множеств записей ([ARCH-2.2.3-impl](implementation.md#arch-2.2.3-impl)); подавляет цензуру и потери ([ARCH-2.2.3](implementation.md#arch-2.2.3)).

<a id="glos-mandatory-zone"></a>

- **Mandatory zone** — свои связи и группы; глубже — политика узла ([ARCH-2.2.4](implementation.md#arch-2.2.4)).

<a id="glos-relevance"></a>

- **Relevance** — политика хранения/ретрансляции, не валидности ([ARCH-2.6.1](concept.md#arch-2.6.1)).

<a id="glos-caps-rate-limit"></a>

- **Caps / rate-limit** — детерминированные лимиты живых объектов и обновлений на ключ ([ARCH-2.6](concept.md#arch-2.6)).

**Trust**

<a id="glos-proof"></a>

- **Proof (subtree)** — все дети каждого parent на пути + перекрёстные связи (C2) + численности ([TRUST-6.1](concept.md#trust-6.1)).

<a id="glos-spot-check"></a>

- **Spot-check** — опрос $k$ случайных участников rosters о записях, затрагивающих proof; расхождение → reject; SHOULD ([TRUST-6.3](concept.md#trust-6.3)).

<a id="glos-trusted-set"></a>

- **Trusted set** — транзитивное замыкание родителей L0 верификатора + его политика ([TRUST-6.2](concept.md#trust-6.2)).

<a id="glos-inclusion-cost"></a>

- **Inclusion cost** — $\approx t$ взаимных живых связей, рекуррентно $\le T_{life}$ ([PRIN-1.3](concept.md#prin-1.3)).

<a id="glos-hijack-localization"></a>

- **Hijack localization** — сжатие окон в $1+N$; чужие marks нестерираемы; против подделки задним числом — `KEY_LOSS` ([DEF-7.3](concept.md#def-7.3), [ARCH-2.3.2](concept.md#arch-2.3.2)).
