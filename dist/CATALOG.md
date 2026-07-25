# Strudel Drum Patterns Catalog 🥁

Total patterns: **1034** across **20** categories.

Import or copy any snippet directly into [Strudel.cc](https://strudel.cc).

---

## (new) Drum and Bass

### (new) Basic Dnb Drum Pattern
**BPM:** 180
**Source:** DrumBeatRepo

```js
// Title: (new) Basic Dnb Drum Pattern
// Category: (new) Drum and Bass
setcpm(180 / 4);
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ [~ ~ ~ sd] ~ ~] [~ [~ ~ ~ sd] [~ sd ~ ~] ~]").bank(bank_sd),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("~ [~ ~ [~ ~ hh ~] [~ ~ hh ~]]").gain("0.85").bank(bank_hh),
  s("hh*8 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [[bd ~ ~ ~] ~ [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - (new) Basic Dnb Drum Pattern
setcpm(180 / 4);
const kit = "RolandTR808";

$: s("[~ [~ ~ ~ sd] ~ ~] [~ [~ ~ ~ sd] [~ sd ~ ~] ~]").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("~ [~ ~ [~ ~ hh ~] [~ ~ hh ~]]").gain("0.85").bank(kit)
$: s("hh*8 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [[bd ~ ~ ~] ~ [~ ~ bd ~] ~]").bank(kit)
```
</details>

---

## Club

### Jersey club
**BPM:** 150
**Source:** DrumBeatRepo

```js
// Title: Jersey club
// Category: Club
setcpm(150 / 4);
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("sd*4").bank(bank_sd),
  s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] [~ ~ bd bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jersey club
setcpm(150 / 4);
const kit = "RolandTR808";

$: s("sd*4").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] [~ ~ bd bd]").bank(kit)
```
</details>

---

## Dancehall

### Modern Dancehall
**BPM:** 105
**Source:** DrumBeatRepo

```js
// Title: Modern Dancehall
// Category: Dancehall
setcpm(105 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[~ ~ ~ sd] [~ ~ sd ~] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Modern Dancehall
setcpm(105 / 4);
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ sd ~] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Reggaeton
**BPM:** 105
**Source:** DrumBeatRepo

```js
// Title: Reggaeton
// Category: Dancehall
setcpm(105 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~]").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggaeton
setcpm(105 / 4);
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Standard dancehall
**BPM:** 105
**Source:** DrumBeatRepo

```js
// Title: Standard dancehall
// Category: Dancehall
setcpm(105 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ [~ ~ sd ~] ~ [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Standard dancehall
setcpm(105 / 4);
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ sd ~] ~ [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(kit)
```
</details>

---

## Drum Machine Patterns

### Afro-Cuban 1 - Break
**Source:** drum-patterns

```js
// Title: Afro-Cuban 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt mt] [mt mt mt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ ~ lt*4").gain("1.0 0.6 0.6 1.0").bank(bank_lt),
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ sd sd sd] [sd ~ ~ ~] ~ ~").gain("0.6 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 1 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ mt mt] [mt mt mt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ lt*4").gain("1.0 0.6 0.6 1.0").bank(kit)
$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ sd sd sd] [sd ~ ~ ~] ~ ~").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Afro-Cuban 1 - Measure A
**Source:** drum-patterns

```js
// Title: Afro-Cuban 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~]").bank(bank_rim),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 1 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~]").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Afro-Cuban 1 - Measure B
**Source:** drum-patterns

```js
// Title: Afro-Cuban 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [~ ~ rim ~] ~ [rim ~ ~ ~]").bank(bank_rim),
  s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 1 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [~ ~ rim ~] ~ [rim ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### Afro-Cuban 2 - Break
**Source:** drum-patterns

```js
// Title: Afro-Cuban 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [mt ~ ~ ~] ~ ~").bank(bank_mt),
  s("~ [~ ~ lt ~] [lt ~]*2 ~").bank(bank_lt),
  s("~ ~ ~ [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[sd sd ~ ~] ~ ~ [sd ~ ~ ~]").gain("0.6 0.6 1.0").bank(bank_sd),
  s("~ ~ ~ [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 2 - Break
const kit = "RolandTR808";

$: s("~ [mt ~ ~ ~] ~ ~").bank(kit)
$: s("~ [~ ~ lt ~] [lt ~]*2 ~").bank(kit)
$: s("~ ~ ~ [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("[sd sd ~ ~] ~ ~ [sd ~ ~ ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ bd ~ ~]").bank(kit)
```
</details>

### Afro-Cuban 2 - Measure A
**Source:** drum-patterns

```js
// Title: Afro-Cuban 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ ~ [lt ~]*2").bank(bank_lt),
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ rim] [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 2 - Measure A
const kit = "RolandTR808";

$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ ~ [lt ~]*2").bank(kit)
$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("[~ ~ ~ rim] [~ ~ rim ~] ~ ~").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Afro-Cuban 2 - Measure B
**Source:** drum-patterns

```js
// Title: Afro-Cuban 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ mt ~] [mt ~ ~ ~]").bank(bank_mt),
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 2 - Measure B
const kit = "RolandTR808";

$: s("~ ~ [~ ~ mt ~] [mt ~ ~ ~]").bank(kit)
$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [~ ~ rim ~] ~ ~").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Afro-Cuban 3 - Break
**Source:** drum-patterns

```js
// Title: Afro-Cuban 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ mt mt] ~ [mt mt ~ ~] [~ ~ mt mt]").gain("0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_mt),
  s("[hh ~ ~ ~] [hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~]").gain("1.0 1.0 0.6 0.6 1.0").bank(bank_hh),
  s("[~ sd ~ ~] [~ sd]*2 [~ ~ ~ sd] [~ sd ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~]").gain("1.0 1.0 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 3 - Break
const kit = "RolandTR808";

$: s("[~ ~ mt mt] ~ [mt mt ~ ~] [~ ~ mt mt]").gain("0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("[hh ~ ~ ~] [hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~]").gain("1.0 1.0 0.6 0.6 1.0").bank(kit)
$: s("[~ sd ~ ~] [~ sd]*2 [~ ~ ~ sd] [~ sd ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~]").gain("1.0 1.0 0.6 0.6 1.0").bank(kit)
```
</details>

### Afro-Cuban 3 - Measure A
**Source:** drum-patterns

```js
// Title: Afro-Cuban 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt ~] [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ rim] ~ ~ ~").bank(bank_rim),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 3 - Measure A
const kit = "RolandTR808";

$: s("~ [~ ~ mt ~] [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("[~ ~ ~ rim] ~ ~ ~").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Afro-Cuban 3 - Measure B
**Source:** drum-patterns

```js
// Title: Afro-Cuban 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt ~] [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ ~ [lt ~]*2").bank(bank_lt),
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ ~ ~").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 3 - Measure B
const kit = "RolandTR808";

$: s("~ [~ ~ mt ~] [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ ~ [lt ~]*2").bank(kit)
$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ ~ ~").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Afro-Cuban 4 - Break
**Source:** drum-patterns

```js
// Title: Afro-Cuban 4 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;

stack(
  s("~ [ht ~]*2 ~ ~").bank(bank_ht),
  s("~ ~ [lt ~]*2 ~").bank(bank_lt),
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[sd ~ ~ sd] ~ ~ [sd ~ ~ ~]").gain("0.6 0.6 1.0").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 4 - Break
const kit = "RolandTR808";

$: s("~ [ht ~]*2 ~ ~").bank(kit)
$: s("~ ~ [lt ~]*2 ~").bank(kit)
$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[sd ~ ~ sd] ~ ~ [sd ~ ~ ~]").gain("0.6 0.6 1.0").bank(kit)
```
</details>

### Afro-Cuban 4 - Measure B
**Source:** drum-patterns

```js
// Title: Afro-Cuban 4 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 4 - Measure B
const kit = "RolandTR808";

$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [~ ~ rim ~] ~ ~").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Afro-Cuban 5 - Break
**Source:** drum-patterns

```js
// Title: Afro-Cuban 5 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[sd ~]*2 [~ ~ sd ~] ~ ~").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 5 - Break
const kit = "RolandTR808";

$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[sd ~]*2 [~ ~ sd ~] ~ ~").bank(kit)
```
</details>

### Afro-Cuban 5 - Measure A
**Source:** drum-patterns

```js
// Title: Afro-Cuban 5 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 5 - Measure A
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ht ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [~ ~ rim ~] ~ ~").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Afro-Cuban 5 - Measure B
**Source:** drum-patterns

```js
// Title: Afro-Cuban 5 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [rim ~ ~ ~] [~ ~ rim ~] ~").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro-Cuban 5 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [rim ~ ~ ~] [~ ~ rim ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Ballad 1 - Break
**Source:** drum-patterns

```js
// Title: Ballad 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [mt mt mt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ ~ lt*4").gain("0.6 0.6 0.6 1.0").bank(bank_lt),
  s("[hh ~]*2 ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ sd sd] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 1 - Break
const kit = "RolandTR808";

$: s("~ ~ [mt mt mt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ lt*4").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("[hh ~]*2 ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [sd ~ sd sd] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Ballad 1 - Measure A
**Source:** drum-patterns

```js
// Title: Ballad 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 1 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Ballad 1 - Measure B
**Source:** drum-patterns

```js
// Title: Ballad 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 1 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Ballad 2 - Break
**Source:** drum-patterns

```js
// Title: Ballad 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [mt ~]*2 ~").bank(bank_mt),
  s("~ ~ ~ lt*4").gain("1.0 0.6 0.6 0.6").bank(bank_lt),
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ sd sd] [sd ~]*2 ~ ~").gain("0.6 0.6 1.0 0.6").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 2 - Break
const kit = "RolandTR808";

$: s("~ ~ [mt ~]*2 ~").bank(kit)
$: s("~ ~ ~ lt*4").gain("1.0 0.6 0.6 0.6").bank(kit)
$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ sd sd] [sd ~]*2 ~ ~").gain("0.6 0.6 1.0 0.6").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Ballad 2 - Measure A
**Source:** drum-patterns

```js
// Title: Ballad 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 2 - Measure A
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 ~").bank(kit)
```
</details>

### Ballad 2 - Measure B
**Source:** drum-patterns

```js
// Title: Ballad 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 2 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ bd ~ ~]").bank(kit)
```
</details>

### Ballad 3 - Break
**Source:** drum-patterns

```js
// Title: Ballad 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ht ht] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [~ ~ lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ ~ sd sd] ~ ~ [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [bd bd ~ ~] [bd bd ~ ~] [bd bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 3 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ ht ht] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ sd sd] ~ ~ [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [bd bd ~ ~] [bd bd ~ ~] [bd bd ~ ~]").bank(kit)
```
</details>

### Ballad 3 - Measure A
**Source:** drum-patterns

```js
// Title: Ballad 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ oh ~ ~]").bank(bank_oh),
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 3 - Measure A
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ oh ~ ~]").bank(kit)
$: s("hh*4").gain("0.85").bank(kit)
$: s("~ ~ [sd ~ ~ ~] [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Ballad 3 - Measure B
**Source:** drum-patterns

```js
// Title: Ballad 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ bd bd] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 3 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd bd] ~ ~").bank(kit)
```
</details>

### Ballad 4 - Break
**Source:** drum-patterns

```js
// Title: Ballad 4 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ mt mt ~] ~ [~ ~ mt ~] [mt mt ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_mt),
  s("~ [~ hh ~ ~] [hh ~ ~ ~] ~").gain("1.0 0.6").bank(bank_hh),
  s("[~ ~ ~ sd] [sd ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd ~ ~] [bd ~ ~ ~] ~").gain("0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 4 - Break
const kit = "RolandTR808";

$: s("[~ mt mt ~] ~ [~ ~ mt ~] [mt mt ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("~ [~ hh ~ ~] [hh ~ ~ ~] ~").gain("1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] [sd ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ bd ~ ~] [bd ~ ~ ~] ~").gain("0.6 1.0 0.6").bank(kit)
```
</details>

### Ballad 4 - Measure A
**Source:** drum-patterns

```js
// Title: Ballad 4 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").gain("1.0 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 4 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").gain("1.0 1.0 0.6 0.6").bank(kit)
```
</details>

### Ballad 4 - Measure B
**Source:** drum-patterns

```js
// Title: Ballad 4 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").gain("1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 4 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").gain("1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### Ballad 5 - Break
**Source:** drum-patterns

```js
// Title: Ballad 5 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ [~ ~ ~ oh] ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("hh*4 [hh hh hh ~] ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] [sd sd ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 5 - Break
const kit = "RolandTR808";

$: s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ ~ oh] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("hh*4 [hh hh hh ~] ~ ~").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] [sd sd ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Ballad 5 - Measure A
**Source:** drum-patterns

```js
// Title: Ballad 5 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(bank_oh),
  s("hh*4 [hh hh hh ~] hh*4 [hh hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 5 - Measure A
const kit = "RolandTR808";

$: s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(kit)
$: s("hh*4 [hh hh hh ~] hh*4 [hh hh hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ ~ ~ bd]").bank(kit)
```
</details>

### Ballad 5 - Measure B
**Source:** drum-patterns

```js
// Title: Ballad 5 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ballad 5 - Measure B
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Blues 1 - Break
**Source:** drum-patterns

```js
// Title: Blues 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 hh*4 [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("sd*12").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4 bd*4 [bd ~ ~ ~] ~").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues 1 - Break
const kit = "RolandTR808";

$: s("hh*4 hh*4 [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("sd*12").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4 bd*4 [bd ~ ~ ~] ~").gain("1.0 0.8").bank(kit)
```
</details>

### Blues 1 - Measure A
**Source:** drum-patterns

```js
// Title: Blues 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*12").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues 1 - Measure A
const kit = "RolandTR808";

$: s("hh*12").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] [bd ~ bd bd] ~").bank(kit)
```
</details>

### Blues 1 - Measure B
**Source:** drum-patterns

```js
// Title: Blues 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*12").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues 1 - Measure B
const kit = "RolandTR808";

$: s("hh*12").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] [bd ~]*2 ~").bank(kit)
```
</details>

### Blues 2 - Break
**Source:** drum-patterns

```js
// Title: Blues 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[~ sd sd ~] [sd sd ~ sd] [sd ~ sd sd] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues 2 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("[~ sd sd ~] [sd sd ~ sd] [sd ~ sd sd] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### Blues 2 - Measure A
**Source:** drum-patterns

```js
// Title: Blues 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [bd ~]*2 [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues 2 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [bd ~]*2 [bd ~]*2 ~").bank(kit)
```
</details>

### Blues 2 - Measure B
**Source:** drum-patterns

```js
// Title: Blues 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*12").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues 2 - Measure B
const kit = "RolandTR808";

$: s("hh*12").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Bossa Nova 1 - Break
**Source:** drum-patterns

```js
// Title: Bossa Nova 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [cr ~ ~ ~] ~ ~").bank(bank_cr),
  s("~ ~ [mt ~]*2 ~").bank(bank_mt),
  s("~ ~ ~ [lt ~ ~ ~]").bank(bank_lt),
  s("[~ ~ hh ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[rim ~ ~ ~] ~ ~ ~").bank(bank_rim),
  s("[~ ~ bd ~] [bd ~ ~ ~] ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa Nova 1 - Break
const kit = "RolandTR808";

$: s("~ [cr ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [mt ~]*2 ~").bank(kit)
$: s("~ ~ ~ [lt ~ ~ ~]").bank(kit)
$: s("[~ ~ hh ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[rim ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] ~ [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa Nova 1 - Measure A
**Source:** drum-patterns

```js
// Title: Bossa Nova 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("[rim ~ ~ ~] [~ ~ rim ~] ~ [rim ~ ~ ~]").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa Nova 1 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("[rim ~ ~ ~] [~ ~ rim ~] ~ [rim ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa Nova 1 - Measure B
**Source:** drum-patterns

```js
// Title: Bossa Nova 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [rim ~ ~ ~] [~ ~ rim ~] ~").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa Nova 1 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [rim ~ ~ ~] [~ ~ rim ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa Nova 2 - Break
**Source:** drum-patterns

```js
// Title: Bossa Nova 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;

stack(
  s("[~ ~ mt ~] [~ ~ mt ~] ~ ~").bank(bank_mt),
  s("~ ~ [~ ~ lt ~] [lt ~ ~ ~]").gain("0.6 1.0").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa Nova 2 - Break
const kit = "RolandTR808";

$: s("[~ ~ mt ~] [~ ~ mt ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ lt ~] [lt ~ ~ ~]").gain("0.6 1.0").bank(kit)
```
</details>

### Bossa Nova 2 - Measure A
**Source:** drum-patterns

```js
// Title: Bossa Nova 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("cr*8").bank(bank_cr),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[~ ~ rim ~] [~ rim ~ ~] [rim ~ ~ rim] ~").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa Nova 2 - Measure A
const kit = "RolandTR808";

$: s("cr*8").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[~ ~ rim ~] [~ rim ~ ~] [rim ~ ~ rim] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa Nova 2 - Measure B
**Source:** drum-patterns

```js
// Title: Bossa Nova 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("cr*8").bank(bank_cr),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa Nova 2 - Measure B
const kit = "RolandTR808";

$: s("cr*8").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Cha-Cha - Break
**Source:** drum-patterns

```js
// Title: Cha-Cha - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ~ ht ~] ~ [ht ~ ~ ~] ~").bank(bank_ht),
  s("~ [lt ~]*2 ~ ~").bank(bank_lt),
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [sd ~ ~ ~]").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Cha-Cha - Break
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ [ht ~ ~ ~] ~").bank(kit)
$: s("~ [lt ~]*2 ~ ~").bank(kit)
$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [sd ~ ~ ~]").bank(kit)
```
</details>

### Cha-Cha - Measure A
**Source:** drum-patterns

```js
// Title: Cha-Cha - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[~ ~ ht ~] [~ ~ ht ~] ~ ~").bank(bank_ht),
  s("~ ~ ~ [lt ~]*2").bank(bank_lt),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Cha-Cha - Measure A
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[~ ~ ht ~] [~ ~ ht ~] ~ ~").bank(kit)
$: s("~ ~ ~ [lt ~]*2").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Cha-Cha - Measure B
**Source:** drum-patterns

```js
// Title: Cha-Cha - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[~ ~ ht ht] ~ [~ ~ ht ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ lt lt] ~ [~ ~ lt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Cha-Cha - Measure B
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[~ ~ ht ht] ~ [~ ~ ht ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ lt lt] ~ [~ ~ lt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Disco 1 - Break
**Source:** drum-patterns

```js
// Title: Disco 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt ~] ~ ~").bank(bank_mt),
  s("[~ ~ oh ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ [lt ~ ~ ~] ~").bank(bank_lt),
  s("[hh hh ~ hh] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd sd ~ sd] [~ sd sd sd] [sd sd ~ ~]").gain("1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("bd*4").gain("0.6 1.0 1.0 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 1 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ mt ~] ~ ~").bank(kit)
$: s("[~ ~ oh ~] ~ ~ ~").bank(kit)
$: s("~ ~ [lt ~ ~ ~] ~").bank(kit)
$: s("[hh hh ~ hh] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [sd sd ~ sd] [~ sd sd sd] [sd sd ~ ~]").gain("1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("bd*4").gain("0.6 1.0 1.0 1.0").bank(kit)
```
</details>

### Disco 1 - Measure A
**Source:** drum-patterns

```js
// Title: Disco 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 1 - Measure A
const kit = "RolandTR808";

$: s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 1 - Measure B
**Source:** drum-patterns

```js
// Title: Disco 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ oh ~ ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ hh] [hh hh ~ hh] [hh ~ hh hh] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] [~ ~ ~ sd] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 1 - Measure B
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ oh ~ ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ hh] [hh hh ~ hh] [hh ~ hh hh] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] [~ ~ ~ sd] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 2 - Break
**Source:** drum-patterns

```js
// Title: Disco 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh hh ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [sd ~]*2 [sd ~]*2 [sd sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 2 - Break
const kit = "RolandTR808";

$: s("[hh hh hh ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [sd ~]*2 [sd ~]*2 [sd sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 2 - Measure A
**Source:** drum-patterns

```js
// Title: Disco 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 2 - Measure A
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 2 - Measure B
**Source:** drum-patterns

```js
// Title: Disco 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[hh ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 2 - Measure B
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[hh ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 3 - Break
**Source:** drum-patterns

```js
// Title: Disco 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cb ~ cb cb]").bank(bank_cb),
  s("~ ~ [mt ~ ~ mt] ~").bank(bank_mt),
  s("hh*4 ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ sd sd] [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 3 - Break
const kit = "RolandTR808";

$: s("~ ~ ~ [cb ~ cb cb]").bank(kit)
$: s("~ ~ [mt ~ ~ mt] ~").bank(kit)
$: s("hh*4 ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [sd ~ sd sd] [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 3 - Measure A
**Source:** drum-patterns

```js
// Title: Disco 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 3 - Measure A
const kit = "RolandTR808";

$: s("[~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 3 - Measure B
**Source:** drum-patterns

```js
// Title: Disco 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 3 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 4 - Break
**Source:** drum-patterns

```js
// Title: Disco 4 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ ~] [~ hh ~ ~] [~ hh ~ ~] [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [sd ~ ~ sd] [sd ~ ~ sd] [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 4 - Break
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ ~] [~ hh ~ ~] [~ hh ~ ~] [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [sd ~ ~ sd] [sd ~ ~ sd] [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 4 - Measure A
**Source:** drum-patterns

```js
// Title: Disco 4 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(bank_oh),
  s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 4 - Measure A
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(kit)
$: s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 4 - Measure B
**Source:** drum-patterns

```js
// Title: Disco 4 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(bank_oh),
  s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] [~ ~ ~ sd] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 4 - Measure B
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(kit)
$: s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] [~ ~ ~ sd] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] [bd ~ ~ ~]").bank(kit)
```
</details>

### Disco 5 - Break
**Source:** drum-patterns

```js
// Title: Disco 5 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ mt*4 ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ oh oh] ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ lt*4").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[hh hh ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ sd*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 5 - Break
const kit = "RolandTR808";

$: s("~ ~ mt*4 ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ oh oh] ~ ~ ~").bank(kit)
$: s("~ ~ ~ lt*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[hh hh ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ sd*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 5 - Measure A
**Source:** drum-patterns

```js
// Title: Disco 5 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh oh] [~ ~ oh ~] [~ ~ oh oh] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ ~] [~ hh]*2 [hh hh ~ ~] [~ hh]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 5 - Measure A
const kit = "RolandTR808";

$: s("[~ ~ oh oh] [~ ~ oh ~] [~ ~ oh oh] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ ~] [~ hh]*2 [hh hh ~ ~] [~ hh]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco 5 - Measure B
**Source:** drum-patterns

```js
// Title: Disco 5 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] ~ ~ [~ ~ ~ oh]").bank(bank_oh),
  s("[hh hh hh ~] [~ hh hh hh] hh*4 [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco 5 - Measure B
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] ~ ~ [~ ~ ~ oh]").bank(kit)
$: s("[hh hh hh ~] [~ hh hh hh] hh*4 [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Endings - Measure A
**Source:** drum-patterns

```js
// Title: Endings - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Endings - Measure A
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Endings - Measure B
**Source:** drum-patterns

```js
// Title: Endings - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Endings - Measure B
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Funk 1 - Break
**Source:** drum-patterns

```js
// Title: Funk 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh ~ ~] [hh ~ ~ ~]").gain("1.0 1.0 0.6 0.6 1.0").bank(bank_hh),
  s("[~ sd sd ~] [sd sd ~ sd] [sd ~ sd sd] [~ ~ sd sd]").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 1.0").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ ~]").gain("1.0 1.0 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 1 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh ~ ~] [hh ~ ~ ~]").gain("1.0 1.0 0.6 0.6 1.0").bank(kit)
$: s("[~ sd sd ~] [sd sd ~ sd] [sd ~ sd sd] [~ ~ sd sd]").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 1.0").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ ~]").gain("1.0 1.0 0.6 0.6 1.0").bank(kit)
```
</details>

### Funk 1 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 1 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Funk 1 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 1 - Measure B
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Funk 10 - Break
**Source:** drum-patterns

```js
// Title: Funk 10 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ hh ~ ~] [~ ~ hh ~] ~").gain("0.85").bank(bank_hh),
  s("[sd sd ~ sd] [sd ~ ~ sd] [sd ~ ~ ~] sd*4").gain("0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(bank_sd),
  s("~ [~ bd ~ ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 10 - Break
const kit = "RolandTR808";

$: s("~ [~ hh ~ ~] [~ ~ hh ~] ~").gain("0.85").bank(kit)
$: s("[sd sd ~ sd] [sd ~ ~ sd] [sd ~ ~ ~] sd*4").gain("0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(kit)
$: s("~ [~ bd ~ ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Funk 10 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 10 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 [~ hh hh hh] hh*4 [~ hh hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 10 - Measure A
const kit = "RolandTR808";

$: s("hh*4 [~ hh hh hh] hh*4 [~ hh hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] ~ ~").bank(kit)
```
</details>

### Funk 10 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 10 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 [~ hh hh hh] hh*4 [~ hh hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 10 - Measure B
const kit = "RolandTR808";

$: s("hh*4 [~ hh hh hh] hh*4 [~ hh hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Funk 11 - Break
**Source:** drum-patterns

```js
// Title: Funk 11 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("~ [~ ht ht ~] [~ ~ ~ ht] ~").gain("0.6 0.6 1.0").bank(bank_ht),
  s("[lt ~ ~ ~] [~ ~ ~ lt] ~ [lt ~ ~ ~]").gain("0.6 1.0 0.6").bank(bank_lt),
  s("[~ ~ sd sd] [sd ~ ~ ~] [sd sd sd ~] [~ ~ sd sd]").gain("0.6 1.0 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 11 - Break
const kit = "RolandTR808";

$: s("~ [~ ht ht ~] [~ ~ ~ ht] ~").gain("0.6 0.6 1.0").bank(kit)
$: s("[lt ~ ~ ~] [~ ~ ~ lt] ~ [lt ~ ~ ~]").gain("0.6 1.0 0.6").bank(kit)
$: s("[~ ~ sd sd] [sd ~ ~ ~] [sd sd sd ~] [~ ~ sd sd]").gain("0.6 1.0 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Funk 11 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 11 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").gain("0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 11 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").gain("0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Funk 11 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 11 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").gain("0.6 1.0").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ bd ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 11 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").gain("0.6 1.0").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Funk 12 - Break
**Source:** drum-patterns

```js
// Title: Funk 12 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("~ ~ mt*4 ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[oh ~]*2 ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ lt*4").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ sd]*2 sd*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 12 - Break
const kit = "RolandTR808";

$: s("~ ~ mt*4 ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[oh ~]*2 ~ ~ ~").bank(kit)
$: s("~ ~ ~ lt*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ sd]*2 sd*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Funk 12 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 12 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] [~ ~ ~ oh] [~ oh]*2 [~ ~ ~ oh]").bank(bank_oh),
  s("[hh hh hh ~] [~ hh hh ~] [hh ~]*2 [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd]*2 [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 12 - Measure A
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [~ ~ ~ oh] [~ oh]*2 [~ ~ ~ oh]").bank(kit)
$: s("[hh hh hh ~] [~ hh hh ~] [hh ~]*2 [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd]*2 [~ ~ ~ bd]").bank(kit)
```
</details>

### Funk 12 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 12 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(bank_oh),
  s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 12 - Measure B
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(kit)
$: s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Funk 13 - Break
**Source:** drum-patterns

```js
// Title: Funk 13 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ mt mt ~] ~ [~ mt]*2").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ ~ sd] [sd ~ ~ ~] [~ sd]*2 [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 13 - Break
const kit = "RolandTR808";

$: s("~ [~ mt mt ~] ~ [~ mt]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ sd] [sd ~ ~ ~] [~ sd]*2 [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Funk 13 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 13 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh hh ~] [hh hh ~ ~] [hh hh hh ~] [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [sd ~]*2").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 13 - Measure A
const kit = "RolandTR808";

$: s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(kit)
$: s("[hh hh hh ~] [hh hh ~ ~] [hh hh hh ~] [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [sd ~]*2").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Funk 13 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 13 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh hh ~] [hh hh ~ ~] [hh hh hh ~] [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 13 - Measure B
const kit = "RolandTR808";

$: s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(kit)
$: s("[hh hh hh ~] [hh hh ~ ~] [hh hh hh ~] [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Funk 14 - Break
**Source:** drum-patterns

```js
// Title: Funk 14 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[sd ~ ~ sd] [sd ~ ~ ~] [sd ~]*2 [sd sd ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_sd),
  s("~ [~ bd ~ ~] ~ [~ bd ~ ~]").gain("0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 14 - Break
const kit = "RolandTR808";

$: s("~ ~ ~ [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("[sd ~ ~ sd] [sd ~ ~ ~] [sd ~]*2 [sd sd ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("~ [~ bd ~ ~] ~ [~ bd ~ ~]").gain("0.6 1.0").bank(kit)
```
</details>

### Funk 14 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 14 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 14 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Funk 14 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 14 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [bd bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 14 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd bd ~ ~] ~").bank(kit)
```
</details>

### Funk 15 - Break
**Source:** drum-patterns

```js
// Title: Funk 15 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ [~ ~ hh ~] ~").gain("0.6 1.0").bank(bank_hh),
  s("[~ ~ sd ~] [sd ~]*2 [sd sd ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").gain("0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 15 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ [~ ~ hh ~] ~").gain("0.6 1.0").bank(kit)
$: s("[~ ~ sd ~] [sd ~]*2 [sd sd ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").gain("0.6 1.0").bank(kit)
```
</details>

### Funk 15 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 15 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 ~").gain("0.85").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 15 - Measure A
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 ~").gain("0.85").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Funk 15 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 15 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 ~").gain("0.85").bank(bank_hh),
  s("~ ~ [sd ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 15 - Measure B
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 ~").gain("0.85").bank(kit)
$: s("~ ~ [sd ~ ~ sd] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Funk 2 - Break
**Source:** drum-patterns

```js
// Title: Funk 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [~ hh ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ ~ sd sd] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [~ bd ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 2 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [~ hh ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ ~ sd sd] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [~ bd ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Funk 2 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ oh] [~ oh]*2 ~").bank(bank_oh),
  s("[hh ~]*2 [hh hh hh ~] ~ [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [~ bd]*2 [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 2 - Measure A
const kit = "RolandTR808";

$: s("~ [~ ~ ~ oh] [~ oh]*2 ~").bank(kit)
$: s("[hh ~]*2 [hh hh hh ~] ~ [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [~ bd]*2 [~ bd ~ ~]").bank(kit)
```
</details>

### Funk 2 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 2 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Funk 3 - Break
**Source:** drum-patterns

```js
// Title: Funk 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] [~ ~ ~ hh] ~ [~ ~ hh ~]").gain("0.6 0.6 1.0").bank(bank_hh),
  s("[~ sd sd sd] [sd sd sd ~] [~ sd sd sd] [sd ~]*2").gain("0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 1.0 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 3 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] [~ ~ ~ hh] ~ [~ ~ hh ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("[~ sd sd sd] [sd sd sd ~] [~ sd sd sd] [sd ~]*2").gain("0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 1.0 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] ~ ~").bank(kit)
```
</details>

### Funk 3 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_hh),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 3 - Measure A
const kit = "RolandTR808";

$: s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
```
</details>

### Funk 3 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_hh),
  s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] ~").gain("1.0 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 3 - Measure B
const kit = "RolandTR808";

$: s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] ~").gain("1.0 0.6 0.6 1.0").bank(kit)
```
</details>

### Funk 4 - Break
**Source:** drum-patterns

```js
// Title: Funk 4 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ht*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("sd*4 ~ sd*4 [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 4 - Break
const kit = "RolandTR808";

$: s("~ ht*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("sd*4 ~ sd*4 [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ bd ~ ~]").bank(kit)
```
</details>

### Funk 4 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 4 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 hh*4 [~ ~ hh ~] [hh hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 4 - Measure A
const kit = "RolandTR808";

$: s("[hh ~]*2 hh*4 [~ ~ hh ~] [hh hh hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Funk 4 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 4 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh hh hh ~] [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] [~ ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 4 - Measure B
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh hh hh ~] [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] [~ ~ ~ sd] ~").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Funk 5 - Break
**Source:** drum-patterns

```js
// Title: Funk 5 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ht*4 ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[hh ~]*2 [~ hh ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 [~ bd ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 5 - Break
const kit = "RolandTR808";

$: s("~ ~ ht*4 ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[hh ~]*2 [~ hh ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 [~ bd ~ ~] ~ ~").bank(kit)
```
</details>

### Funk 5 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 5 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd sd ~ ~] [~ ~ ~ sd] [sd ~ ~ ~]").gain("0.6 1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 5 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd sd ~ ~] [~ ~ ~ sd] [sd ~ ~ ~]").gain("0.6 1.0 0.6 1.0").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Funk 5 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 5 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh hh hh ~] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 5 - Measure B
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh hh hh ~] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Funk 6 - Break
**Source:** drum-patterns

```js
// Title: Funk 6 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [~ ~ lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [sd ~ ~ ~] ~ [~ sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 6 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~ ~ ~] ~ [~ sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Funk 6 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 6 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh ~ hh] [~ ~ hh ~] [hh hh ~ hh] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [sd sd ~ sd] [~ ~ sd ~] [sd sd ~ sd]").gain("0.6 1.0 1.0 0.6 0.6 1.0 1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 6 - Measure A
const kit = "RolandTR808";

$: s("[hh hh ~ hh] [~ ~ hh ~] [hh hh ~ hh] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [sd sd ~ sd] [~ ~ sd ~] [sd sd ~ sd]").gain("0.6 1.0 1.0 0.6 0.6 1.0 1.0 0.6").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(kit)
```
</details>

### Funk 6 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 6 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("~ [~ ~ ~ lt] ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[hh hh ~ hh] [~ ~ hh ~] [hh hh ~ hh] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ [sd sd ~ ~] ~ [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 6 - Measure B
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ [~ ~ ht ~] ~").bank(kit)
$: s("~ [~ ~ ~ lt] ~ [~ ~ ~ lt]").bank(kit)
$: s("[hh hh ~ hh] [~ ~ hh ~] [hh hh ~ hh] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ [sd sd ~ ~] ~ [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(kit)
```
</details>

### Funk 7 - Break
**Source:** drum-patterns

```js
// Title: Funk 7 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [hh ~]*2 ~ ~").gain("0.6 1.0").bank(bank_hh),
  s("[sd ~ ~ sd] ~ [~ sd]*2 sd*4").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_sd),
  s("[~ bd ~ ~] [bd ~]*2 ~ ~").gain("0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 7 - Break
const kit = "RolandTR808";

$: s("~ [hh ~]*2 ~ ~").gain("0.6 1.0").bank(kit)
$: s("[sd ~ ~ sd] ~ [~ sd]*2 sd*4").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("[~ bd ~ ~] [bd ~]*2 ~ ~").gain("0.6 0.6 1.0").bank(kit)
```
</details>

### Funk 7 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 7 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(bank_oh),
  s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] ~ [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 7 - Measure A
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(kit)
$: s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] ~ [~ ~ ~ bd]").bank(kit)
```
</details>

### Funk 7 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 7 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [mt ~ ~ ~]").bank(bank_mt),
  s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(bank_oh),
  s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 7 - Measure B
const kit = "RolandTR808";

$: s("~ ~ ~ [mt ~ ~ ~]").bank(kit)
$: s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(kit)
$: s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Funk 8 - Break
**Source:** drum-patterns

```js
// Title: Funk 8 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ mt ~ ~] [~ mt ~ ~] ~").bank(bank_mt),
  s("~ ~ ~ [hh ~]*2").gain("0.85").bank(bank_hh),
  s("[sd ~]*2 [sd ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ [~ ~ ~ bd] [bd ~]*2").gain("0.6 1.0 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 8 - Break
const kit = "RolandTR808";

$: s("~ [~ mt ~ ~] [~ mt ~ ~] ~").bank(kit)
$: s("~ ~ ~ [hh ~]*2").gain("0.85").bank(kit)
$: s("[sd ~]*2 [sd ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ ~ bd] [bd ~]*2").gain("0.6 1.0 1.0").bank(kit)
```
</details>

### Funk 8 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 8 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*4").bank(bank_oh),
  s("~ [~ ~ sd ~] ~ [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 8 - Measure A
const kit = "RolandTR808";

$: s("oh*4").bank(kit)
$: s("~ [~ ~ sd ~] ~ [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ bd bd] ~").bank(kit)
```
</details>

### Funk 8 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 8 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*4").bank(bank_oh),
  s("~ [~ ~ sd ~] ~ [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 8 - Measure B
const kit = "RolandTR808";

$: s("oh*4").bank(kit)
$: s("~ [~ ~ sd ~] ~ [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ bd bd] ~").bank(kit)
```
</details>

### Funk 9 - Break
**Source:** drum-patterns

```js
// Title: Funk 9 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ sd sd ~] [sd ~ ~ sd] ~ [sd ~ ~ ~]").gain("0.6 0.6 1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ bd] [~ bd ~ ~] [~ bd]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 9 - Break
const kit = "RolandTR808";

$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ sd sd ~] [sd ~ ~ sd] ~ [sd ~ ~ ~]").gain("0.6 0.6 1.0 0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] [~ bd ~ ~] [~ bd]*2 ~").bank(kit)
```
</details>

### Funk 9 - Measure A
**Source:** drum-patterns

```js
// Title: Funk 9 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] ~ ~ ~").bank(bank_oh),
  s("~ [hh hh hh ~] [hh hh hh ~] hh*4").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 9 - Measure A
const kit = "RolandTR808";

$: s("[~ ~ oh ~] ~ ~ ~").bank(kit)
$: s("~ [hh hh hh ~] [hh hh hh ~] hh*4").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ ~ bd]").bank(kit)
```
</details>

### Funk 9 - Measure B
**Source:** drum-patterns

```js
// Title: Funk 9 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ oh]*2 [~ oh]*2 ~").bank(bank_oh),
  s("[hh ~ hh hh] [hh ~ ~ ~] ~ [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ bd bd] [~ bd]*2 [~ bd]*2 [~ bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk 9 - Measure B
const kit = "RolandTR808";

$: s("~ [~ oh]*2 [~ oh]*2 ~").bank(kit)
$: s("[hh ~ hh hh] [hh ~ ~ ~] ~ [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ bd bd] [~ bd]*2 [~ bd]*2 [~ bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### Pop 1 - Break
**Source:** drum-patterns

```js
// Title: Pop 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ lt ~] [lt ~]*2 [lt ~ ~ ~] ~").bank(bank_lt),
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [sd ~]*2 [sd ~ sd sd] [sd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 1 - Break
const kit = "RolandTR808";

$: s("[~ ~ lt ~] [lt ~]*2 [lt ~ ~ ~] ~").bank(kit)
$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [sd ~]*2 [sd ~ sd sd] [sd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Pop 1 - Measure A
**Source:** drum-patterns

```js
// Title: Pop 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 1 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("1.0 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Pop 1 - Measure B
**Source:** drum-patterns

```js
// Title: Pop 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6").bank(bank_hh),
  s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").gain("1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 1 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6").bank(kit)
$: s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").gain("1.0 0.6").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Pop 2 - Break
**Source:** drum-patterns

```js
// Title: Pop 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [mt mt ~ ~] ~").gain("0.6 1.0").bank(bank_mt),
  s("[~ ~ sd sd] ~ ~ sd*4").gain("0.6 1.0 0.6 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~]*2 [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 2 - Break
const kit = "RolandTR808";

$: s("~ ~ [mt mt ~ ~] ~").gain("0.6 1.0").bank(kit)
$: s("[~ ~ sd sd] ~ ~ sd*4").gain("0.6 1.0 0.6 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [~ ~ bd ~] ~").bank(kit)
```
</details>

### Pop 2 - Measure A
**Source:** drum-patterns

```js
// Title: Pop 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [sd ~ ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 2 - Measure A
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [sd ~ ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Pop 2 - Measure B
**Source:** drum-patterns

```js
// Title: Pop 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ ~ sd ~] [~ sd ~ ~]").gain("0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 2 - Measure B
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ ~ sd ~] [~ sd ~ ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### Pop 3 - Break
**Source:** drum-patterns

```js
// Title: Pop 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ mt] ~ ~ ~").bank(bank_mt),
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[sd ~ ~ ~] ~ [~ ~ sd sd] ~").gain("0.6 0.6 1.0").bank(bank_sd),
  s("~ ~ ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 3 - Break
const kit = "RolandTR808";

$: s("[~ ~ ~ mt] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[sd ~ ~ ~] ~ [~ ~ sd sd] ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### Pop 3 - Measure A
**Source:** drum-patterns

```js
// Title: Pop 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[sd ~ ~ sd] ~ [sd ~ ~ sd] ~").bank(bank_sd),
  s("~ [bd ~ bd bd] [~ bd ~ ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 3 - Measure A
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[sd ~ ~ sd] ~ [sd ~ ~ sd] ~").bank(kit)
$: s("~ [bd ~ bd bd] [~ bd ~ ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### Pop 3 - Measure B
**Source:** drum-patterns

```js
// Title: Pop 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ bd bd] [~ bd ~ ~] [bd ~ bd bd] [~ bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 3 - Measure B
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ bd bd] [~ bd ~ ~] [bd ~ bd bd] [~ bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### Pop 4 - Break
**Source:** drum-patterns

```js
// Title: Pop 4 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~]*2 [sd ~ ~ ~] [sd ~ sd sd]").gain("0.6 0.6 0.6 1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").gain("1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 4 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [sd ~]*2 [sd ~ ~ ~] [sd ~ sd sd]").gain("0.6 0.6 0.6 1.0 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").gain("1.0 0.6").bank(kit)
```
</details>

### Pop 4 - Measure A
**Source:** drum-patterns

```js
// Title: Pop 4 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 4 - Measure A
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Pop 4 - Measure B
**Source:** drum-patterns

```js
// Title: Pop 4 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 4 - Measure B
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ bd bd] ~").bank(kit)
```
</details>

### Pop 5 - Break
**Source:** drum-patterns

```js
// Title: Pop 5 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*4").bank(bank_oh),
  s("[~ sd sd sd] [sd ~ sd sd] [sd sd sd ~] sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 5 - Break
const kit = "RolandTR808";

$: s("oh*4").bank(kit)
$: s("[~ sd sd sd] [sd ~ sd sd] [sd sd sd ~] sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Pop 5 - Measure A
**Source:** drum-patterns

```js
// Title: Pop 5 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [sd ~ ~ ~] ~ [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 5 - Measure A
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [sd ~ ~ ~] ~ [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Pop 5 - Measure B
**Source:** drum-patterns

```js
// Title: Pop 5 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] [hh ~ ~ ~] [hh ~ ~ ~] [hh hh ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ ~ sd ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ bd ~ ~]").gain("0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop 5 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] [hh ~ ~ ~] [hh ~ ~ ~] [hh hh ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ ~ sd ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ bd ~ ~]").gain("0.6 0.6 1.0").bank(kit)
```
</details>

### Reggae 1 - Break
**Source:** drum-patterns

```js
// Title: Reggae 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [mt ~]*2 ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [sd ~]*2 ~ [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 1 - Break
const kit = "RolandTR808";

$: s("~ ~ [mt ~]*2 ~").bank(kit)
$: s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [sd ~]*2 ~ [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### Reggae 1 - Measure A
**Source:** drum-patterns

```js
// Title: Reggae 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ [rim ~ ~ rim] [~ rim ~ ~] [rim ~ ~ rim]").bank(bank_rim),
  s("~ bd ~ bd").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 1 - Measure A
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ [rim ~ ~ rim] [~ rim ~ ~] [rim ~ ~ rim]").bank(kit)
$: s("~ bd ~ bd").bank(kit)
```
</details>

### Reggae 1 - Measure B
**Source:** drum-patterns

```js
// Title: Reggae 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[~ ~ rim rim] [~ ~ rim ~] [~ ~ rim rim] [~ ~ rim ~]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("~ bd ~ bd").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 1 - Measure B
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ rim rim] [~ ~ rim ~] [~ ~ rim rim] [~ ~ rim ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ bd ~ bd").bank(kit)
```
</details>

### Reggae 2 - Break
**Source:** drum-patterns

```js
// Title: Reggae 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("0.6 0.6 1.0").bank(bank_mt),
  s("~ ~ [~ ~ lt lt] [lt ~ ~ ~]").gain("0.6 0.6 1.0").bank(bank_lt),
  s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd sd] [sd ~ ~ ~] ~ ~").gain("0.6 0.6 1.0").bank(bank_sd),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 2 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ lt lt] [lt ~ ~ ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd sd] [sd ~ ~ ~] ~ ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### Reggae 2 - Measure A
**Source:** drum-patterns

```js
// Title: Reggae 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] ~").gain("0.85").bank(bank_hh),
  s("~ ~ [rim ~ ~ ~] ~").bank(bank_rim),
  s("~ bd ~ bd").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 2 - Measure A
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] ~").gain("0.85").bank(kit)
$: s("~ ~ [rim ~ ~ ~] ~").bank(kit)
$: s("~ bd ~ bd").bank(kit)
```
</details>

### Reggae 2 - Measure B
**Source:** drum-patterns

```js
// Title: Reggae 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] ~").gain("0.85").bank(bank_hh),
  s("~ rim ~ rim").bank(bank_rim),
  s("~ bd ~ bd").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 2 - Measure B
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] ~").gain("0.85").bank(kit)
$: s("~ rim ~ rim").bank(kit)
$: s("~ bd ~ bd").bank(kit)
```
</details>

### Reggae 3 - Break
**Source:** drum-patterns

```js
// Title: Reggae 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt ~] ~ ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [~ ~ lt ~] [lt ~ ~ ~]").bank(bank_lt),
  s("[sd ~]*2 ~ ~ ~").bank(bank_sd),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 3 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ mt ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ ~ [~ ~ lt ~] [lt ~ ~ ~]").bank(kit)
$: s("[sd ~]*2 ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### Reggae 3 - Measure A
**Source:** drum-patterns

```js
// Title: Reggae 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh hh hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [bd ~ ~ ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 3 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh hh hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ ~ ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### Reggae 3 - Measure B
**Source:** drum-patterns

```js
// Title: Reggae 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 3 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Reggae 4 - Break
**Source:** drum-patterns

```js
// Title: Reggae 4 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ ~ hh] ~ [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[sd sd sd ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ ~ bd] ~ [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 4 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ hh] ~ [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("[sd sd sd ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ bd] ~ [~ bd ~ ~] ~").bank(kit)
```
</details>

### Reggae 4 - Measure A
**Source:** drum-patterns

```js
// Title: Reggae 4 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] ~ [~ oh ~ ~] ~").bank(bank_oh),
  s("[hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[rim ~ ~ ~] [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("~ [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 4 - Measure A
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] ~ [~ oh ~ ~] ~").bank(kit)
$: s("[hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("[rim ~ ~ ~] [~ ~ rim ~] ~ ~").bank(kit)
$: s("~ [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### Reggae 4 - Measure B
**Source:** drum-patterns

```js
// Title: Reggae 4 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] ~ [~ oh ~ ~] ~").bank(bank_oh),
  s("[hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[rim ~ ~ ~] [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("[~ ~ bd ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 4 - Measure B
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] ~ [~ oh ~ ~] ~").bank(kit)
$: s("[hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("[rim ~ ~ ~] [~ ~ rim ~] ~ ~").bank(kit)
$: s("[~ ~ bd ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Reggae 5 - Break
**Source:** drum-patterns

```js
// Title: Reggae 5 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ mt] [~ mt mt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [~ lt]*2 ~").bank(bank_lt),
  s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").bank(bank_sd),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 5 - Break
const kit = "RolandTR808";

$: s("[~ ~ ~ mt] [~ mt mt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ lt]*2 ~").bank(kit)
$: s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### Reggae 5 - Measure A
**Source:** drum-patterns

```js
// Title: Reggae 5 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 5 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Reggae 5 - Measure B
**Source:** drum-patterns

```js
// Title: Reggae 5 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh oh] [~ ~ oh oh] [~ ~ oh oh] [~ ~ oh oh]").bank(bank_oh),
  s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [rim ~ ~ ~] ~ [rim ~ ~ rim]").bank(bank_rim),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae 5 - Measure B
const kit = "RolandTR808";

$: s("[~ ~ oh oh] [~ ~ oh oh] [~ ~ oh oh] [~ ~ oh oh]").bank(kit)
$: s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("~ [rim ~ ~ ~] ~ [rim ~ ~ rim]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Rhythm & Blues 1 - Break
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ~ mt ~] ~ [mt ~ ~ ~] ~").bank(bank_mt),
  s("~ [lt ~ ~ ~] [~ ~ lt ~] ~").bank(bank_lt),
  s("[sd sd ~ sd] [~ sd sd sd] [~ sd]*2 sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 1 - Break
const kit = "RolandTR808";

$: s("[~ ~ mt ~] ~ [mt ~ ~ ~] ~").bank(kit)
$: s("~ [lt ~ ~ ~] [~ ~ lt ~] ~").bank(kit)
$: s("[sd sd ~ sd] [~ sd sd sd] [~ sd]*2 sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Rhythm & Blues 1 - Measure A
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ [sd ~ ~ sd]").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 1 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ ~] ~ [sd ~ ~ sd]").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Rhythm & Blues 1 - Measure B
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 1 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ bd bd] ~").bank(kit)
```
</details>

### Rhythm & Blues 2 - Break
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [mt mt ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[sd sd ~ ~] ~ ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ bd bd] [~ ~ bd bd] [~ ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 2 - Break
const kit = "RolandTR808";

$: s("~ [mt mt ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd ~ ~] ~ ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd bd] [~ ~ bd bd] [~ ~ bd bd] ~").bank(kit)
```
</details>

### Rhythm & Blues 2 - Measure A
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ bd]*2 [~ ~ bd bd] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 2 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ bd]*2 [~ ~ bd bd] [~ bd ~ ~]").bank(kit)
```
</details>

### Rhythm & Blues 2 - Measure B
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("sd*4").bank(bank_sd),
  s("[~ ~ ~ bd] [~ bd bd ~] [~ bd]*2 [~ bd bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 2 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("sd*4").bank(kit)
$: s("[~ ~ ~ bd] [~ bd bd ~] [~ bd]*2 [~ bd bd ~]").bank(kit)
```
</details>

### Rhythm & Blues 3 - Break
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ lt ~ ~] ~ ~").bank(bank_lt),
  s("[hh ~ ~ hh] [hh ~ ~ hh] ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] ~ [sd ~ sd sd] [~ ~ sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] ~ [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 3 - Break
const kit = "RolandTR808";

$: s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ lt ~ ~] ~ ~").bank(kit)
$: s("[hh ~ ~ hh] [hh ~ ~ hh] ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] ~ [sd ~ sd sd] [~ ~ sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] ~ [~ ~ ~ bd]").bank(kit)
```
</details>

### Rhythm & Blues 3 - Measure A
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd]*2 [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 3 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd]*2 [~ bd ~ ~]").bank(kit)
```
</details>

### Rhythm & Blues 3 - Measure B
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ sd sd] ~ [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ bd bd] ~ [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 3 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ [sd ~ sd sd] ~ [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ bd bd] ~ [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Rhythm & Blues 4 - Break
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 4 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt mt] [mt ~ ~ ~] [mt ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ ~ hh] ~ [~ ~ hh ~] ~").gain("0.85").bank(bank_hh),
  s("[~ sd sd ~] [sd ~ ~ ~] [~ ~ sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 4 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ mt mt] [mt ~ ~ ~] [mt ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ hh] ~ [~ ~ hh ~] ~").gain("0.85").bank(kit)
$: s("[~ sd sd ~] [sd ~ ~ ~] [~ ~ sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ bd ~ ~] ~").bank(kit)
```
</details>

### Rhythm & Blues 4 - Measure A
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 4 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 4 - Measure A
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ bd bd] ~").bank(kit)
```
</details>

### Rhythm & Blues 4 - Measure B
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 4 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ [sd ~ ~ sd]").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 4 - Measure B
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] ~ [sd ~ ~ sd]").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Rhythm & Blues 5 - Break
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 5 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [mt mt mt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [lt lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ sd sd ~] ~ ~ [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 5 - Break
const kit = "RolandTR808";

$: s("~ [mt mt mt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [lt lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ sd sd ~] ~ ~ [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Rhythm & Blues 5 - Measure A
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 5 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd bd ~ bd] [bd ~]*2 [bd bd ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 5 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd bd ~ bd] [bd ~]*2 [bd bd ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Rhythm & Blues 5 - Measure B
**Source:** drum-patterns

```js
// Title: Rhythm & Blues 5 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ bd bd] [~ ~ ~ bd] [bd ~ bd bd] [~ bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rhythm & Blues 5 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ bd bd] [~ ~ ~ bd] [bd ~ bd bd] [~ bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### Rock 1 - Break
**Source:** drum-patterns

```js
// Title: Rock 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ ht] [ht ~ ~ ht] [ht ~ ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~] sd*4").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 1 - Break
const kit = "RolandTR808";

$: s("[~ ~ ~ ht] [ht ~ ~ ht] [ht ~ ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~] sd*4").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Rock 1 - Measure A
**Source:** drum-patterns

```js
// Title: Rock 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.6 1.0 0.6 1.0").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 1 - Measure A
const kit = "RolandTR808";

$: s("hh*4").gain("0.6 1.0 0.6 1.0").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Rock 1 - Measure B
**Source:** drum-patterns

```js
// Title: Rock 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 1 - Measure B
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### Rock 2 - Break
**Source:** drum-patterns

```js
// Title: Rock 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cr ~]*2").bank(bank_cr),
  s("~ mt*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ lt*4 ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("sd*4 ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 [~ bd ~ ~] [bd ~]*2 [bd ~]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 2 - Break
const kit = "RolandTR808";

$: s("~ ~ ~ [cr ~]*2").bank(kit)
$: s("~ mt*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ lt*4 ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("sd*4 ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 [~ bd ~ ~] [bd ~]*2 [bd ~]*2").bank(kit)
```
</details>

### Rock 2 - Measure A
**Source:** drum-patterns

```js
// Title: Rock 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ oh]").bank(bank_oh),
  s("hh*4 hh*4 hh*4 [hh hh hh ~]").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] [~ ~ ~ bd]").gain("1.0 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 2 - Measure A
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ oh]").bank(kit)
$: s("hh*4 hh*4 hh*4 [hh hh hh ~]").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] [~ ~ ~ bd]").gain("1.0 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### Rock 2 - Measure B
**Source:** drum-patterns

```js
// Title: Rock 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(bank_oh),
  s("hh*4 [hh hh hh ~] hh*4 [hh hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ [sd ~]*2").bank(bank_sd),
  s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 2 - Measure B
const kit = "RolandTR808";

$: s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(kit)
$: s("hh*4 [hh hh hh ~] hh*4 [hh hh hh ~]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] ~ [sd ~]*2").bank(kit)
$: s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] [~ ~ ~ bd]").bank(kit)
```
</details>

### Rock 3 - Break
**Source:** drum-patterns

```js
// Title: Rock 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 3 - Break
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Rock 3 - Measure A
**Source:** drum-patterns

```js
// Title: Rock 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 3 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Rock 3 - Measure B
**Source:** drum-patterns

```js
// Title: Rock 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 3 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Rock 4 - Break
**Source:** drum-patterns

```js
// Title: Rock 4 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("sd*16").gain("1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 4 - Break
const kit = "RolandTR808";

$: s("sd*16").gain("1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Rock 4 - Measure A
**Source:** drum-patterns

```js
// Title: Rock 4 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 4 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Rock 4 - Measure B
**Source:** drum-patterns

```js
// Title: Rock 4 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("sd*4").gain("0.6 1.0 0.6 1.0").bank(bank_sd),
  s("bd*4").gain("0.6 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 4 - Measure B
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("sd*4").gain("0.6 1.0 0.6 1.0").bank(kit)
$: s("bd*4").gain("0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### Rock 5 - Break
**Source:** drum-patterns

```js
// Title: Rock 5 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ ~]").gain("0.6 1.0 1.0 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 5 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ ~]").gain("0.6 1.0 1.0 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Rock 5 - Measure A
**Source:** drum-patterns

```js
// Title: Rock 5 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 5 - Measure A
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Rock 5 - Measure B
**Source:** drum-patterns

```js
// Title: Rock 5 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock 5 - Measure B
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Samba 1 - Break
**Source:** drum-patterns

```js
// Title: Samba 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;

stack(
  s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [~ ~ lt lt] [lt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[sd ~ sd sd] [sd ~ ~ ~] ~ [~ ~ sd ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 1 - Break
const kit = "RolandTR808";

$: s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ lt lt] [lt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[sd ~ sd sd] [sd ~ ~ ~] ~ [~ ~ sd ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Samba 1 - Measure A
**Source:** drum-patterns

```js
// Title: Samba 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[~ ~ ~ mt] ~ ~ ~").bank(bank_mt),
  s("~ [~ ~ ~ lt] ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[~ hh hh ~] [~ hh hh ~] [~ hh hh ~] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 1 - Measure A
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[~ ~ ~ mt] ~ ~ ~").bank(kit)
$: s("~ [~ ~ ~ lt] ~ [~ ~ ~ lt]").bank(kit)
$: s("[~ hh hh ~] [~ hh hh ~] [~ hh hh ~] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba 1 - Measure B
**Source:** drum-patterns

```js
// Title: Samba 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~]*2 [cb cb ~ cb] [~ cb cb ~] [cb cb ~ cb]").bank(bank_cb),
  s("~ ~ [~ ~ ~ mt] ~").bank(bank_mt),
  s("[~ hh]*2 [~ ~ hh ~] [hh ~ ~ ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 1 - Measure B
const kit = "RolandTR808";

$: s("[cb ~]*2 [cb cb ~ cb] [~ cb cb ~] [cb cb ~ cb]").bank(kit)
$: s("~ ~ [~ ~ ~ mt] ~").bank(kit)
$: s("[~ hh]*2 [~ ~ hh ~] [hh ~ ~ ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba 2 - Break
**Source:** drum-patterns

```js
// Title: Samba 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("[mt ~ ~ mt] [~ ~ mt ~] [~ mt ~ ~] [mt ~ ~ mt]").bank(bank_mt),
  s("~ [lt ~ ~ ~] [~ ~ lt ~] ~").bank(bank_lt),
  s("[~ sd sd ~] [~ ~ ~ sd] [sd ~ ~ ~] [~ sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 2 - Break
const kit = "RolandTR808";

$: s("[mt ~ ~ mt] [~ ~ mt ~] [~ mt ~ ~] [mt ~ ~ mt]").bank(kit)
$: s("~ [lt ~ ~ ~] [~ ~ lt ~] ~").bank(kit)
$: s("[~ sd sd ~] [~ ~ ~ sd] [sd ~ ~ ~] [~ sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Samba 2 - Measure A
**Source:** drum-patterns

```js
// Title: Samba 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[~ ~ rim ~] [~ rim ~ ~] [rim ~ ~ ~] ~").bank(bank_rim),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 2 - Measure A
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[~ ~ rim ~] [~ rim ~ ~] [rim ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba 2 - Measure B
**Source:** drum-patterns

```js
// Title: Samba 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ mt] ~ ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[~ rim ~ ~] [~ rim ~ ~] [~ rim ~ ~] [~ rim ~ ~]").bank(bank_rim),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 2 - Measure B
const kit = "RolandTR808";

$: s("~ [~ ~ ~ mt] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ lt]").bank(kit)
$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[~ rim ~ ~] [~ rim ~ ~] [~ rim ~ ~] [~ rim ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba 3 - Break
**Source:** drum-patterns

```js
// Title: Samba 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] [ht ~ ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ [mt ~ ~ ~] ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ ~ oh]").bank(bank_oh),
  s("~ ~ [~ ~ ~ lt] [~ ~ lt ~]").bank(bank_lt),
  s("[hh hh ~ ~] [~ ~ hh hh] [~ ~ hh ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ sd] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 3 - Break
const kit = "RolandTR808";

$: s("[~ ~ ht ~] [ht ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [mt ~ ~ ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ oh]").bank(kit)
$: s("~ ~ [~ ~ ~ lt] [~ ~ lt ~]").bank(kit)
$: s("[hh hh ~ ~] [~ ~ hh hh] [~ ~ hh ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ sd] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba 3 - Measure A
**Source:** drum-patterns

```js
// Title: Samba 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 3 - Measure A
const kit = "RolandTR808";

$: s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### Samba 3 - Measure B
**Source:** drum-patterns

```js
// Title: Samba 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ hh]*2 [~ ~ hh ~] [hh ~ ~ hh] [~ ~ hh ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("[sd ~]*2 [sd sd ~ sd] [~ sd sd ~] [sd sd ~ sd]").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("0.6 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba 3 - Measure B
const kit = "RolandTR808";

$: s("[~ hh]*2 [~ ~ hh ~] [hh ~ ~ hh] [~ ~ hh ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[sd ~]*2 [sd sd ~ sd] [~ sd sd ~] [sd sd ~ sd]").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("0.6 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### Shuffle 1 - Break
**Source:** drum-patterns

```js
// Title: Shuffle 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [~ ~ sd ~] [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [bd bd ~ bd] [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle 1 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ sd ~] [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [bd bd ~ bd] [bd ~ bd bd] ~").bank(kit)
```
</details>

### Shuffle 1 - Measure A
**Source:** drum-patterns

```js
// Title: Shuffle 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle 1 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] ~ ~").bank(kit)
```
</details>

### Shuffle 1 - Measure B
**Source:** drum-patterns

```js
// Title: Shuffle 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle 1 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Shuffle 2 - Break
**Source:** drum-patterns

```js
// Title: Shuffle 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ sd sd ~] sd*4 [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle 2 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ sd sd ~] sd*4 [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Shuffle 2 - Measure A
**Source:** drum-patterns

```js
// Title: Shuffle 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle 2 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Shuffle 2 - Measure B
**Source:** drum-patterns

```js
// Title: Shuffle 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle 2 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Ska - Break
**Source:** drum-patterns

```js
// Title: Ska - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;

stack(
  s("~ [mt ~]*2 ~ ~").bank(bank_mt),
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[sd ~ sd sd] ~ [sd ~]*2 [sd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ska - Break
const kit = "RolandTR808";

$: s("~ [mt ~]*2 ~ ~").bank(kit)
$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[sd ~ sd sd] ~ [sd ~]*2 [sd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Ska - Measure A
**Source:** drum-patterns

```js
// Title: Ska - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ska - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 1.0 0.6 1.0 0.6 1.0 0.6 1.0").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Ska - Measure B
**Source:** drum-patterns

```js
// Title: Ska - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ska - Measure B
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Swing 1 - Break
**Source:** drum-patterns

```js
// Title: Swing 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [~ ~ sd sd] sd*4 ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 1 - Break
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [~ ~ sd sd] sd*4 ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] ~ ~ ~").bank(kit)
```
</details>

### Swing 1 - Measure A
**Source:** drum-patterns

```js
// Title: Swing 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 1 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### Swing 1 - Measure B
**Source:** drum-patterns

```js
// Title: Swing 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 1 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### Swing 2 - Break
**Source:** drum-patterns

```js
// Title: Swing 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ hh ~] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [~ ~ ~ sd] [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd bd bd ~] [bd bd bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 2 - Break
const kit = "RolandTR808";

$: s("~ ~ [~ ~ hh ~] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ ~ sd] [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd bd ~] [bd bd bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Swing 2 - Measure A
**Source:** drum-patterns

```js
// Title: Swing 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ hh hh ~] [~ hh]*2 ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 2 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ hh hh ~] [~ hh]*2 ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### Swing 2 - Measure B
**Source:** drum-patterns

```js
// Title: Swing 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ hh hh ~] [~ hh]*2 ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ bd] [~ bd bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 2 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ hh hh ~] [~ hh]*2 ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ bd] [~ bd bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### Swing 3 - Break
**Source:** drum-patterns

```js
// Title: Swing 3 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [mt mt ~ ~] [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[oh ~ ~ oh] [~ ~ oh ~] [~ oh ~ ~] ~").bank(bank_oh),
  s("[~ sd sd ~] [~ ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 3 - Break
const kit = "RolandTR808";

$: s("~ [mt mt ~ ~] [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[oh ~ ~ oh] [~ ~ oh ~] [~ oh ~ ~] ~").bank(kit)
$: s("[~ sd sd ~] [~ ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### Swing 3 - Measure A
**Source:** drum-patterns

```js
// Title: Swing 3 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ ~ cr ~] [~ cr]*2 ~").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd bd ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 3 - Measure A
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ ~ cr ~] [~ cr]*2 ~").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Swing 3 - Measure B
**Source:** drum-patterns

```js
// Title: Swing 3 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ ~ cr ~] [~ cr ~ ~] ~").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing 3 - Measure B
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ ~ cr ~] [~ cr ~ ~] ~").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Twist 1 - Break
**Source:** drum-patterns

```js
// Title: Twist 1 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [mt ~]*2 ~ ~").bank(bank_mt),
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ ~ ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist 1 - Break
const kit = "RolandTR808";

$: s("~ [mt ~]*2 ~ ~").bank(kit)
$: s("hh*4").gain("0.85").bank(kit)
$: s("~ ~ ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Twist 1 - Measure A
**Source:** drum-patterns

```js
// Title: Twist 1 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist 1 - Measure A
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Twist 1 - Measure B
**Source:** drum-patterns

```js
// Title: Twist 1 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [sd ~]*2 ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist 1 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [sd ~]*2 ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Twist 2 - Break
**Source:** drum-patterns

```js
// Title: Twist 2 - Break
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [mt ~]*2 ~").bank(bank_mt),
  s("~ [sd ~]*2 ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist 2 - Break
const kit = "RolandTR808";

$: s("~ ~ [mt ~]*2 ~").bank(kit)
$: s("~ [sd ~]*2 ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Twist 2 - Measure A
**Source:** drum-patterns

```js
// Title: Twist 2 - Measure A
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.6 0.6 1.0 0.6 1.0").bank(bank_hh),
  s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist 2 - Measure A
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.6 0.6 1.0 0.6 1.0").bank(kit)
$: s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Twist 2 - Measure B
**Source:** drum-patterns

```js
// Title: Twist 2 - Measure B
// Category: Drum Machine Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist 2 - Measure B
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

---

## Drum Machine Patterns (260)

### AfroCub1
**Source:** drum-patterns

```js
// Title: AfroCub1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ rim] [~ ~ rim ~] ~ [rim ~ ~ ~]").bank(bank_rim),
  s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub1
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("[~ ~ ~ rim] [~ ~ rim ~] ~ [rim ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### AfroCub2
**Source:** drum-patterns

```js
// Title: AfroCub2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_rim = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [~ ~ ht ~] ~ ~").bank(bank_ht),
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("[~ ~ ~ rim] ~ ~ [rim ~ ~ ~]").bank(bank_rim),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub2
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [~ ~ ht ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("[~ ~ ~ rim] ~ ~ [rim ~ ~ ~]").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### AfroCub3
**Source:** drum-patterns

```js
// Title: AfroCub3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_rim = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [cr ~]*2 [cr ~]*2 [cr ~]*2").bank(bank_cr),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub3
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [cr ~]*2 [cr ~]*2 [cr ~]*2").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ [~ ~ rim ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### AfroCub4
**Source:** drum-patterns

```js
// Title: AfroCub4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [cr ~]*2 [cr ~]*2 [cr ~]*2").bank(bank_cr),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("[~ ~ ~ rim] [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~]").bank(bank_rim),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub4
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [cr ~]*2 [cr ~]*2 [cr ~]*2").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("[~ ~ ~ rim] [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~]").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### AfroCub5
**Source:** drum-patterns

```js
// Title: AfroCub5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.6 0.6 1.0 1.0").bank(bank_hh),
  s("[mt ~ ~ ~] ~ [mt ~]*2 ~").bank(bank_mt),
  s("[~ ~ sd sd] [~ sd sd ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ lt*4").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("bd*4").gain("1.0 0.6 1.0 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub5
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.6 0.6 1.0 1.0").bank(kit)
$: s("[mt ~ ~ ~] ~ [mt ~]*2 ~").bank(kit)
$: s("[~ ~ sd sd] [~ sd sd ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ lt*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.6 1.0 1.0").bank(kit)
```
</details>

### AfroCub6
**Source:** drum-patterns

```js
// Title: AfroCub6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[rim ~ rim rim] [~ rim]*2 [rim ~]*2 [rim rim ~ rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[cb ~ cb cb] [~ cb]*2 [cb ~]*2 [cb cb ~ cb]").bank(bank_cb),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub6
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[rim ~ rim rim] [~ rim]*2 [rim ~]*2 [rim rim ~ rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[cb ~ cb cb] [~ cb]*2 [cb ~]*2 [cb cb ~ cb]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### AfroCub7
**Source:** drum-patterns

```js
// Title: AfroCub7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_rim = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [cr ~]*2 [cr ~ cr cr] [cr ~]*2").bank(bank_cr),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [mt ~]*2 ~").bank(bank_mt),
  s("~ [rim ~ ~ ~] ~ ~").bank(bank_rim),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub7
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [cr ~]*2 [cr ~ cr cr] [cr ~]*2").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [mt ~]*2 ~").bank(kit)
$: s("~ [rim ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### AfroCub8
**Source:** drum-patterns

```js
// Title: AfroCub8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.6 0.6 1.0 1.0").bank(bank_hh),
  s("~ ~ [ht ht ht ~] ~").gain("0.6 0.6 1.0").bank(bank_ht),
  s("[mt ~ ~ ~] ~ ~ [mt mt mt ~]").gain("1.0 0.6 0.6 1.0").bank(bank_mt),
  s("[~ ~ sd sd] [~ sd sd ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub8
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.6 0.6 1.0 1.0").bank(kit)
$: s("~ ~ [ht ht ht ~] ~").gain("0.6 0.6 1.0").bank(kit)
$: s("[mt ~ ~ ~] ~ ~ [mt mt mt ~]").gain("1.0 0.6 0.6 1.0").bank(kit)
$: s("[~ ~ sd sd] [~ sd sd ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### AfroCub9
**Source:** drum-patterns

```js
// Title: AfroCub9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ ~ ht] ~ ~").bank(bank_ht),
  s("[~ ~ ~ mt] ~ [~ ~ ~ mt] ~").bank(bank_mt),
  s("[~ sd sd ~] [~ sd sd ~] [~ sd sd ~] [~ sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [~ ~ ~ lt]").bank(bank_lt),
  s("cb*4").bank(bank_cb),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCub9
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ [~ ~ ~ ht] ~ ~").bank(kit)
$: s("[~ ~ ~ mt] ~ [~ ~ ~ mt] ~").bank(kit)
$: s("[~ sd sd ~] [~ sd sd ~] [~ sd sd ~] [~ sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ ~ lt]").bank(kit)
$: s("cb*4").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### AfroCubBreak1
**Source:** drum-patterns

```js
// Title: AfroCubBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [ht ~ ~ ~]").gain("1.1 0.7").bank(bank_ht),
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("[~ ~ ~ sd] [~ ~ sd ~] [sd ~ ~ ~] ~").gain("1.1 0.7").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[cb ~ cb cb] [cb ~]*2 ~ ~").bank(bank_cb),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCubBreak1
const kit = "RolandTR808";

$: s("~ ~ ~ [ht ~ ~ ~]").gain("1.1 0.7").bank(kit)
$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ sd ~] [sd ~ ~ ~] ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[cb ~ cb cb] [cb ~]*2 ~ ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### AfroCubBreak2
**Source:** drum-patterns

```js
// Title: AfroCubBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("[~ ~ ~ mt] ~ [~ ~ ~ mt] ~").bank(bank_mt),
  s("[~ ~ sd ~] [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd]").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("~ [~ ~ lt ~] [lt ~ ~ ~] [~ ~ lt ~]").gain("0.6 1.0 0.6").bank(bank_lt),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCubBreak2
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[~ ~ ~ mt] ~ [~ ~ ~ mt] ~").bank(kit)
$: s("[~ ~ sd ~] [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd]").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [~ ~ lt ~] [lt ~ ~ ~] [~ ~ lt ~]").gain("0.6 1.0 0.6").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### AfroCubBreak3
**Source:** drum-patterns

```js
// Title: AfroCubBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ [~ ht ht ~] ~").gain("0.6 1.0").bank(bank_ht),
  s("~ [~ ~ mt mt] ~ ~").gain("1.0 0.6").bank(bank_mt),
  s("[sd sd ~ sd] [sd ~ ~ ~] ~ ~").gain("1.0 0.6 1.0 1.0").bank(bank_sd),
  s("~ ~ ~ [lt lt ~ lt]").gain("1.0 0.6 0.6").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCubBreak3
const kit = "RolandTR808";

$: s("~ ~ [~ ht ht ~] ~").gain("0.6 1.0").bank(kit)
$: s("~ [~ ~ mt mt] ~ ~").gain("1.0 0.6").bank(kit)
$: s("[sd sd ~ sd] [sd ~ ~ ~] ~ ~").gain("1.0 0.6 1.0 1.0").bank(kit)
$: s("~ ~ ~ [lt lt ~ lt]").gain("1.0 0.6 0.6").bank(kit)
```
</details>

### AfroCubBreak4
**Source:** drum-patterns

```js
// Title: AfroCubBreak4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_cb = bank_default;

stack(
  s("~ ~ ~ [ht ~ ht ht]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [mt mt ~ mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [lt ~ ~ ~] ~").bank(bank_lt),
  s("[cb ~ cb cb] ~ [~ ~ cb cb] ~").bank(bank_cb)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCubBreak4
const kit = "RolandTR808";

$: s("~ ~ ~ [ht ~ ht ht]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [mt mt ~ mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [lt ~ ~ ~] ~").bank(kit)
$: s("[cb ~ cb cb] ~ [~ ~ cb cb] ~").bank(kit)
```
</details>

### AfroCubBreak5
**Source:** drum-patterns

```js
// Title: AfroCubBreak5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_cb = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ [mt ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd ~ sd sd] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ [cb ~]*2 [cb ~]*2").bank(bank_cb)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCubBreak5
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ [mt ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd ~ sd sd] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [cb ~]*2 [cb ~]*2").bank(kit)
```
</details>

### AfroCubBreak6
**Source:** drum-patterns

```js
// Title: AfroCubBreak6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("~ [ht ~]*2 ~ ~").bank(bank_ht),
  s("[mt mt ~ mt] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [sd sd ~ sd] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [lt ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AfroCubBreak6
const kit = "RolandTR808";

$: s("~ [ht ~]*2 ~ ~").bank(kit)
$: s("[mt mt ~ mt] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [sd sd ~ sd] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [lt ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Blues1
**Source:** drum-patterns

```js
// Title: Blues1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] hh*4 ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd]*2 ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues1
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] hh*4 ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd]*2 ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] [bd ~]*2 ~").bank(kit)
```
</details>

### Blues2
**Source:** drum-patterns

```js
// Title: Blues2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*12").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues2
const kit = "RolandTR808";

$: s("hh*12").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Blues3
**Source:** drum-patterns

```js
// Title: Blues3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 hh*4 [hh hh ~ hh] ~").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_hh),
  s("~ ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] [bd ~]*2 ~").gain("0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues3
const kit = "RolandTR808";

$: s("hh*4 hh*4 [hh hh ~ hh] ~").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("~ ~ [~ ~ oh ~] ~").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] [bd ~]*2 ~").gain("0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Blues4
**Source:** drum-patterns

```js
// Title: Blues4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ ~] ~").bank(bank_cr),
  s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh]*2 ~").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues4
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ ~] ~").bank(kit)
$: s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh]*2 ~").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ oh ~] ~").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] [bd ~ bd bd] ~").bank(kit)
```
</details>

### Blues5
**Source:** drum-patterns

```js
// Title: Blues5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").bank(bank_cr),
  s("[~ ~ ~ hh] ~ ~ ~").gain("0.85").bank(bank_hh)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues5
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").bank(kit)
$: s("[~ ~ ~ hh] ~ ~ ~").gain("0.85").bank(kit)
```
</details>

### Blues6
**Source:** drum-patterns

```js
// Title: Blues6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] cr*4 ~").bank(bank_cr),
  s("[~ ~ ~ hh] ~ [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("~ ~ [~ ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blues6
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] cr*4 ~").bank(kit)
$: s("[~ ~ ~ hh] ~ [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("~ ~ [~ ~ bd bd] ~").bank(kit)
```
</details>

### BluesBreak1
**Source:** drum-patterns

```js
// Title: BluesBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ [~ mt ~ ~] ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").gain("1.1 0.7").bank(bank_sd),
  s("~ [~ ~ ~ lt] ~ ~").gain("1.1 0.7").bank(bank_lt),
  s("[bd ~ ~ ~] [bd ~]*2 [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BluesBreak1
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ mt ~ ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").gain("1.1 0.7").bank(kit)
$: s("~ [~ ~ ~ lt] ~ ~").gain("1.1 0.7").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [bd ~ bd bd] ~").bank(kit)
```
</details>

### BluesBreak2
**Source:** drum-patterns

```js
// Title: BluesBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ~ cr] ~").bank(bank_cr),
  s("[hh ~ ~ ~] [~ ~ hh ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[~ sd sd sd] [~ ~ ~ sd] [~ sd ~ ~] ~").gain("0.6 0.6 1.0 0.6 1.1").bank(bank_sd),
  s("[bd ~ ~ ~] [bd bd bd ~] [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BluesBreak2
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ cr] ~").bank(kit)
$: s("[hh ~ ~ ~] [~ ~ hh ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("[~ sd sd sd] [~ ~ ~ sd] [~ sd ~ ~] ~").gain("0.6 0.6 1.0 0.6 1.1").bank(kit)
$: s("[bd ~ ~ ~] [bd bd bd ~] [bd ~ bd bd] ~").bank(kit)
```
</details>

### BluesBreak3
**Source:** drum-patterns

```js
// Title: BluesBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("[~ ~ ~ hh] [~ ~ hh ~] ~ ~").gain("0.85").bank(bank_hh),
  s("[~ sd sd sd] sd*4 [sd sd ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.1").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BluesBreak3
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[~ ~ ~ hh] [~ ~ hh ~] ~ ~").gain("0.85").bank(kit)
$: s("[~ sd sd sd] sd*4 [sd sd ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.1").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd bd] ~").bank(kit)
```
</details>

### Boogie1
**Source:** drum-patterns

```js
// Title: Boogie1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cr*4").bank(bank_cr),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [bd ~ ~ bd] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Boogie1
const kit = "RolandTR808";

$: s("cr*4").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [bd ~ ~ bd] [~ ~ ~ bd]").bank(kit)
```
</details>

### Boogie2
**Source:** drum-patterns

```js
// Title: Boogie2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [cr ~ ~ cr] [cr ~ ~ cr] [cr ~ ~ cr]").bank(bank_cr),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Boogie2
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [cr ~ ~ cr] [cr ~ ~ cr] [cr ~ ~ cr]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Boogie3
**Source:** drum-patterns

```js
// Title: Boogie3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [cr ~ ~ cr] [cr ~ ~ cr] [cr ~ ~ cr]").bank(bank_cr),
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ sd]").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Boogie3
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [cr ~ ~ cr] [cr ~ ~ cr] [cr ~ ~ cr]").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ sd]").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ ~ bd] ~").bank(kit)
```
</details>

### BoogieBreak1
**Source:** drum-patterns

```js
// Title: BoogieBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ ~ cr ~] [~ cr ~ ~] ~").bank(bank_cr),
  s("~ [mt mt ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ sd sd ~] [~ ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ [~ ~ lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BoogieBreak1
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ ~ cr ~] [~ cr ~ ~] ~").bank(kit)
$: s("~ [mt mt ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ sd sd ~] [~ ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### BoogieBreak2
**Source:** drum-patterns

```js
// Title: BoogieBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("[~ ~ ~ mt] [mt mt ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd sd sd ~] [~ ~ sd sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ [~ lt lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BoogieBreak2
const kit = "RolandTR808";

$: s("[~ ~ ~ mt] [mt mt ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd sd ~] [~ ~ sd sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ lt lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### BoogieBreak3
**Source:** drum-patterns

```js
// Title: BoogieBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("[~ ~ ~ mt] ~ [~ mt ~ ~] ~").bank(bank_mt),
  s("[~ sd sd ~] [sd sd ~ sd] [sd ~ sd sd] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[lt ~ ~ ~] [~ ~ lt ~] ~ ~").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BoogieBreak3
const kit = "RolandTR808";

$: s("[~ ~ ~ mt] ~ [~ mt ~ ~] ~").bank(kit)
$: s("[~ sd sd ~] [sd sd ~ sd] [sd ~ sd sd] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[lt ~ ~ ~] [~ ~ lt ~] ~ ~").bank(kit)
```
</details>

### Bossa1
**Source:** drum-patterns

```js
// Title: Bossa1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("cr*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ mt ~] ~ [mt ~ ~ ~] [~ ~ mt ~]").bank(bank_mt),
  s("[rim ~ ~ ~] [~ ~ rim ~] ~ [rim ~ ~ ~]").gain("0.6 0.6 1.0").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa1
const kit = "RolandTR808";

$: s("cr*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ mt ~] ~ [mt ~ ~ ~] [~ ~ mt ~]").bank(kit)
$: s("[rim ~ ~ ~] [~ ~ rim ~] ~ [rim ~ ~ ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa2
**Source:** drum-patterns

```js
// Title: Bossa2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("[~ ~ rim ~] [rim ~ ~ ~] [rim ~]*2 [~ ~ rim ~]").gain("0.6 1.0 0.6 0.6 0.6").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa2
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ rim ~] [rim ~ ~ ~] [rim ~]*2 [~ ~ rim ~]").gain("0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa3
**Source:** drum-patterns

```js
// Title: Bossa3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~]").bank(bank_cr),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[rim ~]*2 [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~]").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa3
const kit = "RolandTR808";

$: s("[~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~]").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[rim ~]*2 [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa4
**Source:** drum-patterns

```js
// Title: Bossa4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~]").bank(bank_cr),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[rim ~]*2 [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~]").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa4
const kit = "RolandTR808";

$: s("[~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~]").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[rim ~]*2 [~ ~ rim ~] [~ ~ rim ~] [~ ~ rim ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa5
**Source:** drum-patterns

```js
// Title: Bossa5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("cr*4").bank(bank_cr),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[rim ~]*2 [~ ~ rim ~] [rim ~ ~ ~] ~").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa5
const kit = "RolandTR808";

$: s("cr*4").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[rim ~]*2 [~ ~ rim ~] [rim ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Bossa6
**Source:** drum-patterns

```js
// Title: Bossa6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_rim = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("cr*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("~ [~ ~ mt ~] ~ ~").bank(bank_mt),
  s("~ [rim ~ ~ ~] [~ ~ rim ~] ~").gain("1.0 0.6").bank(bank_rim),
  s("~ ~ ~ [lt ~ ~ ~]").bank(bank_lt),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Bossa6
const kit = "RolandTR808";

$: s("cr*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [~ ~ mt ~] ~ ~").bank(kit)
$: s("~ [rim ~ ~ ~] [~ ~ rim ~] ~").gain("1.0 0.6").bank(kit)
$: s("~ ~ ~ [lt ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### BossaBreak1
**Source:** drum-patterns

```js
// Title: BossaBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(bank_hh),
  s("[mt ~ ~ ~] ~ ~ ~").bank(bank_mt),
  s("[sd ~]*2 [~ ~ sd ~] [sd ~ ~ sd] ~").gain("0.6 1.0 0.6 0.6 1.0").bank(bank_sd),
  s("[~ ~ lt ~] [~ ~ lt ~] [lt ~ ~ ~] ~").gain("1.0 0.6 0.6").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BossaBreak1
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(kit)
$: s("[mt ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[sd ~]*2 [~ ~ sd ~] [sd ~ ~ sd] ~").gain("0.6 1.0 0.6 0.6 1.0").bank(kit)
$: s("[~ ~ lt ~] [~ ~ lt ~] [lt ~ ~ ~] ~").gain("1.0 0.6 0.6").bank(kit)
```
</details>

### BossaBreak2
**Source:** drum-patterns

```js
// Title: BossaBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ht ~] ~ ~").bank(bank_ht),
  s("[~ ~ mt ~] ~ ~ [~ ~ mt ~]").bank(bank_mt),
  s("[sd ~ ~ ~] [sd ~ ~ ~] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("~ ~ [lt ~ ~ ~] ~").bank(bank_lt),
  s("[bd ~ ~ ~] [~ bd]*2 ~ [~ ~ bd ~]").gain("1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BossaBreak2
const kit = "RolandTR808";

$: s("~ [~ ~ ht ~] ~ ~").bank(kit)
$: s("[~ ~ mt ~] ~ ~ [~ ~ mt ~]").bank(kit)
$: s("[sd ~ ~ ~] [sd ~ ~ ~] ~ [sd ~ ~ ~]").bank(kit)
$: s("~ ~ [lt ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ bd]*2 ~ [~ ~ bd ~]").gain("1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### BossaBreak3
**Source:** drum-patterns

```js
// Title: BossaBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ ht ~] ~ ~ ~").gain("1.1 0.7").bank(bank_ht),
  s("~ ~ [~ ~ mt ~] ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").gain("0.6 1.1").bank(bank_sd),
  s("~ [~ ~ lt ~] ~ ~").gain("1.1 0.7").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BossaBreak3
const kit = "RolandTR808";

$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ ~ ht ~] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ [~ ~ mt ~] ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").gain("0.6 1.1").bank(kit)
$: s("~ [~ ~ lt ~] ~ ~").gain("1.1 0.7").bank(kit)
```
</details>

### ChaCha1
**Source:** drum-patterns

```js
// Title: ChaCha1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [mt ~]*2").bank(bank_mt),
  s("~ [~ ~ sd ~] ~ ~").bank(bank_sd),
  s("[~ ~ rim ~] ~ [~ ~ rim ~] ~").bank(bank_rim),
  s("cb*4").bank(bank_cb),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChaCha1
const kit = "RolandTR808";

$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("~ ~ ~ [mt ~]*2").bank(kit)
$: s("~ [~ ~ sd ~] ~ ~").bank(kit)
$: s("[~ ~ rim ~] ~ [~ ~ rim ~] ~").bank(kit)
$: s("cb*4").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### ChaCha2
**Source:** drum-patterns

```js
// Title: ChaCha2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [hh ~]*2 ~ [hh ~]*2").gain("0.85").bank(bank_hh),
  s("oh ~ oh ~").bank(bank_oh),
  s("~ ~ ~ [mt ~ ~ ~]").bank(bank_mt),
  s("~ [~ ~ sd ~] ~ ~").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("cb*4").bank(bank_cb),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChaCha2
const kit = "RolandTR808";

$: s("~ [hh ~]*2 ~ [hh ~]*2").gain("0.85").bank(kit)
$: s("oh ~ oh ~").bank(kit)
$: s("~ ~ ~ [mt ~ ~ ~]").bank(kit)
$: s("~ [~ ~ sd ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("cb*4").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### ChaCha3
**Source:** drum-patterns

```js
// Title: ChaCha3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [~ ~ sd ~] ~ ~").bank(bank_sd),
  s("~ ~ ~ [lt ~]*2").bank(bank_lt),
  s("cb*4").bank(bank_cb),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChaCha3
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [~ ~ sd ~] ~ ~").bank(kit)
$: s("~ ~ ~ [lt ~]*2").bank(kit)
$: s("cb*4").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(kit)
```
</details>

### ChaChaBreak1
**Source:** drum-patterns

```js
// Title: ChaChaBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt ~] ~ [~ ~ mt ~]").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(bank_sd),
  s("[~ ~ lt ~] ~ [lt ~ ~ ~] ~").gain("1.1 0.7").bank(bank_lt),
  s("~ ~ ~ [~ ~ cb ~]").bank(bank_cb),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChaChaBreak1
const kit = "RolandTR808";

$: s("~ [~ ~ mt ~] ~ [~ ~ mt ~]").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(kit)
$: s("[~ ~ lt ~] ~ [lt ~ ~ ~] ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ ~ [~ ~ cb ~]").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### ChaChaBreak2
**Source:** drum-patterns

```js
// Title: ChaChaBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_cb = bank_default;

stack(
  s("~ [mt mt ~ ~] [~ ~ mt mt] ~").gain("1.0 0.6 1.0 0.6").bank(bank_mt),
  s("~ [~ ~ ~ lt] [lt ~ ~ ~] [~ lt lt ~]").gain("1.0 0.6 1.0 0.6").bank(bank_lt),
  s("[cb ~ ~ ~] ~ ~ ~").bank(bank_cb)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChaChaBreak2
const kit = "RolandTR808";

$: s("~ [mt mt ~ ~] [~ ~ mt mt] ~").gain("1.0 0.6 1.0 0.6").bank(kit)
$: s("~ [~ ~ ~ lt] [lt ~ ~ ~] [~ lt lt ~]").gain("1.0 0.6 1.0 0.6").bank(kit)
$: s("[cb ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### ChaChaBreak3
**Source:** drum-patterns

```js
// Title: ChaChaBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("[~ ~ mt ~] [~ ~ mt mt] ~ ~").gain("0.6 1.0 0.6").bank(bank_mt),
  s("~ [sd ~ ~ ~] ~ ~").gain("1.1 0.7").bank(bank_sd),
  s("~ ~ [~ ~ lt ~] [lt lt ~ lt]").gain("0.6 1.0 0.6 0.6").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChaChaBreak3
const kit = "RolandTR808";

$: s("[~ ~ mt ~] [~ ~ mt mt] ~ ~").gain("0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~ ~ ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ [~ ~ lt ~] [lt lt ~ lt]").gain("0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### Charleston1
**Source:** drum-patterns

```js
// Title: Charleston1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] [cr ~ ~ cr] [cr ~ ~ ~] [cr ~ ~ cr]").bank(bank_cr),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Charleston1
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] [cr ~ ~ cr] [cr ~ ~ ~] [cr ~ ~ cr]").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### CharlestonBreak1
**Source:** drum-patterns

```js
// Title: CharlestonBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - CharlestonBreak1
const kit = "RolandTR808";

$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Disco1
**Source:** drum-patterns

```js
// Title: Disco1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ ~ hh hh] hh*4 [~ ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ oh ~ oh").bank(bank_oh),
  s("[~ ~ cp ~] [~ ~ cp ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(bank_cp),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco1
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ ~ hh hh] hh*4 [~ ~ hh hh]").gain("0.85").bank(kit)
$: s("~ oh ~ oh").bank(kit)
$: s("[~ ~ cp ~] [~ ~ cp ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco10
**Source:** drum-patterns

```js
// Title: Disco10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 [~ hh hh ~] [hh ~]*2 ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [oh ~ ~ ~]").bank(bank_oh),
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("[~ ~ cp ~] [cp ~ ~ ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(bank_cp),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco10
const kit = "RolandTR808";

$: s("hh*4 [~ hh hh ~] [hh ~]*2 ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [oh ~ ~ ~]").bank(kit)
$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("[~ ~ cp ~] [cp ~ ~ ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco11
**Source:** drum-patterns

```js
// Title: Disco11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 ~ [hh ~]*2 ~").gain("0.85").bank(bank_hh),
  s("[~ oh ~ ~] ~ [~ oh ~ ~] ~").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ cp ~ ~] [cp ~ ~ ~] ~ [cp ~ ~ ~]").bank(bank_cp),
  s("[bd ~ ~ ~] [bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco11
const kit = "RolandTR808";

$: s("[hh ~]*2 ~ [hh ~]*2 ~").gain("0.85").bank(kit)
$: s("[~ oh ~ ~] ~ [~ oh ~ ~] ~").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[~ cp ~ ~] [cp ~ ~ ~] ~ [cp ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ bd]").bank(kit)
```
</details>

### Disco12
**Source:** drum-patterns

```js
// Title: Disco12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_tamb = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd]").bank(bank_sd),
  s("[tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb]").bank(bank_tamb),
  s("[bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~] [bd bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco12
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd]").bank(kit)
$: s("[tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb]").bank(kit)
$: s("[bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~] [bd bd ~ ~]").bank(kit)
```
</details>

### Disco2
**Source:** drum-patterns

```js
// Title: Disco2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ ~ hh hh] hh*4 [~ ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ oh ~ oh").bank(bank_oh),
  s("[~ ~ cp ~] [~ ~ cp ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(bank_cp),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco2
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ ~ hh hh] hh*4 [~ ~ hh hh]").gain("0.85").bank(kit)
$: s("~ oh ~ oh").bank(kit)
$: s("[~ ~ cp ~] [~ ~ cp ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco3
**Source:** drum-patterns

```js
// Title: Disco3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh ~ ~] hh*4 [hh hh ~ ~] hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[~ ~ cp ~] [cp ~ ~ ~] ~ [cp ~]*2").bank(bank_cp),
  s("[bd ~ ~ ~] [bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco3
const kit = "RolandTR808";

$: s("[hh hh ~ ~] hh*4 [hh hh ~ ~] hh*4").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(kit)
$: s("[~ ~ cp ~] [cp ~ ~ ~] ~ [cp ~]*2").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### Disco4
**Source:** drum-patterns

```js
// Title: Disco4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_tamb = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ hh hh hh] [~ hh hh hh] [~ hh]*2 [~ hh hh hh]").gain("0.85").bank(bank_hh),
  s("[sd ~ ~ ~] [sd ~ ~ ~] [sd ~]*2 [sd ~ ~ ~]").bank(bank_sd),
  s("~ cp ~ cp").bank(bank_cp),
  s("[tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb]").bank(bank_tamb),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco4
const kit = "RolandTR808";

$: s("[~ hh hh hh] [~ hh hh hh] [~ hh]*2 [~ hh hh hh]").gain("0.85").bank(kit)
$: s("[sd ~ ~ ~] [sd ~ ~ ~] [sd ~]*2 [sd ~ ~ ~]").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("[tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco5
**Source:** drum-patterns

```js
// Title: Disco5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 [~ hh hh hh] [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("~ [cp ~ ~ ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(bank_cp),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco5
const kit = "RolandTR808";

$: s("hh*4 [~ hh hh hh] [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("~ [cp ~ ~ ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco6
**Source:** drum-patterns

```js
// Title: Disco6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_tamb = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [hh ~ ~ ~] [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[sd sd sd ~] [sd ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("tamb*8").bank(bank_tamb),
  s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco6
const kit = "RolandTR808";

$: s("~ [hh ~ ~ ~] [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[sd sd sd ~] [sd ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("tamb*8").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### Disco7
**Source:** drum-patterns

```js
// Title: Disco7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ hh hh hh] [~ hh hh hh] [~ ~ ~ hh] [~ hh hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("~ [cp ~ ~ ~] [cp ~ ~ ~] [cp cp ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[cb ~ ~ ~] [cb ~ ~ ~] [cb cb cb ~] [cb ~ ~ ~]").bank(bank_cb),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco7
const kit = "RolandTR808";

$: s("[~ hh hh hh] [~ hh hh hh] [~ ~ ~ hh] [~ hh hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("~ [cp ~ ~ ~] [cp ~ ~ ~] [cp cp ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[cb ~ ~ ~] [cb ~ ~ ~] [cb cb cb ~] [cb ~ ~ ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco8
**Source:** drum-patterns

```js
// Title: Disco8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ oh] [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(bank_oh),
  s("~ [sd ~ ~ ~] [~ ~ ~ sd] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[cp ~]*2 [cp ~ ~ ~] ~ [cp ~ ~ ~]").bank(bank_cp),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco8
const kit = "RolandTR808";

$: s("[hh hh hh ~] [~ hh hh ~] [hh hh hh ~] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ ~ oh] [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(kit)
$: s("~ [sd ~ ~ ~] [~ ~ ~ sd] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[cp ~]*2 [cp ~ ~ ~] ~ [cp ~ ~ ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco9
**Source:** drum-patterns

```js
// Title: Disco9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_cb = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh hh] [~ ~ hh ~] [~ ~ hh hh] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ ~ cp ~] [cp ~ ~ ~] [cp ~]*2 [cp ~]*2").bank(bank_cp),
  s("cb*4").bank(bank_cb),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco9
const kit = "RolandTR808";

$: s("[~ ~ hh hh] [~ ~ hh ~] [~ ~ hh hh] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[~ ~ cp ~] [cp ~ ~ ~] [cp ~]*2 [cp ~]*2").bank(kit)
$: s("cb*4").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### DiscoBreak1
**Source:** drum-patterns

```js
// Title: DiscoBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ oh ~] [~ ~ oh ~] ~").bank(bank_oh),
  s("~ [~ ~ sd ~] ~ ~").bank(bank_sd),
  s("[~ ~ cp ~] [cp ~ ~ ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(bank_cp),
  s("[bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ bd] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak1
const kit = "RolandTR808";

$: s("~ ~ [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ [~ ~ oh ~] [~ ~ oh ~] ~").bank(kit)
$: s("~ [~ ~ sd ~] ~ ~").bank(kit)
$: s("[~ ~ cp ~] [cp ~ ~ ~] [~ ~ cp ~] [cp ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ bd] [bd ~ ~ ~]").bank(kit)
```
</details>

### DiscoBreak2
**Source:** drum-patterns

```js
// Title: DiscoBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [hh ~ ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("~ [~ ~ oh ~] ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [~ sd]*2 ~").bank(bank_sd),
  s("~ ~ ~ [lt lt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak2
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [hh ~ ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("~ [~ ~ oh ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ sd]*2 ~").bank(kit)
$: s("~ ~ ~ [lt lt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [bd ~]*2 ~").bank(kit)
```
</details>

### DiscoBreak3
**Source:** drum-patterns

```js
// Title: DiscoBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_tamb = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("[~ ~ mt ~] ~ ~ ~").bank(bank_mt),
  s("[sd sd ~ ~] ~ [sd sd ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ tamb ~] [tamb ~ ~ ~] ~ ~").bank(bank_tamb),
  s("~ bd ~ bd").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak3
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ht ~] ~").bank(kit)
$: s("[~ ~ mt ~] ~ ~ ~").bank(kit)
$: s("[sd sd ~ ~] ~ [sd sd ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ tamb ~] [tamb ~ ~ ~] ~ ~").bank(kit)
$: s("~ bd ~ bd").bank(kit)
```
</details>

### DiscoBreak4
**Source:** drum-patterns

```js
// Title: DiscoBreak4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;

stack(
  s("~ [ht ~]*2 ~ ~").bank(bank_ht),
  s("~ ~ ~ mt*4").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ sd ~] ~ sd*4 ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak4
const kit = "RolandTR808";

$: s("~ [ht ~]*2 ~ ~").bank(kit)
$: s("~ ~ ~ mt*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ sd ~] ~ sd*4 ~").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### DiscoBreak5
**Source:** drum-patterns

```js
// Title: DiscoBreak5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ [~ ~ ~ mt] [mt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [sd sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [~ lt lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [bd ~ ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak5
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ ~ mt] [mt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [sd sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ lt lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [bd ~ ~ ~] ~ ~").bank(kit)
```
</details>

### DiscoBreak6
**Source:** drum-patterns

```js
// Title: DiscoBreak6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2").gain("0.85").bank(bank_hh),
  s("sd*8").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak6
const kit = "RolandTR808";

$: s("[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2").gain("0.85").bank(kit)
$: s("sd*8").bank(kit)
```
</details>

### DiscoBreak7
**Source:** drum-patterns

```js
// Title: DiscoBreak7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_tamb = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [ht ~ ~ ~] ~").bank(bank_ht),
  s("[~ ~ mt ~] ~ ~ [~ ~ mt ~]").bank(bank_mt),
  s("[sd ~ ~ ~] [~ ~ sd ~] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb]").bank(bank_tamb),
  s("~ [bd ~ ~ ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak7
const kit = "RolandTR808";

$: s("~ ~ [ht ~ ~ ~] ~").bank(kit)
$: s("[~ ~ mt ~] ~ ~ [~ ~ mt ~]").bank(kit)
$: s("[sd ~ ~ ~] [~ ~ sd ~] ~ [sd ~ ~ ~]").bank(kit)
$: s("[tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb] [tamb ~ tamb tamb]").bank(kit)
$: s("~ [bd ~ ~ ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### DiscoBreak8
**Source:** drum-patterns

```js
// Title: DiscoBreak8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[sd sd ~ sd] [sd sd ~ sd] [sd sd ~ sd] [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak8
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[sd sd ~ sd] [sd sd ~ sd] [sd sd ~ sd] [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### DiscoBreak9
**Source:** drum-patterns

```js
// Title: DiscoBreak9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [hh ~ ~ ~] ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ sd ~] ~ [~ ~ sd sd] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ ~ bd ~] [bd ~ ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DiscoBreak9
const kit = "RolandTR808";

$: s("~ [hh ~ ~ ~] ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ sd ~] ~ [~ ~ sd sd] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] ~ ~").bank(kit)
```
</details>

### Ending1
**Source:** drum-patterns

```js
// Title: Ending1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ending1
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Ending2
**Source:** drum-patterns

```js
// Title: Ending2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [cr ~ ~ ~] ~").bank(bank_cr),
  s("~ [mt ~ ~ ~] ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ ~").gain("1.1 0.7").bank(bank_sd),
  s("~ ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ending2
const kit = "RolandTR808";

$: s("~ ~ [cr ~ ~ ~] ~").bank(kit)
$: s("~ [mt ~ ~ ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Ending3
**Source:** drum-patterns

```js
// Title: Ending3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [cr ~ ~ ~] ~").bank(bank_cr),
  s("[~ ~ ~ mt] [mt ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd sd ~ ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ [~ ~ lt ~] ~ ~").bank(bank_lt),
  s("~ ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ending3
const kit = "RolandTR808";

$: s("~ ~ [cr ~ ~ ~] ~").bank(kit)
$: s("[~ ~ ~ mt] [mt ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd ~ ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ lt ~] ~ ~").bank(kit)
$: s("~ ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Funk1
**Source:** drum-patterns

```js
// Title: Funk1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.6 0.6 0.6 1.0").bank(bank_hh),
  s("~ ~ ~ [~ ~ ~ oh]").bank(bank_oh),
  s("[~ ~ sd ~] ~ ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ bd ~ ~] ~").gain("0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk1
const kit = "RolandTR808";

$: s("hh*4").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ ~ oh]").bank(kit)
$: s("[~ ~ sd ~] ~ ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ bd ~ ~] ~").gain("0.6 0.6 1.0").bank(kit)
```
</details>

### Funk10
**Source:** drum-patterns

```js
// Title: Funk10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ hh ~] [~ ~ ~ hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[oh ~ ~ oh] [~ ~ ~ oh] [~ oh ~ ~] ~").bank(bank_oh),
  s("[~ sd sd ~] [sd ~ ~ ~] [sd ~]*2 [~ sd ~ ~]").gain("0.6 0.6 1.0 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd]*2 [bd ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk10
const kit = "RolandTR808";

$: s("~ [~ ~ hh ~] [~ ~ ~ hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[oh ~ ~ oh] [~ ~ ~ oh] [~ oh ~ ~] ~").bank(kit)
$: s("[~ sd sd ~] [sd ~ ~ ~] [sd ~]*2 [~ sd ~ ~]").gain("0.6 0.6 1.0 0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd]*2 [bd ~ ~ bd]").bank(kit)
```
</details>

### Funk11
**Source:** drum-patterns

```js
// Title: Funk11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] [hh ~ ~ ~] [~ hh hh ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [~ oh]*2 ~ ~").bank(bank_oh),
  s("[~ ~ sd ~] [~ ~ sd ~] [sd ~ ~ sd] [~ sd ~ ~]").gain("1.0 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd]*2 [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk11
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] [hh ~ ~ ~] [~ hh hh ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ [~ oh]*2 ~ ~").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [sd ~ ~ sd] [~ sd ~ ~]").gain("1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[bd ~ ~ ~] [~ bd]*2 [~ bd ~ ~] ~").bank(kit)
```
</details>

### Funk12
**Source:** drum-patterns

```js
// Title: Funk12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ hh hh ~] [~ hh]*2 [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ [sd ~ ~ sd] [sd ~]*2 [~ sd ~ ~]").gain("1.0 0.6 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ bd]*2 [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk12
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ hh hh ~] [~ hh]*2 [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ [sd ~ ~ sd] [sd ~]*2 [~ sd ~ ~]").gain("1.0 0.6 0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ bd]*2 [bd ~ ~ ~]").bank(kit)
```
</details>

### Funk13
**Source:** drum-patterns

```js
// Title: Funk13
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [~ hh hh ~] [hh ~]*2 ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ oh] ~ ~ [oh ~ ~ ~]").bank(bank_oh),
  s("~ [~ ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]").bank(bank_sd),
  s("~ [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk13
const kit = "RolandTR808";

$: s("[hh ~]*2 [~ hh hh ~] [hh ~]*2 ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ oh] ~ ~ [oh ~ ~ ~]").bank(kit)
$: s("~ [~ ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]").bank(kit)
$: s("~ [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~]").bank(kit)
```
</details>

### Funk14
**Source:** drum-patterns

```js
// Title: Funk14
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [~ hh hh ~] [hh ~]*2 ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ oh] ~ ~ [oh ~ ~ ~]").bank(bank_oh),
  s("~ [~ ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]").bank(bank_sd),
  s("~ [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk14
const kit = "RolandTR808";

$: s("[hh ~]*2 [~ hh hh ~] [hh ~]*2 ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ oh] ~ ~ [oh ~ ~ ~]").bank(kit)
$: s("~ [~ ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]").bank(kit)
$: s("~ [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~]").bank(kit)
```
</details>

### Funk15
**Source:** drum-patterns

```js
// Title: Funk15
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ ~ ~] [hh ~ hh hh] [hh ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_hh),
  s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ ~ sd] [~ sd]*2 [~ sd ~ ~] [~ sd ~ ~]").gain("1.0 0.6 0.6 0.6 1.0").bank(bank_sd),
  s("[bd bd ~ ~] ~ [bd ~]*2 [bd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk15
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ ~ ~] [hh ~ hh hh] [hh ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(kit)
$: s("[~ ~ ~ sd] [~ sd]*2 [~ sd ~ ~] [~ sd ~ ~]").gain("1.0 0.6 0.6 0.6 1.0").bank(kit)
$: s("[bd bd ~ ~] ~ [bd ~]*2 [bd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Funk2
**Source:** drum-patterns

```js
// Title: Funk2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("~ [~ sd ~ ~] ~ ~").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[bd ~]*2 [~ ~ bd bd] ~ [~ bd ~ ~]").gain("0.6 0.6 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk2
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ ht ~] ~").bank(kit)
$: s("~ [~ sd ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[bd ~]*2 [~ ~ bd bd] ~ [~ bd ~ ~]").gain("0.6 0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### Funk3
**Source:** drum-patterns

```js
// Title: Funk3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.6 0.6 0.6 1.0").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ [~ ~ ht ~] ~ ~").bank(bank_ht),
  s("[~ sd ~ ~] ~ [~ ~ sd ~] ~").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk3
const kit = "RolandTR808";

$: s("hh*4").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ [~ ~ ht ~] ~ ~").bank(kit)
$: s("[~ sd ~ ~] ~ [~ ~ sd ~] ~").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Funk4
**Source:** drum-patterns

```js
// Title: Funk4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [~ mt mt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ ~ sd] ~ ~ [~ sd ~ ~]").gain("0.6 1.0").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ ~ bd] ~").gain("0.6 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk4
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ ~ [~ mt mt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ sd] ~ ~ [~ sd ~ ~]").gain("0.6 1.0").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ ~ bd] ~").gain("0.6 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### Funk5
**Source:** drum-patterns

```js
// Title: Funk5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.6 0.6 0.6 1.0").bank(bank_hh),
  s("[~ oh ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ ~ ~ mt]").bank(bank_mt),
  s("[~ ~ ~ sd] ~ ~ [sd sd ~ ~]").gain("0.6 1.0 0.6").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ bd bd] [~ bd bd ~] [~ ~ bd ~]").gain("0.6 1.0 1.0 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk5
const kit = "RolandTR808";

$: s("hh*4").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("[~ oh ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ mt]").bank(kit)
$: s("[~ ~ ~ sd] ~ ~ [sd sd ~ ~]").gain("0.6 1.0 0.6").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd bd] [~ bd bd ~] [~ ~ bd ~]").gain("0.6 1.0 1.0 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Funk6
**Source:** drum-patterns

```js
// Title: Funk6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("1.0 1.0 0.6 0.6").bank(bank_hh),
  s("~ [~ oh ~ ~] [~ ~ oh ~] ~").bank(bank_oh),
  s("~ [~ ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd bd]").gain("0.6 0.6 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk6
const kit = "RolandTR808";

$: s("hh*4").gain("1.0 1.0 0.6 0.6").bank(kit)
$: s("~ [~ oh ~ ~] [~ ~ oh ~] ~").bank(kit)
$: s("~ [~ ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd bd]").gain("0.6 0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### Funk7
**Source:** drum-patterns

```js
// Title: Funk7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh ~ hh] [hh ~ ~ hh] [hh ~ hh hh] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [~ sd sd ~] [~ sd ~ ~] [sd ~ ~ sd]").gain("0.6 0.6 0.6 1.0 1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk7
const kit = "RolandTR808";

$: s("[hh hh ~ hh] [hh ~ ~ hh] [hh ~ hh hh] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [~ sd sd ~] [~ sd ~ ~] [sd ~ ~ sd]").gain("0.6 0.6 0.6 1.0 1.0 0.6").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Funk8
**Source:** drum-patterns

```js
// Title: Funk8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh hh ~] [hh ~ hh hh] [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_hh),
  s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ [~ sd ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk8
const kit = "RolandTR808";

$: s("[hh hh hh ~] [hh ~ hh hh] [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ [~ sd ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(kit)
$: s("[bd ~ ~ bd] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Funk9
**Source:** drum-patterns

```js
// Title: Funk9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh hh ~ ~] [hh ~ ~ hh] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ ht ~]").bank(bank_ht),
  s("[~ ~ ~ sd] [~ ~ sd sd] [~ sd sd ~] [~ sd]*2").gain("1.0 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Funk9
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh hh ~ ~] [hh ~ ~ hh] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ ht ~]").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ sd sd] [~ sd sd ~] [~ sd]*2").gain("1.0 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### FunkBreak1
**Source:** drum-patterns

```js
// Title: FunkBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ ht] ~").bank(bank_ht),
  s("~ ~ [mt ~ ~ ~] ~").bank(bank_mt),
  s("[~ sd sd ~] sd*4 [~ sd sd ~] [~ sd sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [lt ~ ~ ~]").bank(bank_lt),
  s("[bd ~ ~ bd] ~ [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak1
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ ht] ~").bank(kit)
$: s("~ ~ [mt ~ ~ ~] ~").bank(kit)
$: s("[~ sd sd ~] sd*4 [~ sd sd ~] [~ sd sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [lt ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ ~ bd] ~").bank(kit)
```
</details>

### FunkBreak10
**Source:** drum-patterns

```js
// Title: FunkBreak10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cr ~ ~ ~]").bank(bank_cr),
  s("[~ ~ ~ mt] ~ ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ [~ ~ sd sd] ~").gain("0.6 0.6 1.0").bank(bank_sd),
  s("~ [~ ~ lt ~] ~ ~").gain("1.1 0.7").bank(bank_lt),
  s("~ ~ ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak10
const kit = "RolandTR808";

$: s("~ ~ ~ [cr ~ ~ ~]").bank(kit)
$: s("[~ ~ ~ mt] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ [~ ~ sd sd] ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ [~ ~ lt ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### FunkBreak11
**Source:** drum-patterns

```js
// Title: FunkBreak11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [ht ht ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ ~ [~ mt ~ ~]").bank(bank_mt),
  s("~ [~ ~ sd ~] ~ ~").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[bd ~ ~ ~] [bd ~ ~ bd] [bd ~]*2 [bd ~ ~ ~]").gain("0.6 0.6 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak11
const kit = "RolandTR808";

$: s("~ ~ [ht ht ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ mt ~ ~]").bank(kit)
$: s("~ [~ ~ sd ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ bd] [bd ~]*2 [bd ~ ~ ~]").gain("0.6 0.6 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### FunkBreak12
**Source:** drum-patterns

```js
// Title: FunkBreak12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] ~ [hh ~ ~ hh] ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ sd sd ~] sd*4 [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~ ~ bd] ~ [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak12
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] ~ [hh ~ ~ hh] ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ sd sd ~] sd*4 [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ ~ bd] ~").bank(kit)
```
</details>

### FunkBreak13
**Source:** drum-patterns

```js
// Title: FunkBreak13
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [mt mt mt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ sd*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~ ~ bd] ~ [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak13
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [mt mt mt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ sd*4 ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ ~ bd] ~").bank(kit)
```
</details>

### FunkBreak14
**Source:** drum-patterns

```js
// Title: FunkBreak14
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~]*2").gain("1.1 0.7").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ ~ ~ bd] [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak14
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 ~").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~]*2").gain("1.1 0.7").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ ~ bd] [~ bd]*2").bank(kit)
```
</details>

### FunkBreak15
**Source:** drum-patterns

```js
// Title: FunkBreak15
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").gain("1.1 0.7").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak15
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 ~").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").gain("1.1 0.7").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ ~ bd] ~").bank(kit)
```
</details>

### FunkBreak2
**Source:** drum-patterns

```js
// Title: FunkBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ ~ [ht ht ~ ht]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [mt ~ ~ ~] ~").bank(bank_mt),
  s("~ [sd ~ sd sd] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak2
const kit = "RolandTR808";

$: s("[hh ~]*2 ~ ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ ~ ~ [ht ht ~ ht]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [mt ~ ~ ~] ~").bank(kit)
$: s("~ [sd ~ sd sd] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ ~ bd] ~").bank(kit)
```
</details>

### FunkBreak3
**Source:** drum-patterns

```js
// Title: FunkBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ oh]*2 ~ ~ ~").bank(bank_oh),
  s("~ ~ [~ ~ ~ ht] ~").bank(bank_ht),
  s("~ ~ [mt mt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ [sd ~]*2 ~ ~").bank(bank_sd),
  s("~ ~ ~ [~ lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd bd ~ bd] ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak3
const kit = "RolandTR808";

$: s("[hh ~]*2 ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ oh]*2 ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ ~ ht] ~").bank(kit)
$: s("~ ~ [mt mt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~]*2 ~ ~").bank(kit)
$: s("~ ~ ~ [~ lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ bd] ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### FunkBreak4
**Source:** drum-patterns

```js
// Title: FunkBreak4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ sd sd ~] [sd ~ ~ ~]").gain("1.1 0.6 0.6 1.1").bank(bank_sd),
  s("[bd ~]*2 [~ bd]*2 [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak4
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ sd sd ~] [sd ~ ~ ~]").gain("1.1 0.6 0.6 1.1").bank(kit)
$: s("[bd ~]*2 [~ bd]*2 [~ ~ ~ bd] ~").bank(kit)
```
</details>

### FunkBreak5
**Source:** drum-patterns

```js
// Title: FunkBreak5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("~ [~ ~ ht ht] ~ ~").gain("0.6 1.0").bank(bank_ht),
  s("[~ ~ ~ mt] [mt ~ ~ ~] ~ ~").gain("0.6 1.0").bank(bank_mt),
  s("[sd sd ~ ~] ~ ~ [sd ~ sd sd]").gain("0.6 1.0 0.6 1.0 1.0").bank(bank_sd),
  s("~ ~ [~ lt lt ~] ~").gain("0.6 1.0").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak5
const kit = "RolandTR808";

$: s("~ [~ ~ ht ht] ~ ~").gain("0.6 1.0").bank(kit)
$: s("[~ ~ ~ mt] [mt ~ ~ ~] ~ ~").gain("0.6 1.0").bank(kit)
$: s("[sd sd ~ ~] ~ ~ [sd ~ sd sd]").gain("0.6 1.0 0.6 1.0 1.0").bank(kit)
$: s("~ ~ [~ lt lt ~] ~").gain("0.6 1.0").bank(kit)
```
</details>

### FunkBreak6
**Source:** drum-patterns

```js
// Title: FunkBreak6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd sd ~ sd] [~ ~ sd ~] [~ ~ sd sd]").gain("0.6 1.0 1.0 1.1 1.0 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ bd ~ ~] ~").gain("1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak6
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [sd sd ~ sd] [~ ~ sd ~] [~ ~ sd sd]").gain("0.6 1.0 1.0 1.1 1.0 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ bd ~ ~] ~").gain("1.0 0.6").bank(kit)
```
</details>

### FunkBreak7
**Source:** drum-patterns

```js
// Title: FunkBreak7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ht ht ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[~ sd sd sd] [sd ~ sd sd] [sd ~ sd ~] ~").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.1").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd ~ ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak7
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ht ht ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ sd sd sd] [sd ~ sd sd] [sd ~ sd ~] ~").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.1").bank(kit)
$: s("[bd ~ ~ ~] [~ bd ~ ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### FunkBreak8
**Source:** drum-patterns

```js
// Title: FunkBreak8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ht ~ ~] ~").bank(bank_ht),
  s("[sd ~ ~ sd] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~]").gain("0.6 1.0 1.0 0.6 1.1").bank(bank_sd),
  s("~ ~ [~ ~ lt ~] ~").bank(bank_lt),
  s("~ [~ bd ~ ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak8
const kit = "RolandTR808";

$: s("~ ~ [~ ht ~ ~] ~").bank(kit)
$: s("[sd ~ ~ sd] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~]").gain("0.6 1.0 1.0 0.6 1.1").bank(kit)
$: s("~ ~ [~ ~ lt ~] ~").bank(kit)
$: s("~ [~ bd ~ ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### FunkBreak9
**Source:** drum-patterns

```js
// Title: FunkBreak9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ [ht ht ~ ~] ~").gain("0.6 1.0").bank(bank_ht),
  s("~ [~ ~ mt mt] ~ ~").gain("0.6 1.0").bank(bank_mt),
  s("sd*4 ~ ~ ~").gain("0.6 0.6 0.6 1.0").bank(bank_sd),
  s("~ ~ ~ [lt lt ~ ~]").gain("0.6 1.0").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkBreak9
const kit = "RolandTR808";

$: s("~ ~ [ht ht ~ ~] ~").gain("0.6 1.0").bank(kit)
$: s("~ [~ ~ mt mt] ~ ~").gain("0.6 1.0").bank(kit)
$: s("sd*4 ~ ~ ~").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [lt lt ~ ~]").gain("0.6 1.0").bank(kit)
```
</details>

### Jazz1
**Source:** drum-patterns

```js
// Title: Jazz1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jazz1
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ bd ~ ~] ~ ~").bank(kit)
```
</details>

### Jazz2
**Source:** drum-patterns

```js
// Title: Jazz2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ sd ~] ~ [~ sd]*2 ~").gain("0.6 1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jazz2
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ sd ~] ~ [~ sd]*2 ~").gain("0.6 1.0 0.6").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Jazz3
**Source:** drum-patterns

```js
// Title: Jazz3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_sd),
  s("~ [~ ~ bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jazz3
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
$: s("~ [~ ~ bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Jazz4
**Source:** drum-patterns

```js
// Title: Jazz4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ sd ~] ~ [sd ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jazz4
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ sd ~] ~ [sd ~ ~ sd] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ bd ~ ~] ~ ~").bank(kit)
```
</details>

### Jazz5
**Source:** drum-patterns

```js
// Title: Jazz5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jazz5
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Jazz6
**Source:** drum-patterns

```js
// Title: Jazz6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("~ [~ sd ~ ~] [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jazz6
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [~ sd ~ ~] [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~]*2 ~ ~ ~").bank(kit)
```
</details>

### JazzBreak1
**Source:** drum-patterns

```js
// Title: JazzBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr ~ ~] ~ ~").gain("0.6 0.6 1.0 0.6").bank(bank_cr),
  s("~ ~ [~ mt mt mt] ~").gain("1.0 0.6 0.6").bank(bank_mt),
  s("[~ ~ ~ sd] [~ ~ sd sd] [sd ~ ~ ~] ~").gain("1.0 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - JazzBreak1
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr ~ ~] ~ ~").gain("0.6 0.6 1.0 0.6").bank(kit)
$: s("~ ~ [~ mt mt mt] ~").gain("1.0 0.6 0.6").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ sd sd] [sd ~ ~ ~] ~").gain("1.0 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] [~ bd ~ ~] ~ ~").bank(kit)
```
</details>

### JazzBreak2
**Source:** drum-patterns

```js
// Title: JazzBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ ~ mt*4 ~").gain("0.6 1.0 0.6 0.6").bank(bank_mt),
  s("[~ ~ sd sd] [sd sd sd ~] ~ ~").gain("0.6 1.0 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - JazzBreak2
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ mt*4 ~").gain("0.6 1.0 0.6 0.6").bank(kit)
$: s("[~ ~ sd sd] [sd sd sd ~] ~ ~").gain("0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### JazzBreak3
**Source:** drum-patterns

```js
// Title: JazzBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] ~ ~").gain("0.6 0.6 1.0 0.6 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] ~ sd*4 ~").gain("1.0 0.6 1.0 0.6 0.6").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - JazzBreak3
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] ~ ~").gain("0.6 0.6 1.0 0.6 0.6").bank(kit)
$: s("[~ ~ ~ sd] ~ sd*4 ~").gain("1.0 0.6 1.0 0.6 0.6").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] ~ ~").bank(kit)
```
</details>

### March1
**Source:** drum-patterns

```js
// Title: March1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[sd ~]*2 [sd sd ~ sd] [sd ~]*2 sd*4").gain("1.0 0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - March1
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[sd ~]*2 [sd sd ~ sd] [sd ~]*2 sd*4").gain("1.0 0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### March2
**Source:** drum-patterns

```js
// Title: March2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[sd ~ sd sd] [sd ~ sd sd] [sd ~ sd sd] sd*4").gain("1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - March2
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[sd ~ sd sd] [sd ~ sd sd] [sd ~ sd sd] sd*4").gain("1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### MarchBreak1
**Source:** drum-patterns

```js
// Title: MarchBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ cr ~] [~ ~ cr ~]").bank(bank_cr),
  s("~ ~ [ht ~ ~ ~] ~").gain("1.1 0.7").bank(bank_ht),
  s("~ [mt ~ ~ ~] ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ ~").gain("1.1 0.7").bank(bank_sd),
  s("~ ~ ~ [lt ~ ~ ~]").gain("1.1 0.7").bank(bank_lt),
  s("[~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MarchBreak1
const kit = "RolandTR808";

$: s("~ ~ [~ ~ cr ~] [~ ~ cr ~]").bank(kit)
$: s("~ ~ [ht ~ ~ ~] ~").gain("1.1 0.7").bank(kit)
$: s("~ [mt ~ ~ ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ ~ [lt ~ ~ ~]").gain("1.1 0.7").bank(kit)
$: s("[~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### MarchBreak2
**Source:** drum-patterns

```js
// Title: MarchBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] ~").gain("0.6 1.0 0.6").bank(bank_hh),
  s("[sd ~ sd sd] [~ ~ sd ~] sd*4 [~ ~ sd ~]").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MarchBreak2
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] ~").gain("0.6 1.0 0.6").bank(kit)
$: s("[sd ~ sd sd] [~ ~ sd ~] sd*4 [~ ~ sd ~]").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Paso1
**Source:** drum-patterns

```js
// Title: Paso1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~]*2 [cr ~]*2 [cr ~ cr cr] [cr ~]*2").bank(bank_cr),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd sd] [~ ~ sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Paso1
const kit = "RolandTR808";

$: s("[cr ~]*2 [cr ~]*2 [cr ~ cr cr] [cr ~]*2").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd sd] [~ ~ sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Paso2
**Source:** drum-patterns

```js
// Title: Paso2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cr*8").bank(bank_cr),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [sd ~]*2 [sd ~]*2").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Paso2
const kit = "RolandTR808";

$: s("cr*8").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [sd ~]*2 [sd ~]*2").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### PasoBreak1
**Source:** drum-patterns

```js
// Title: PasoBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd sd ~ sd] [~ sd sd ~] [sd sd ~ sd] [sd ~]*2").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PasoBreak1
const kit = "RolandTR808";

$: s("[sd sd ~ sd] [~ sd sd ~] [sd sd ~ sd] [sd ~]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### PasoBreak2
**Source:** drum-patterns

```js
// Title: PasoBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ [~ mt mt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ sd]*2 ~ ~ [sd ~ sd ~]").gain("1.1 0.7").bank(bank_sd),
  s("~ ~ [~ lt]*2 ~").bank(bank_lt),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PasoBreak2
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ [~ mt mt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ sd]*2 ~ ~ [sd ~ sd ~]").gain("1.1 0.7").bank(kit)
$: s("~ ~ [~ lt]*2 ~").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Pop1
**Source:** drum-patterns

```js
// Title: Pop1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ bd] [~ bd]*2 [bd bd ~ bd] [~ bd]*2").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop1
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ bd] [~ bd]*2 [bd bd ~ bd] [~ bd]*2").gain("1.0 0.8").bank(kit)
```
</details>

### Pop10
**Source:** drum-patterns

```js
// Title: Pop10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 hh*4 hh*4 ~").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(bank_hh),
  s("~ ~ ~ [~ oh]*2").bank(bank_oh),
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").gain("1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~]*2 ~ [bd bd ~ bd] [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop10
const kit = "RolandTR808";

$: s("hh*4 hh*4 hh*4 ~").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(kit)
$: s("~ ~ ~ [~ oh]*2").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").gain("1.0 0.6 1.0").bank(kit)
$: s("[bd ~]*2 ~ [bd bd ~ bd] [~ bd]*2").bank(kit)
```
</details>

### Pop11
**Source:** drum-patterns

```js
// Title: Pop11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh]").gain("0.85").bank(bank_hh),
  s("sd*4").gain("0.6 1.0 0.6 1.0").bank(bank_sd),
  s("[~ ~ bd ~] [~ bd]*2 [~ ~ bd ~] [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop11
const kit = "RolandTR808";

$: s("[~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh]").gain("0.85").bank(kit)
$: s("sd*4").gain("0.6 1.0 0.6 1.0").bank(kit)
$: s("[~ ~ bd ~] [~ bd]*2 [~ ~ bd ~] [~ bd]*2").bank(kit)
```
</details>

### Pop12
**Source:** drum-patterns

```js
// Title: Pop12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 [~ hh]*2 hh*4 [~ hh]*2").gain("0.85").bank(bank_hh),
  s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop12
const kit = "RolandTR808";

$: s("hh*4 [~ hh]*2 hh*4 [~ hh]*2").gain("0.85").bank(kit)
$: s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd]").bank(kit)
```
</details>

### Pop2
**Source:** drum-patterns

```js
// Title: Pop2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd bd] [bd ~]*2 [~ bd bd bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop2
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ bd bd bd] [bd ~]*2 [~ bd bd bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Pop3
**Source:** drum-patterns

```js
// Title: Pop3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ ~ hh] [hh ~]*2 [hh ~ ~ hh]").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ bd] [~ bd ~ ~] [bd bd ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop3
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ ~ hh] [hh ~]*2 [hh ~ ~ hh]").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ bd] [~ bd ~ ~] [bd bd ~ bd] ~").bank(kit)
```
</details>

### Pop4
**Source:** drum-patterns

```js
// Title: Pop4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ bd bd] [~ bd]*2 [~ bd]*2 [~ bd]*2").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop4
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ bd bd] [~ bd]*2 [~ bd]*2 [~ bd]*2").gain("1.0 0.8").bank(kit)
```
</details>

### Pop5
**Source:** drum-patterns

```js
// Title: Pop5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ bd] ~ [bd bd ~ bd] [~ ~ bd bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop5
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ bd] ~ [bd bd ~ bd] [~ ~ bd bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Pop6
**Source:** drum-patterns

```js
// Title: Pop6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ bd] ~ [bd bd ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop6
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ bd] ~ [bd bd ~ bd] ~").bank(kit)
```
</details>

### Pop7
**Source:** drum-patterns

```js
// Title: Pop7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [~ ~ hh ~] [hh ~]*2 [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ oh ~ oh").bank(bank_oh),
  s("[bd ~ bd bd] [~ ~ bd ~] [~ ~ bd bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop7
const kit = "RolandTR808";

$: s("[hh ~]*2 [~ ~ hh ~] [hh ~]*2 [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ oh ~ oh").bank(kit)
$: s("[bd ~ bd bd] [~ ~ bd ~] [~ ~ bd bd] [~ ~ bd ~]").bank(kit)
```
</details>

### Pop8
**Source:** drum-patterns

```js
// Title: Pop8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.6 1.0 0.6 1.0").bank(bank_hh),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop8
const kit = "RolandTR808";

$: s("hh*4").gain("0.6 1.0 0.6 1.0").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Pop9
**Source:** drum-patterns

```js
// Title: Pop9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.6 0.6 0.6 1.0 0.6 1.0").bank(bank_hh),
  s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ [~ ~ sd ~] ~ [sd ~]*2").gain("1.0 1.0 0.6").bank(bank_sd),
  s("[bd ~]*2 ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pop9
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~ ~ ~]").gain("0.6 0.6 0.6 1.0 0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ [~ ~ sd ~] ~ [sd ~]*2").gain("1.0 1.0 0.6").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### PopBreak1
**Source:** drum-patterns

```js
// Title: PopBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [ht ht ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [mt ~ ~ mt] ~ ~").bank(bank_mt),
  s("sd*4 ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [lt lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd bd ~ ~] ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PopBreak1
const kit = "RolandTR808";

$: s("~ ~ [ht ht ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [mt ~ ~ mt] ~ ~").bank(kit)
$: s("sd*4 ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [lt lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ ~] ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### PopBreak2
**Source:** drum-patterns

```js
// Title: PopBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ht ~] ~ ~").gain("1.1 0.7").bank(bank_ht),
  s("[~ ~ ~ mt] ~ ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(bank_sd),
  s("~ ~ [~ lt ~ ~] ~").gain("1.1 0.7").bank(bank_lt),
  s("[~ bd bd ~] [bd bd ~ bd] [bd ~ bd bd] [~ bd bd bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PopBreak2
const kit = "RolandTR808";

$: s("~ [~ ~ ht ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("[~ ~ ~ mt] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(kit)
$: s("~ ~ [~ lt ~ ~] ~").gain("1.1 0.7").bank(kit)
$: s("[~ bd bd ~] [bd bd ~ bd] [bd ~ bd bd] [~ bd bd bd]").gain("1.0 0.8").bank(kit)
```
</details>

### PopBreak3
**Source:** drum-patterns

```js
// Title: PopBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ ~ ~ [~ ht ht ht]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [mt mt ~ mt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ sd ~] [~ ~ sd ~] ~ ~").gain("1.1 0.7").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PopBreak3
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ht ht ht]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [mt mt ~ mt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### PopBreak4
**Source:** drum-patterns

```js
// Title: PopBreak4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ sd sd ~] [sd ~ ~ ~]").gain("1.1 0.6 0.6 1.1").bank(bank_sd),
  s("[bd ~]*2 [~ bd]*2 [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PopBreak4
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ sd sd ~] [sd ~ ~ ~]").gain("1.1 0.6 0.6 1.1").bank(kit)
$: s("[bd ~]*2 [~ bd]*2 [~ ~ ~ bd] ~").bank(kit)
```
</details>

### PopBreak5
**Source:** drum-patterns

```js
// Title: PopBreak5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cr cr ~ ~]").bank(bank_cr),
  s("[~ ~ ~ mt] ~ ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ [~ sd ~ ~] ~").gain("1.1 0.7").bank(bank_sd),
  s("~ [~ ~ lt ~] ~ ~").gain("1.1 0.7").bank(bank_lt),
  s("~ ~ ~ [bd bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PopBreak5
const kit = "RolandTR808";

$: s("~ ~ ~ [cr cr ~ ~]").bank(kit)
$: s("[~ ~ ~ mt] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ [~ sd ~ ~] ~").gain("1.1 0.7").bank(kit)
$: s("~ [~ ~ lt ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ ~ [bd bd ~ ~]").bank(kit)
```
</details>

### PopBreak6
**Source:** drum-patterns

```js
// Title: PopBreak6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ [~ ~ ~ hh] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ [mt mt mt ~] ~ ~").gain("1.0 0.6 0.6").bank(bank_mt),
  s("[sd ~ ~ ~] [~ ~ ~ sd] ~ ~").bank(bank_sd),
  s("~ ~ [~ ~ ~ lt] [lt lt lt ~]").gain("0.6 0.6 0.6 1.0").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PopBreak6
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ ~ ~ hh] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ [mt mt mt ~] ~ ~").gain("1.0 0.6 0.6").bank(kit)
$: s("[sd ~ ~ ~] [~ ~ ~ sd] ~ ~").bank(kit)
$: s("~ ~ [~ ~ ~ lt] [lt lt lt ~]").gain("0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Reggae1
**Source:** drum-patterns

```js
// Title: Reggae1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh ~ hh] ~ [hh ~]*2 [hh ~]*2").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_hh),
  s("~ [oh ~ ~ ~] ~ ~").bank(bank_oh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("bd*4").gain("0.6 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae1
const kit = "RolandTR808";

$: s("[hh hh ~ hh] ~ [hh ~]*2 [hh ~]*2").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("~ [oh ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("bd*4").gain("0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### Reggae10
**Source:** drum-patterns

```js
// Title: Reggae10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ sd] [~ ~ sd ~]").bank(bank_sd),
  s("[~ ~ rim rim] [~ ~ rim rim] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae10
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ sd] [~ ~ sd ~]").bank(kit)
$: s("[~ ~ rim rim] [~ ~ rim rim] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Reggae11
**Source:** drum-patterns

```js
// Title: Reggae11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ ~ hh ~] [hh ~ hh hh] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ oh ~ ~] [oh ~ ~ ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [rim ~ ~ ~] ~").bank(bank_rim),
  s("~ ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae11
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ ~ hh ~] [hh ~ hh hh] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ oh ~ ~] [oh ~ ~ ~] ~ [~ ~ oh ~]").bank(kit)
$: s("~ ~ [rim ~ ~ ~] ~").bank(kit)
$: s("~ ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Reggae12
**Source:** drum-patterns

```js
// Title: Reggae12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [rim ~ ~ ~] ~").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ bd]*2 [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae12
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [rim ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ bd]*2 [bd ~ ~ ~]").bank(kit)
```
</details>

### Reggae2
**Source:** drum-patterns

```js
// Title: Reggae2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ [rim ~ ~ ~] ~ [rim ~]*2").gain("1.0 1.0 0.6").bank(bank_rim),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae2
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ [rim ~ ~ ~] ~ [rim ~]*2").gain("1.0 1.0 0.6").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~]*2 ~").bank(kit)
```
</details>

### Reggae3
**Source:** drum-patterns

```js
// Title: Reggae3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh hh] [~ ~ hh ~] [~ ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ [rim ~ ~ ~] [~ rim ~ ~] [rim ~ ~ ~]").gain("1.0 0.6 1.0").bank(bank_rim),
  s("[bd ~ ~ bd] ~ [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae3
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh hh] [~ ~ hh ~] [~ ~ hh hh]").gain("0.85").bank(kit)
$: s("~ [rim ~ ~ ~] [~ rim ~ ~] [rim ~ ~ ~]").gain("1.0 0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Reggae4
**Source:** drum-patterns

```js
// Title: Reggae4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ rim ~ rim").bank(bank_rim),
  s("~ [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae4
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ rim ~ rim").bank(kit)
$: s("~ [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### Reggae5
**Source:** drum-patterns

```js
// Title: Reggae5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("[~ ~ ~ rim] [~ ~ rim ~] [~ ~ rim ~] [rim ~ ~ ~]").bank(bank_rim),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae5
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("[~ ~ ~ rim] [~ ~ rim ~] [~ ~ rim ~] [rim ~ ~ ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Reggae6
**Source:** drum-patterns

```js
// Title: Reggae6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_hh),
  s("~ [rim ~]*2 ~ [rim ~]*2").bank(bank_rim),
  s("~ ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae6
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("~ [rim ~]*2 ~ [rim ~]*2").bank(kit)
$: s("~ ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Reggae7
**Source:** drum-patterns

```js
// Title: Reggae7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0").bank(bank_hh),
  s("[rim ~ ~ ~] [~ rim ~ ~] [~ rim ~ ~] ~").gain("0.6 0.6 1.0").bank(bank_rim),
  s("~ [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae7
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0").bank(kit)
$: s("[rim ~ ~ ~] [~ rim ~ ~] [~ rim ~ ~] ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Reggae8
**Source:** drum-patterns

```js
// Title: Reggae8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ oh] ~ [~ oh ~ ~] ~").bank(bank_oh),
  s("[rim ~ ~ ~] [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("[~ ~ bd ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae8
const kit = "RolandTR808";

$: s("[hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ oh] ~ [~ oh ~ ~] ~").bank(kit)
$: s("[rim ~ ~ ~] [~ ~ rim ~] ~ ~").bank(kit)
$: s("[~ ~ bd ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Reggae9
**Source:** drum-patterns

```js
// Title: Reggae9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ hh hh ~] [~ hh]*2 ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ rim] ~ [~ rim]*2 ~").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae9
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ hh hh ~] [~ hh]*2 ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ rim] ~ [~ rim]*2 ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### ReggaeBreak1
**Source:** drum-patterns

```js
// Title: ReggaeBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ [ht ht ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ ~").bank(bank_sd),
  s("~ ~ [lt ~]*2 ~").bank(bank_lt),
  s("[bd ~ ~ ~] ~ ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak1
const kit = "RolandTR808";

$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [ht ht ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [lt ~]*2 ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### ReggaeBreak2
**Source:** drum-patterns

```js
// Title: ReggaeBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [ht ~ ~ ~] ~").bank(bank_ht),
  s("~ ~ ~ [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("~ [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak2
const kit = "RolandTR808";

$: s("~ [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ ~ [ht ~ ~ ~] ~").bank(kit)
$: s("~ ~ ~ [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("~ [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### ReggaeBreak3
**Source:** drum-patterns

```js
// Title: ReggaeBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [ht ht ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[~ ~ mt mt] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd sd ~ ~] [~ ~ sd sd] ~ [sd sd ~ ~]").gain("0.6 0.6 0.6 0.6 1.0 1.0").bank(bank_sd),
  s("~ [lt ~ ~ ~] [~ ~ lt ~] ~").bank(bank_lt),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak3
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ ~ [ht ht ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ mt mt] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd ~ ~] [~ ~ sd sd] ~ [sd sd ~ ~]").gain("0.6 0.6 0.6 0.6 1.0 1.0").bank(kit)
$: s("~ [lt ~ ~ ~] [~ ~ lt ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### ReggaeBreak4
**Source:** drum-patterns

```js
// Title: ReggaeBreak4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [hh ~ ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [oh ~ ~ ~]").bank(bank_oh),
  s("[sd ~ sd ~] [~ ~ sd ~] [sd ~]*2 [sd ~ ~ ~]").gain("1.1 0.6 0.6 1.0 1.0 1.0").bank(bank_sd),
  s("~ ~ ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak4
const kit = "RolandTR808";

$: s("~ [hh ~ ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [oh ~ ~ ~]").bank(kit)
$: s("[sd ~ sd ~] [~ ~ sd ~] [sd ~]*2 [sd ~ ~ ~]").gain("1.1 0.6 0.6 1.0 1.0 1.0").bank(kit)
$: s("~ ~ ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### ReggaeBreak5
**Source:** drum-patterns

```js
// Title: ReggaeBreak5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] ~ [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ [oh ~ ~ ~] [~ ~ oh ~] ~").bank(bank_oh),
  s("[sd ~ ~ ~] [~ ~ sd ~] ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(bank_sd),
  s("[~ ~ bd ~] [bd ~ ~ ~] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak5
const kit = "RolandTR808";

$: s("[~ ~ hh ~] ~ [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ [oh ~ ~ ~] [~ ~ oh ~] ~").bank(kit)
$: s("[sd ~ ~ ~] [~ ~ sd ~] ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] [bd ~]*2 ~").bank(kit)
```
</details>

### ReggaeBreak6
**Source:** drum-patterns

```js
// Title: ReggaeBreak6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [oh ~ ~ ~]").bank(bank_oh),
  s("~ ~ [ht ht ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ ~").bank(bank_sd),
  s("~ ~ [~ ~ lt ~] [lt ~ ~ ~]").gain("0.6 1.0").bank(bank_lt),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak6
const kit = "RolandTR808";

$: s("~ ~ ~ [oh ~ ~ ~]").bank(kit)
$: s("~ ~ [ht ht ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ lt ~] [lt ~ ~ ~]").gain("0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### ReggaeBreak7
**Source:** drum-patterns

```js
// Title: ReggaeBreak7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ oh ~ ~] ~").bank(bank_oh),
  s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd sd sd sd] ~ ~ ~").gain("0.6 0.6 0.6 1.0").bank(bank_sd),
  s("~ ~ [~ lt ~ ~] ~").bank(bank_lt),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").gain("0.6 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak7
const kit = "RolandTR808";

$: s("~ ~ [~ oh ~ ~] ~").bank(kit)
$: s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd sd sd] ~ ~ ~").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("~ ~ [~ lt ~ ~] ~").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").gain("0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### ReggaeBreak8
**Source:** drum-patterns

```js
// Title: ReggaeBreak8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[~ ~ ~ ht] [ht ht ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ mt ~] [mt ~ ~ ~] ~").bank(bank_mt),
  s("[sd ~]*2 ~ ~ ~").bank(bank_sd),
  s("~ ~ [~ lt lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak8
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ oh ~] ~").bank(kit)
$: s("[~ ~ ~ ht] [ht ht ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ mt ~] [mt ~ ~ ~] ~").bank(kit)
$: s("[sd ~]*2 ~ ~ ~").bank(kit)
$: s("~ ~ [~ lt lt lt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### ReggaeBreak9
**Source:** drum-patterns

```js
// Title: ReggaeBreak9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ [~ ~ ht ht] ~").gain("1.0 0.6").bank(bank_ht),
  s("[~ ~ mt mt] [~ ~ mt mt] ~ ~").gain("1.0 0.6 1.0 0.6").bank(bank_mt),
  s("~ [sd sd ~ ~] [sd sd ~ ~] ~").gain("1.0 0.6 1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ReggaeBreak9
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ ht ht] ~").gain("1.0 0.6").bank(kit)
$: s("[~ ~ mt mt] [~ ~ mt mt] ~ ~").gain("1.0 0.6 1.0 0.6").bank(kit)
$: s("~ [sd sd ~ ~] [sd sd ~ ~] ~").gain("1.0 0.6 1.0 0.6").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Rnb1
**Source:** drum-patterns

```js
// Title: Rnb1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [sd ~ ~ sd] [sd sd ~ ~] [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 ~ [~ ~ bd ~] [~ bd bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb1
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] [sd sd ~ ~] [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd ~] [~ bd bd ~]").bank(kit)
```
</details>

### Rnb10
**Source:** drum-patterns

```js
// Title: Rnb10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").gain("1.0 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb10
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").gain("1.0 0.6 0.6 1.0").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ bd bd] ~").bank(kit)
```
</details>

### Rnb11
**Source:** drum-patterns

```js
// Title: Rnb11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 [hh hh hh ~] hh*4 [hh hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(bank_oh),
  s("[~ ~ ~ sd] ~ ~ [~ sd ~ ~]").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ ~ bd] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb11
const kit = "RolandTR808";

$: s("hh*4 [hh hh hh ~] hh*4 [hh hh hh ~]").gain("0.85").bank(kit)
$: s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(kit)
$: s("[~ ~ ~ sd] ~ ~ [~ sd ~ ~]").bank(kit)
$: s("[bd bd ~ ~] [~ ~ ~ bd] [bd ~]*2 ~").bank(kit)
```
</details>

### Rnb12
**Source:** drum-patterns

```js
// Title: Rnb12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6").bank(bank_hh),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [bd ~]*2 [~ bd bd ~]").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb12
const kit = "RolandTR808";

$: s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [bd ~]*2 [~ bd bd ~]").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### Rnb2
**Source:** drum-patterns

```js
// Title: Rnb2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [sd ~ ~ ~] [~ sd ~ ~] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ bd bd] [~ bd]*2 [~ ~ ~ bd] [~ bd]*2").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb2
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ ~] [~ sd ~ ~] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ bd bd] [~ bd]*2 [~ ~ ~ bd] [~ bd]*2").gain("1.0 0.8").bank(kit)
```
</details>

### Rnb3
**Source:** drum-patterns

```js
// Title: Rnb3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [~ bd]*2 [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb3
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [~ bd]*2 [~ bd]*2").bank(kit)
```
</details>

### Rnb4
**Source:** drum-patterns

```js
// Title: Rnb4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~]*2 ~ [bd bd ~ bd] [~ bd bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb4
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~]*2 ~ [bd bd ~ bd] [~ bd bd ~]").bank(kit)
```
</details>

### Rnb5
**Source:** drum-patterns

```js
// Title: Rnb5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ bd bd ~] [~ bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb5
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ bd bd ~] [~ bd bd ~] ~").bank(kit)
```
</details>

### Rnb6
**Source:** drum-patterns

```js
// Title: Rnb6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ ~ bd ~] ~ [~ bd]*2 [~ bd bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb6
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[~ ~ bd ~] ~ [~ bd]*2 [~ bd bd ~]").bank(kit)
```
</details>

### Rnb7
**Source:** drum-patterns

```js
// Title: Rnb7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ bd bd] ~ [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb7
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ bd bd] ~ [bd ~ bd bd] ~").bank(kit)
```
</details>

### Rnb8
**Source:** drum-patterns

```js
// Title: Rnb8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~]").bank(bank_cr),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb8
const kit = "RolandTR808";

$: s("[~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Rnb9
**Source:** drum-patterns

```js
// Title: Rnb9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ bd] [~ ~ ~ bd] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rnb9
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ bd] [~ ~ ~ bd] [bd ~]*2 ~").bank(kit)
```
</details>

### RnbBreak1
**Source:** drum-patterns

```js
// Title: RnbBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~]*2 ~ ~ ~").bank(bank_cr),
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ ~]").gain("1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[bd ~]*2 ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RnbBreak1
const kit = "RolandTR808";

$: s("[cr ~]*2 ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ ~]").gain("1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[bd ~]*2 ~ ~ ~").bank(kit)
```
</details>

### RnbBreak2
**Source:** drum-patterns

```js
// Title: RnbBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ ~ ~] ~ ~").gain("0.6 0.6 1.0").bank(bank_hh),
  s("~ [sd ~ sd sd] [~ sd sd sd] [~ ~ sd sd]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [bd bd ~ ~]").gain("0.6 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RnbBreak2
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ ~ ~] ~ ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ [sd ~ sd sd] [~ sd sd sd] [~ ~ sd sd]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [bd bd ~ ~]").gain("0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### RnbBreak3
**Source:** drum-patterns

```js
// Title: RnbBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ ~ ~ [ht ~ ~ ~]").bank(bank_ht),
  s("~ ~ [~ ~ mt ~] [~ ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ sd sd] [sd sd ~ sd] [~ sd ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RnbBreak3
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [ht ~ ~ ~]").bank(kit)
$: s("~ ~ [~ ~ mt ~] [~ ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ sd sd] [sd sd ~ sd] [~ sd ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ [~ bd ~ ~]").bank(kit)
```
</details>

### RnbBreak4
**Source:** drum-patterns

```js
// Title: RnbBreak4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cr ~ ~ ~]").bank(bank_cr),
  s("[~ ~ sd ~] [~ sd ~ ~] [sd ~ ~ sd] [~ ~ sd ~]").gain("1.1 0.7").bank(bank_sd),
  s("[bd bd ~ bd] [bd ~ bd bd] [~ bd bd ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RnbBreak4
const kit = "RolandTR808";

$: s("~ ~ ~ [cr ~ ~ ~]").bank(kit)
$: s("[~ ~ sd ~] [~ sd ~ ~] [sd ~ ~ sd] [~ ~ sd ~]").gain("1.1 0.7").bank(kit)
$: s("[bd bd ~ bd] [bd ~ bd bd] [~ bd bd ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### RnbBreak5
**Source:** drum-patterns

```js
// Title: RnbBreak5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ [cr ~]*2").bank(bank_cr),
  s("~ [~ ~ ~ mt] [mt ~ ~ ~] ~").gain("0.6 1.0").bank(bank_mt),
  s("~ [sd sd ~ ~] [~ ~ sd sd] ~").gain("1.0 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ [bd ~]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RnbBreak5
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ [cr ~]*2").bank(kit)
$: s("~ [~ ~ ~ mt] [mt ~ ~ ~] ~").gain("0.6 1.0").bank(kit)
$: s("~ [sd sd ~ ~] [~ ~ sd sd] ~").gain("1.0 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ [bd ~]*2").bank(kit)
```
</details>

### RnbBreak6
**Source:** drum-patterns

```js
// Title: RnbBreak6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ cr ~]").bank(bank_cr),
  s("~ [~ ~ mt ~] ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(bank_sd),
  s("[~ bd ~ ~] [bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RnbBreak6
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ cr ~]").bank(kit)
$: s("~ [~ ~ mt ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(kit)
$: s("[~ bd ~ ~] [bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~]").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### Rock1
**Source:** drum-patterns

```js
// Title: Rock1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("1.0 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").gain("1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock1
const kit = "RolandTR808";

$: s("hh*8").gain("1.0 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").gain("1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### Rock10
**Source:** drum-patterns

```js
// Title: Rock10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").gain("0.6 1.0").bank(bank_sd),
  s("[bd ~ bd bd] [~ bd ~ ~] [bd ~ bd bd] [~ bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock10
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").gain("0.6 1.0").bank(kit)
$: s("[bd ~ bd bd] [~ bd ~ ~] [bd ~ bd bd] [~ bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### Rock11
**Source:** drum-patterns

```js
// Title: Rock11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("[~ ~ sd ~] ~ ~ [sd ~ ~ ~]").gain("0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock11
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ sd ~] ~ ~ [sd ~ ~ ~]").gain("0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Rock12
**Source:** drum-patterns

```js
// Title: Rock12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").gain("1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock12
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").gain("1.0 0.6 1.0").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Rock13
**Source:** drum-patterns

```js
// Title: Rock13
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock13
const kit = "RolandTR808";

$: s("hh*16").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
```
</details>

### Rock14
**Source:** drum-patterns

```js
// Title: Rock14
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ bd bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock14
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ bd bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Rock2
**Source:** drum-patterns

```js
// Title: Rock2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock2
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### Rock3
**Source:** drum-patterns

```js
// Title: Rock3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ [sd ~]*2").gain("1.0 1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock3
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~ ~ ~] ~ [sd ~]*2").gain("1.0 1.0 0.6").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Rock4
**Source:** drum-patterns

```js
// Title: Rock4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock4
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Rock5
**Source:** drum-patterns

```js
// Title: Rock5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock5
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Rock6
**Source:** drum-patterns

```js
// Title: Rock6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock6
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Rock7
**Source:** drum-patterns

```js
// Title: Rock7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").gain("1.0 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock7
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").gain("1.0 0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### Rock8
**Source:** drum-patterns

```js
// Title: Rock8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").gain("1.0 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock8
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").gain("1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[bd ~]*2 ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Rock9
**Source:** drum-patterns

```js
// Title: Rock9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd]").gain("1.0 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock9
const kit = "RolandTR808";

$: s("hh*8").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd]").gain("1.0 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### RockBreak1
**Source:** drum-patterns

```js
// Title: RockBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [ht ht ht ~]").gain("1.0 0.6 0.6").bank(bank_ht),
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("[~ ~ sd ~] [sd ~ ~ ~] ~ ~").gain("0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").gain("0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak1
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [ht ht ht ~]").gain("1.0 0.6 0.6").bank(kit)
$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("[~ ~ sd ~] [sd ~ ~ ~] ~ ~").gain("0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").gain("0.6 0.6 1.0").bank(kit)
```
</details>

### RockBreak10
**Source:** drum-patterns

```js
// Title: RockBreak10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 ~ ~").gain("1.0 0.6 1.0 0.6").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ ~ [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ [sd ~ ~ ~] [sd ~]*2 [~ ~ sd sd]").gain("1.0 1.0 1.0 1.0 0.6").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak10
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 ~ ~").gain("1.0 0.6 1.0 0.6").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ ~ ~ [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~ ~ ~] [sd ~]*2 [~ ~ sd sd]").gain("1.0 1.0 1.0 1.0 0.6").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
```
</details>

### RockBreak11
**Source:** drum-patterns

```js
// Title: RockBreak11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ cr ~] ~ ~").bank(bank_cr),
  s("[hh ~]*2 [hh ~ ~ ~] ~ ~").gain("0.6 0.6 1.0").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").gain("0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak11
const kit = "RolandTR808";

$: s("~ [~ ~ cr ~] ~ ~").bank(kit)
$: s("[hh ~]*2 [hh ~ ~ ~] ~ ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").gain("0.6 1.0").bank(kit)
```
</details>

### RockBreak12
**Source:** drum-patterns

```js
// Title: RockBreak12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [ht ht ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [mt mt ~ mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd sd ~ sd] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [~ lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak12
const kit = "RolandTR808";

$: s("~ ~ [ht ht ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [mt mt ~ mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd ~ sd] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### RockBreak2
**Source:** drum-patterns

```js
// Title: RockBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ cr]").bank(bank_cr),
  s("~ ~ [~ ~ ~ ht] ~").bank(bank_ht),
  s("~ ~ [mt mt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd ~]*2 [sd sd sd ~] ~ ~").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_sd),
  s("~ ~ ~ lt*4").gain("0.6 0.6 0.6 1.0").bank(bank_lt),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak2
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ cr]").bank(kit)
$: s("~ ~ [~ ~ ~ ht] ~").bank(kit)
$: s("~ ~ [mt mt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd ~]*2 [sd sd sd ~] ~ ~").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ lt*4").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### RockBreak3
**Source:** drum-patterns

```js
// Title: RockBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("[sd ~]*2 [sd ~]*2 [sd ~]*2 [sd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.1").bank(bank_sd),
  s("[lt ~]*2 [lt ~]*2 [lt ~]*2 ~").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak3
const kit = "RolandTR808";

$: s("[sd ~]*2 [sd ~]*2 [sd ~]*2 [sd ~ ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.1").bank(kit)
$: s("[lt ~]*2 [lt ~]*2 [lt ~]*2 ~").bank(kit)
```
</details>

### RockBreak4
**Source:** drum-patterns

```js
// Title: RockBreak4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ cr ~]").bank(bank_cr),
  s("~ [sd ~ ~ ~] [sd ~ ~ ~] ~").gain("1.1 0.7").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ ~ bd ~]").gain("0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak4
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ cr ~]").bank(kit)
$: s("~ [sd ~ ~ ~] [sd ~ ~ ~] ~").gain("1.1 0.7").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ ~ bd ~]").gain("0.6 0.6 1.0").bank(kit)
```
</details>

### RockBreak5
**Source:** drum-patterns

```js
// Title: RockBreak5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ ~ ~] ~ ~").gain("0.6 0.6 1.0").bank(bank_hh),
  s("~ ~ ~ [oh ~ ~ ~]").bank(bank_oh),
  s("~ ~ ~ [ht ht ht ~]").gain("1.0 0.6 1.0").bank(bank_ht),
  s("~ ~ [mt ~]*2 ~").gain("0.6 1.0").bank(bank_mt),
  s("~ [sd ~ sd sd] ~ ~").gain("1.0 0.6 0.6").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak5
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ ~ ~] ~ ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [oh ~ ~ ~]").bank(kit)
$: s("~ ~ ~ [ht ht ht ~]").gain("1.0 0.6 1.0").bank(kit)
$: s("~ ~ [mt ~]*2 ~").gain("0.6 1.0").bank(kit)
$: s("~ [sd ~ sd sd] ~ ~").gain("1.0 0.6 0.6").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### RockBreak6
**Source:** drum-patterns

```js
// Title: RockBreak6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ cr]").bank(bank_cr),
  s("~ ~ ~ [~ ht ~ ~]").bank(bank_ht),
  s("~ ~ ~ [mt ~ ~ ~]").bank(bank_mt),
  s("[sd ~]*2 [sd sd sd ~] [~ sd sd sd] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ ~ bd]").gain("0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak6
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ cr]").bank(kit)
$: s("~ ~ ~ [~ ht ~ ~]").bank(kit)
$: s("~ ~ ~ [mt ~ ~ ~]").bank(kit)
$: s("[sd ~]*2 [sd sd sd ~] [~ sd sd sd] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ ~ bd]").gain("0.6 0.6 1.0").bank(kit)
```
</details>

### RockBreak7
**Source:** drum-patterns

```js
// Title: RockBreak7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ [~ ~ mt ~] ~ ~").bank(bank_mt),
  s("[~ ~ sd ~] ~ ~ [sd ~ ~ ~]").gain("0.6 1.1").bank(bank_sd),
  s("~ ~ [~ ~ lt ~] ~").bank(bank_lt),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak7
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ ~ mt ~] ~ ~").bank(kit)
$: s("[~ ~ sd ~] ~ ~ [sd ~ ~ ~]").gain("0.6 1.1").bank(kit)
$: s("~ ~ [~ ~ lt ~] ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### RockBreak8
**Source:** drum-patterns

```js
// Title: RockBreak8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~]*2 [~ ~ sd ~] [sd ~ ~ ~]").bank(bank_sd),
  s("lt*8").gain("0.6 0.6 1.0 1.0 0.6 1.0 1.0 0.6").bank(bank_lt),
  s("bd*4").gain("0.6 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak8
const kit = "RolandTR808";

$: s("~ [sd ~]*2 [~ ~ sd ~] [sd ~ ~ ~]").bank(kit)
$: s("lt*8").gain("0.6 0.6 1.0 1.0 0.6 1.0 1.0 0.6").bank(kit)
$: s("bd*4").gain("0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### RockBreak9
**Source:** drum-patterns

```js
// Title: RockBreak9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ [ht ht ht ~]").gain("0.6 0.6 1.0").bank(bank_ht),
  s("~ ~ [mt mt ~ mt] ~").gain("0.6 1.0 1.0").bank(bank_mt),
  s("~ [sd ~]*2 ~ ~").bank(bank_sd),
  s("bd ~ bd ~").gain("1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockBreak9
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [ht ht ht ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ [mt mt ~ mt] ~").gain("0.6 1.0 1.0").bank(kit)
$: s("~ [sd ~]*2 ~ ~").bank(kit)
$: s("bd ~ bd ~").gain("1.0 0.6").bank(kit)
```
</details>

### Samba1
**Source:** drum-patterns

```js
// Title: Samba1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr]").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[mt ~]*2 [~ ~ ~ mt] [~ mt ~ ~] ~").gain("0.6 1.0 0.6 0.6").bank(bank_mt),
  s("~ [~ lt ~ ~] [~ ~ ~ lt] [~ lt lt ~]").gain("0.6 0.6 0.6 1.0").bank(bank_lt),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba1
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr]").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[mt ~]*2 [~ ~ ~ mt] [~ mt ~ ~] ~").gain("0.6 1.0 0.6 0.6").bank(kit)
$: s("~ [~ lt ~ ~] [~ ~ ~ lt] [~ lt lt ~]").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba2
**Source:** drum-patterns

```js
// Title: Samba2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr]").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[mt ~]*2 ~ [mt ~ ~ ~] ~").gain("0.6 1.0 0.6").bank(bank_mt),
  s("~ [~ lt ~ ~] [~ ~ ~ lt] [~ lt ~ ~]").bank(bank_lt),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba2
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr]").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[mt ~]*2 ~ [mt ~ ~ ~] ~").gain("0.6 1.0 0.6").bank(kit)
$: s("~ [~ lt ~ ~] [~ ~ ~ lt] [~ lt ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba3
**Source:** drum-patterns

```js
// Title: Samba3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr]").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[mt ~]*2 ~ [mt ~ ~ ~] ~").gain("0.6 1.0 0.6").bank(bank_mt),
  s("~ [~ lt ~ ~] [~ ~ ~ lt] [~ lt ~ ~]").bank(bank_lt),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba3
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr] [cr ~ cr cr]").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[mt ~]*2 ~ [mt ~ ~ ~] ~").gain("0.6 1.0 0.6").bank(kit)
$: s("~ [~ lt ~ ~] [~ ~ ~ lt] [~ lt ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba4
**Source:** drum-patterns

```js
// Title: Samba4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ hh]*2 [~ ~ hh ~] [hh ~ ~ hh] [~ ~ hh ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_hh),
  s("[ht ~]*2 ~ ~ ~").bank(bank_ht),
  s("~ [mt mt ~ mt] ~ ~").gain("0.6 0.6 1.0").bank(bank_mt),
  s("~ ~ [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [lt lt ~ lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("0.6 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba4
const kit = "RolandTR808";

$: s("[~ hh]*2 [~ ~ hh ~] [hh ~ ~ hh] [~ ~ hh ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[ht ~]*2 ~ ~ ~").bank(kit)
$: s("~ [mt mt ~ mt] ~ ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [lt lt ~ lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("0.6 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### Samba5
**Source:** drum-patterns

```js
// Title: Samba5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [cr ~ cr cr] [~ cr cr ~] [cr cr ~ ~]").bank(bank_cr),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ [~ mt ~ ~] ~ [~ ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ rim ~] ~ [rim ~ ~ rim] ~").bank(bank_rim),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba5
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [cr ~ cr cr] [~ cr cr ~] [cr cr ~ ~]").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ [~ mt ~ ~] ~ [~ ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ rim ~] ~ [rim ~ ~ rim] ~").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba6
**Source:** drum-patterns

```js
// Title: Samba6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~]*2 cr*4 [~ cr]*2 [cr ~]*2").bank(bank_cr),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[rim ~]*2 [~ ~ ~ rim] [~ rim]*2 ~").bank(bank_rim),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba6
const kit = "RolandTR808";

$: s("[cr ~]*2 cr*4 [~ cr]*2 [cr ~]*2").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ mt mt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[rim ~]*2 [~ ~ ~ rim] [~ rim]*2 ~").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### SambaBreak1
**Source:** drum-patterns

```js
// Title: SambaBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [ht ~]*2 ~").bank(bank_ht),
  s("~ [mt ~ mt mt] ~ ~").gain("1.0 0.6 0.6").bank(bank_mt),
  s("[sd sd sd ~] ~ ~ ~").gain("0.6 0.6 1.0").bank(bank_sd),
  s("~ ~ ~ [lt lt lt ~]").gain("0.6 0.6 1.0").bank(bank_lt),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SambaBreak1
const kit = "RolandTR808";

$: s("~ ~ [ht ~]*2 ~").bank(kit)
$: s("~ [mt ~ mt mt] ~ ~").gain("1.0 0.6 0.6").bank(kit)
$: s("[sd sd sd ~] ~ ~ ~").gain("0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [lt lt lt ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### SambaBreak2
**Source:** drum-patterns

```js
// Title: SambaBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ [mt ~]*2 ~").bank(bank_mt),
  s("[sd sd sd ~] ~ ~ [sd ~]*2").gain("1.0 0.6 0.6 1.0 1.0").bank(bank_sd),
  s("~ [lt ~]*2 ~ ~").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SambaBreak2
const kit = "RolandTR808";

$: s("~ ~ [mt ~]*2 ~").bank(kit)
$: s("[sd sd sd ~] ~ ~ [sd ~]*2").gain("1.0 0.6 0.6 1.0 1.0").bank(kit)
$: s("~ [lt ~]*2 ~ ~").bank(kit)
```
</details>

### SambaBreak3
**Source:** drum-patterns

```js
// Title: SambaBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[mt ~]*2 ~ ~ ~").gain("0.6 1.0").bank(bank_mt),
  s("[sd ~]*2 [~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ ~]").gain("0.6 1.0 0.6 1.0 1.0").bank(bank_sd),
  s("~ [~ ~ lt ~] [lt ~ ~ ~] ~").gain("0.6 1.0").bank(bank_lt),
  s("~ ~ ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SambaBreak3
const kit = "RolandTR808";

$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[mt ~]*2 ~ ~ ~").gain("0.6 1.0").bank(kit)
$: s("[sd ~]*2 [~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ ~]").gain("0.6 1.0 0.6 1.0 1.0").bank(kit)
$: s("~ [~ ~ lt ~] [lt ~ ~ ~] ~").gain("0.6 1.0").bank(kit)
$: s("~ ~ ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### Shuffle1
**Source:** drum-patterns

```js
// Title: Shuffle1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle1
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] ~ ~").bank(kit)
```
</details>

### Shuffle2
**Source:** drum-patterns

```js
// Title: Shuffle2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle2
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Shuffle3
**Source:** drum-patterns

```js
// Title: Shuffle3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] [~ sd]*2 [sd sd ~ ~] ~").gain("1.0 0.6 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle3
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] [~ sd]*2 [sd sd ~ ~] ~").gain("1.0 0.6 0.6 0.6 1.0").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Shuffle4
**Source:** drum-patterns

```js
// Title: Shuffle4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle4
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~]*2 [~ bd ~ ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Shuffle5
**Source:** drum-patterns

```js
// Title: Shuffle5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] [~ ~ ~ sd] [sd sd ~ ~] ~").gain("1.0 0.6 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle5
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ ~ sd] [sd sd ~ ~] ~").gain("1.0 0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Shuffle6
**Source:** drum-patterns

```js
// Title: Shuffle6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[sd ~ sd sd] [~ sd sd ~] [sd sd ~ sd] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("[bd ~ bd bd] [~ bd bd ~] [bd bd ~ bd] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Shuffle6
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [~ cr cr ~] [cr cr ~ cr] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[sd ~ sd sd] [~ sd sd ~] [sd sd ~ sd] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[bd ~ bd bd] [~ bd bd ~] [bd bd ~ bd] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### ShuffleBreak1
**Source:** drum-patterns

```js
// Title: ShuffleBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ht ~ ~] ~").bank(bank_ht),
  s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_mt),
  s("sd*4 [sd sd ~ ~] ~ ~").gain("1.0 0.6 1.0 1.0 0.6 1.0").bank(bank_sd),
  s("~ ~ [~ ~ lt lt] ~").gain("0.6 1.0").bank(bank_lt),
  s("[bd ~ ~ ~] [~ bd bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ShuffleBreak1
const kit = "RolandTR808";

$: s("~ ~ [~ ht ~ ~] ~").bank(kit)
$: s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
$: s("sd*4 [sd sd ~ ~] ~ ~").gain("1.0 0.6 1.0 1.0 0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ lt lt] ~").gain("0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] ~ ~").bank(kit)
```
</details>

### ShuffleBreak2
**Source:** drum-patterns

```js
// Title: ShuffleBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ ht] [~ ht]*2 ~").gain("0.6 1.0 1.0").bank(bank_ht),
  s("~ [~ ~ mt ~] [mt ~]*2 ~").gain("1.0 1.0 0.6").bank(bank_mt),
  s("[~ sd sd sd] [sd sd ~ ~] ~ ~").gain("0.6 1.0 1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ShuffleBreak2
const kit = "RolandTR808";

$: s("~ [~ ~ ~ ht] [~ ht]*2 ~").gain("0.6 1.0 1.0").bank(kit)
$: s("~ [~ ~ mt ~] [mt ~]*2 ~").gain("1.0 1.0 0.6").bank(kit)
$: s("[~ sd sd sd] [sd sd ~ ~] ~ ~").gain("0.6 1.0 1.0 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### ShuffleBreak3
**Source:** drum-patterns

```js
// Title: ShuffleBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ mt mt mt] ~").gain("1.0 0.6 1.0").bank(bank_mt),
  s("[~ sd]*2 [sd sd ~ sd] ~ ~").gain("0.6 1.0 0.6 1.0 0.6").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ShuffleBreak3
const kit = "RolandTR808";

$: s("~ ~ [~ mt mt mt] ~").gain("1.0 0.6 1.0").bank(kit)
$: s("[~ sd]*2 [sd sd ~ sd] ~ ~").gain("0.6 1.0 0.6 1.0 0.6").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Ska1
**Source:** drum-patterns

```js
// Title: Ska1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ska1
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Ska2
**Source:** drum-patterns

```js
// Title: Ska2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ska2
const kit = "RolandTR808";

$: s("hh*8").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Ska3
**Source:** drum-patterns

```js
// Title: Ska3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ska3
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### SkaBreak1
**Source:** drum-patterns

```js
// Title: SkaBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_sd = bank_default;

stack(
  s("[sd ~ sd sd] [sd ~]*2 [sd ~ sd sd] sd*4").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SkaBreak1
const kit = "RolandTR808";

$: s("[sd ~ sd sd] [sd ~]*2 [sd ~ sd sd] sd*4").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### SkaBreak2
**Source:** drum-patterns

```js
// Title: SkaBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("oh ~ oh ~").bank(bank_oh),
  s("[~ ~ sd sd] [sd ~]*2 [~ ~ sd sd] sd*4").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SkaBreak2
const kit = "RolandTR808";

$: s("oh ~ oh ~").bank(kit)
$: s("[~ ~ sd sd] [sd ~]*2 [~ ~ sd sd] sd*4").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### SkaBreak3
**Source:** drum-patterns

```js
// Title: SkaBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("~ [~ ~ mt ~] ~ ~").bank(bank_mt),
  s("[~ ~ sd ~] ~ ~ ~").bank(bank_sd),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SkaBreak3
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ ~ [~ ~ ht ~] ~").bank(kit)
$: s("~ [~ ~ mt ~] ~ ~").bank(kit)
$: s("[~ ~ sd ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Slow1
**Source:** drum-patterns

```js
// Title: Slow1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [bd ~]*2 [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow1
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [bd ~]*2 [~ bd ~ ~]").bank(kit)
```
</details>

### Slow10
**Source:** drum-patterns

```js
// Title: Slow10
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow10
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ bd]*2").bank(kit)
```
</details>

### Slow11
**Source:** drum-patterns

```js
// Title: Slow11
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 [hh hh hh ~] hh*4 [hh hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ bd bd] [~ ~ ~ bd] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow11
const kit = "RolandTR808";

$: s("hh*4 [hh hh hh ~] hh*4 [hh hh hh ~]").gain("0.85").bank(kit)
$: s("~ [~ ~ ~ oh] ~ [~ ~ ~ oh]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ bd bd] [~ ~ ~ bd] [bd ~]*2 ~").bank(kit)
```
</details>

### Slow12
**Source:** drum-patterns

```js
// Title: Slow12
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 [hh hh ~ hh] hh*4 [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow12
const kit = "RolandTR808";

$: s("hh*4 [hh hh ~ hh] hh*4 [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ bd ~ ~]").bank(kit)
```
</details>

### Slow2
**Source:** drum-patterns

```js
// Title: Slow2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow2
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Slow3
**Source:** drum-patterns

```js
// Title: Slow3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow3
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh hh hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~]*2 ~").bank(kit)
```
</details>

### Slow4
**Source:** drum-patterns

```js
// Title: Slow4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh hh hh ~] [~ ~ hh ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ ~ oh] ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow4
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh hh hh ~] [~ ~ hh ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ [~ ~ ~ oh] ~ [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] ~ ~").bank(kit)
```
</details>

### Slow5
**Source:** drum-patterns

```js
// Title: Slow5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd bd] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow5
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd bd] ~ ~").bank(kit)
```
</details>

### Slow6
**Source:** drum-patterns

```js
// Title: Slow6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow6
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Slow7
**Source:** drum-patterns

```js
// Title: Slow7
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow7
const kit = "RolandTR808";

$: s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(kit)
```
</details>

### Slow8
**Source:** drum-patterns

```js
// Title: Slow8
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~]*2 ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow8
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 ~ [~ ~ bd ~]").bank(kit)
```
</details>

### Slow9
**Source:** drum-patterns

```js
// Title: Slow9
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ ~ hh ~] [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [oh ~ ~ ~] ~ ~").bank(bank_oh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Slow9
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ ~ hh ~] [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [oh ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### SlowBreak1
**Source:** drum-patterns

```js
// Title: SlowBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SlowBreak1
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] ~ sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### SlowBreak2
**Source:** drum-patterns

```js
// Title: SlowBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ [mt ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("~ ~ ~ [lt ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SlowBreak2
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 ~ ~").gain("0.85").bank(kit)
$: s("~ ~ [mt ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [lt ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### SlowBreak3
**Source:** drum-patterns

```js
// Title: SlowBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ ~ mt] ~ ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ [~ sd ~ ~] [sd sd ~ ~]").gain("0.6 0.6 1.0 1.0").bank(bank_sd),
  s("~ [~ lt ~ ~] ~ ~").gain("1.1 0.7").bank(bank_lt),
  s("[~ bd ~ ~] [bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SlowBreak3
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[~ ~ ~ mt] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ [~ sd ~ ~] [sd sd ~ ~]").gain("0.6 0.6 1.0 1.0").bank(kit)
$: s("~ [~ lt ~ ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("[~ bd ~ ~] [bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### SlowBreak4
**Source:** drum-patterns

```js
// Title: SlowBreak4
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [~ ~ ht ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [mt ~ ~ ~] ~").bank(bank_mt),
  s("[~ ~ ~ sd] [sd ~]*2 ~ ~").gain("0.6 1.0 0.6").bank(bank_sd),
  s("~ ~ ~ [lt ~]*2").bank(bank_lt),
  s("[bd ~ ~ ~] ~ ~ [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SlowBreak4
const kit = "RolandTR808";

$: s("[hh ~]*2 ~ ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ ~ [~ ~ ht ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [mt ~ ~ ~] ~").bank(kit)
$: s("[~ ~ ~ sd] [sd ~]*2 ~ ~").gain("0.6 1.0 0.6").bank(kit)
$: s("~ ~ ~ [lt ~]*2").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ [~ bd]*2").bank(kit)
```
</details>

### SlowBreak5
**Source:** drum-patterns

```js
// Title: SlowBreak5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [~ ~ oh ~] ~ ~").bank(bank_oh),
  s("~ [mt ~ ~ ~] ~ [~ mt mt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd ~ ~ ~] ~ [~ sd]*2 [sd ~ ~ ~]").gain("0.6 0.6 1.0 1.0").bank(bank_sd),
  s("[~ ~ bd ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SlowBreak5
const kit = "RolandTR808";

$: s("[~ ~ hh ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [~ ~ oh ~] ~ ~").bank(kit)
$: s("~ [mt ~ ~ ~] ~ [~ mt mt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd ~ ~ ~] ~ [~ sd]*2 [sd ~ ~ ~]").gain("0.6 0.6 1.0 1.0").bank(kit)
$: s("[~ ~ bd ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### SlowBreak6
**Source:** drum-patterns

```js
// Title: SlowBreak6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_oh = bank_default;
let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr cr ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ ~ [oh ~ ~ ~] ~").bank(bank_oh),
  s("~ ~ ~ [~ ~ ht ~]").gain("1.1 0.7").bank(bank_ht),
  s("~ [~ ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ [sd ~ ~ ~] ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(bank_sd),
  s("[bd bd ~ ~] ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SlowBreak6
const kit = "RolandTR808";

$: s("[cr cr ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [oh ~ ~ ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ ht ~]").gain("1.1 0.7").bank(kit)
$: s("~ [~ ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~ ~ ~] ~ [sd ~ ~ ~]").gain("1.1 0.7").bank(kit)
$: s("[bd bd ~ ~] ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Swing1
**Source:** drum-patterns

```js
// Title: Swing1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing1
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Swing2
**Source:** drum-patterns

```js
// Title: Swing2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ sd]*2 ~").gain("1.0 1.0 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing2
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd]*2 ~").gain("1.0 1.0 0.6").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] ~ ~").bank(kit)
```
</details>

### Swing3
**Source:** drum-patterns

```js
// Title: Swing3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing3
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Swing5
**Source:** drum-patterns

```js
// Title: Swing5
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing5
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Swing6
**Source:** drum-patterns

```js
// Title: Swing6
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing6
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ cr cr ~] [~ cr]*2 ~").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ sd] [~ sd ~ ~] [~ sd ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### SwingBreak1
**Source:** drum-patterns

```js
// Title: SwingBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd ~]*2 [sd ~]*2 [sd ~]*2 ~").gain("1.1 0.7").bank(bank_sd),
  s("[~ bd]*2 [~ bd]*2 [~ bd]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SwingBreak1
const kit = "RolandTR808";

$: s("[sd ~]*2 [sd ~]*2 [sd ~]*2 ~").gain("1.1 0.7").bank(kit)
$: s("[~ bd]*2 [~ bd]*2 [~ bd]*2 ~").bank(kit)
```
</details>

### SwingBreak2
**Source:** drum-patterns

```js
// Title: SwingBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ht ht] ~ ~").gain("0.6 1.0").bank(bank_ht),
  s("[~ ~ ~ mt] [mt ~ ~ ~] ~ ~").gain("0.6 1.0").bank(bank_mt),
  s("[sd sd ~ ~] ~ ~ ~").gain("0.6 1.0").bank(bank_sd),
  s("~ ~ [~ lt lt ~] ~").gain("0.6 1.0").bank(bank_lt),
  s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SwingBreak2
const kit = "RolandTR808";

$: s("~ [~ ~ ht ht] ~ ~").gain("0.6 1.0").bank(kit)
$: s("[~ ~ ~ mt] [mt ~ ~ ~] ~ ~").gain("0.6 1.0").bank(kit)
$: s("[sd sd ~ ~] ~ ~ ~").gain("0.6 1.0").bank(kit)
$: s("~ ~ [~ lt lt ~] ~").gain("0.6 1.0").bank(kit)
$: s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### SwingBreak3
**Source:** drum-patterns

```js
// Title: SwingBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] ~ ~ ~").bank(bank_cr),
  s("~ ~ [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ ~ sd] [~ ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SwingBreak3
const kit = "RolandTR808";

$: s("[cr ~ cr cr] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### Tango1
**Source:** drum-patterns

```js
// Title: Tango1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~]*2").gain("0.6 0.6 0.6 0.6 1.0").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Tango1
const kit = "RolandTR808";

$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~]*2").gain("0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### TangoBreak1
**Source:** drum-patterns

```js
// Title: TangoBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [sd ~]*2 [sd ~]*2").gain("0.6 1.0 0.6 0.6 0.6 0.6").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 [bd ~]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TangoBreak1
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [sd ~]*2 [sd ~]*2").gain("0.6 1.0 0.6 0.6 0.6 0.6").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 [bd ~]*2").bank(kit)
```
</details>

### Twist1
**Source:** drum-patterns

```js
// Title: Twist1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [cr ~]*2 [cr ~]*2 [cr ~]*2").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("hh*4").gain("0.6 0.6 0.6 1.0").bank(bank_hh),
  s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist1
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [cr ~]*2 [cr ~]*2 [cr ~]*2").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("hh*4").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 1.0").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Twist2
**Source:** drum-patterns

```js
// Title: Twist2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cr*8").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_cr),
  s("[~ ~ sd ~] [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 0.6 1.0 1.0").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist2
const kit = "RolandTR808";

$: s("cr*8").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ sd ~] [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 0.6 1.0 1.0").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Twist3
**Source:** drum-patterns

```js
// Title: Twist3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] [cr ~]*2 [cr ~ ~ ~] [cr ~ ~ ~]").gain("0.6 0.6 1.0 0.6 0.6").bank(bank_cr),
  s("hh*8").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6").bank(bank_hh),
  s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 0.6").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Twist3
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] [cr ~]*2 [cr ~ ~ ~] [cr ~ ~ ~]").gain("0.6 0.6 1.0 0.6 0.6").bank(kit)
$: s("hh*8").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6").bank(kit)
$: s("~ [sd ~]*2 ~ [sd ~ ~ ~]").gain("0.6 1.0 0.6").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### TwistBreak1
**Source:** drum-patterns

```js
// Title: TwistBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("[mt ~]*2 [mt ~]*2 [mt ~]*2 ~").bank(bank_mt),
  s("[sd ~]*2 [sd ~]*2 ~ [sd ~]*2").gain("0.6 0.6 0.6 0.6 1.1 1.1").bank(bank_sd),
  s("~ ~ [lt ~]*2 ~").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TwistBreak1
const kit = "RolandTR808";

$: s("[mt ~]*2 [mt ~]*2 [mt ~]*2 ~").bank(kit)
$: s("[sd ~]*2 [sd ~]*2 ~ [sd ~]*2").gain("0.6 0.6 0.6 0.6 1.1 1.1").bank(kit)
$: s("~ ~ [lt ~]*2 ~").bank(kit)
```
</details>

### TwistBreak2
**Source:** drum-patterns

```js
// Title: TwistBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("[~ ~ mt ~] [mt ~]*2 ~ ~").bank(bank_mt),
  s("[sd ~ sd ~] [sd ~]*2 [sd ~]*2 sd*4").gain("1.1 0.6 0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6").bank(bank_sd),
  s("~ ~ [lt ~]*2 ~").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TwistBreak2
const kit = "RolandTR808";

$: s("[~ ~ mt ~] [mt ~]*2 ~ ~").bank(kit)
$: s("[sd ~ sd ~] [sd ~]*2 [sd ~]*2 sd*4").gain("1.1 0.6 0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6").bank(kit)
$: s("~ ~ [lt ~]*2 ~").bank(kit)
```
</details>

### TwistBreak3
**Source:** drum-patterns

```js
// Title: TwistBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;

stack(
  s("~ ~ ~ [~ ~ cr ~]").bank(bank_cr),
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ ~ [mt mt ~ mt] [~ mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd sd ~ sd] [~ sd sd sd] ~ [~ ~ sd ~]").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TwistBreak3
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ cr ~]").bank(kit)
$: s("hh*4").gain("0.85").bank(kit)
$: s("~ ~ [mt mt ~ mt] [~ mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd ~ sd] [~ sd sd sd] ~ [~ ~ sd ~]").gain("0.6 0.6 0.6 1.0 0.6 0.6 1.0").bank(kit)
```
</details>

### Waltz1
**Source:** drum-patterns

```js
// Title: Waltz1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] [cr ~ ~ cr] [cr ~ ~ ~] ~").bank(bank_cr),
  s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Waltz1
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] [cr ~ ~ cr] [cr ~ ~ ~] ~").bank(kit)
$: s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Waltz2
**Source:** drum-patterns

```js
// Title: Waltz2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Waltz2
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Waltz3
**Source:** drum-patterns

```js
// Title: Waltz3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] [cr ~ ~ ~] [cr ~ ~ cr] ~").bank(bank_cr),
  s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] [sd ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Waltz3
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] [cr ~ ~ ~] [cr ~ ~ cr] ~").bank(kit)
$: s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] [sd ~ ~ sd] ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### WaltzBreak1
**Source:** drum-patterns

```js
// Title: WaltzBreak1
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~]*2 [sd ~]*2 ~").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - WaltzBreak1
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ [sd ~]*2 [sd ~]*2 ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### WaltzBreak2
**Source:** drum-patterns

```js
// Title: WaltzBreak2
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ [mt ~ ~ ~] ~ ~").gain("1.1 0.7").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ ~").gain("1.1 0.7").bank(bank_sd),
  s("~ ~ [lt ~ ~ ~] ~").gain("1.1 0.7").bank(bank_lt),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - WaltzBreak2
const kit = "RolandTR808";

$: s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ [mt ~ ~ ~] ~ ~").gain("1.1 0.7").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ [lt ~ ~ ~] ~").gain("1.1 0.7").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### WaltzBreak3
**Source:** drum-patterns

```js
// Title: WaltzBreak3
// Category: Drum Machine Patterns (260)
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;
let bank_lt = bank_default;

stack(
  s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ [mt ~]*2 ~ ~").bank(bank_mt),
  s("[sd ~ ~ ~] ~ ~ ~").gain("1.1 0.7").bank(bank_sd),
  s("~ ~ [lt ~]*2 ~").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - WaltzBreak3
const kit = "RolandTR808";

$: s("~ [hh ~ ~ ~] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ [mt ~]*2 ~ ~").bank(kit)
$: s("[sd ~ ~ ~] ~ ~ ~").gain("1.1 0.7").bank(kit)
$: s("~ ~ [lt ~]*2 ~").bank(kit)
```
</details>

---

## Dub

### Dub
**BPM:** 140
**Source:** DrumBeatRepo

```js
// Title: Dub
// Category: Dub
setcpm(140 / 4);
let bank_default = "RolandTR808";

let bank_bd = bank_default;
let bank_sd = bank_default;
let bank_hh = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("bd ~ bd ~").gain("1.0 0.8").bank(bank_bd),
  s("[[x ~ ~ ~] ~ ~ ~] [[x ~ ~ ~] ~ ~ ~] [[x ~ ~ ~] ~ ~ ~] [x ~ x ~]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth),
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ ~ [sd ~ ~ ~] ~] [~ ~ [sd ~ ~ ~] ~] [~ ~ [sd ~ ~ ~] ~] [~ ~ [sd ~]*2 ~]").bank(bank_sd),
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ [hh ~]*2 ~ [hh ~ ~ ~]] [~ [hh hh hh ~] ~ [hh ~ ~ ~]] [~ [hh ~]*2 ~ [hh hh ~ ~]] [~ [hh ~]*2 ~ [hh ~ hh hh]]").gain("0.85").bank(bank_hh),
  s("[[x ~ ~ ~] ~ ~ ~] ~ [~ ~ [~ ~ x ~] ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dub
setcpm(140 / 4);
const kit = "RolandTR808";

$: s("bd ~ bd ~").gain("1.0 0.8").bank(kit)
$: s("[[x ~ ~ ~] ~ ~ ~] [[x ~ ~ ~] ~ ~ ~] [[x ~ ~ ~] ~ ~ ~] [x ~ x ~]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
$: s("~ sd ~ sd").bank(kit)
$: s("[~ ~ [sd ~ ~ ~] ~] [~ ~ [sd ~ ~ ~] ~] [~ ~ [sd ~ ~ ~] ~] [~ ~ [sd ~]*2 ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[~ [hh ~]*2 ~ [hh ~ ~ ~]] [~ [hh hh hh ~] ~ [hh ~ ~ ~]] [~ [hh ~]*2 ~ [hh hh ~ ~]] [~ [hh ~]*2 ~ [hh ~ hh hh]]").gain("0.85").bank(kit)
$: s("[[x ~ ~ ~] ~ ~ ~] ~ [~ ~ [~ ~ x ~] ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

---

## EBM

### EBM
**BPM:** 120
**Source:** DrumBeatRepo

```js
// Title: EBM
// Category: EBM
setcpm(120 / 4);
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ cp ~] [cp ~]*2 [~ ~ cp ~] [~ ~ cp cp] [~ ~ cp cp] [cp cp ~ ~] [~ cp]*2 [~ ~ cp ~]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ [sd ~ ~ ~] ~ [sd ~ sd sd]]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - EBM
setcpm(120 / 4);
const kit = "RolandTR808";

$: s("[~ ~ cp ~] [cp ~]*2 [~ ~ cp ~] [~ ~ cp cp] [~ ~ cp cp] [cp cp ~ ~] [~ cp]*2 [~ ~ cp ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ [sd ~ ~ ~] ~ [sd ~ sd sd]]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

---

## EDM literature patterns

### bighouse_AM
**Source:** drum-patterns

```js
// Title: bighouse_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[mt ~ ~ mt] [~ ~ mt ~] [mt mt ~ ~] [~ ~ mt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ hh hh ~] [~ ~ hh ~] [~ ~ hh hh] [~ ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ ~ ~ [~ ~ ~ sd]").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - bighouse_AM
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[mt ~ ~ mt] [~ ~ mt ~] [mt mt ~ ~] [~ ~ mt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ hh hh ~] [~ ~ hh ~] [~ ~ hh hh] [~ ~ hh hh]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ ~ ~ [~ ~ ~ sd]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### bigroomhouse_AM
**Source:** drum-patterns

```js
// Title: bigroomhouse_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ oh oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ hh ~] [~ ~ hh hh] [~ hh hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ [~ ~ ~ sd] [~ sd ~ ~] ~").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - bigroomhouse_AM
const kit = "RolandTR808";

$: s("[~ oh oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh hh] [~ hh hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ [~ ~ ~ sd] [~ sd ~ ~] ~").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### breakashleysroach_EH
**Source:** drum-patterns

```js
// Title: breakashleysroach_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_tamb = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("tamb*16 [tamb*4 tamb*4 tamb*4 [tamb tamb tamb ~]]").bank(bank_tamb),
  s("[~ ~ [~ ~ oh ~] ~] [~ ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("[[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2] [[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~]*2 [~ ~ bd ~] [~ bd bd ~] ~] [[bd ~]*2 [~ ~ bd ~] [~ bd bd ~] ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakashleysroach_EH
const kit = "RolandTR808";

$: s("tamb*16 [tamb*4 tamb*4 tamb*4 [tamb tamb tamb ~]]").bank(kit)
$: s("[~ ~ [~ ~ oh ~] ~] [~ ~ [~ ~ oh ~] ~]").bank(kit)
$: s("[[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2] [[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~]*2 [~ ~ bd ~] [~ bd bd ~] ~] [[bd ~]*2 [~ ~ bd ~] [~ bd bd ~] ~]").gain("1.0 0.8").bank(kit)
```
</details>

### breakbeat_SA
**Source:** drum-patterns

```js
// Title: breakbeat_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*32").bank(bank_oh),
  s("[[sd ~ sd sd] [sd sd sd ~] [~ sd sd sd] sd*4] [[sd ~ sd sd] [sd sd sd ~] [~ sd sd sd] sd*4]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd bd ~ ~] [~ bd bd ~] [bd bd ~ ~] [~ bd bd bd] [bd bd ~ ~] [~ bd bd ~] [bd bd ~ ~] [~ bd bd bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakbeat_SA
const kit = "RolandTR808";

$: s("oh*32").bank(kit)
$: s("[[sd ~ sd sd] [sd sd sd ~] [~ sd sd sd] sd*4] [[sd ~ sd sd] [sd sd sd ~] [~ sd sd sd] sd*4]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ ~] [~ bd bd ~] [bd bd ~ ~] [~ bd bd bd] [bd bd ~ ~] [~ bd bd ~] [bd bd ~ ~] [~ bd bd bd]").gain("1.0 0.8").bank(kit)
```
</details>

### breakbreaks(standard)_DMR
**Source:** drum-patterns

```js
// Title: breakbreaks(standard)_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[hh ~]*2 [hh ~]*2 [hh hh hh ~] [hh ~]*2] [hh ~]*2 [hh ~ hh hh] [hh ~]*2 [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [[bd ~ ~ ~] ~ [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakbreaks(standard)_DMR
const kit = "RolandTR808";

$: s("[[hh ~]*2 [hh ~]*2 [hh hh hh ~] [hh ~]*2] [hh ~]*2 [hh ~ hh hh] [hh ~]*2 [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [[bd ~ ~ ~] ~ [~ ~ bd ~] ~]").bank(kit)
```
</details>

### breakcontemporarykick_DMR
**Source:** drum-patterns

```js
// Title: breakcontemporarykick_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ ~] ~ [~ ~ sd ~]] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [[~ ~ bd ~] [~ ~ ~ bd] [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakcontemporarykick_DMR
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ ~] ~ [~ ~ sd ~]] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [[~ ~ bd ~] [~ ~ ~ bd] [~ ~ bd ~] ~]").bank(kit)
```
</details>

### breakcontemporarysnare_DMR
**Source:** drum-patterns

```js
// Title: breakcontemporarysnare_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[hh ~]*2 [hh ~ hh hh] [hh ~]*2 [hh ~]*2] hh*8").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]] [~ ~ ~ [sd ~ ~ ~]]").bank(bank_sd),
  s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [[bd ~ ~ ~] [bd ~ ~ bd] [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakcontemporarysnare_DMR
const kit = "RolandTR808";

$: s("[[hh ~]*2 [hh ~ hh hh] [hh ~]*2 [hh ~]*2] hh*8").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]] [~ ~ ~ [sd ~ ~ ~]]").bank(kit)
$: s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [[bd ~ ~ ~] [bd ~ ~ bd] [~ ~ bd ~] ~]").bank(kit)
```
</details>

### breakelectro(standard)_DMR
**Source:** drum-patterns

```js
// Title: breakelectro(standard)_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[hh ~]*2 [hh ~ hh hh] [hh hh hh ~] [hh ~]*2] [[hh ~]*2 [hh ~ hh hh] [hh hh hh ~] [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] [~ ~ bd ~] ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakelectro(standard)_DMR
const kit = "RolandTR808";

$: s("[[hh ~]*2 [hh ~ hh hh] [hh hh hh ~] [hh ~]*2] [[hh ~]*2 [hh ~ hh hh] [hh hh hh ~] [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] [~ ~ bd ~] ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### breakfunkbreak_SA
**Source:** drum-patterns

```js
// Title: breakfunkbreak_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ [~ ~ oh ~] [~ ~ oh ~] ~] [~ [~ ~ oh ~] [~ ~ oh ~] ~]").bank(bank_oh),
  s("[hh*4 [hh hh ~ ~] [hh hh ~ ~] hh*4] [hh*4 [hh hh ~ ~] [hh hh ~ ~] hh*4]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]] [~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]]").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakfunkbreak_SA
const kit = "RolandTR808";

$: s("[~ [~ ~ oh ~] [~ ~ oh ~] ~] [~ [~ ~ oh ~] [~ ~ oh ~] ~]").bank(kit)
$: s("[hh*4 [hh hh ~ ~] [hh hh ~ ~] hh*4] [hh*4 [hh hh ~ ~] [hh hh ~ ~] hh*4]").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]] [~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]]").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### breakfunkydrummer_EH
**Source:** drum-patterns

```js
// Title: breakfunkydrummer_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ [~ ~ ~ oh] ~ [~ oh ~ ~]] [~ [~ ~ ~ oh] ~ [~ oh ~ ~]]").bank(bank_oh),
  s("[hh*4 [hh hh hh ~] hh*4 [hh ~ hh hh]] [hh*4 [hh hh hh ~] hh*4 [hh ~ hh hh]]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ sd]] [~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ sd]]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~] [bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakfunkydrummer_EH
const kit = "RolandTR808";

$: s("[~ [~ ~ ~ oh] ~ [~ oh ~ ~]] [~ [~ ~ ~ oh] ~ [~ oh ~ ~]]").bank(kit)
$: s("[hh*4 [hh hh hh ~] hh*4 [hh ~ hh hh]] [hh*4 [hh hh hh ~] hh*4 [hh ~ hh hh]]").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ sd]] [~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ sd]]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~] [bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### breakhybrid_DMR
**Source:** drum-patterns

```js
// Title: breakhybrid_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[bd ~ bd ~] [bd ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakhybrid_DMR
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[bd ~ bd ~] [bd ~ bd ~]").bank(kit)
```
</details>

### breakimpeach_EH
**Source:** drum-patterns

```js
// Title: breakimpeach_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ [~ ~ oh ~] ~] [~ ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("[[hh ~]*2 [hh ~ hh hh] [hh ~ ~ ~] [hh ~]*2] [[hh ~]*2 [hh ~ hh hh] [hh ~ ~ ~] [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ bd ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakimpeach_EH
const kit = "RolandTR808";

$: s("[~ ~ [~ ~ oh ~] ~] [~ ~ [~ ~ oh ~] ~]").bank(kit)
$: s("[[hh ~]*2 [hh ~ hh hh] [hh ~ ~ ~] [hh ~]*2] [[hh ~]*2 [hh ~ hh hh] [hh ~ ~ ~] [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ bd ~]").gain("1.0 0.8").bank(kit)
```
</details>

### breakirregular_DMR
**Source:** drum-patterns

```js
// Title: breakirregular_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] ~ ~ [sd ~ ~ ~] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~] [[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakirregular_DMR
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] ~ ~ [sd ~ ~ ~] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~] [[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~]").bank(kit)
```
</details>

### breakitsanewday_EH
**Source:** drum-patterns

```js
// Title: breakitsanewday_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[bd ~]*2 ~ [~ ~ bd bd] [~ ~ ~ bd] [bd ~]*2 ~ [~ ~ bd bd] [~ ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakitsanewday_EH
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd bd] [~ ~ ~ bd] [bd ~]*2 ~ [~ ~ bd bd] [~ ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### breakpapawastoo_EH
**Source:** drum-patterns

```js
// Title: breakpapawastoo_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ [hh ~ ~ ~] [hh ~]*2 [hh ~ hh hh]] [~ [hh ~ ~ ~] [hh ~]*2 [hh ~ hh hh]]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[~ [cp ~ ~ ~] ~ ~] [~ [cp ~ ~ ~] ~ ~]").bank(bank_cp),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakpapawastoo_EH
const kit = "RolandTR808";

$: s("[~ [hh ~ ~ ~] [hh ~]*2 [hh ~ hh hh]] [~ [hh ~ ~ ~] [hh ~]*2 [hh ~ hh hh]]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[~ [cp ~ ~ ~] ~ ~] [~ [cp ~ ~ ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### breakpolyrhythmic_DMR
**Source:** drum-patterns

```js
// Title: breakpolyrhythmic_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ sd] [sd ~ sd sd] [~ [sd ~]*2 [~ ~ sd ~] [sd ~ ~ ~]]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] ~] [[~ ~ bd ~] ~ [bd ~ ~ ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakpolyrhythmic_DMR
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ sd] [sd ~ sd sd] [~ [sd ~]*2 [~ ~ sd ~] [sd ~ ~ ~]]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] ~] [[~ ~ bd ~] ~ [bd ~ ~ ~] ~]").bank(kit)
```
</details>

### breakrolling_DMR
**Source:** drum-patterns

```js
// Title: breakrolling_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~] [[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakrolling_DMR
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~] [[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~]").bank(kit)
```
</details>

### breaksyntheticsubs_EH
**Source:** drum-patterns

```js
// Title: breaksyntheticsubs_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [[~ ~ oh ~] ~ ~ ~]").bank(bank_oh),
  s("hh*8 [[hh ~ ~ ~] [hh ~]*2 [hh ~]*2 [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [~ bd bd bd] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd] [~ bd bd bd] [~ ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breaksyntheticsubs_EH
const kit = "RolandTR808";

$: s("~ [[~ ~ oh ~] ~ ~ ~]").bank(kit)
$: s("hh*8 [[hh ~ ~ ~] [hh ~]*2 [hh ~]*2 [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [~ bd bd bd] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd] [~ bd bd bd] [~ ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### breaktakemetomardigras_EH
**Source:** drum-patterns

```js
// Title: breaktakemetomardigras_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ [sd ~ ~ sd] [~ ~ sd ~] [~ sd]*2] [~ [sd ~ ~ sd] [~ ~ sd ~] [~ sd]*2]").bank(bank_sd),
  s("[sd ~]*2 [~ sd ~ ~] [~ sd ~ ~] [sd ~ ~ ~] [sd ~]*2 [~ sd ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("~ [~ ~ ~ [~ ~ oh ~]]").bank(bank_oh),
  s("[hh ~]*2 [hh ~ hh hh] [~ ~ hh ~] [hh ~ hh hh] [hh ~ ~ ~] [hh ~ hh hh] [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ bd ~ ~] [[bd ~ ~ bd] ~ [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breaktakemetomardigras_EH
const kit = "RolandTR808";

$: s("[~ [sd ~ ~ sd] [~ ~ sd ~] [~ sd]*2] [~ [sd ~ ~ sd] [~ ~ sd ~] [~ sd]*2]").bank(kit)
$: s("[sd ~]*2 [~ sd ~ ~] [~ sd ~ ~] [sd ~ ~ ~] [sd ~]*2 [~ sd ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("~ [~ ~ ~ [~ ~ oh ~]]").bank(kit)
$: s("[hh ~]*2 [hh ~ hh hh] [~ ~ hh ~] [hh ~ hh hh] [hh ~ ~ ~] [hh ~ hh hh] [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]]").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ bd ~ ~] [[bd ~ ~ bd] ~ [~ ~ bd ~] ~]").bank(kit)
```
</details>

### breakthebigbeat_EH
**Source:** drum-patterns

```js
// Title: breakthebigbeat_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ oh ~ oh] [~ oh ~ oh]").bank(bank_oh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~] [[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakthebigbeat_EH
const kit = "RolandTR808";

$: s("[~ oh ~ oh] [~ oh ~ oh]").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~] [[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~]").gain("1.0 0.8").bank(kit)
```
</details>

### breakunconventional_DMR
**Source:** drum-patterns

```js
// Title: breakunconventional_DMR
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ ~ [sd ~ ~ ~] [~ ~ sd ~]] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] ~] [[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakunconventional_DMR
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ ~ [sd ~ ~ ~] [~ ~ sd ~]] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] ~] [[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] ~]").bank(kit)
```
</details>

### breakwalkthisway_EH
**Source:** drum-patterns

```js
// Title: breakwalkthisway_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[oh ~ ~ ~] ~ ~ ~] [[oh ~ ~ ~] ~ ~ ~]").bank(bank_oh),
  s("[[~ ~ hh ~] [hh ~]*2 [hh ~]*2 [hh ~]*2] [[~ ~ hh ~] [hh ~]*2 [hh ~]*2 [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 ~] [[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakwalkthisway_EH
const kit = "RolandTR808";

$: s("[[oh ~ ~ ~] ~ ~ ~] [[oh ~ ~ ~] ~ ~ ~]").bank(kit)
$: s("[[~ ~ hh ~] [hh ~]*2 [hh ~]*2 [hh ~]*2] [[~ ~ hh ~] [hh ~]*2 [hh ~]*2 [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 ~] [[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 ~]").gain("1.0 0.8").bank(kit)
```
</details>

### breakwhenthelevee_EH
**Source:** drum-patterns

```js
// Title: breakwhenthelevee_EH
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd bd] ~] [[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd bd] ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - breakwhenthelevee_EH
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd bd] ~] [[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd bd] ~]").gain("1.0 0.8").bank(kit)
```
</details>

### brithouse_SA
**Source:** drum-patterns

```js
// Title: brithouse_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ rd ~] [~ ~ rd ~] [~ ~ rd ~] [~ ~ rd ~]").bank(bank_rd),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - brithouse_SA
const kit = "RolandTR808";

$: s("[~ ~ rd ~] [~ ~ rd ~] [~ ~ rd ~] [~ ~ rd ~]").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### chicagohouse_SA
**Source:** drum-patterns

```js
// Title: chicagohouse_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*16").gain("0.9 0.5 0.7 0.5").bank(bank_oh),
  s("[~ ~ mt ~] ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ [~ ~ hh ~] [~ ~ ~ hh]").gain("0.85").bank(bank_hh),
  s("~ [cp ~ ~ ~] ~ [cp ~ ~ cp]").bank(bank_cp),
  s("[~ sd ~ ~] [sd ~ ~ sd] [~ ~ sd ~] [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - chicagohouse_SA
const kit = "RolandTR808";

$: s("oh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ mt ~] ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ [~ ~ hh ~] [~ ~ ~ hh]").gain("0.85").bank(kit)
$: s("~ [cp ~ ~ ~] ~ [cp ~ ~ cp]").bank(kit)
$: s("[~ sd ~ ~] [sd ~ ~ sd] [~ ~ sd ~] [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2").bank(kit)
```
</details>

### classichouse_CCM
**Source:** drum-patterns

```js
// Title: classichouse_CCM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ [~ ~ ~ mt] [~ ~ mt ~] [~ ~ mt ~]").bank(bank_mt),
  s("[hh hh hh ~] [~ hh hh hh] [hh hh hh ~] [~ hh hh hh]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - classichouse_CCM
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ [~ ~ ~ mt] [~ ~ mt ~] [~ ~ mt ~]").bank(kit)
$: s("[hh hh hh ~] [~ hh hh hh] [hh hh hh ~] [~ hh hh hh]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### deephouse_CCM
**Source:** drum-patterns

```js
// Title: deephouse_CCM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_lc = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ [~ ~ lc ~] ~ [~ ~ lc ~]] [~ [~ ~ lc ~] ~ [~ ~ lc ~]]").bank(bank_lc),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ [hh ~ hh hh] ~ [hh ~ hh hh]] [~ [hh ~ hh hh] ~ [hh ~ hh hh]]").gain("0.85").bank(bank_hh),
  s("[[~ ~ ~ sd] ~ [~ ~ ~ sd] ~] [~ ~ ~ sd] ~ [~ ~ ~ sd] [~ ~ ~ sd]").bank(bank_sd),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - deephouse_CCM
const kit = "RolandTR808";

$: s("[~ [~ ~ lc ~] ~ [~ ~ lc ~]] [~ [~ ~ lc ~] ~ [~ ~ lc ~]]").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[~ [hh ~ hh hh] ~ [hh ~ hh hh]] [~ [hh ~ hh hh] ~ [hh ~ hh hh]]").gain("0.85").bank(kit)
$: s("[[~ ~ ~ sd] ~ [~ ~ ~ sd] ~] [~ ~ ~ sd] ~ [~ ~ ~ sd] [~ ~ ~ sd]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### deephouse_SA
**Source:** drum-patterns

```js
// Title: deephouse_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_cl = bank_default;
let bank_sd = bank_default;
let bank_mt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ cl ~ ~] ~ [~ cl ~ ~] ~").bank(bank_cl),
  s("[~ ~ ~ sd] ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[~ ~ mt ~] [~ ~ ~ mt] [~ ~ mt ~] ~").bank(bank_mt),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - deephouse_SA
const kit = "RolandTR808";

$: s("[~ cl ~ ~] ~ [~ cl ~ ~] ~").bank(kit)
$: s("[~ ~ ~ sd] ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[~ ~ mt ~] [~ ~ ~ mt] [~ ~ mt ~] ~").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### deeptechhouse_AM
**Source:** drum-patterns

```js
// Title: deeptechhouse_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("sd*32").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ ~ hh] [~ hh ~ ~] [~ ~ ~ hh] [~ hh ~ ~] [~ ~ ~ hh] [~ hh ~ ~] [~ ~ ~ hh] [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ cp ~ cp] [~ cp ~ cp]").bank(bank_cp),
  s("[~ [sd ~ ~ sd] ~ [sd ~ ~ ~]] [~ [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ ~]]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - deeptechhouse_AM
const kit = "RolandTR808";

$: s("sd*32").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[~ ~ ~ hh] [~ hh ~ ~] [~ ~ ~ hh] [~ hh ~ ~] [~ ~ ~ hh] [~ hh ~ ~] [~ ~ ~ hh] [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("[~ cp ~ cp] [~ cp ~ cp]").bank(kit)
$: s("[~ [sd ~ ~ sd] ~ [sd ~ ~ ~]] [~ [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ ~]]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### dirtyhouse_SA
**Source:** drum-patterns

```js
// Title: dirtyhouse_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] ~ [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ mt ~] ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ [~ ~ hh ~] [~ ~ ~ hh]").gain("0.85").bank(bank_hh),
  s("[~ ~ cp ~] [cp ~ ~ ~] [cp ~]*2 [cp ~ ~ ~]").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - dirtyhouse_SA
const kit = "RolandTR808";

$: s("[~ ~ oh ~] ~ [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[~ ~ mt ~] ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ [~ ~ hh ~] [~ ~ ~ hh]").gain("0.85").bank(kit)
$: s("[~ ~ cp ~] [cp ~ ~ ~] [cp ~]*2 [cp ~ ~ ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### frenchhouse_SA
**Source:** drum-patterns

```js
// Title: frenchhouse_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd sd sd ~] [sd ~ sd sd] [sd sd sd ~] [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ oh]*2 [~ oh]*2 [~ oh]*2 [~ oh]*2").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - frenchhouse_SA
const kit = "RolandTR808";

$: s("[sd sd sd ~] [sd ~ sd sd] [sd sd sd ~] [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ oh]*2 [~ oh]*2 [~ oh]*2 [~ oh]*2").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### house_CCM
**Source:** drum-patterns

```js
// Title: house_CCM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~ ~ ~] [hh ~ ~ hh] [hh ~ ~ ~] [hh hh ~ hh] [hh ~ ~ ~] [hh ~ ~ hh] [hh ~ ~ ~] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("[~ cp ~ cp] [~ [cp ~ ~ ~] [~ ~ ~ cp] [~ ~ cp ~]]").bank(bank_cp),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - house_CCM
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh ~ ~ ~] [hh ~ ~ hh] [hh ~ ~ ~] [hh hh ~ hh] [hh ~ ~ ~] [hh ~ ~ hh] [hh ~ ~ ~] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("[~ cp ~ cp] [~ [cp ~ ~ ~] [~ ~ ~ cp] [~ ~ cp ~]]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### house_DMM
**Source:** drum-patterns

```js
// Title: house_DMM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - house_DMM
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### house_DMPS
**Source:** drum-patterns

```js
// Title: house_DMPS
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [~ [cp cp ~ cp] [~ ~ cp cp] ~]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - house_DMPS
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("~ [~ [cp cp ~ cp] [~ ~ cp cp] ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### house_SA
**Source:** drum-patterns

```js
// Title: house_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ oh ~ ~] [~ ~ oh ~] [~ oh ~ ~]").bank(bank_oh),
  s("[~ ~ mt ~] ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - house_SA
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ oh ~ ~] [~ ~ oh ~] [~ oh ~ ~]").bank(kit)
$: s("[~ ~ mt ~] ~ [~ ~ mt ~] ~").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### housewithchords_CCM
**Source:** drum-patterns

```js
// Title: housewithchords_CCM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_cl = bank_default;
let bank_bon = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cl ~]*2").bank(bank_cl),
  s("~ [~ ~ bon ~] ~ [~ ~ bon ~]").bank(bank_bon),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~ ~ ~] [hh ~ ~ ~] [hh hh ~ ~] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - housewithchords_CCM
const kit = "RolandTR808";

$: s("~ ~ ~ [cl ~]*2").bank(kit)
$: s("~ [~ ~ bon ~] ~ [~ ~ bon ~]").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh ~ ~ ~] [hh ~ ~ ~] [hh hh ~ ~] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### minimalhouse_AM
**Source:** drum-patterns

```js
// Title: minimalhouse_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("~ [~ rim ~ ~] ~ [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - minimalhouse_AM
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("~ [~ rim ~ ~] ~ [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### organichouse_AM
**Source:** drum-patterns

```js
// Title: organichouse_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("sd*32").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ oh oh ~] [~ ~ oh ~] [~ oh oh ~] [~ ~ oh ~] [~ oh oh ~] [~ ~ oh ~] [~ oh oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ cp ~ cp] [~ [cp ~ ~ ~] [~ cp ~ ~] [cp ~ ~ ~]]").bank(bank_cp),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - organichouse_AM
const kit = "RolandTR808";

$: s("sd*32").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ oh oh ~] [~ ~ oh ~] [~ oh oh ~] [~ ~ oh ~] [~ oh oh ~] [~ ~ oh ~] [~ oh oh ~] [~ ~ oh ~]").bank(kit)
$: s("[~ cp ~ cp] [~ [cp ~ ~ ~] [~ cp ~ ~] [cp ~ ~ ~]]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### polishedhouse_AM
**Source:** drum-patterns

```js
// Title: polishedhouse_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ sd ~] [~ sd sd sd] [~ ~ sd ~] [~ sd sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - polishedhouse_AM
const kit = "RolandTR808";

$: s("[~ ~ sd ~] [~ sd sd sd] [~ ~ sd ~] [~ sd sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### simplejackinhouse_SA
**Source:** drum-patterns

```js
// Title: simplejackinhouse_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd sd ~ sd] [~ ~ sd ~] [sd sd ~ sd] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ oh ~ ~] ~ [~ oh]*2 ~").bank(bank_oh),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - simplejackinhouse_SA
const kit = "RolandTR808";

$: s("[sd sd ~ sd] [~ ~ sd ~] [sd sd ~ sd] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ oh ~ ~] ~ [~ oh]*2 ~").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### slowdeephouse_SA
**Source:** drum-patterns

```js
// Title: slowdeephouse_SA
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;

stack(
  s("sd*16").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ oh oh] [~ ~ oh oh] [~ oh oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - slowdeephouse_SA
const kit = "RolandTR808";

$: s("sd*16").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ oh oh] [~ ~ oh oh] [~ oh oh ~] [~ ~ oh ~]").bank(kit)
$: s("hh*4").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
```
</details>

### slowhouse_AM
**Source:** drum-patterns

```js
// Title: slowhouse_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_cl = bank_default;
let bank_tamb = bank_default;
let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ [cl ~ ~ ~]] [~ ~ ~ [cl ~ ~ ~]]").bank(bank_cl),
  s("[tamb tamb tamb ~] [tamb ~ tamb tamb] [tamb tamb tamb ~] [tamb ~ tamb tamb] [tamb tamb tamb ~] [tamb ~ tamb tamb] [tamb tamb tamb ~] [tamb ~ tamb tamb]").bank(bank_tamb),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ cp ~ cp] [~ cp ~ cp]").bank(bank_cp),
  s("[[~ ~ ~ rim] ~ [~ rim ~ ~] ~] [[~ ~ ~ rim] ~ [~ rim ~ ~] ~]").bank(bank_rim),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] [[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - slowhouse_AM
const kit = "RolandTR808";

$: s("[~ ~ ~ [cl ~ ~ ~]] [~ ~ ~ [cl ~ ~ ~]]").bank(kit)
$: s("[tamb tamb tamb ~] [tamb ~ tamb tamb] [tamb tamb tamb ~] [tamb ~ tamb tamb] [tamb tamb tamb ~] [tamb ~ tamb tamb] [tamb tamb tamb ~] [tamb ~ tamb tamb]").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[~ cp ~ cp] [~ cp ~ cp]").bank(kit)
$: s("[[~ ~ ~ rim] ~ [~ rim ~ ~] ~] [[~ ~ ~ rim] ~ [~ rim ~ ~] ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] [[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2]").gain("1.0 0.8").bank(kit)
```
</details>

### techno1_DMM
**Source:** drum-patterns

```js
// Title: techno1_DMM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ oh ~ ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~ hh hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("[~ cp ~ cp] [~ cp ~ cp]").bank(bank_cp),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - techno1_DMM
const kit = "RolandTR808";

$: s("[~ oh ~ ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh ~ hh hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("[~ cp ~ cp] [~ cp ~ cp]").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### technoDMPS_AM
**Source:** drum-patterns

```js
// Title: technoDMPS_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_tamb = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~]").bank(bank_tamb),
  s("[[~ ~ oh ~] ~ [~ ~ oh ~] ~] [[~ ~ oh ~] ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("[[hh ~ ~ hh] [hh ~ hh hh] [hh hh ~ ~] [hh ~]*2] [hh ~ ~ hh] [hh ~]*2 [hh hh hh ~] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[~ [sd sd ~ ~] [sd ~]*2 [~ sd sd ~]] [~ [sd ~ sd sd] ~ [sd ~]*2]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4 [[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - technoDMPS_AM
const kit = "RolandTR808";

$: s("[~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~] [~ tamb tamb ~]").bank(kit)
$: s("[[~ ~ oh ~] ~ [~ ~ oh ~] ~] [[~ ~ oh ~] ~ [~ ~ oh ~] ~]").bank(kit)
$: s("[[hh ~ ~ hh] [hh ~ hh hh] [hh hh ~ ~] [hh ~]*2] [hh ~ ~ hh] [hh ~]*2 [hh hh hh ~] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[~ [sd sd ~ ~] [sd ~]*2 [~ sd sd ~]] [~ [sd ~ sd sd] ~ [sd ~]*2]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4 [[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2]").gain("1.0 0.8").bank(kit)
```
</details>

### technochugging_AM
**Source:** drum-patterns

```js
// Title: technochugging_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ oh oh ~] [~ oh oh oh] [~ ~ oh oh] [~ oh oh oh] [~ oh oh ~] [~ oh oh oh] [~ ~ oh oh] [~ oh oh oh]").bank(bank_oh),
  s("[~ [~ ~ hh ~] [~ ~ ~ hh] [~ ~ hh ~]] [~ [~ hh ~ ~] [~ ~ hh ~] [~ hh ~ ~]]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("bd*4 [bd ~ ~ ~] [bd ~ ~ ~] [bd bd ~ ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - technochugging_AM
const kit = "RolandTR808";

$: s("[~ oh oh ~] [~ oh oh oh] [~ ~ oh oh] [~ oh oh oh] [~ oh oh ~] [~ oh oh oh] [~ ~ oh oh] [~ oh oh oh]").bank(kit)
$: s("[~ [~ ~ hh ~] [~ ~ ~ hh] [~ ~ hh ~]] [~ [~ hh ~ ~] [~ ~ hh ~] [~ hh ~ ~]]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("bd*4 [bd ~ ~ ~] [bd ~ ~ ~] [bd bd ~ ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### technodarkberlin_AM
**Source:** drum-patterns

```js
// Title: technodarkberlin_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_cp = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh oh]").bank(bank_oh),
  s("[~ [~ ~ mt ~] ~ [~ ~ mt ~]] [~ [~ ~ mt ~] ~ [~ ~ mt ~]]").bank(bank_mt),
  s("[~ [cp ~ ~ ~] ~ ~] [~ [cp ~ ~ ~] [~ ~ ~ cp] ~]").bank(bank_cp),
  s("[~ ~ [rim ~ ~ ~] ~] [~ ~ [rim ~ ~ rim] ~]").bank(bank_rim),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - technodarkberlin_AM
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh oh]").bank(kit)
$: s("[~ [~ ~ mt ~] ~ [~ ~ mt ~]] [~ [~ ~ mt ~] ~ [~ ~ mt ~]]").bank(kit)
$: s("[~ [cp ~ ~ ~] ~ ~] [~ [cp ~ ~ ~] [~ ~ ~ cp] ~]").bank(kit)
$: s("[~ ~ [rim ~ ~ ~] ~] [~ ~ [rim ~ ~ rim] ~]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### technogrindinganalogue_AM
**Source:** drum-patterns

```js
// Title: technogrindinganalogue_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("sd*4 sd*4").bank(bank_sd),
  s("oh*4 oh*4").bank(bank_oh),
  s("[[~ ~ mt ~] ~ ~ ~] [[~ ~ mt ~] ~ ~ ~]").bank(bank_mt),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ [cp ~ ~ ~] ~ ~] [~ [cp ~ ~ ~] ~ ~]").bank(bank_cp),
  s("[rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("bd*4 [bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - technogrindinganalogue_AM
const kit = "RolandTR808";

$: s("sd*4 sd*4").bank(kit)
$: s("oh*4 oh*4").bank(kit)
$: s("[[~ ~ mt ~] ~ ~ ~] [[~ ~ mt ~] ~ ~ ~]").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ [cp ~ ~ ~] ~ ~] [~ [cp ~ ~ ~] ~ ~]").bank(kit)
$: s("[rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~] [rim rim ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4 [bd ~ ~ bd] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### technohardcore_CCM
**Source:** drum-patterns

```js
// Title: technohardcore_CCM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[mt ~ mt mt] [~ ~ mt ~] [mt ~ mt mt] [~ ~ mt ~] [mt ~ mt mt] [~ ~ mt ~] [mt ~ mt mt] [~ ~ mt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ cp ~ cp] [~ cp ~ cp]").bank(bank_cp),
  s("[sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd] [~ ~ sd ~]").bank(bank_sd),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - technohardcore_CCM
const kit = "RolandTR808";

$: s("[mt ~ mt mt] [~ ~ mt ~] [mt ~ mt mt] [~ ~ mt ~] [mt ~ mt mt] [~ ~ mt ~] [mt ~ mt mt] [~ ~ mt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ cp ~ cp] [~ cp ~ cp]").bank(kit)
$: s("[sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd] [~ ~ sd ~] [sd ~ ~ sd] [~ ~ sd ~]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### technoindustrial_AM
**Source:** drum-patterns

```js
// Title: technoindustrial_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[[mt ~]*2 [~ mt]*2 [mt ~]*2 [~ mt]*2] [[mt ~]*2 [~ mt]*2 [mt ~]*2 [~ mt]*2]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ [~ ~ hh ~] ~ [~ ~ hh ~]] [~ [~ ~ hh ~] ~ [~ ~ hh ~]]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[rim ~ ~ ~] [rim ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - technoindustrial_AM
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[[mt ~]*2 [~ mt]*2 [mt ~]*2 [~ mt]*2] [[mt ~]*2 [~ mt]*2 [mt ~]*2 [~ mt]*2]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ [~ ~ hh ~] ~ [~ ~ hh ~]] [~ [~ ~ hh ~] ~ [~ ~ hh ~]]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[rim ~ ~ ~] [rim ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### technominimal_CCM
**Source:** drum-patterns

```js
// Title: technominimal_CCM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_lc = bank_default;
let bank_bon = bank_default;
let bank_rd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("sd*32").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[[~ ~ ~ lc] ~ [~ ~ ~ lc] ~] [[~ ~ ~ lc] ~ [~ ~ ~ lc] ~]").bank(bank_lc),
  s("[~ [~ ~ bon ~] ~ [~ ~ bon ~]] [~ [~ ~ bon ~] ~ [~ ~ bon ~]]").bank(bank_bon),
  s("[rd ~ ~ rd] [~ rd]*2 [~ ~ rd ~] [~ ~ rd ~] [rd ~ ~ rd] [~ rd]*2 [~ ~ rd ~] [~ ~ rd ~]").bank(bank_rd),
  s("oh*4 oh*4").bank(bank_oh),
  s("[~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh]").gain("0.85").bank(bank_hh),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - technominimal_CCM
const kit = "RolandTR808";

$: s("sd*32").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[[~ ~ ~ lc] ~ [~ ~ ~ lc] ~] [[~ ~ ~ lc] ~ [~ ~ ~ lc] ~]").bank(kit)
$: s("[~ [~ ~ bon ~] ~ [~ ~ bon ~]] [~ [~ ~ bon ~] ~ [~ ~ bon ~]]").bank(kit)
$: s("[rd ~ ~ rd] [~ rd]*2 [~ ~ rd ~] [~ ~ rd ~] [rd ~ ~ rd] [~ rd]*2 [~ ~ rd ~] [~ ~ rd ~]").bank(kit)
$: s("oh*4 oh*4").bank(kit)
$: s("[~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh] [~ hh hh hh]").gain("0.85").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### technothumping_AM
**Source:** drum-patterns

```js
// Title: technothumping_AM
// Category: EDM literature patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_oh = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("rd*4 rd*4").bank(bank_rd),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ ~ [~ ~ mt ~]] [~ ~ ~ [~ ~ mt ~]]").bank(bank_mt),
  s("hh*32").gain("0.85").bank(bank_hh),
  s("[[~ ~ cp ~] [~ ~ cp ~] [~ ~ ~ cp] [~ cp]*2] [[~ ~ cp ~] [~ ~ cp ~] [~ ~ ~ cp] [~ cp]*2]").bank(bank_cp),
  s("[[rim ~]*2 ~ ~ ~] [[rim ~]*2 ~ ~ ~]").bank(bank_rim),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - technothumping_AM
const kit = "RolandTR808";

$: s("rd*4 rd*4").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[~ ~ ~ [~ ~ mt ~]] [~ ~ ~ [~ ~ mt ~]]").bank(kit)
$: s("hh*32").gain("0.85").bank(kit)
$: s("[[~ ~ cp ~] [~ ~ cp ~] [~ ~ ~ cp] [~ cp]*2] [[~ ~ cp ~] [~ ~ cp ~] [~ ~ ~ cp] [~ cp]*2]").bank(kit)
$: s("[[rim ~]*2 ~ ~ ~] [[rim ~]*2 ~ ~ ~]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

---

## FR 3 Patterns

### beguine
**Source:** drum-patterns

```js
// Title: beguine
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_cl = bank_default;
let bank_sd = bank_default;
let bank_lc = bank_default;
let bank_hc = bank_default;
let bank_hh = bank_default;

stack(
  s("[cl ~ ~ ~] [~ ~ cl ~] ~ [cl ~ ~ ~] [~ [cl ~ ~ ~] [cl ~ ~ ~] ~]").bank(bank_cl),
  s("sd*8 sd*8").bank(bank_sd),
  s("[lc ~ ~ ~] ~ [lc ~ ~ ~] [lc ~ ~ ~] [lc ~ ~ ~] ~ [lc ~ ~ ~] [lc ~ ~ ~]").bank(bank_lc),
  s("[~ ~ hc ~] [~ ~ hc ~] [~ ~ hc ~] [~ ~ hc ~] [hc ~]*2 [~ ~ hc ~] [~ ~ hc ~] [~ ~ hc ~]").bank(bank_hc),
  s("[[~ ~ hh ~] ~ ~ ~] [[~ ~ hh ~] ~ ~ ~]").gain("0.85").bank(bank_hh)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - beguine
const kit = "RolandTR808";

$: s("[cl ~ ~ ~] [~ ~ cl ~] ~ [cl ~ ~ ~] [~ [cl ~ ~ ~] [cl ~ ~ ~] ~]").bank(kit)
$: s("sd*8 sd*8").bank(kit)
$: s("[lc ~ ~ ~] ~ [lc ~ ~ ~] [lc ~ ~ ~] [lc ~ ~ ~] ~ [lc ~ ~ ~] [lc ~ ~ ~]").bank(kit)
$: s("[~ ~ hc ~] [~ ~ hc ~] [~ ~ hc ~] [~ ~ hc ~] [hc ~]*2 [~ ~ hc ~] [~ ~ hc ~] [~ ~ hc ~]").bank(kit)
$: s("[[~ ~ hh ~] ~ ~ ~] [[~ ~ hh ~] ~ ~ ~]").gain("0.85").bank(kit)
```
</details>

### bossanova
**Source:** drum-patterns

```js
// Title: bossanova
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd ~ ~ ~] [~ ~ sd ~] ~ [sd ~ ~ ~] [~ [sd ~ ~ ~] [~ ~ sd ~] ~]").bank(bank_sd),
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[rim ~ ~ ~] [~ ~ rim ~] ~ [rim ~ ~ ~] [~ [rim ~ ~ ~] [~ ~ rim ~] ~]").bank(bank_rim),
  s("[[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~] [[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - bossanova
const kit = "RolandTR808";

$: s("[sd ~ ~ ~] [~ ~ sd ~] ~ [sd ~ ~ ~] [~ [sd ~ ~ ~] [~ ~ sd ~] ~]").bank(kit)
$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[rim ~ ~ ~] [~ ~ rim ~] ~ [rim ~ ~ ~] [~ [rim ~ ~ ~] [~ ~ rim ~] ~]").bank(kit)
$: s("[[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~] [[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~]").bank(kit)
```
</details>

### foxtrot
**Source:** drum-patterns

```js
// Title: foxtrot
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd ~ sd ~] [sd ~ sd ~]").bank(bank_sd),
  s("[~ hh ~ hh] [~ hh ~ hh]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[bd ~ bd ~] [bd ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - foxtrot
const kit = "RolandTR808";

$: s("[sd ~ sd ~] [sd ~ sd ~]").bank(kit)
$: s("[~ hh ~ hh] [~ hh ~ hh]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[bd ~ bd ~] [bd ~ bd ~]").bank(kit)
```
</details>

### habanera
**Source:** drum-patterns

```js
// Title: habanera
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ bd ~] [bd ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - habanera
const kit = "RolandTR808";

$: s("[sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ bd ~] [bd ~ bd ~]").bank(kit)
```
</details>

### mambo
**Source:** drum-patterns

```js
// Title: mambo
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_lc = bank_default;
let bank_hc = bank_default;
let bank_rim = bank_default;

stack(
  s("sd*8 sd*8").bank(bank_sd),
  s("[~ ~ ~ [lc ~]*2] [~ ~ ~ [lc ~]*2]").bank(bank_lc),
  s("[~ [~ ~ hc ~] [hc ~ ~ ~] ~] [~ [~ ~ hc ~] [hc ~ ~ ~] ~]").bank(bank_hc),
  s("rim*4 rim*4").bank(bank_rim)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - mambo
const kit = "RolandTR808";

$: s("sd*8 sd*8").bank(kit)
$: s("[~ ~ ~ [lc ~]*2] [~ ~ ~ [lc ~]*2]").bank(kit)
$: s("[~ [~ ~ hc ~] [hc ~ ~ ~] ~] [~ [~ ~ hc ~] [hc ~ ~ ~] ~]").bank(kit)
$: s("rim*4 rim*4").bank(kit)
```
</details>

### march
**Source:** drum-patterns

```js
// Title: march
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh ~] [hh ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[bd ~ bd ~] [bd ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - march
const kit = "RolandTR808";

$: s("[hh ~ hh ~] [hh ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[bd ~ bd ~] [bd ~ bd ~]").bank(kit)
```
</details>

### rhumba
**Source:** drum-patterns

```js
// Title: rhumba
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_cl = bank_default;
let bank_sd = bank_default;
let bank_lc = bank_default;
let bank_hc = bank_default;
let bank_bd = bank_default;

stack(
  s("[cl ~ ~ ~] [~ ~ cl ~] ~ [cl ~ ~ ~] [~ [cl ~ ~ ~] [cl ~ ~ ~] ~]").bank(bank_cl),
  s("[[sd ~ sd sd] [sd ~]*2 [sd ~]*2 [sd ~]*2] [[sd ~ sd sd] [sd ~]*2 [sd ~]*2 [sd ~]*2]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ ~ [lc ~]*2] [~ ~ ~ [lc ~]*2]").bank(bank_lc),
  s("[~ [hc ~ ~ ~] [~ ~ hc ~] [~ ~ hc ~]] [~ ~ [~ ~ hc ~] [~ ~ hc ~]]").bank(bank_hc),
  s("[[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~] [[bd ~]*2 [bd ~]*2 [bd ~ ~ ~] ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - rhumba
const kit = "RolandTR808";

$: s("[cl ~ ~ ~] [~ ~ cl ~] ~ [cl ~ ~ ~] [~ [cl ~ ~ ~] [cl ~ ~ ~] ~]").bank(kit)
$: s("[[sd ~ sd sd] [sd ~]*2 [sd ~]*2 [sd ~]*2] [[sd ~ sd sd] [sd ~]*2 [sd ~]*2 [sd ~]*2]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ [lc ~]*2] [~ ~ ~ [lc ~]*2]").bank(kit)
$: s("[~ [hc ~ ~ ~] [~ ~ hc ~] [~ ~ hc ~]] [~ ~ [~ ~ hc ~] [~ ~ hc ~]]").bank(kit)
$: s("[[bd ~]*2 [~ ~ bd ~] [bd ~ ~ ~] ~] [[bd ~]*2 [bd ~]*2 [bd ~ ~ ~] ~]").gain("1.0 0.8").bank(kit)
```
</details>

### rocknroll
**Source:** drum-patterns

```js
// Title: rocknroll
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ [sd ~]*2 ~ [sd ~ ~ ~]] [~ [sd ~]*2 ~ [sd ~ ~ ~]]").bank(bank_sd),
  s("[[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~] [[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - rocknroll
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ [sd ~]*2 ~ [sd ~ ~ ~]] [~ [sd ~]*2 ~ [sd ~ ~ ~]]").bank(kit)
$: s("[[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~] [[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~]").bank(kit)
```
</details>

### samba
**Source:** drum-patterns

```js
// Title: samba
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_lc = bank_default;
let bank_hc = bank_default;

stack(
  s("sd*8 sd*8").bank(bank_sd),
  s("[~ ~ [lc ~ ~ ~] ~] [~ ~ [lc ~ ~ ~] ~]").bank(bank_lc),
  s("[hc ~ ~ ~] [hc ~ ~ ~] ~ [~ ~ hc ~] [[~ ~ hc ~] [~ ~ hc ~] ~ ~]").bank(bank_hc)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - samba
const kit = "RolandTR808";

$: s("sd*8 sd*8").bank(kit)
$: s("[~ ~ [lc ~ ~ ~] ~] [~ ~ [lc ~ ~ ~] ~]").bank(kit)
$: s("[hc ~ ~ ~] [hc ~ ~ ~] ~ [~ ~ hc ~] [[~ ~ hc ~] [~ ~ hc ~] ~ ~]").bank(kit)
```
</details>

### swing
**Source:** drum-patterns

```js
// Title: swing
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ [sd ~ ~ sd] ~ [sd ~ ~ sd]] [~ [sd ~ ~ sd] ~ [sd ~ ~ sd]]").bank(bank_sd),
  s("[hh ~ hh ~] [hh ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[bd ~ bd ~] [bd ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - swing
const kit = "RolandTR808";

$: s("[~ [sd ~ ~ sd] ~ [sd ~ ~ sd]] [~ [sd ~ ~ sd] ~ [sd ~ ~ sd]]").bank(kit)
$: s("[hh ~ hh ~] [hh ~ hh ~]").gain("0.85").bank(kit)
$: s("[bd ~ bd ~] [bd ~ bd ~]").bank(kit)
```
</details>

### tango
**Source:** drum-patterns

```js
// Title: tango
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ [~ ~ hh ~]] [~ ~ ~ [~ ~ hh ~]]").gain("0.85").bank(bank_hh),
  s("[[sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~]*2] [[sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~]*2]").bank(bank_sd),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - tango
const kit = "RolandTR808";

$: s("[~ ~ ~ [~ ~ hh ~]] [~ ~ ~ [~ ~ hh ~]]").gain("0.85").bank(kit)
$: s("[[sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~]*2] [[sd ~ ~ ~] [sd ~ ~ ~] [sd ~ ~ ~] [sd ~]*2]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### waltz
**Source:** drum-patterns

```js
// Title: waltz
// Category: FR 3 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] [~ ~ hh ~] ~ [hh ~ ~ ~] [[~ ~ hh ~] ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [sd ~ ~ ~] [sd ~]*2 [~ ~ sd ~] [[sd ~ ~ ~] [sd ~]*2 ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~] [[~ ~ bd ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - waltz
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] [~ ~ hh ~] ~ [hh ~ ~ ~] [[~ ~ hh ~] ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [sd ~ ~ ~] [sd ~]*2 [~ ~ sd ~] [[sd ~ ~ ~] [sd ~]*2 ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~] [[~ ~ bd ~] ~ ~ ~]").bank(kit)
```
</details>

---

## Hardcore Techno

### Gabber
**BPM:** 200
**Source:** DrumBeatRepo

```js
// Title: Gabber
// Category: Hardcore Techno
setcpm(200 / 4);
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ [~ ~ ~ cr]]").bank(bank_cr),
  s("oh*8 oh*8").bank(bank_oh),
  s("cp*4 cp*4").bank(bank_cp),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Gabber
setcpm(200 / 4);
const kit = "RolandTR808";

$: s("~ [~ ~ ~ [~ ~ ~ cr]]").bank(kit)
$: s("oh*8 oh*8").bank(kit)
$: s("cp*4 cp*4").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

---

## Hip-Hop

### Jul type beat
**BPM:** 143
**Source:** DrumBeatRepo

```js
// Title: Jul type beat
// Category: Hip-Hop
setcpm(143 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ [~ ~ hh ~] ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ [~ ~ hh ~] ~] [[~ ~ ~ hh] ~ ~ [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~]").bank(bank_sd),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jul type beat
setcpm(143 / 4);
const kit = "RolandTR808";

$: s("~ [~ ~ [~ ~ hh ~] ~]").gain("0.85").bank(kit)
$: s("[~ ~ [~ ~ hh ~] ~] [[~ ~ ~ hh] ~ ~ [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Trap
**BPM:** 140
**Source:** DrumBeatRepo

```js
// Title: Trap
// Category: Hip-Hop
setcpm(140 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh hh hh ~] [[hh ~]*2 [hh hh hh ~] [hh ~]*2 [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ ~ [sd ~ ~ ~] ~] [~ ~ [sd ~ ~ ~] ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~] [~ [bd ~ ~ ~] [~ ~ bd ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Trap
setcpm(140 / 4);
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh hh hh ~] [[hh ~]*2 [hh hh hh ~] [hh ~]*2 [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ ~ [sd ~ ~ ~] ~] [~ ~ [sd ~ ~ ~] ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~] [~ [bd ~ ~ ~] [~ ~ bd ~] ~]").bank(kit)
```
</details>

---

## Hypnotic Techno

### Son Clave
**BPM:** 128
**Source:** DrumBeatRepo

```js
// Title: Son Clave
// Category: Hypnotic Techno
setcpm(128 / 4);
let bank_default = "RolandTR808";

let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[x ~ ~ x] [~ ~ x ~] [~ ~ x ~] [x ~ ~ ~]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth),
  s("x*8").gain("1.0 0.8").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Son Clave
setcpm(128 / 4);
const kit = "RolandTR808";

$: s("[x ~ ~ x] [~ ~ x ~] [~ ~ x ~] [x ~ ~ ~]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
$: s("x*8").gain("1.0 0.8").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Tresillo
**BPM:** 128
**Source:** DrumBeatRepo

```js
// Title: Tresillo
// Category: Hypnotic Techno
setcpm(128 / 4);
let bank_default = "RolandTR808";

let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[x ~ ~ x] [~ ~ x ~] ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth),
  s("[x ~]*2 [x ~]*2 ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Tresillo
setcpm(128 / 4);
const kit = "RolandTR808";

$: s("[x ~ ~ x] [~ ~ x ~] ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
$: s("[x ~]*2 [x ~]*2 ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ ~").bank(kit)
```
</details>

---

## Metal

### Half time groove
**BPM:** 145
**Source:** DrumBeatRepo

```js
// Title: Half time groove
// Category: Metal
setcpm(145 / 4);
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_cr = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("cr*4").bank(bank_cr),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Half time groove
setcpm(145 / 4);
const kit = "RolandTR808";

$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("cr*4").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Blast beat
**BPM:** 180
**Source:** DrumBeatRepo

```js
// Title: Blast beat
// Category: Metal
setcpm(180 / 4);
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ sd]*2 [~ sd]*2 [~ sd]*2 [~ sd]*2").bank(bank_sd),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("bd*8").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Blast beat
setcpm(180 / 4);
const kit = "RolandTR808";

$: s("[~ sd]*2 [~ sd]*2 [~ sd]*2 [~ sd]*2").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("bd*8").gain("1.0 0.8").bank(kit)
```
</details>

### Metal
**BPM:** 180
**Source:** DrumBeatRepo

```js
// Title: Metal
// Category: Metal
setcpm(180 / 4);
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("hh*4").gain("0.85").bank(bank_hh),
  s("bd*16").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Metal
setcpm(180 / 4);
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("hh*4").gain("0.85").bank(kit)
$: s("bd*16").gain("1.0 0.8").bank(kit)
```
</details>

---

## Psytrance

### Psytrance
**BPM:** 135
**Source:** DrumBeatRepo

```js
// Title: Psytrance
// Category: Psytrance
setcpm(135 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd),
  s("[~ x x x] [~ x x x] [~ x x x] [~ x x x]").gain("1.0 0.8").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Psytrance
setcpm(135 / 4);
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
$: s("[~ x x x] [~ x x x] [~ x x x] [~ x x x]").gain("1.0 0.8").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

---

## Punk

### Eight note fill
**BPM:** 170
**Source:** DrumBeatRepo

```js
// Title: Eight note fill
// Category: Punk
setcpm(170 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Eight note fill
setcpm(170 / 4);
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~]*2 ~").bank(kit)
```
</details>

### Quarter note groove variation
**BPM:** 170
**Source:** DrumBeatRepo

```js
// Title: Quarter note groove variation
// Category: Punk
setcpm(170 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Quarter note groove variation
setcpm(170 / 4);
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Quarter note groove
**BPM:** 170
**Source:** DrumBeatRepo

```js
// Title: Quarter note groove
// Category: Punk
setcpm(170 / 4);
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Quarter note groove
setcpm(170 / 4);
const kit = "RolandTR808";

$: s("hh*4").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

---

## Rock

### Rock
**BPM:** 145
**Source:** DrumBeatRepo

```js
// Title: Rock
// Category: Rock
setcpm(145 / 4);
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("hh*4").gain("0.85").bank(bank_hh),
  s("[bd ~]*2 ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock
setcpm(145 / 4);
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("hh*4").gain("0.85").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Rock variation
**BPM:** 145
**Source:** DrumBeatRepo

```js
// Title: Rock variation
// Category: Rock
setcpm(145 / 4);
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_cr = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("cr*4").bank(bank_cr),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rock variation
setcpm(145 / 4);
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("cr*4").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

---

## TB03 Generated Patterns

### TB03_PTN1_01
**Source:** drum-patterns

```js
// Title: TB03_PTN1_01
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ lt] ~ ~ ~").bank(bank_lt),
  s("~ ~ [~ lt ~ ~] ~").bank(bank_lt),
  s("~ ~ [~ ~ sd sd] [sd sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ bd bd ~] bd*4 ~ ~").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_01
const kit = "RolandTR808";

$: s("[~ ~ ~ lt] ~ ~ ~").bank(kit)
$: s("~ ~ [~ lt ~ ~] ~").bank(kit)
$: s("~ ~ [~ ~ sd sd] [sd sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ bd bd ~] bd*4 ~ ~").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN1_02
**Source:** drum-patterns

```js
// Title: TB03_PTN1_02
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ~ ht] ~").bank(bank_ht),
  s("~ ~ [oh ~ ~ ~] ~").bank(bank_oh),
  s("~ [lt ~ ~ ~] ~ ~").bank(bank_lt),
  s("[~ ~ lt ~] ~ ~ ~").bank(bank_lt),
  s("~ [~ ~ cp cp] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[bd ~ ~ ~] [~ bd ~ ~] [~ bd bd ~] [bd bd bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_02
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ ht] ~").bank(kit)
$: s("~ ~ [oh ~ ~ ~] ~").bank(kit)
$: s("~ [lt ~ ~ ~] ~ ~").bank(kit)
$: s("[~ ~ lt ~] ~ ~ ~").bank(kit)
$: s("~ [~ ~ cp cp] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ bd ~ ~] [~ bd bd ~] [bd bd bd ~]").bank(kit)
```
</details>

### TB03_PTN1_03
**Source:** drum-patterns

```js
// Title: TB03_PTN1_03
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ hh ~] ~ [~ ~ ~ hh]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ cp ~] ~").bank(bank_cp),
  s("[~ ~ bd bd] [bd ~ ~ bd] [bd bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_03
const kit = "RolandTR808";

$: s("~ [~ ~ hh ~] ~ [~ ~ ~ hh]").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ cp ~] ~").bank(kit)
$: s("[~ ~ bd bd] [bd ~ ~ bd] [bd bd ~ ~] ~").bank(kit)
```
</details>

### TB03_PTN1_04
**Source:** drum-patterns

```js
// Title: TB03_PTN1_04
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ rd ~ ~]").bank(bank_rd),
  s("[ht ~ ~ ~] [~ ht ~ ~] ~ ~").bank(bank_ht),
  s("[~ ~ lt lt] ~ [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ ~ [~ ~ cp cp]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[~ bd ~ ~] [bd ~ bd bd] [~ ~ bd bd] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_04
const kit = "RolandTR808";

$: s("~ ~ ~ [~ rd ~ ~]").bank(kit)
$: s("[ht ~ ~ ~] [~ ht ~ ~] ~ ~").bank(kit)
$: s("[~ ~ lt lt] ~ [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ cp cp]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ bd ~ ~] [bd ~ bd bd] [~ ~ bd bd] [bd ~ ~ ~]").bank(kit)
```
</details>

### TB03_PTN1_05
**Source:** drum-patterns

```js
// Title: TB03_PTN1_05
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bon = bank_default;
let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd ~ ~ ~] ~ ~ ~").bank(bank_sd),
  s("~ ~ ~ [bon ~ ~ ~]").bank(bank_bon),
  s("~ [cb ~ ~ ~] ~ ~").bank(bank_cb),
  s("~ ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("[~ hh ~ ~] [~ hh ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_05
const kit = "RolandTR808";

$: s("[sd ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [bon ~ ~ ~]").bank(kit)
$: s("~ [cb ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ ht ~] ~").bank(kit)
$: s("[~ hh ~ ~] [~ hh ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] [~ ~ ~ bd]").bank(kit)
```
</details>

### TB03_PTN1_06
**Source:** drum-patterns

```js
// Title: TB03_PTN1_06
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ [~ cr ~ ~] ~").bank(bank_cr),
  s("~ [~ ~ rd ~] ~ ~").bank(bank_rd),
  s("~ [~ ht ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ [~ ~ lt lt] [lt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ ~ cp cp] [cp ~ ~ cp] [cp ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd),
  s("~ ~ ~ [~ ~ ~ x]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_06
const kit = "RolandTR808";

$: s("~ ~ [~ cr ~ ~] ~").bank(kit)
$: s("~ [~ ~ rd ~] ~ ~").bank(kit)
$: s("~ [~ ht ~ ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ lt lt] [lt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ cp cp] [cp ~ ~ cp] [cp ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ x]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_07
**Source:** drum-patterns

```js
// Title: TB03_PTN1_07
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ~ rd] ~").bank(bank_rd),
  s("~ ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("[~ ~ ~ oh] [oh ~ ~ ~] ~ [~ ~ ~ oh]").bank(bank_oh),
  s("~ ~ [lt ~ ~ ~] ~").bank(bank_lt),
  s("[~ ~ cp ~] ~ ~ ~").bank(bank_cp),
  s("[bd bd ~ ~] [~ bd bd bd] [~ bd ~ ~] [bd bd bd ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_07
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ rd] ~").bank(kit)
$: s("~ ~ [~ ~ ht ~] ~").bank(kit)
$: s("[~ ~ ~ oh] [oh ~ ~ ~] ~ [~ ~ ~ oh]").bank(kit)
$: s("~ ~ [lt ~ ~ ~] ~").bank(kit)
$: s("[~ ~ cp ~] ~ ~ ~").bank(kit)
$: s("[bd bd ~ ~] [~ bd bd bd] [~ bd ~ ~] [bd bd bd ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN1_08
**Source:** drum-patterns

```js
// Title: TB03_PTN1_08
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ lt ~] ~ ~").bank(bank_lt),
  s("[bd bd ~ ~] [~ ~ ~ bd] [bd ~ bd bd] bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_08
const kit = "RolandTR808";

$: s("~ [~ ~ lt ~] ~ ~").bank(kit)
$: s("[bd bd ~ ~] [~ ~ ~ bd] [bd ~ bd bd] bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN1_09
**Source:** drum-patterns

```js
// Title: TB03_PTN1_09
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ~] ~ ~ ~").bank(bank_ht),
  s("~ [~ lt lt lt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ [cp cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[~ ~ bd bd] [bd ~ ~ ~] ~ [~ bd bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_09
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ lt lt lt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [cp cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[~ ~ bd bd] [bd ~ ~ ~] ~ [~ bd bd ~]").bank(kit)
```
</details>

### TB03_PTN1_10
**Source:** drum-patterns

```js
// Title: TB03_PTN1_10
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [~ ~ ~ rd]").bank(bank_rd),
  s("~ ~ ~ [~ ht ht ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [cp ~ ~ ~]").bank(bank_cp),
  s("[~ bd bd ~] bd*4 [~ ~ ~ bd] ~").gain("1.0 0.8").bank(bank_bd),
  s("~ ~ [~ ~ x ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_10
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ rd]").bank(kit)
$: s("~ ~ ~ [~ ht ht ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [cp ~ ~ ~]").bank(kit)
$: s("[~ bd bd ~] bd*4 [~ ~ ~ bd] ~").gain("1.0 0.8").bank(kit)
$: s("~ ~ [~ ~ x ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_11
**Source:** drum-patterns

```js
// Title: TB03_PTN1_11
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ ht]").bank(bank_ht),
  s("~ [oh ~ ~ ~] ~ ~").bank(bank_oh),
  s("~ [~ cp ~ ~] [cp cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("bd*4 [~ ~ ~ bd] [~ ~ ~ bd] [bd ~]*2").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_11
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ ht]").bank(kit)
$: s("~ [oh ~ ~ ~] ~ ~").bank(kit)
$: s("~ [~ cp ~ ~] [cp cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4 [~ ~ ~ bd] [~ ~ ~ bd] [bd ~]*2").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN1_12
**Source:** drum-patterns

```js
// Title: TB03_PTN1_12
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] ~ ~ [ht ~ ~ ~]").bank(bank_ht),
  s("[~ ~ ~ oh] ~ ~ ~").bank(bank_oh),
  s("~ [~ ~ ~ hh] [~ ~ hh ~] ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ lt ~ ~]").bank(bank_lt),
  s("[cp ~ ~ ~] [~ ~ cp ~] ~ ~").bank(bank_cp),
  s("[~ bd ~ ~] ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_12
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ ~ [ht ~ ~ ~]").bank(kit)
$: s("[~ ~ ~ oh] ~ ~ ~").bank(kit)
$: s("~ [~ ~ ~ hh] [~ ~ hh ~] ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ lt ~ ~]").bank(kit)
$: s("[cp ~ ~ ~] [~ ~ cp ~] ~ ~").bank(kit)
$: s("[~ bd ~ ~] ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### TB03_PTN1_13
**Source:** drum-patterns

```js
// Title: TB03_PTN1_13
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ht ~ ~]").bank(bank_ht),
  s("~ ~ [~ lt lt ~] [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("cp*4 [cp ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ [~ bd bd bd] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_13
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ht ~ ~]").bank(kit)
$: s("~ ~ [~ lt lt ~] [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("cp*4 [cp ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ bd bd bd] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### TB03_PTN1_14
**Source:** drum-patterns

```js
// Title: TB03_PTN1_14
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ sd ~ ~] ~ ~ ~").bank(bank_sd),
  s("~ ~ [~ ht ~ ~] ~").bank(bank_ht),
  s("[lt ~ ~ ~] [~ ~ lt ~] [lt ~ ~ ~] [~ lt]*2").bank(bank_lt),
  s("~ [~ bd]*2 [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_14
const kit = "RolandTR808";

$: s("[~ sd ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ht ~ ~] ~").bank(kit)
$: s("[lt ~ ~ ~] [~ ~ lt ~] [lt ~ ~ ~] [~ lt]*2").bank(kit)
$: s("~ [~ bd]*2 [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### TB03_PTN1_15
**Source:** drum-patterns

```js
// Title: TB03_PTN1_15
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ lt]*2 [lt ~ ~ ~] ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ cp ~ ~] cp*4 ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[bd ~]*2 [~ ~ bd bd] ~ [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_15
const kit = "RolandTR808";

$: s("~ ~ ~ [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ lt]*2 [lt ~ ~ ~] ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ cp ~ ~] cp*4 ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 [~ ~ bd bd] ~ [~ bd ~ ~]").bank(kit)
```
</details>

### TB03_PTN1_16
**Source:** drum-patterns

```js
// Title: TB03_PTN1_16
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[~ oh]*2 ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ ~ lt] ~ ~").bank(bank_lt),
  s("[bd ~ ~ ~] [~ bd bd ~] [bd ~ bd bd] [bd ~ bd bd]").gain("1.0 0.8").bank(bank_bd),
  s("[~ ~ x ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_16
const kit = "RolandTR808";

$: s("[~ oh]*2 ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("~ [~ ~ ~ lt] ~ ~").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] [bd ~ bd bd] [bd ~ bd bd]").gain("1.0 0.8").bank(kit)
$: s("[~ ~ x ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_17
**Source:** drum-patterns

```js
// Title: TB03_PTN1_17
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ [~ ~ sd ~] ~ ~").bank(bank_sd),
  s("[~ oh]*2 [oh oh ~ ~] ~ ~").bank(bank_oh),
  s("~ ~ ~ hh*4").gain("0.85").bank(bank_hh),
  s("~ [~ ~ ~ cp] [cp cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd),
  s("[~ ~ x ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_17
const kit = "RolandTR808";

$: s("~ [~ ~ sd ~] ~ ~").bank(kit)
$: s("[~ oh]*2 [oh oh ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ hh*4").gain("0.85").bank(kit)
$: s("~ [~ ~ ~ cp] [cp cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
$: s("[~ ~ x ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_18
**Source:** drum-patterns

```js
// Title: TB03_PTN1_18
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ~] ~ ~ ~").bank(bank_ht),
  s("~ [~ ~ hh hh] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ lt] ~").bank(bank_lt),
  s("[~ lt lt lt] [lt ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ bd ~ ~] [bd bd bd ~] [~ bd bd bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_18
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ ~ hh hh] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ lt] ~").bank(kit)
$: s("[~ lt lt lt] [lt ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ bd ~ ~] [bd bd bd ~] [~ bd bd bd]").bank(kit)
```
</details>

### TB03_PTN1_19
**Source:** drum-patterns

```js
// Title: TB03_PTN1_19
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [~ cr ~ ~]").bank(bank_cr),
  s("~ [ht ~ ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ [~ lt ~ ~] [~ ~ ~ lt]").bank(bank_lt),
  s("[bd ~ bd bd] [~ bd bd bd] [~ ~ bd bd] [bd ~ ~ ~]").gain("1.0 0.8").bank(bank_bd),
  s("~ ~ [x ~ ~ ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_19
const kit = "RolandTR808";

$: s("~ ~ ~ [~ cr ~ ~]").bank(kit)
$: s("~ [ht ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [~ lt ~ ~] [~ ~ ~ lt]").bank(kit)
$: s("[bd ~ bd bd] [~ bd bd bd] [~ ~ bd bd] [bd ~ ~ ~]").gain("1.0 0.8").bank(kit)
$: s("~ ~ [x ~ ~ ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_20
**Source:** drum-patterns

```js
// Title: TB03_PTN1_20
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [ht ~ ~ ~]").bank(bank_ht),
  s("[~ oh ~ ~] [~ oh ~ ~] ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[~ ~ bd ~] [~ ~ ~ bd] bd*4 [~ bd bd ~]").gain("1.0 0.8").bank(bank_bd),
  s("~ [x ~ ~ ~] ~ ~").note(bass_key).octave(bass_octave).transpose(3).decay(0.2).sustain(0).sound(bass_synth),
  s("[x ~ ~ ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_20
const kit = "RolandTR808";

$: s("~ ~ ~ [ht ~ ~ ~]").bank(kit)
$: s("[~ oh ~ ~] [~ oh ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ lt]").bank(kit)
$: s("[~ ~ bd ~] [~ ~ ~ bd] bd*4 [~ bd bd ~]").gain("1.0 0.8").bank(kit)
$: s("~ [x ~ ~ ~] ~ ~").note("c").octave(1).transpose(3).decay(0.2).sustain(0).sound("sawtooth")
$: s("[x ~ ~ ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_21
**Source:** drum-patterns

```js
// Title: TB03_PTN1_21
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] ~ ~ ~").bank(bank_ht),
  s("[~ ~ ~ sd] ~ ~ ~").bank(bank_sd),
  s("~ ~ [~ ~ cp ~] ~").bank(bank_cp),
  s("[bd bd ~ ~] [bd ~ ~ ~] ~ bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_21
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ ~ ~").bank(kit)
$: s("[~ ~ ~ sd] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ cp ~] ~").bank(kit)
$: s("[bd bd ~ ~] [bd ~ ~ ~] ~ bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN1_22
**Source:** drum-patterns

```js
// Title: TB03_PTN1_22
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_hc = bank_default;
let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ~ hc] ~").bank(bank_hc),
  s("~ ~ ~ [~ ~ ht ~]").bank(bank_ht),
  s("~ [~ ~ hh hh] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [cp ~ ~ ~]").bank(bank_cp),
  s("[~ bd bd bd] [bd ~ ~ ~] [~ ~ bd ~] [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_22
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ hc] ~").bank(kit)
$: s("~ ~ ~ [~ ~ ht ~]").bank(kit)
$: s("~ [~ ~ hh hh] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [cp ~ ~ ~]").bank(kit)
$: s("[~ bd bd bd] [bd ~ ~ ~] [~ ~ bd ~] [~ bd]*2").bank(kit)
```
</details>

### TB03_PTN1_23
**Source:** drum-patterns

```js
// Title: TB03_PTN1_23
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [~ ~ ~ ht]").bank(bank_ht),
  s("~ ~ [~ lt lt lt] [lt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [~ bd ~ ~]").bank(bank_bd),
  s("~ [~ ~ ~ x] ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_23
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ ht]").bank(kit)
$: s("~ ~ [~ lt lt lt] [lt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [~ bd ~ ~]").bank(kit)
$: s("~ [~ ~ ~ x] ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_24
**Source:** drum-patterns

```js
// Title: TB03_PTN1_24
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ sd ~ ~] ~ ~").bank(bank_sd),
  s("~ ~ ~ [~ ~ ~ ht]").bank(bank_ht),
  s("~ [oh ~]*2 ~ [~ oh oh ~]").bank(bank_oh),
  s("~ ~ [~ ~ ~ hh] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[lt ~]*2 ~ [~ lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ ~ ~ cp] ~ ~").bank(bank_cp),
  s("[~ ~ ~ bd] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_24
const kit = "RolandTR808";

$: s("~ [~ sd ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ ht]").bank(kit)
$: s("~ [oh ~]*2 ~ [~ oh oh ~]").bank(kit)
$: s("~ ~ [~ ~ ~ hh] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[lt ~]*2 ~ [~ lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ ~ cp] ~ ~").bank(kit)
$: s("[~ ~ ~ bd] ~ ~ ~").bank(kit)
```
</details>

### TB03_PTN2_01
**Source:** drum-patterns

```js
// Title: TB03_PTN2_01
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ht ~ ~] ~ ~").bank(bank_ht),
  s("bd*4 [bd ~ bd bd] [~ ~ bd bd] bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_01
const kit = "RolandTR808";

$: s("~ [~ ht ~ ~] ~ ~").bank(kit)
$: s("bd*4 [bd ~ bd bd] [~ ~ bd bd] bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN2_02
**Source:** drum-patterns

```js
// Title: TB03_PTN2_02
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ht] ~ [~ ht]*2 [ht ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [lt ~]*2 ~").bank(bank_lt),
  s("[~ ~ bd ~] [bd bd ~ bd] ~ [~ bd bd bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_02
const kit = "RolandTR808";

$: s("[ht ~ ~ ht] ~ [~ ht]*2 [ht ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [lt ~]*2 ~").bank(kit)
$: s("[~ ~ bd ~] [bd bd ~ bd] ~ [~ bd bd bd]").bank(kit)
```
</details>

### TB03_PTN2_03
**Source:** drum-patterns

```js
// Title: TB03_PTN2_03
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ rd ~ ~] ~ ~").bank(bank_rd),
  s("[~ ~ ht ht] [~ ~ ~ ht] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[oh oh ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("~ [~ ~ cp ~] ~ ~").bank(bank_cp),
  s("~ [bd ~ ~ ~] bd*4 [bd bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_03
const kit = "RolandTR808";

$: s("~ [~ rd ~ ~] ~ ~").bank(kit)
$: s("[~ ~ ht ht] [~ ~ ~ ht] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[oh oh ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("~ [~ ~ cp ~] ~ ~").bank(kit)
$: s("~ [bd ~ ~ ~] bd*4 [bd bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN2_04
**Source:** drum-patterns

```js
// Title: TB03_PTN2_04
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ ht] [~ ht ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ ~ [oh oh oh ~]").bank(bank_oh),
  s("~ [lt ~ lt lt] [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~]*2 ~ [~ ~ bd bd] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_04
const kit = "RolandTR808";

$: s("[~ ~ ~ ht] [~ ht ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [oh oh oh ~]").bank(kit)
$: s("~ [lt ~ lt lt] [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd bd] [~ ~ ~ bd]").bank(kit)
```
</details>

### TB03_PTN2_05
**Source:** drum-patterns

```js
// Title: TB03_PTN2_05
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_hc = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[hc ~ ~ ~] ~ ~ ~").bank(bank_hc),
  s("~ ~ [~ ~ ~ oh] [~ oh ~ ~]").bank(bank_oh),
  s("~ [hh ~ ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ lt ~] [~ lt lt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ cp ~ ~] ~ ~ ~").bank(bank_cp),
  s("[~ ~ ~ bd] ~ [bd bd ~ ~] ~").bank(bank_bd),
  s("~ ~ ~ [x ~ ~ ~]").note(bass_key).octave(bass_octave).transpose(2).decay(0.2).sustain(0).sound(bass_synth),
  s("~ ~ ~ [~ ~ x ~]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_05
const kit = "RolandTR808";

$: s("[hc ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ ~ oh] [~ oh ~ ~]").bank(kit)
$: s("~ [hh ~ ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ lt ~] [~ lt lt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ cp ~ ~] ~ ~ ~").bank(kit)
$: s("[~ ~ ~ bd] ~ [bd bd ~ ~] ~").bank(kit)
$: s("~ ~ ~ [x ~ ~ ~]").note("c").octave(1).transpose(2).decay(0.2).sustain(0).sound("sawtooth")
$: s("~ ~ ~ [~ ~ x ~]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN2_06
**Source:** drum-patterns

```js
// Title: TB03_PTN2_06
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ lt ~] ~ ~ ~").bank(bank_lt),
  s("[lt ~ ~ ~] ~ ~ ~").bank(bank_lt),
  s("[~ bd]*2 [bd bd ~ bd] [bd bd ~ ~] [~ bd bd ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_06
const kit = "RolandTR808";

$: s("[~ ~ lt ~] ~ ~ ~").bank(kit)
$: s("[lt ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[~ bd]*2 [bd bd ~ bd] [bd bd ~ ~] [~ bd bd ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN2_07
**Source:** drum-patterns

```js
// Title: TB03_PTN2_07
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ hh] [hh ~ ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ cp cp]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[bd bd ~ ~] ~ [bd bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_07
const kit = "RolandTR808";

$: s("[~ ~ ~ hh] [hh ~ ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ cp cp]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ ~] ~ [bd bd bd ~] ~").bank(kit)
```
</details>

### TB03_PTN2_08
**Source:** drum-patterns

```js
// Title: TB03_PTN2_08
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [lt ~ ~ ~] ~").bank(bank_lt),
  s("~ [cp ~ ~ ~] ~ ~").bank(bank_cp),
  s("~ [~ ~ ~ bd] [~ bd ~ ~] [~ bd bd bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_08
const kit = "RolandTR808";

$: s("~ ~ [lt ~ ~ ~] ~").bank(kit)
$: s("~ [cp ~ ~ ~] ~ ~").bank(kit)
$: s("~ [~ ~ ~ bd] [~ bd ~ ~] [~ bd bd bd]").bank(kit)
```
</details>

### TB03_PTN2_09
**Source:** drum-patterns

```js
// Title: TB03_PTN2_09
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ lt ~] [~ ~ lt ~]").bank(bank_lt),
  s("[~ ~ lt ~] ~ ~ ~").bank(bank_lt),
  s("[bd bd ~ ~] [bd bd ~ ~] [~ bd ~ ~] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_09
const kit = "RolandTR808";

$: s("~ ~ [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ lt ~] [~ ~ lt ~]").bank(kit)
$: s("[~ ~ lt ~] ~ ~ ~").bank(kit)
$: s("[bd bd ~ ~] [bd bd ~ ~] [~ bd ~ ~] [~ ~ ~ bd]").bank(kit)
```
</details>

### TB03_PTN2_10
**Source:** drum-patterns

```js
// Title: TB03_PTN2_10
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[~ ~ rd ~] ~ ~ ~").bank(bank_rd),
  s("[~ ht ~ ~] ~ [~ ~ ~ ht] [~ ~ ~ ht]").bank(bank_ht),
  s("[oh ~ ~ ~] [~ ~ ~ oh] [oh oh ~ ~] ~").bank(bank_oh),
  s("[~ ~ ~ cp] [cp ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ ~ [~ ~ bd ~] [bd ~]*2").bank(bank_bd),
  s("~ [~ x ~ ~] ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_10
const kit = "RolandTR808";

$: s("[~ ~ rd ~] ~ ~ ~").bank(kit)
$: s("[~ ht ~ ~] ~ [~ ~ ~ ht] [~ ~ ~ ht]").bank(kit)
$: s("[oh ~ ~ ~] [~ ~ ~ oh] [oh oh ~ ~] ~").bank(kit)
$: s("[~ ~ ~ cp] [cp ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ bd ~] [bd ~]*2").bank(kit)
$: s("~ [~ x ~ ~] ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN2_11
**Source:** drum-patterns

```js
// Title: TB03_PTN2_11
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_bon = bank_default;
let bank_cb = bank_default;
let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[bon ~ ~ ~] ~ ~ ~").bank(bank_bon),
  s("~ ~ ~ [~ cb ~ ~]").bank(bank_cb),
  s("~ [~ ~ rd ~] ~ ~").bank(bank_rd),
  s("[~ ht ~ ~] ~ ~ ~").bank(bank_ht),
  s("~ ~ [~ ~ hh hh] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("~ [~ cp]*2 [cp cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[~ ~ bd bd] [bd ~ ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_11
const kit = "RolandTR808";

$: s("[bon ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ cb ~ ~]").bank(kit)
$: s("~ [~ ~ rd ~] ~ ~").bank(kit)
$: s("[~ ht ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ hh hh] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("~ [~ cp]*2 [cp cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd bd] [bd ~ ~ ~] ~ ~").bank(kit)
```
</details>

### TB03_PTN2_12
**Source:** drum-patterns

```js
// Title: TB03_PTN2_12
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("~ [~ oh oh oh] ~ ~").bank(bank_oh),
  s("[lt ~ ~ ~] ~ [~ ~ lt ~] [~ lt ~ ~]").bank(bank_lt),
  s("[~ bd bd bd] ~ [~ bd ~ ~] [~ ~ bd bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_12
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("~ [~ oh oh oh] ~ ~").bank(kit)
$: s("[lt ~ ~ ~] ~ [~ ~ lt ~] [~ lt ~ ~]").bank(kit)
$: s("[~ bd bd bd] ~ [~ bd ~ ~] [~ ~ bd bd]").bank(kit)
```
</details>

### TB03_PTN2_13
**Source:** drum-patterns

```js
// Title: TB03_PTN2_13
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [oh ~ ~ ~]").bank(bank_oh),
  s("~ [~ ~ ~ hh] ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ [lt lt lt ~] [~ lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ ~ [~ cp ~ ~]").bank(bank_cp),
  s("bd*4 ~ [~ ~ ~ bd] ~").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_13
const kit = "RolandTR808";

$: s("~ ~ ~ [oh ~ ~ ~]").bank(kit)
$: s("~ [~ ~ ~ hh] ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ [lt lt lt ~] [~ lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ cp ~ ~]").bank(kit)
$: s("bd*4 ~ [~ ~ ~ bd] ~").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN2_14
**Source:** drum-patterns

```js
// Title: TB03_PTN2_14
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] [~ ~ ht ~] ~ ~").bank(bank_ht),
  s("[~ lt ~ ~] ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("~ [~ ~ ~ cp] cp*4 ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[bd ~ ~ bd] [~ bd ~ ~] ~ [bd bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_14
const kit = "RolandTR808";

$: s("[~ ~ ht ~] [~ ~ ht ~] ~ ~").bank(kit)
$: s("[~ lt ~ ~] ~ ~ [~ ~ lt ~]").bank(kit)
$: s("~ [~ ~ ~ cp] cp*4 ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ bd ~ ~] ~ [bd bd ~ ~]").bank(kit)
```
</details>

### TB03_PTN2_15
**Source:** drum-patterns

```js
// Title: TB03_PTN2_15
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ [~ ~ ~ lt] ~ ~").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ sd]").bank(bank_sd),
  s("[bd bd ~ bd] [bd bd bd ~] [bd bd bd ~] [bd bd ~ ~]").gain("1.0 0.8").bank(bank_bd),
  s("[~ ~ x ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_15
const kit = "RolandTR808";

$: s("~ [~ ~ ~ lt] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ sd]").bank(kit)
$: s("[bd bd ~ bd] [bd bd bd ~] [bd bd bd ~] [bd bd ~ ~]").gain("1.0 0.8").bank(kit)
$: s("[~ ~ x ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN2_16
**Source:** drum-patterns

```js
// Title: TB03_PTN2_16
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] ~ ~ ~").bank(bank_oh),
  s("~ [~ lt lt ~] ~ [~ ~ ~ lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd bd bd ~] [~ ~ ~ bd] bd*4 [bd bd bd ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_16
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] ~ ~ ~").bank(kit)
$: s("~ [~ lt lt ~] ~ [~ ~ ~ lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd bd ~] [~ ~ ~ bd] bd*4 [bd bd bd ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN2_17
**Source:** drum-patterns

```js
// Title: TB03_PTN2_17
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ cb ~] ~").bank(bank_cb),
  s("[~ ht ~ ~] ~ ~ ~").bank(bank_ht),
  s("~ ~ [~ hh]*2 [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ cp cp ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[bd ~]*2 ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_17
const kit = "RolandTR808";

$: s("~ ~ [~ ~ cb ~] ~").bank(kit)
$: s("[~ ht ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ hh]*2 [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ cp cp ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### TB03_PTN2_18
**Source:** drum-patterns

```js
// Title: TB03_PTN2_18
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [ht ~ ~ ~] ~ ~").bank(bank_ht),
  s("[~ ~ ~ oh] ~ ~ [~ ~ ~ oh]").bank(bank_oh),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[cp cp cp ~] ~ [cp ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ [~ bd bd bd] [~ bd bd bd] [bd bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_18
const kit = "RolandTR808";

$: s("~ [ht ~ ~ ~] ~ ~").bank(kit)
$: s("[~ ~ ~ oh] ~ ~ [~ ~ ~ oh]").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[cp cp cp ~] ~ [cp ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ bd bd bd] [~ bd bd bd] [bd bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN2_19
**Source:** drum-patterns

```js
// Title: TB03_PTN2_19
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[ht ~ ~ ~] [ht ~ ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ [~ ~ hh hh] ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ bd ~ ~] ~ [~ bd ~ ~]").bank(bank_bd),
  s("[~ x ~ ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_19
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] [ht ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ hh hh] ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ bd ~ ~] ~ [~ bd ~ ~]").bank(kit)
$: s("[~ x ~ ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN2_20
**Source:** drum-patterns

```js
// Title: TB03_PTN2_20
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ rd ~ ~] ~ ~").bank(bank_rd),
  s("~ ~ ~ [~ ht ~ ~]").bank(bank_ht),
  s("[~ lt lt ~] ~ ~ [~ ~ ~ lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ [~ lt ~ ~] ~").bank(bank_lt),
  s("~ [cp ~]*2 ~ ~").bank(bank_cp),
  s("~ ~ [~ ~ sd ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ [bd ~]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_20
const kit = "RolandTR808";

$: s("~ [~ rd ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ht ~ ~]").bank(kit)
$: s("[~ lt lt ~] ~ ~ [~ ~ ~ lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ lt ~ ~] ~").bank(kit)
$: s("~ [cp ~]*2 ~ ~").bank(kit)
$: s("~ ~ [~ ~ sd ~] ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ [bd ~]*2").bank(kit)
```
</details>

### TB03_PTN2_21
**Source:** drum-patterns

```js
// Title: TB03_PTN2_21
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ [~ lt ~ ~] [~ ~ lt ~] ~").bank(bank_lt),
  s("bd*4 [bd ~ ~ ~] ~ ~").gain("1.0 0.8").bank(bank_bd),
  s("~ ~ ~ [~ ~ x ~]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_21
const kit = "RolandTR808";

$: s("~ ~ ~ [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ [~ lt ~ ~] [~ ~ lt ~] ~").bank(kit)
$: s("bd*4 [bd ~ ~ ~] ~ ~").gain("1.0 0.8").bank(kit)
$: s("~ ~ ~ [~ ~ x ~]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN2_22
**Source:** drum-patterns

```js
// Title: TB03_PTN2_22
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ht] ~ [~ ~ ht ~] [~ ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ oh ~] [~ oh ~ ~] [oh ~ ~ ~]").bank(bank_oh),
  s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(bank_hh),
  s("[bd bd ~ ~] [~ bd ~ ~] [bd ~ ~ ~] [~ ~ bd bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_22
const kit = "RolandTR808";

$: s("[~ ~ ht ht] ~ [~ ~ ht ~] [~ ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ oh ~] [~ oh ~ ~] [oh ~ ~ ~]").bank(kit)
$: s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(kit)
$: s("[bd bd ~ ~] [~ bd ~ ~] [bd ~ ~ ~] [~ ~ bd bd]").bank(kit)
```
</details>

### TB03_PTN2_23
**Source:** drum-patterns

```js
// Title: TB03_PTN2_23
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("~ [~ cp cp ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ [~ ~ ~ bd] bd*4 [bd bd ~ bd]").gain("1.0 0.8").bank(bank_bd),
  s("~ [x ~ ~ ~] ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_23
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("~ [~ cp cp ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ ~ bd] bd*4 [bd bd ~ bd]").gain("1.0 0.8").bank(kit)
$: s("~ [x ~ ~ ~] ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN2_24
**Source:** drum-patterns

```js
// Title: TB03_PTN2_24
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ [~ ~ ~ ht] ~").bank(bank_ht),
  s("~ [~ oh ~ ~] ~ ~").bank(bank_oh),
  s("~ [~ ~ ~ hh] [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [lt lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("bd*4 [bd ~ ~ ~] [~ ~ bd ~] ~").gain("1.0 0.8").bank(bank_bd),
  s("~ ~ [~ x ~ ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_24
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ ht] ~").bank(kit)
$: s("~ [~ oh ~ ~] ~ ~").bank(kit)
$: s("~ [~ ~ ~ hh] [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [lt lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4 [bd ~ ~ ~] [~ ~ bd ~] ~").gain("1.0 0.8").bank(kit)
$: s("~ ~ [~ x ~ ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_01
**Source:** drum-patterns

```js
// Title: TB03_PTN3_01
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ht ~ ~] ~").bank(bank_ht),
  s("bd*4 [bd bd ~ ~] [~ ~ bd bd] [~ ~ bd bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_01
const kit = "RolandTR808";

$: s("~ ~ [~ ht ~ ~] ~").bank(kit)
$: s("bd*4 [bd bd ~ ~] [~ ~ bd bd] [~ ~ bd bd]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN3_02
**Source:** drum-patterns

```js
// Title: TB03_PTN3_02
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ht ~] [ht ~]*2").bank(bank_ht),
  s("~ ~ [~ ~ ~ oh] ~").bank(bank_oh),
  s("[~ ~ ~ lt] ~ ~ ~").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ cp]").bank(bank_cp),
  s("[bd bd bd ~] [bd ~ ~ ~] [~ bd ~ ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_02
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ht ~] [ht ~]*2").bank(kit)
$: s("~ ~ [~ ~ ~ oh] ~").bank(kit)
$: s("[~ ~ ~ lt] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ cp]").bank(kit)
$: s("[bd bd bd ~] [bd ~ ~ ~] [~ bd ~ ~] [~ bd ~ ~]").bank(kit)
```
</details>

### TB03_PTN3_03
**Source:** drum-patterns

```js
// Title: TB03_PTN3_03
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ oh ~ ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("[~ lt ~ ~] [~ ~ ~ lt] ~ ~").bank(bank_lt),
  s("~ ~ [~ ~ ~ cp] ~").bank(bank_cp),
  s("[bd ~ bd bd] ~ [bd ~ ~ ~] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_03
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ oh ~ ~] ~ [~ ~ oh ~]").bank(kit)
$: s("[~ lt ~ ~] [~ ~ ~ lt] ~ ~").bank(kit)
$: s("~ ~ [~ ~ ~ cp] ~").bank(kit)
$: s("[bd ~ bd bd] ~ [bd ~ ~ ~] [~ ~ ~ bd]").bank(kit)
```
</details>

### TB03_PTN3_04
**Source:** drum-patterns

```js
// Title: TB03_PTN3_04
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [ht ~ ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[~ hh ~ ~] [~ ~ ~ hh] ~ ~").gain("0.85").bank(bank_hh),
  s("~ [~ ~ lt ~] ~ ~").bank(bank_lt),
  s("[~ ~ ~ bd] [~ bd ~ ~] ~ bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_04
const kit = "RolandTR808";

$: s("~ [ht ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ oh ~] ~").bank(kit)
$: s("[~ hh ~ ~] [~ ~ ~ hh] ~ ~").gain("0.85").bank(kit)
$: s("~ [~ ~ lt ~] ~ ~").bank(kit)
$: s("[~ ~ ~ bd] [~ bd ~ ~] ~ bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN3_05
**Source:** drum-patterns

```js
// Title: TB03_PTN3_05
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ [~ rd ~ ~] ~ ~").bank(bank_rd),
  s("~ [~ ~ ~ oh] oh*4 [oh ~ ~ ~]").bank(bank_oh),
  s("[~ ~ lt ~] ~ ~ ~").bank(bank_lt),
  s("[~ bd]*2 [bd ~]*2 ~ [~ bd ~ ~]").bank(bank_bd),
  s("[x ~ ~ ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_05
const kit = "RolandTR808";

$: s("~ [~ rd ~ ~] ~ ~").bank(kit)
$: s("~ [~ ~ ~ oh] oh*4 [oh ~ ~ ~]").bank(kit)
$: s("[~ ~ lt ~] ~ ~ ~").bank(kit)
$: s("[~ bd]*2 [bd ~]*2 ~ [~ bd ~ ~]").bank(kit)
$: s("[x ~ ~ ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_06
**Source:** drum-patterns

```js
// Title: TB03_PTN3_06
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[~ ~ ht ~] [~ ht ~ ~] ~ [~ ht ~ ~]").bank(bank_ht),
  s("~ ~ ~ [oh ~ ~ ~]").bank(bank_oh),
  s("~ [~ ~ lt ~] ~ ~").bank(bank_lt),
  s("[bd bd ~ bd] [bd ~ ~ ~] [~ bd bd ~] [~ ~ bd bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_06
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[~ ~ ht ~] [~ ht ~ ~] ~ [~ ht ~ ~]").bank(kit)
$: s("~ ~ ~ [oh ~ ~ ~]").bank(kit)
$: s("~ [~ ~ lt ~] ~ ~").bank(kit)
$: s("[bd bd ~ bd] [bd ~ ~ ~] [~ bd bd ~] [~ ~ bd bd]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN3_07
**Source:** drum-patterns

```js
// Title: TB03_PTN3_07
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] [~ ~ ~ ht] [~ ~ ht ~] [~ ~ ht ht]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ [~ lt ~ ~] ~ ~").bank(bank_lt),
  s("[~ bd]*2 [~ ~ bd ~] [bd bd ~ bd] [bd bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_07
const kit = "RolandTR808";

$: s("[~ ~ ht ~] [~ ~ ~ ht] [~ ~ ht ~] [~ ~ ht ht]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ lt ~ ~] ~ ~").bank(kit)
$: s("[~ bd]*2 [~ ~ bd ~] [bd bd ~ bd] [bd bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN3_08
**Source:** drum-patterns

```js
// Title: TB03_PTN3_08
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ~] [~ ~ ~ ht] ~ ~").bank(bank_ht),
  s("~ [lt ~ ~ ~] [lt ~ ~ ~] ~").bank(bank_lt),
  s("[~ ~ ~ cp] ~ ~ ~").bank(bank_cp),
  s("[~ bd bd ~] [~ bd bd ~] ~ [bd bd bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_08
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] [~ ~ ~ ht] ~ ~").bank(kit)
$: s("~ [lt ~ ~ ~] [lt ~ ~ ~] ~").bank(kit)
$: s("[~ ~ ~ cp] ~ ~ ~").bank(kit)
$: s("[~ bd bd ~] [~ bd bd ~] ~ [bd bd bd ~]").bank(kit)
```
</details>

### TB03_PTN3_09
**Source:** drum-patterns

```js
// Title: TB03_PTN3_09
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh oh oh ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ lt] ~ ~ ~").bank(bank_lt),
  s("~ [bd bd bd ~] [~ bd bd bd] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_09
const kit = "RolandTR808";

$: s("[oh oh oh ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ ~ lt] ~ ~ ~").bank(kit)
$: s("~ [bd bd bd ~] [~ bd bd bd] [bd ~ ~ ~]").bank(kit)
```
</details>

### TB03_PTN3_10
**Source:** drum-patterns

```js
// Title: TB03_PTN3_10
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ hh ~] ~ ~").gain("0.85").bank(bank_hh),
  s("[~ bd bd bd] [~ bd ~ ~] [bd ~ ~ bd] bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_10
const kit = "RolandTR808";

$: s("~ [~ ~ hh ~] ~ ~").gain("0.85").bank(kit)
$: s("[~ bd bd bd] [~ bd ~ ~] [bd ~ ~ bd] bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN3_11
**Source:** drum-patterns

```js
// Title: TB03_PTN3_11
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[~ ~ ht ~] ~ ~ ~").bank(bank_ht),
  s("[~ ~ ~ oh] [oh ~ ~ ~] ~ [oh ~ ~ ~]").bank(bank_oh),
  s("~ ~ [hh ~ ~ hh] ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[bd bd ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd),
  s("~ ~ [~ x ~ ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_11
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ ~ ~").bank(kit)
$: s("[~ ~ ~ oh] [oh ~ ~ ~] ~ [oh ~ ~ ~]").bank(kit)
$: s("~ ~ [hh ~ ~ hh] ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ ~ lt]").bank(kit)
$: s("[bd bd ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
$: s("~ ~ [~ x ~ ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_12
**Source:** drum-patterns

```js
// Title: TB03_PTN3_12
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[~ ht ~ ~] ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("~ ~ [~ oh ~ ~] ~").bank(bank_oh),
  s("~ [~ ~ ~ hh] ~ ~").gain("0.85").bank(bank_hh),
  s("~ [~ lt ~ ~] ~ [lt ~ ~ ~]").bank(bank_lt),
  s("[~ ~ bd bd] [bd ~ ~ ~] [~ ~ ~ bd] [~ bd bd bd]").bank(bank_bd),
  s("[x ~ ~ ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_12
const kit = "RolandTR808";

$: s("[~ ht ~ ~] ~ [~ ~ ht ~] ~").bank(kit)
$: s("~ ~ [~ oh ~ ~] ~").bank(kit)
$: s("~ [~ ~ ~ hh] ~ ~").gain("0.85").bank(kit)
$: s("~ [~ lt ~ ~] ~ [lt ~ ~ ~]").bank(kit)
$: s("[~ ~ bd bd] [bd ~ ~ ~] [~ ~ ~ bd] [~ bd bd bd]").bank(kit)
$: s("[x ~ ~ ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_13
**Source:** drum-patterns

```js
// Title: TB03_PTN3_13
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ lt] ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ lt ~ ~] ~ ~ ~").bank(bank_lt),
  s("~ [~ bd bd ~] [bd bd ~ bd] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_13
const kit = "RolandTR808";

$: s("~ [~ ~ ~ lt] ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ lt ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ bd bd ~] [bd bd ~ bd] [bd ~ ~ ~]").bank(kit)
```
</details>

### TB03_PTN3_14
**Source:** drum-patterns

```js
// Title: TB03_PTN3_14
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] ~ [~ ht ~ ~] [~ ht ht ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [~ ~ ~ lt] [lt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ ~ ~ lt] ~ ~ ~").bank(bank_lt),
  s("[bd bd ~ ~] [~ bd bd bd] [bd ~]*2 [~ ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_14
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ [~ ht ~ ~] [~ ht ht ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ ~ lt] [lt ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ lt] ~ ~ ~").bank(kit)
$: s("[bd bd ~ ~] [~ bd bd bd] [bd ~]*2 [~ ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN3_15
**Source:** drum-patterns

```js
// Title: TB03_PTN3_15
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[~ ~ ht ~] ~ ~ ~").bank(bank_ht),
  s("~ ~ [~ lt lt lt] [~ lt lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd bd ~ bd] [bd bd ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_15
const kit = "RolandTR808";

$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[~ ~ ht ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ lt lt lt] [~ lt lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ bd] [bd bd ~ ~] ~ ~").bank(kit)
```
</details>

### TB03_PTN3_16
**Source:** drum-patterns

```js
// Title: TB03_PTN3_16
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [~ ~ ht ~]").bank(bank_ht),
  s("~ [lt ~ ~ ~] [~ lt lt lt] [~ ~ ~ lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ bd bd bd] [~ bd bd bd] [bd ~ ~ ~] [~ bd ~ ~]").gain("1.0 0.8").bank(bank_bd),
  s("[x ~ ~ ~] ~ ~ [x ~ ~ ~]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_16
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ht ~]").bank(kit)
$: s("~ [lt ~ ~ ~] [~ lt lt lt] [~ ~ ~ lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ bd bd bd] [~ bd bd bd] [bd ~ ~ ~] [~ bd ~ ~]").gain("1.0 0.8").bank(kit)
$: s("[x ~ ~ ~] ~ ~ [x ~ ~ ~]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_17
**Source:** drum-patterns

```js
// Title: TB03_PTN3_17
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [ht ht ht ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ [~ oh oh oh] [~ ~ ~ oh]").bank(bank_oh),
  s("[bd bd ~ bd] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(bank_bd),
  s("[~ ~ x ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_17
const kit = "RolandTR808";

$: s("~ ~ ~ [ht ht ht ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ oh oh oh] [~ ~ ~ oh]").bank(kit)
$: s("[bd bd ~ bd] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(kit)
$: s("[~ ~ x ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_18
**Source:** drum-patterns

```js
// Title: TB03_PTN3_18
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ ht] ~ ~ ~").bank(bank_ht),
  s("~ ~ [~ ~ hh ~] ~").gain("0.85").bank(bank_hh),
  s("[bd bd bd ~] [bd ~ bd bd] [bd bd ~ ~] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_18
const kit = "RolandTR808";

$: s("[~ ~ ~ ht] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ hh ~] ~").gain("0.85").bank(kit)
$: s("[bd bd bd ~] [bd ~ bd bd] [bd bd ~ ~] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN3_19
**Source:** drum-patterns

```js
// Title: TB03_PTN3_19
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_oh = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ [cr ~ ~ ~] ~ ~").bank(bank_cr),
  s("~ ~ ~ [oh oh oh ~]").bank(bank_oh),
  s("[~ bd bd bd] [~ ~ bd bd] bd*4 ~").gain("1.0 0.8").bank(bank_bd),
  s("~ ~ ~ [~ ~ ~ x]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_19
const kit = "RolandTR808";

$: s("~ [cr ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [oh oh oh ~]").bank(kit)
$: s("[~ bd bd bd] [~ ~ bd bd] bd*4 ~").gain("1.0 0.8").bank(kit)
$: s("~ ~ ~ [~ ~ ~ x]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_20
**Source:** drum-patterns

```js
// Title: TB03_PTN3_20
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ht ~ ~] ~ ~").bank(bank_ht),
  s("~ [~ ~ lt lt] [~ lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ cp]").bank(bank_cp),
  s("[~ ~ bd bd] [bd ~ ~ ~] [bd ~ ~ ~] [bd bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_20
const kit = "RolandTR808";

$: s("~ [~ ht ~ ~] ~ ~").bank(kit)
$: s("~ [~ ~ lt lt] [~ lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ ~ cp]").bank(kit)
$: s("[~ ~ bd bd] [bd ~ ~ ~] [bd ~ ~ ~] [bd bd ~ ~]").bank(kit)
```
</details>

### TB03_PTN3_21
**Source:** drum-patterns

```js
// Title: TB03_PTN3_21
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [lt ~ ~ ~] [lt lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~]*2 ~ ~ [~ bd bd bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_21
const kit = "RolandTR808";

$: s("~ [lt ~ ~ ~] [lt lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 ~ ~ [~ bd bd bd]").bank(kit)
```
</details>

### TB03_PTN3_22
**Source:** drum-patterns

```js
// Title: TB03_PTN3_22
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[~ ~ ~ oh] [oh ~ oh oh] [oh ~]*2 ~").bank(bank_oh),
  s("[~ lt ~ ~] ~ ~ ~").bank(bank_lt),
  s("[~ ~ bd ~] ~ ~ ~").bank(bank_bd),
  s("~ [~ x ~ ~] [~ x ~ ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_22
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [oh ~ oh oh] [oh ~]*2 ~").bank(kit)
$: s("[~ lt ~ ~] ~ ~ ~").bank(kit)
$: s("[~ ~ bd ~] ~ ~ ~").bank(kit)
$: s("~ [~ x ~ ~] [~ x ~ ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_23
**Source:** drum-patterns

```js
// Title: TB03_PTN3_23
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("~ ~ ~ [~ ~ ~ oh]").bank(bank_oh),
  s("[~ hh ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [lt ~ ~ ~] ~ ~").bank(bank_lt),
  s("~ [~ cp ~ ~] ~ ~").bank(bank_cp),
  s("[~ ~ bd bd] [~ ~ bd bd] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_23
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ht ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ oh]").bank(kit)
$: s("[~ hh ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [lt ~ ~ ~] ~ ~").bank(kit)
$: s("~ [~ cp ~ ~] ~ ~").bank(kit)
$: s("[~ ~ bd bd] [~ ~ bd bd] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### TB03_PTN3_24
**Source:** drum-patterns

```js
// Title: TB03_PTN3_24
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [ht ht ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[~ oh ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ lt lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ ~ ~ bd] [bd bd ~ bd] [~ ~ bd ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_24
const kit = "RolandTR808";

$: s("~ ~ [ht ht ~ ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ oh ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ lt lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ bd] [bd bd ~ bd] [~ ~ bd ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### TB03_PTN4_01
**Source:** drum-patterns

```js
// Title: TB03_PTN4_01
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ rd] ~ ~ ~").bank(bank_rd),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("~ [~ ~ ~ lt] ~ ~").bank(bank_lt),
  s("[bd bd bd ~] [bd ~]*2 bd*4 [bd bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_01
const kit = "RolandTR808";

$: s("[~ ~ ~ rd] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("~ [~ ~ ~ lt] ~ ~").bank(kit)
$: s("[bd bd bd ~] [bd ~]*2 bd*4 [bd bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN4_02
**Source:** drum-patterns

```js
// Title: TB03_PTN4_02
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ ht] ~ ~ ~").bank(bank_ht),
  s("[lt ~ ~ ~] ~ [~ ~ lt ~] ~").bank(bank_lt),
  s("[~ bd bd ~] [bd ~]*2 [bd bd ~ bd] [bd ~ ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_02
const kit = "RolandTR808";

$: s("[~ ~ ~ ht] ~ ~ ~").bank(kit)
$: s("[lt ~ ~ ~] ~ [~ ~ lt ~] ~").bank(kit)
$: s("[~ bd bd ~] [bd ~]*2 [bd bd ~ bd] [bd ~ ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN4_03
**Source:** drum-patterns

```js
// Title: TB03_PTN4_03
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[~ ht ~ ~] [ht ~ ~ ~] ~ [ht ~ ~ ~]").bank(bank_ht),
  s("~ ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[~ ~ bd ~] [~ bd bd bd] [bd ~ bd bd] [~ bd bd bd]").gain("1.0 0.8").bank(bank_bd),
  s("[~ ~ ~ x] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_03
const kit = "RolandTR808";

$: s("[~ ht ~ ~] [ht ~ ~ ~] ~ [ht ~ ~ ~]").bank(kit)
$: s("~ ~ [~ sd ~ ~] ~").bank(kit)
$: s("[~ ~ bd ~] [~ bd bd bd] [bd ~ bd bd] [~ bd bd bd]").gain("1.0 0.8").bank(kit)
$: s("[~ ~ ~ x] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_04
**Source:** drum-patterns

```js
// Title: TB03_PTN4_04
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ht ~] [ht ~ ~ ~]").bank(bank_ht),
  s("~ ~ [~ ~ ~ oh] [~ ~ ~ oh]").bank(bank_oh),
  s("~ [lt ~]*2 ~ ~").bank(bank_lt),
  s("[~ cp cp ~] ~ [cp ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ [~ ~ ~ bd] [~ bd ~ ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_04
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ht ~] [ht ~ ~ ~]").bank(kit)
$: s("~ ~ [~ ~ ~ oh] [~ ~ ~ oh]").bank(kit)
$: s("~ [lt ~]*2 ~ ~").bank(kit)
$: s("[~ cp cp ~] ~ [cp ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ ~ bd] [~ bd ~ ~] [~ bd ~ ~]").bank(kit)
```
</details>

### TB03_PTN4_05
**Source:** drum-patterns

```js
// Title: TB03_PTN4_05
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ ~ [~ ht ~ ~]").bank(bank_ht),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ [cp ~ ~ ~] ~").bank(bank_cp),
  s("[~ sd ~ ~] ~ ~ ~").bank(bank_sd),
  s("~ [~ bd bd bd] [~ ~ bd ~] ~").bank(bank_bd),
  s("~ ~ [~ x ~ ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_05
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ht ~ ~]").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [cp ~ ~ ~] ~").bank(kit)
$: s("[~ sd ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ bd bd bd] [~ ~ bd ~] ~").bank(kit)
$: s("~ ~ [~ x ~ ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_06
**Source:** drum-patterns

```js
// Title: TB03_PTN4_06
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[~ ht ~ ~] ~ [~ ht ~ ~] ~").bank(bank_ht),
  s("~ ~ ~ [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] ~").bank(bank_bd),
  s("[~ ~ ~ x] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_06
const kit = "RolandTR808";

$: s("[~ ht ~ ~] ~ [~ ht ~ ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] ~").bank(kit)
$: s("[~ ~ ~ x] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_07
**Source:** drum-patterns

```js
// Title: TB03_PTN4_07
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_ht = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ [~ ~ cr ~] ~ ~").bank(bank_cr),
  s("[~ ht ~ ~] [ht ~ ~ ~] [~ ~ ~ ht] ~").bank(bank_ht),
  s("[bd ~ ~ bd] ~ [bd bd bd ~] [~ bd bd bd]").gain("1.0 0.8").bank(bank_bd),
  s("[~ ~ x ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_07
const kit = "RolandTR808";

$: s("~ [~ ~ cr ~] ~ ~").bank(kit)
$: s("[~ ht ~ ~] [ht ~ ~ ~] [~ ~ ~ ht] ~").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd bd bd ~] [~ bd bd bd]").gain("1.0 0.8").bank(kit)
$: s("[~ ~ x ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_08
**Source:** drum-patterns

```js
// Title: TB03_PTN4_08
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ lt ~ ~] ~ ~ ~").bank(bank_lt),
  s("[bd ~]*2 [~ bd bd bd] bd*4 [bd bd ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_08
const kit = "RolandTR808";

$: s("[~ lt ~ ~] ~ ~ ~").bank(kit)
$: s("[bd ~]*2 [~ bd bd bd] bd*4 [bd bd ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN4_09
**Source:** drum-patterns

```js
// Title: TB03_PTN4_09
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ht ~ ht").bank(bank_ht),
  s("[~ ~ ~ oh] ~ ~ ~").bank(bank_oh),
  s("[lt ~ ~ ~] ~ ~ ~").bank(bank_lt),
  s("~ [~ bd bd bd] [~ bd bd bd] [~ bd bd bd]").gain("1.0 0.8").bank(bank_bd),
  s("[~ ~ x ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_09
const kit = "RolandTR808";

$: s("~ ht ~ ht").bank(kit)
$: s("[~ ~ ~ oh] ~ ~ ~").bank(kit)
$: s("[lt ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ bd bd bd] [~ bd bd bd] [~ bd bd bd]").gain("1.0 0.8").bank(kit)
$: s("[~ ~ x ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_10
**Source:** drum-patterns

```js
// Title: TB03_PTN4_10
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ~] ~ ~ ~").bank(bank_ht),
  s("~ [lt ~ ~ ~] ~ [~ lt ~ ~]").bank(bank_lt),
  s("[~ cp cp cp] [~ ~ ~ cp] [~ cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ ~ [bd ~ ~ ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_10
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [lt ~ ~ ~] ~ [~ lt ~ ~]").bank(kit)
$: s("[~ cp cp cp] [~ ~ ~ cp] [~ cp ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [bd ~ ~ ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### TB03_PTN4_11
**Source:** drum-patterns

```js
// Title: TB03_PTN4_11
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ~ ht] ~").bank(bank_ht),
  s("~ ~ ~ [~ ~ ~ lt]").bank(bank_lt),
  s("~ [~ ~ sd ~] ~ ~").bank(bank_sd),
  s("[bd bd ~ ~] ~ [bd bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_11
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ ht] ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ lt]").bank(kit)
$: s("~ [~ ~ sd ~] ~ ~").bank(kit)
$: s("[bd bd ~ ~] ~ [bd bd bd ~] ~").bank(kit)
```
</details>

### TB03_PTN4_12
**Source:** drum-patterns

```js
// Title: TB03_PTN4_12
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ [~ rd ~ ~] ~").bank(bank_rd),
  s("~ ~ [~ ~ ~ ht] [ht ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ ~ [~ ~ ~ oh]").bank(bank_oh),
  s("[~ ~ ~ lt] ~ ~ ~").bank(bank_lt),
  s("~ [~ lt ~ ~] ~ ~").bank(bank_lt),
  s("~ ~ [cp ~ ~ ~] [~ cp cp ~]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[bd bd bd ~] ~ [~ ~ bd ~] ~").bank(bank_bd),
  s("~ [~ ~ ~ x] ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_12
const kit = "RolandTR808";

$: s("~ ~ [~ rd ~ ~] ~").bank(kit)
$: s("~ ~ [~ ~ ~ ht] [ht ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ ~ oh]").bank(kit)
$: s("[~ ~ ~ lt] ~ ~ ~").bank(kit)
$: s("~ [~ lt ~ ~] ~ ~").bank(kit)
$: s("~ ~ [cp ~ ~ ~] [~ cp cp ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd bd ~] ~ [~ ~ bd ~] ~").bank(kit)
$: s("~ [~ ~ ~ x] ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_13
**Source:** drum-patterns

```js
// Title: TB03_PTN4_13
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_bon = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ bon ~]").bank(bank_bon),
  s("~ ~ [~ lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ ~ ~ sd] ~ ~").bank(bank_sd),
  s("bd*4 [bd bd ~ ~] ~ [~ ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_13
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ bon ~]").bank(kit)
$: s("~ ~ [~ lt lt ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ ~ sd] ~ ~").bank(kit)
$: s("bd*4 [bd bd ~ ~] ~ [~ ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN4_14
**Source:** drum-patterns

```js
// Title: TB03_PTN4_14
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cb ~ ~ ~]").bank(bank_cb),
  s("~ [~ ~ rd ~] ~ ~").bank(bank_rd),
  s("~ [~ ht ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ ~ [~ oh oh ~]").bank(bank_oh),
  s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(bank_hh),
  s("~ [~ ~ ~ lt] [lt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ cp]").bank(bank_cp),
  s("[~ bd bd ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_14
const kit = "RolandTR808";

$: s("~ ~ ~ [cb ~ ~ ~]").bank(kit)
$: s("~ [~ ~ rd ~] ~ ~").bank(kit)
$: s("~ [~ ht ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ oh oh ~]").bank(kit)
$: s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(kit)
$: s("~ [~ ~ ~ lt] [lt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ ~ cp]").bank(kit)
$: s("[~ bd bd ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### TB03_PTN4_15
**Source:** drum-patterns

```js
// Title: TB03_PTN4_15
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("ht ~ ht ~").bank(bank_ht),
  s("[~ lt lt ~] [~ ~ ~ lt] ~ [~ lt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ cp cp ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ ~ [~ bd ~ ~] [~ ~ bd bd]").bank(bank_bd),
  s("~ ~ ~ [x ~ ~ ~]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_15
const kit = "RolandTR808";

$: s("ht ~ ht ~").bank(kit)
$: s("[~ lt lt ~] [~ ~ ~ lt] ~ [~ lt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ cp cp ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ bd ~ ~] [~ ~ bd bd]").bank(kit)
$: s("~ ~ ~ [x ~ ~ ~]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_16
**Source:** drum-patterns

```js
// Title: TB03_PTN4_16
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [ht ~ ~ ~] [ht ~ ~ ~] ~").bank(bank_ht),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[~ lt ~ ~] ~ [~ ~ lt lt] [lt lt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[bd ~ bd bd] [~ bd bd bd] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_16
const kit = "RolandTR808";

$: s("~ [ht ~ ~ ~] [ht ~ ~ ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[~ lt ~ ~] ~ [~ ~ lt lt] [lt lt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ bd bd] [~ bd bd bd] ~ ~").bank(kit)
```
</details>

### TB03_PTN4_17
**Source:** drum-patterns

```js
// Title: TB03_PTN4_17
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[ht ~ ~ ht] ~ [ht ~ ~ ~] ~").bank(bank_ht),
  s("~ ~ [~ ~ oh ~] [~ oh ~ ~]").bank(bank_oh),
  s("[~ lt lt ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ bd bd bd] [~ bd ~ ~] [bd ~ ~ bd]").bank(bank_bd),
  s("~ ~ [~ ~ ~ x] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_17
const kit = "RolandTR808";

$: s("[ht ~ ~ ht] ~ [ht ~ ~ ~] ~").bank(kit)
$: s("~ ~ [~ ~ oh ~] [~ oh ~ ~]").bank(kit)
$: s("[~ lt lt ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ bd bd bd] [~ bd ~ ~] [bd ~ ~ bd]").bank(kit)
$: s("~ ~ [~ ~ ~ x] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_18
**Source:** drum-patterns

```js
// Title: TB03_PTN4_18
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ [ht ~ ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ [~ lt ~ ~] ~").bank(bank_lt),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("~ ~ [~ ~ cp cp] [cp ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[~ ~ ~ bd] [~ bd bd bd] [bd ~ ~ ~] [~ bd]*2").bank(bank_bd),
  s("[x ~ ~ ~] ~ ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_18
const kit = "RolandTR808";

$: s("~ [ht ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [~ lt ~ ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("~ ~ [~ ~ cp cp] [cp ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ bd] [~ bd bd bd] [bd ~ ~ ~] [~ bd]*2").bank(kit)
$: s("[x ~ ~ ~] ~ ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_19
**Source:** drum-patterns

```js
// Title: TB03_PTN4_19
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[~ ~ ~ ht] [ht ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ lt ~ ~] ~").bank(bank_lt),
  s("[sd sd ~ ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ bd ~] [~ bd bd bd] [~ ~ bd bd] [~ bd ~ ~]").bank(bank_bd),
  s("~ ~ [x ~ ~ ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_19
const kit = "RolandTR808";

$: s("[~ ~ ~ ht] [ht ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ ~ [~ lt ~ ~] ~").bank(kit)
$: s("[sd sd ~ ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd ~] [~ bd bd bd] [~ ~ bd bd] [~ bd ~ ~]").bank(kit)
$: s("~ ~ [x ~ ~ ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_20
**Source:** drum-patterns

```js
// Title: TB03_PTN4_20
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ht ~ ~]").bank(bank_ht),
  s("~ [hh ~ ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("[~ lt]*2 [~ ~ ~ lt] [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ [~ ~ cp ~] ~ [cp ~ ~ ~]").bank(bank_cp),
  s("[~ ~ bd ~] ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_20
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ht ~ ~]").bank(kit)
$: s("~ [hh ~ ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("[~ lt]*2 [~ ~ ~ lt] [lt lt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ cp ~] ~ [cp ~ ~ ~]").bank(kit)
$: s("[~ ~ bd ~] ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### TB03_PTN4_21
**Source:** drum-patterns

```js
// Title: TB03_PTN4_21
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ht ~ ~] ~ ~").bank(bank_ht),
  s("~ [~ ~ ~ hh] [hh hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[lt ~ ~ ~] [~ ~ lt ~] [~ ~ lt ~] [~ ~ ~ lt]").bank(bank_lt),
  s("~ ~ [~ ~ ~ cp] [cp ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[~ bd bd bd] [bd ~ ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_21
const kit = "RolandTR808";

$: s("~ [~ ht ~ ~] ~ ~").bank(kit)
$: s("~ [~ ~ ~ hh] [hh hh ~ ~] ~").gain("0.85").bank(kit)
$: s("[lt ~ ~ ~] [~ ~ lt ~] [~ ~ lt ~] [~ ~ ~ lt]").bank(kit)
$: s("~ ~ [~ ~ ~ cp] [cp ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ bd bd bd] [bd ~ ~ ~] ~ ~").bank(kit)
```
</details>

### TB03_PTN4_22
**Source:** drum-patterns

```js
// Title: TB03_PTN4_22
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ht] [ht ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ ~ ~ [lt lt ~ lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[~ bd bd ~] [~ bd ~ ~] [~ bd bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_22
const kit = "RolandTR808";

$: s("[ht ~ ~ ht] [ht ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [lt lt ~ lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ bd bd ~] [~ bd ~ ~] [~ bd bd bd] ~").bank(kit)
```
</details>

### TB03_PTN4_23
**Source:** drum-patterns

```js
// Title: TB03_PTN4_23
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [ht ~ ~ ~] [~ ~ ht ~]").bank(bank_ht),
  s("~ [~ lt ~ ~] ~ ~").bank(bank_lt),
  s("[~ bd bd bd] [bd ~ bd bd] [~ bd]*2 [bd bd ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_23
const kit = "RolandTR808";

$: s("~ ~ [ht ~ ~ ~] [~ ~ ht ~]").bank(kit)
$: s("~ [~ lt ~ ~] ~ ~").bank(kit)
$: s("[~ bd bd bd] [bd ~ bd bd] [~ bd]*2 [bd bd ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### TB03_PTN4_24
**Source:** drum-patterns

```js
// Title: TB03_PTN4_24
// Category: TB03 Generated Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ [ht ht ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ lt lt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[~ bd ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd bd bd]").bank(bank_bd),
  s("~ [x ~ ~ ~] [~ ~ ~ x] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_24
const kit = "RolandTR808";

$: s("~ ~ [ht ht ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ lt lt ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [sd ~ ~ ~]").bank(kit)
$: s("[~ bd ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd bd bd]").bank(kit)
$: s("~ [x ~ ~ ~] [~ ~ ~ x] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

---

## TB03 Patterns

### TB03_PTN1_01
**Source:** drum-patterns

```js
// Title: TB03_PTN1_01
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

stack(
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ bd]").gain("1.0 0.6 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_01
const kit = "RolandTR808";

$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ bd]").gain("1.0 0.6 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_02
**Source:** drum-patterns

```js
// Title: TB03_PTN1_02
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ht ht]").gain("0.6 1.0").bank(bank_ht),
  s("~ ~ [~ ~ ~ oh] ~").bank(bank_oh),
  s("~ ~ [~ lt ~ ~] ~").bank(bank_lt),
  s("~ ~ ~ [lt lt ~ ~]").gain("0.6 1.0").bank(bank_lt),
  s("[bd ~ ~ bd] [bd ~]*2 [bd ~]*2 ~").gain("1.0 0.6 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_02
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ht ht]").gain("0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ ~ oh] ~").bank(kit)
$: s("~ ~ [~ lt ~ ~] ~").bank(kit)
$: s("~ ~ ~ [lt lt ~ ~]").gain("0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] [bd ~]*2 [bd ~]*2 ~").gain("1.0 0.6 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_03
**Source:** drum-patterns

```js
// Title: TB03_PTN1_03
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_cp = bank_default;

stack(
  s("[lt lt ~ ~] ~ [~ ~ ~ lt] [~ ~ ~ lt]").gain("1.0 0.6 1.0 0.6").bank(bank_lt),
  s("~ ~ [cp ~ ~ ~] [~ ~ cp ~]").gain("0.6 1.0").bank(bank_cp)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_03
const kit = "RolandTR808";

$: s("[lt lt ~ ~] ~ [~ ~ ~ lt] [~ ~ ~ lt]").gain("1.0 0.6 1.0 0.6").bank(kit)
$: s("~ ~ [cp ~ ~ ~] [~ ~ cp ~]").gain("0.6 1.0").bank(kit)
```
</details>

### TB03_PTN1_04
**Source:** drum-patterns

```js
// Title: TB03_PTN1_04
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ [~ ~ ~ bd] [bd bd bd ~]").gain("1.0 0.6 0.6 0.6").bank(bank_bd),
  s("~ [~ x ~ ~] ~ ~").note(bass_key).octave(bass_octave).transpose(10).decay(0.2).sustain(0).sound(bass_synth),
  s("~ ~ [x ~ ~ ~] ~").note(bass_key).octave(bass_octave).transpose(7).decay(0.2).sustain(0).sound(bass_synth),
  s("x*4 [~ ~ x x] [~ x ~ ~] [~ ~ ~ x]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_04
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ bd] [bd bd bd ~]").gain("1.0 0.6 0.6 0.6").bank(kit)
$: s("~ [~ x ~ ~] ~ ~").note("c").octave(1).transpose(10).decay(0.2).sustain(0).sound("sawtooth")
$: s("~ ~ [x ~ ~ ~] ~").note("c").octave(1).transpose(7).decay(0.2).sustain(0).sound("sawtooth")
$: s("x*4 [~ ~ x x] [~ x ~ ~] [~ ~ ~ x]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_05
**Source:** drum-patterns

```js
// Title: TB03_PTN1_05
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [oh ~ oh oh]").gain("0.6 1.0 0.6").bank(bank_oh),
  s("~ [lt ~ ~ lt] [~ ~ lt ~] ~").gain("0.6 1.0 1.0").bank(bank_lt),
  s("[cp ~]*2 ~ ~ ~").gain("1.0 0.6").bank(bank_cp),
  s("~ ~ ~ [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_05
const kit = "RolandTR808";

$: s("~ ~ ~ [oh ~ oh oh]").gain("0.6 1.0 0.6").bank(kit)
$: s("~ [lt ~ ~ lt] [~ ~ lt ~] ~").gain("0.6 1.0 1.0").bank(kit)
$: s("[cp ~]*2 ~ ~ ~").gain("1.0 0.6").bank(kit)
$: s("~ ~ ~ [~ bd ~ ~]").bank(kit)
```
</details>

### TB03_PTN1_06
**Source:** drum-patterns

```js
// Title: TB03_PTN1_06
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ cr] ~ ~ ~").bank(bank_cr),
  s("~ [~ ~ rd ~] ~ [~ ~ ~ rd]").gain("1.0 0.6").bank(bank_rd),
  s("[~ ht ht ~] [~ ht]*2 [~ ht ht ht] [~ ht ~ ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_ht),
  s("[oh ~ ~ ~] [oh ~ ~ ~] ~ ~").gain("1.0 0.6").bank(bank_oh),
  s("~ ~ [lt ~ ~ ~] [lt ~ ~ ~]").bank(bank_lt),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_06
const kit = "RolandTR808";

$: s("[~ ~ ~ cr] ~ ~ ~").bank(kit)
$: s("~ [~ ~ rd ~] ~ [~ ~ ~ rd]").gain("1.0 0.6").bank(kit)
$: s("[~ ht ht ~] [~ ht]*2 [~ ht ht ht] [~ ht ~ ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("[oh ~ ~ ~] [oh ~ ~ ~] ~ ~").gain("1.0 0.6").bank(kit)
$: s("~ ~ [lt ~ ~ ~] [lt ~ ~ ~]").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### TB03_PTN1_07
**Source:** drum-patterns

```js
// Title: TB03_PTN1_07
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("bd*4 [~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ ~]").gain("1.0 0.6 0.6 0.6 1.0 0.6 1.0").bank(bank_bd),
  s("~ ~ ~ [~ ~ x ~]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_07
const kit = "RolandTR808";

$: s("bd*4 [~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ ~]").gain("1.0 0.6 0.6 0.6 1.0 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ x ~]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN1_08
**Source:** drum-patterns

```js
// Title: TB03_PTN1_08
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bon = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ bon ~]").bank(bank_bon),
  s("~ ~ ~ [~ oh ~ ~]").bank(bank_oh),
  s("~ ~ [~ ~ ~ hh] [hh ~ ~ ~]").gain("0.6 1.0").bank(bank_hh),
  s("[~ ~ lt ~] [~ lt ~ ~] ~ ~").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ cp]").bank(bank_cp),
  s("[bd bd ~ bd] [bd ~ bd bd] [bd bd bd ~] ~").gain("1.0 0.6 1.0 0.6 0.6 0.6 1.0 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_08
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ bon ~]").bank(kit)
$: s("~ ~ ~ [~ oh ~ ~]").bank(kit)
$: s("~ ~ [~ ~ ~ hh] [hh ~ ~ ~]").gain("0.6 1.0").bank(kit)
$: s("[~ ~ lt ~] [~ lt ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ cp]").bank(kit)
$: s("[bd bd ~ bd] [bd ~ bd bd] [bd bd bd ~] ~").gain("1.0 0.6 1.0 0.6 0.6 0.6 1.0 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN1_09
**Source:** drum-patterns

```js
// Title: TB03_PTN1_09
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

stack(
  s("[~ ~ bd _] [_ bd ~ bd] [_ _ bd bd] [_ bd bd _]").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_09
const kit = "RolandTR808";

$: s("[~ ~ bd _] [_ bd ~ bd] [_ _ bd bd] [_ bd bd _]").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_10
**Source:** drum-patterns

```js
// Title: TB03_PTN1_10
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ lt lt] lt*4").gain("0.6 1.0 0.6 1.0 0.6 0.6").bank(bank_lt),
  s("bd*4 bd*4 [bd bd ~ ~] ~").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_10
const kit = "RolandTR808";

$: s("~ ~ [~ ~ lt lt] lt*4").gain("0.6 1.0 0.6 1.0 0.6 0.6").bank(kit)
$: s("bd*4 bd*4 [bd bd ~ ~] ~").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN1_11
**Source:** drum-patterns

```js
// Title: TB03_PTN1_11
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_cp = bank_default;

stack(
  s("~ ~ [~ ~ ~ hh] hh*4").gain("0.6 1.0 1.0 0.6 0.6").bank(bank_hh),
  s("cp*4 cp*4 [cp cp cp ~] ~").gain("0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 1.0 1.0 0.6").bank(bank_cp)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_11
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ hh] hh*4").gain("0.6 1.0 1.0 0.6 0.6").bank(kit)
$: s("cp*4 cp*4 [cp cp cp ~] ~").gain("0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 1.0 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN1_12
**Source:** drum-patterns

```js
// Title: TB03_PTN1_12
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ [~ oh oh oh] oh*4").gain("1.0 0.6 1.0 0.6 1.0 1.0 0.6").bank(bank_oh),
  s("lt*4 lt*4 [lt ~ ~ ~] ~").gain("1.0 0.6 1.0 0.6 0.6 1.0 1.0 0.6 0.6").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_12
const kit = "RolandTR808";

$: s("~ ~ [~ oh oh oh] oh*4").gain("1.0 0.6 1.0 0.6 1.0 1.0 0.6").bank(kit)
$: s("lt*4 lt*4 [lt ~ ~ ~] ~").gain("1.0 0.6 1.0 0.6 0.6 1.0 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_13
**Source:** drum-patterns

```js
// Title: TB03_PTN1_13
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("lt*4 lt*4 [lt lt lt ~] ~").gain("0.6 0.6 1.0 1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0").bank(bank_lt),
  s("~ ~ [~ ~ ~ bd] bd*4").gain("0.6 0.6 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_13
const kit = "RolandTR808";

$: s("lt*4 lt*4 [lt lt lt ~] ~").gain("0.6 0.6 1.0 1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ ~ bd] bd*4").gain("0.6 0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN1_14
**Source:** drum-patterns

```js
// Title: TB03_PTN1_14
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ cp*4 cp*4").gain("0.6 0.6 1.0 0.6 1.0 0.6 0.6 1.0").bank(bank_cp),
  s("bd*4 bd*4 ~ ~").gain("0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_14
const kit = "RolandTR808";

$: s("~ ~ cp*4 cp*4").gain("0.6 0.6 1.0 0.6 1.0 0.6 0.6 1.0").bank(kit)
$: s("bd*4 bd*4 ~ ~").gain("0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN1_15
**Source:** drum-patterns

```js
// Title: TB03_PTN1_15
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_cp = bank_default;

stack(
  s("~ ~ [~ oh oh oh] oh*4").gain("0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(bank_oh),
  s("cp*4 cp*4 [cp ~ ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6").bank(bank_cp)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_15
const kit = "RolandTR808";

$: s("~ ~ [~ oh oh oh] oh*4").gain("0.6 1.0 0.6 1.0 0.6 1.0 0.6").bank(kit)
$: s("cp*4 cp*4 [cp ~ ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_16
**Source:** drum-patterns

```js
// Title: TB03_PTN1_16
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ _ _ _] [~ _ ~ ~]").bank(bank_cp),
  s("[~ ~ bd _] [bd _ bd bd] [bd ~ ~ ~] [bd ~ bd bd]").gain("1.0 0.6 1.0 0.6 1.0 1.0 1.0 1.0 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_16
const kit = "RolandTR808";

$: s("~ ~ [~ _ _ _] [~ _ ~ ~]").bank(kit)
$: s("[~ ~ bd _] [bd _ bd bd] [bd ~ ~ ~] [bd ~ bd bd]").gain("1.0 0.6 1.0 0.6 1.0 1.0 1.0 1.0 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN1_17
**Source:** drum-patterns

```js
// Title: TB03_PTN1_17
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ht ~ ~]").bank(bank_ht),
  s("~ [~ ~ ~ _] ~ ~").bank(bank_lt),
  s("~ [_ _ ~ ~] [~ _ ~ ~] [~ ~ ~ _]").bank(bank_cp),
  s("[~ ~ ~ bd] [~ ~ bd ~] [bd ~]*2 [bd ~]*2").gain("0.6 0.6 1.0 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_17
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ht ~ ~]").bank(kit)
$: s("~ [~ ~ ~ _] ~ ~").bank(kit)
$: s("~ [_ _ ~ ~] [~ _ ~ ~] [~ ~ ~ _]").bank(kit)
$: s("[~ ~ ~ bd] [~ ~ bd ~] [bd ~]*2 [bd ~]*2").gain("0.6 0.6 1.0 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_18
**Source:** drum-patterns

```js
// Title: TB03_PTN1_18
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [ht ~ ~ ~]").bank(bank_ht),
  s("~ [~ bd bd _] [bd bd bd _] [~ bd _ bd]").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_18
const kit = "RolandTR808";

$: s("~ ~ ~ [ht ~ ~ ~]").bank(kit)
$: s("~ [~ bd bd _] [bd bd bd _] [~ bd _ bd]").gain("0.6 1.0 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_19
**Source:** drum-patterns

```js
// Title: TB03_PTN1_19
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ oh _] [_ _ _ _] [~ oh ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_oh),
  s("[bd _ _ bd] [_ _ ~ ~] ~ [~ ~ bd _]").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_19
const kit = "RolandTR808";

$: s("~ [~ ~ oh _] [_ _ _ _] [~ oh ~ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("[bd _ _ bd] [_ _ ~ ~] ~ [~ ~ bd _]").gain("0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_20
**Source:** drum-patterns

```js
// Title: TB03_PTN1_20
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] [~ ~ oh ~] ~ ~").gain("0.6 1.0").bank(bank_oh),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("~ ~ [cp ~ ~ ~] ~").bank(bank_cp),
  s("[~ bd bd ~] [~ ~ ~ bd] [~ ~ ~ bd] [~ bd ~ ~]").gain("0.6 1.0 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_20
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [~ ~ oh ~] ~ ~").gain("0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("~ ~ [cp ~ ~ ~] ~").bank(kit)
$: s("[~ bd bd ~] [~ ~ ~ bd] [~ ~ ~ bd] [~ bd ~ ~]").gain("0.6 1.0 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN1_21
**Source:** drum-patterns

```js
// Title: TB03_PTN1_21
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [oh oh ~ ~] ~ ~").gain("0.6 1.0").bank(bank_oh),
  s("~ ~ [~ ~ lt ~] ~").bank(bank_lt),
  s("~ [~ ~ ~ cp] ~ ~").bank(bank_cp),
  s("[~ ~ bd bd] [~ ~ bd ~] [bd bd ~ bd] bd*4").gain("0.6 1.0 0.6 0.6 1.0 1.0 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_21
const kit = "RolandTR808";

$: s("~ [oh oh ~ ~] ~ ~").gain("0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ lt ~] ~").bank(kit)
$: s("~ [~ ~ ~ cp] ~ ~").bank(kit)
$: s("[~ ~ bd bd] [~ ~ bd ~] [bd bd ~ bd] bd*4").gain("0.6 1.0 0.6 0.6 1.0 1.0 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_22
**Source:** drum-patterns

```js
// Title: TB03_PTN1_22
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ht _] ~").bank(bank_ht),
  s("[~ ~ bd bd] [bd _ ~ ~] [bd bd ~ ~] [~ ~ bd _]").gain("0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_22
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ht _] ~").bank(kit)
$: s("[~ ~ bd bd] [bd _ ~ ~] [bd bd ~ ~] [~ ~ bd _]").gain("0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN1_23
**Source:** drum-patterns

```js
// Title: TB03_PTN1_23
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ht ~ ~] [_ ~ ~ ~]").bank(bank_ht),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[bd bd ~ bd] [bd bd _ ~] [~ ~ bd bd] [~ ~ ~ bd]").gain("0.6 1.0 1.0 1.0 0.6 0.6 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_23
const kit = "RolandTR808";

$: s("~ ~ [~ ht ~ ~] [_ ~ ~ ~]").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[bd bd ~ bd] [bd bd _ ~] [~ ~ bd bd] [~ ~ ~ bd]").gain("0.6 1.0 1.0 1.0 0.6 0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN1_24
**Source:** drum-patterns

```js
// Title: TB03_PTN1_24
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ht ~]").bank(bank_ht),
  s("[bd _ _ _] [_ _ bd bd] [_ _ _ _] [bd bd ~ bd]").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN1_24
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ht ~]").bank(kit)
$: s("[bd _ _ _] [_ _ bd bd] [_ _ _ _] [bd bd ~ bd]").gain("0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_01
**Source:** drum-patterns

```js
// Title: TB03_PTN2_01
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ ht]").bank(bank_ht),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("~ [lt ~ lt _] [~ ~ _ lt] [~ lt ~ ~]").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_lt),
  s("~ ~ [cp cp ~ ~] [_ ~ ~ ~]").gain("0.6 1.0 0.6").bank(bank_cp),
  s("[bd bd _ _] [~ _ ~ ~] ~ ~").gain("1.0 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_01
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ ht]").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("~ [lt ~ lt _] [~ ~ _ lt] [~ lt ~ ~]").gain("0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ ~ [cp cp ~ ~] [_ ~ ~ ~]").gain("0.6 1.0 0.6").bank(kit)
$: s("[bd bd _ _] [~ _ ~ ~] ~ ~").gain("1.0 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_02
**Source:** drum-patterns

```js
// Title: TB03_PTN2_02
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

stack(
  s("[bd _ _ _] [bd _ _ bd] [_ bd _ _] [_ ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_02
const kit = "RolandTR808";

$: s("[bd _ _ _] [bd _ _ bd] [_ bd _ _] [_ ~ ~ ~]").bank(kit)
```
</details>

### TB03_PTN2_03
**Source:** drum-patterns

```js
// Title: TB03_PTN2_03
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;

stack(
  s("oh*4 oh*4 [oh ~ ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0").bank(bank_oh),
  s("~ ~ [~ hh hh hh] hh*4").gain("0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(bank_hh)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_03
const kit = "RolandTR808";

$: s("oh*4 oh*4 [oh ~ ~ ~] ~").gain("0.6 0.6 1.0 0.6 0.6 1.0 0.6 0.6 1.0").bank(kit)
$: s("~ ~ [~ hh hh hh] hh*4").gain("0.6 0.6 1.0 0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN2_04
**Source:** drum-patterns

```js
// Title: TB03_PTN2_04
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ht*4 ht*4").gain("0.6 0.6 1.0 0.6 1.0 0.6 1.0 1.0").bank(bank_ht),
  s("bd*4 bd*4 ~ ~").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_04
const kit = "RolandTR808";

$: s("~ ~ ht*4 ht*4").gain("0.6 0.6 1.0 0.6 1.0 0.6 1.0 1.0").bank(kit)
$: s("bd*4 bd*4 ~ ~").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN2_05
**Source:** drum-patterns

```js
// Title: TB03_PTN2_05
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [oh ~ ~ ~] ~ ~").bank(bank_oh),
  s("~ [~ ~ ~ hh] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ lt ~] ~").bank(bank_lt),
  s("~ ~ ~ [~ cp ~ ~]").bank(bank_cp),
  s("[bd bd bd _] [~ bd _ ~] [bd _ ~ bd] [_ ~ bd _]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_05
const kit = "RolandTR808";

$: s("~ [oh ~ ~ ~] ~ ~").bank(kit)
$: s("~ [~ ~ ~ hh] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ lt ~] ~").bank(kit)
$: s("~ ~ ~ [~ cp ~ ~]").bank(kit)
$: s("[bd bd bd _] [~ bd _ ~] [bd _ ~ bd] [_ ~ bd _]").bank(kit)
```
</details>

### TB03_PTN2_06
**Source:** drum-patterns

```js
// Title: TB03_PTN2_06
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [oh _ ~ ~]").bank(bank_oh),
  s("[~ ~ ~ hh] [_ ~ ~ ~] ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [lt ~ ~ ~] [~ ~ ~ lt]").bank(bank_lt),
  s("[bd bd bd ~] [~ bd bd _] [~ bd _ bd] ~").gain("1.0 0.6 1.0 1.0 0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_06
const kit = "RolandTR808";

$: s("~ ~ ~ [oh _ ~ ~]").bank(kit)
$: s("[~ ~ ~ hh] [_ ~ ~ ~] ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ ~ [lt ~ ~ ~] [~ ~ ~ lt]").bank(kit)
$: s("[bd bd bd ~] [~ bd bd _] [~ bd _ bd] ~").gain("1.0 0.6 1.0 1.0 0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN2_07
**Source:** drum-patterns

```js
// Title: TB03_PTN2_07
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ _ ~] [hh ~ ~ ~] [~ ~ ~ hh]").gain("0.6 1.0 0.6").bank(bank_hh),
  s("[bd _ bd _] [_ bd ~ ~] [~ _ bd _] [_ bd ~ ~]").gain("1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_07
const kit = "RolandTR808";

$: s("~ [~ ~ _ ~] [hh ~ ~ ~] [~ ~ ~ hh]").gain("0.6 1.0 0.6").bank(kit)
$: s("[bd _ bd _] [_ bd ~ ~] [~ _ bd _] [_ bd ~ ~]").gain("1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN2_08
**Source:** drum-patterns

```js
// Title: TB03_PTN2_08
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("~ [~ ~ cb ~] ~ ~").bank(bank_cb),
  s("[~ ~ ~ ht] [_ ~ ~ ~] [~ ~ _ ~] ~").bank(bank_ht),
  s("~ [~ ~ ~ _] ~ ~").bank(bank_oh),
  s("[bd _ bd ~] [~ bd ~ ~] [bd ~ ~ bd] [_ bd _ bd]").gain("1.0 0.6 0.6 1.0 1.0 0.6 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_08
const kit = "RolandTR808";

$: s("~ ~ [~ sd ~ ~] ~").bank(kit)
$: s("~ [~ ~ cb ~] ~ ~").bank(kit)
$: s("[~ ~ ~ ht] [_ ~ ~ ~] [~ ~ _ ~] ~").bank(kit)
$: s("~ [~ ~ ~ _] ~ ~").bank(kit)
$: s("[bd _ bd ~] [~ bd ~ ~] [bd ~ ~ bd] [_ bd _ bd]").gain("1.0 0.6 0.6 1.0 1.0 0.6 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_09
**Source:** drum-patterns

```js
// Title: TB03_PTN2_09
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ [~ ~ ~ lt] [~ lt ~ ~] [~ lt ~ ~]").gain("1.0 0.6 1.0").bank(bank_lt),
  s("[~ ~ bd _] [_ bd ~ ~] [_ ~ ~ bd] [_ ~ bd bd]").gain("1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_09
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ ~ ~ lt] [~ lt ~ ~] [~ lt ~ ~]").gain("1.0 0.6 1.0").bank(kit)
$: s("[~ ~ bd _] [_ bd ~ ~] [_ ~ ~ bd] [_ ~ bd bd]").gain("1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_10
**Source:** drum-patterns

```js
// Title: TB03_PTN2_10
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ [~ ~ lt lt] [_ ~ ~ lt] [_ ~ ~ ~]").gain("1.0 0.6 0.6 1.0 0.6").bank(bank_lt),
  s("[~ bd]*2 [_ _ ~ ~] [~ bd ~ ~] [~ bd _ _]").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_10
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ ~ lt lt] [_ ~ ~ lt] [_ ~ ~ ~]").gain("1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ bd]*2 [_ _ ~ ~] [~ bd ~ ~] [~ bd _ _]").gain("1.0 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_11
**Source:** drum-patterns

```js
// Title: TB03_PTN2_11
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ [~ ~ ~ lt] [_ _ lt ~] [~ lt _ ~]").gain("1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_lt),
  s("[~ ~ bd _] [_ bd ~ ~] ~ [bd ~ ~ bd]").gain("1.0 0.6 0.6 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_11
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ ~ ~ lt] [_ _ lt ~] [~ lt _ ~]").gain("1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ bd _] [_ bd ~ ~] ~ [bd ~ ~ bd]").gain("1.0 0.6 0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN2_12
**Source:** drum-patterns

```js
// Title: TB03_PTN2_12
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[lt ~ ~ lt] [_ _ lt _] [~ ~ lt ~] ~").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_lt),
  s("[~ bd bd ~] ~ [bd ~ ~ bd] [_ bd ~ bd]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_12
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[lt ~ ~ lt] [_ _ lt _] [~ ~ lt ~] ~").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
$: s("[~ bd bd ~] ~ [bd ~ ~ bd] [_ bd ~ bd]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN2_13
**Source:** drum-patterns

```js
// Title: TB03_PTN2_13
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("~ ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[bd bd bd _] [~ ~ bd bd] [_ bd ~ ~] [_ bd bd bd]").gain("0.6 0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_13
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[bd bd bd _] [~ ~ bd bd] [_ bd ~ ~] [_ bd bd bd]").gain("0.6 0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_14
**Source:** drum-patterns

```js
// Title: TB03_PTN2_14
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hc = bank_default;
let bank_cb = bank_default;
let bank_cr = bank_default;
let bank_rd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ sd]").bank(bank_sd),
  s("~ ~ ~ [~ hc ~ ~]").bank(bank_hc),
  s("[~ ~ ~ sd] ~ ~ ~").bank(bank_sd),
  s("~ [~ ~ ~ cb] ~ ~").bank(bank_cb),
  s("~ ~ ~ [~ ~ cr ~]").bank(bank_cr),
  s("~ ~ [~ ~ ~ rd] ~").bank(bank_rd),
  s("[bd bd bd ~] [bd bd bd ~] [bd bd bd ~] [bd ~ ~ ~]").gain("0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_14
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ sd]").bank(kit)
$: s("~ ~ ~ [~ hc ~ ~]").bank(kit)
$: s("[~ ~ ~ sd] ~ ~ ~").bank(kit)
$: s("~ [~ ~ ~ cb] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ cr ~]").bank(kit)
$: s("~ ~ [~ ~ ~ rd] ~").bank(kit)
$: s("[bd bd bd ~] [bd bd bd ~] [bd bd bd ~] [bd ~ ~ ~]").gain("0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_15
**Source:** drum-patterns

```js
// Title: TB03_PTN2_15
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

stack(
  s("bd*16").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_15
const kit = "RolandTR808";

$: s("bd*16").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_16
**Source:** drum-patterns

```js
// Title: TB03_PTN2_16
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_cr = bank_default;
let bank_rd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ sd ~] ~ ~ ~").bank(bank_sd),
  s("~ [~ ~ cr ~] ~ ~").bank(bank_cr),
  s("~ ~ [~ ~ ~ rd] ~").bank(bank_rd),
  s("[bd bd ~ bd] ~ [~ _ bd ~] [bd bd _ _]").gain("1.0 1.0 1.0 0.6 0.6 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_16
const kit = "RolandTR808";

$: s("[~ ~ sd ~] ~ ~ ~").bank(kit)
$: s("~ [~ ~ cr ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ ~ rd] ~").bank(kit)
$: s("[bd bd ~ bd] ~ [~ _ bd ~] [bd bd _ _]").gain("1.0 1.0 1.0 0.6 0.6 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_17
**Source:** drum-patterns

```js
// Title: TB03_PTN2_17
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ~] ~ [ht ~ ~ ~] [~ ~ ~ ht]").bank(bank_ht),
  s("[~ ~ ~ lt] ~ ~ ~").bank(bank_lt),
  s("~ [~ ~ bd ~] [~ bd ~ ~] [bd ~]*2").gain("1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_17
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] ~ [ht ~ ~ ~] [~ ~ ~ ht]").bank(kit)
$: s("[~ ~ ~ lt] ~ ~ ~").bank(kit)
$: s("~ [~ ~ bd ~] [~ bd ~ ~] [bd ~]*2").gain("1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_18
**Source:** drum-patterns

```js
// Title: TB03_PTN2_18
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ht] [~ ~ ~ ht] [~ ht ~ ~] ~").bank(bank_ht),
  s("[~ lt ~ ~] ~ [lt ~ ~ ~] [~ ~ lt ~]").bank(bank_lt),
  s("[~ ~ bd ~] [bd bd bd ~] [~ ~ bd bd] [bd bd ~ bd]").gain("1.0 0.6 0.6 0.6 1.0 0.6 1.0 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_18
const kit = "RolandTR808";

$: s("[ht ~ ~ ht] [~ ~ ~ ht] [~ ht ~ ~] ~").bank(kit)
$: s("[~ lt ~ ~] ~ [lt ~ ~ ~] [~ ~ lt ~]").bank(kit)
$: s("[~ ~ bd ~] [bd bd bd ~] [~ ~ bd bd] [bd bd ~ bd]").gain("1.0 0.6 0.6 0.6 1.0 0.6 1.0 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN2_19
**Source:** drum-patterns

```js
// Title: TB03_PTN2_19
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht _ _ ~] ~ [ht _ _ ~] ~").bank(bank_ht),
  s("[~ ~ ~ lt] [_ ~ ~ ~] ~ ~").gain("1.0 0.6").bank(bank_lt),
  s("~ [~ bd _ _] [~ ~ ~ bd] [_ _ bd bd]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_19
const kit = "RolandTR808";

$: s("[ht _ _ ~] ~ [ht _ _ ~] ~").bank(kit)
$: s("[~ ~ ~ lt] [_ ~ ~ ~] ~ ~").gain("1.0 0.6").bank(kit)
$: s("~ [~ bd _ _] [~ ~ ~ bd] [_ _ bd bd]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_20
**Source:** drum-patterns

```js
// Title: TB03_PTN2_20
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ~] [ht ~ ~ ~] [~ ~ ~ ht] [~ ~ ~ ht]").bank(bank_ht),
  s("[~ lt ~ ~] ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[~ ~ ~ bd] [~ bd ~ ~] [bd bd ~ ~] [_ ~ ~ ~]").gain("1.0 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_20
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] [ht ~ ~ ~] [~ ~ ~ ht] [~ ~ ~ ht]").bank(kit)
$: s("[~ lt ~ ~] ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[~ ~ ~ bd] [~ bd ~ ~] [bd bd ~ ~] [_ ~ ~ ~]").gain("1.0 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_21
**Source:** drum-patterns

```js
// Title: TB03_PTN2_21
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ht] [~ ~ ~ ht] [_ _ _ _] [_ ~ ht ~]").bank(bank_ht),
  s("[~ lt ~ ~] ~ ~ [~ lt ~ ~]").bank(bank_lt),
  s("[~ ~ bd ~] [bd bd bd ~] ~ [~ ~ ~ bd]").gain("1.0 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_21
const kit = "RolandTR808";

$: s("[ht ~ ~ ht] [~ ~ ~ ht] [_ _ _ _] [_ ~ ht ~]").bank(kit)
$: s("[~ lt ~ ~] ~ ~ [~ lt ~ ~]").bank(kit)
$: s("[~ ~ bd ~] [bd bd bd ~] ~ [~ ~ ~ bd]").gain("1.0 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN2_22
**Source:** drum-patterns

```js
// Title: TB03_PTN2_22
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [ht ~ ~ ht] ~").bank(bank_ht),
  s("~ ~ [~ lt ~ ~] ~").bank(bank_lt),
  s("~ ~ [~ ~ bd ~] [bd bd _ ~]").gain("1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_22
const kit = "RolandTR808";

$: s("~ ~ [ht ~ ~ ht] ~").bank(kit)
$: s("~ ~ [~ lt ~ ~] ~").bank(kit)
$: s("~ ~ [~ ~ bd ~] [bd bd _ ~]").gain("1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN2_23
**Source:** drum-patterns

```js
// Title: TB03_PTN2_23
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ~ ~ ~] [ht ~ ~ ~] [_ _ ~ ~] [ht ~]*2").bank(bank_ht),
  s("[~ lt _ ~] ~ ~ [~ lt ~ ~]").gain("1.0 0.6 1.0").bank(bank_lt),
  s("[~ ~ ~ bd] [~ bd bd bd] ~ [~ ~ ~ bd]").gain("1.0 0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_23
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] [ht ~ ~ ~] [_ _ ~ ~] [ht ~]*2").bank(kit)
$: s("[~ lt _ ~] ~ ~ [~ lt ~ ~]").gain("1.0 0.6 1.0").bank(kit)
$: s("[~ ~ ~ bd] [~ bd bd bd] ~ [~ ~ ~ bd]").gain("1.0 0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN2_24
**Source:** drum-patterns

```js
// Title: TB03_PTN2_24
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht _ _ _] ~ [~ ~ ~ ht] [_ _ ~ ~]").bank(bank_ht),
  s("~ [lt _ _ _] ~ ~").gain("1.0 0.6 0.6 0.6").bank(bank_lt),
  s("~ ~ [bd _ _ ~] [~ ~ bd bd]").gain("1.0 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN2_24
const kit = "RolandTR808";

$: s("[ht _ _ _] ~ [~ ~ ~ ht] [_ _ ~ ~]").bank(kit)
$: s("~ [lt _ _ _] ~ ~").gain("1.0 0.6 0.6 0.6").bank(kit)
$: s("~ ~ [bd _ _ ~] [~ ~ bd bd]").gain("1.0 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN3_01
**Source:** drum-patterns

```js
// Title: TB03_PTN3_01
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ [~ bd bd bd] [bd ~ bd bd]").gain("1.0 0.6 0.6 0.6 0.6 0.6").bank(bank_bd),
  s("~ [x ~ ~ ~] ~ ~").note(bass_key).octave(bass_octave).transpose(10).decay(0.2).sustain(0).sound(bass_synth),
  s("~ [~ ~ ~ x] ~ ~").note(bass_key).octave(bass_octave).transpose(7).decay(0.2).sustain(0).sound(bass_synth),
  s("x*4 [~ x x ~] [x ~ ~ ~] [~ x ~ ~]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_01
const kit = "RolandTR808";

$: s("~ ~ [~ bd bd bd] [bd ~ bd bd]").gain("1.0 0.6 0.6 0.6 0.6 0.6").bank(kit)
$: s("~ [x ~ ~ ~] ~ ~").note("c").octave(1).transpose(10).decay(0.2).sustain(0).sound("sawtooth")
$: s("~ [~ ~ ~ x] ~ ~").note("c").octave(1).transpose(7).decay(0.2).sustain(0).sound("sawtooth")
$: s("x*4 [~ x x ~] [x ~ ~ ~] [~ x ~ ~]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_02
**Source:** drum-patterns

```js
// Title: TB03_PTN3_02
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ cr] ~ ~ ~").bank(bank_cr),
  s("~ [~ ~ rd ~] ~ [~ ~ ~ rd]").gain("1.0 0.6").bank(bank_rd),
  s("[~ ht ht ~] [~ ht]*2 [~ ht ht ht] [~ ht ~ ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(bank_ht),
  s("[oh ~ ~ ~] [oh ~ ~ ~] ~ ~").gain("1.0 0.6").bank(bank_oh),
  s("~ ~ [lt ~ ~ ~] [lt ~ ~ ~]").bank(bank_lt),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_02
const kit = "RolandTR808";

$: s("[~ ~ ~ cr] ~ ~ ~").bank(kit)
$: s("~ [~ ~ rd ~] ~ [~ ~ ~ rd]").gain("1.0 0.6").bank(kit)
$: s("[~ ht ht ~] [~ ht]*2 [~ ht ht ht] [~ ht ~ ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6").bank(kit)
$: s("[oh ~ ~ ~] [oh ~ ~ ~] ~ ~").gain("1.0 0.6").bank(kit)
$: s("~ ~ [lt ~ ~ ~] [lt ~ ~ ~]").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### TB03_PTN3_03
**Source:** drum-patterns

```js
// Title: TB03_PTN3_03
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bon = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ bon ~]").bank(bank_bon),
  s("~ ~ ~ [~ oh ~ ~]").bank(bank_oh),
  s("~ ~ [~ ~ ~ hh] [hh ~ ~ ~]").gain("0.6 1.0").bank(bank_hh),
  s("[~ ~ lt ~] [~ lt ~ ~] ~ ~").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ cp]").bank(bank_cp),
  s("[bd bd ~ bd] [bd ~ bd bd] [bd bd bd ~] ~").gain("1.0 0.6 1.0 0.6 0.6 0.6 1.0 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_03
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ bon ~]").bank(kit)
$: s("~ ~ ~ [~ oh ~ ~]").bank(kit)
$: s("~ ~ [~ ~ ~ hh] [hh ~ ~ ~]").gain("0.6 1.0").bank(kit)
$: s("[~ ~ lt ~] [~ lt ~ ~] ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ cp]").bank(kit)
$: s("[bd bd ~ bd] [bd ~ bd bd] [bd bd bd ~] ~").gain("1.0 0.6 1.0 0.6 0.6 0.6 1.0 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_04
**Source:** drum-patterns

```js
// Title: TB03_PTN3_04
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ lt] ~").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[~ ~ ~ _] [_ ~ ~ ~] [cp ~ ~ ~] ~").bank(bank_cp),
  s("[bd _ ~ ~] [~ ~ ~ bd] [~ ~ _ ~] [~ bd _ ~]").gain("1.0 0.6 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_04
const kit = "RolandTR808";

$: s("[~ ~ oh ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ lt] ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ lt]").bank(kit)
$: s("[~ ~ ~ _] [_ ~ ~ ~] [cp ~ ~ ~] ~").bank(kit)
$: s("[bd _ ~ ~] [~ ~ ~ bd] [~ ~ _ ~] [~ bd _ ~]").gain("1.0 0.6 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_05
**Source:** drum-patterns

```js
// Title: TB03_PTN3_05
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ oh ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ [hh ~ ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ [lt _ ~ ~] ~").bank(bank_lt),
  s("[~ ~ _ ~] ~ ~ [~ ~ ~ lt]").gain("0.6 1.0").bank(bank_lt),
  s("~ ~ [~ ~ ~ cp] [~ ~ _ ~]").gain("1.0 0.6").bank(bank_cp),
  s("[bd ~ ~ bd] [~ ~ bd _] [~ ~ bd ~] [~ bd ~ ~]").gain("0.6 0.6 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_05
const kit = "RolandTR808";

$: s("[~ oh ~ ~] ~ ~ ~").bank(kit)
$: s("~ [hh ~ ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("~ ~ [lt _ ~ ~] ~").bank(kit)
$: s("[~ ~ _ ~] ~ ~ [~ ~ ~ lt]").gain("0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ ~ cp] [~ ~ _ ~]").gain("1.0 0.6").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd _] [~ ~ bd ~] [~ bd ~ ~]").gain("0.6 0.6 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_06
**Source:** drum-patterns

```js
// Title: TB03_PTN3_06
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;

stack(
  s("[~ ~ lt ~] [~ lt ~ ~] [~ ~ ~ lt] [lt ~ ~ ~]").gain("1.0 0.6 0.6 1.0").bank(bank_lt),
  s("~ ~ [lt lt ~ ~] [~ ~ lt lt]").gain("1.0 0.6 1.0 0.6").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_06
const kit = "RolandTR808";

$: s("[~ ~ lt ~] [~ lt ~ ~] [~ ~ ~ lt] [lt ~ ~ ~]").gain("1.0 0.6 0.6 1.0").bank(kit)
$: s("~ ~ [lt lt ~ ~] [~ ~ lt lt]").gain("1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_07
**Source:** drum-patterns

```js
// Title: TB03_PTN3_07
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ _ ~] ~ [~ _ ~ ~]").bank(bank_lt),
  s("[~ ~ ~ bd] [~ bd]*2 [~ bd bd ~] [bd ~]*2").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_07
const kit = "RolandTR808";

$: s("~ [~ ~ _ ~] ~ [~ _ ~ ~]").bank(kit)
$: s("[~ ~ ~ bd] [~ bd]*2 [~ bd bd ~] [bd ~]*2").gain("1.0 0.6 1.0 0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN3_08
**Source:** drum-patterns

```js
// Title: TB03_PTN3_08
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

stack(
  s("~ bd*4 ~ bd*4").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_08
const kit = "RolandTR808";

$: s("~ bd*4 ~ bd*4").gain("1.0 0.6 0.6 1.0 0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN3_09
**Source:** drum-patterns

```js
// Title: TB03_PTN3_09
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ hh]").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ lt ~ ~]").bank(bank_lt),
  s("~ [~ ~ ~ lt] [~ lt]*2 ~").gain("1.0 1.0 0.6").bank(bank_lt),
  s("~ [~ cp ~ ~] ~ ~").bank(bank_cp),
  s("[bd bd bd ~] ~ ~ ~").gain("1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_09
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ hh]").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ lt ~ ~]").bank(kit)
$: s("~ [~ ~ ~ lt] [~ lt]*2 ~").gain("1.0 1.0 0.6").bank(kit)
$: s("~ [~ cp ~ ~] ~ ~").bank(kit)
$: s("[bd bd bd ~] ~ ~ ~").gain("1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN3_10
**Source:** drum-patterns

```js
// Title: TB03_PTN3_10
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] ~ ~ ~").gain("1.0 1.0 0.6").bank(bank_hh),
  s("~ [lt ~ lt lt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ [~ cp cp ~] [cp ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ ~ ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_10
const kit = "RolandTR808";

$: s("[hh ~ hh hh] ~ ~ ~").gain("1.0 1.0 0.6").bank(kit)
$: s("~ [lt ~ lt lt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ cp cp ~] [cp ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ bd ~]").bank(kit)
```
</details>

### TB03_PTN3_11
**Source:** drum-patterns

```js
// Title: TB03_PTN3_11
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ lt] [~ ~ ~ lt] [~ ~ ~ lt] [~ ~ ~ lt]").gain("0.6 1.0 0.6 1.0").bank(bank_lt),
  s("[bd bd bd ~] [bd bd bd ~] [bd bd bd ~] [bd bd bd ~]").gain("0.6 1.0 0.6 1.0 0.6 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_11
const kit = "RolandTR808";

$: s("[~ ~ ~ lt] [~ ~ ~ lt] [~ ~ ~ lt] [~ ~ ~ lt]").gain("0.6 1.0 0.6 1.0").bank(kit)
$: s("[bd bd bd ~] [bd bd bd ~] [bd bd bd ~] [bd bd bd ~]").gain("0.6 1.0 0.6 1.0 0.6 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN3_12
**Source:** drum-patterns

```js
// Title: TB03_PTN3_12
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ lt] [lt ~ ~ ~] ~ [lt lt ~ ~]").gain("1.0 0.6 0.6 0.6").bank(bank_lt),
  s("~ [~ ~ ~ cp] [cp ~ ~ ~] ~").gain("1.0 0.6").bank(bank_cp),
  s("[bd ~]*2 [~ bd bd ~] [~ ~ bd bd] [~ ~ bd bd]").gain("0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_12
const kit = "RolandTR808";

$: s("[~ ~ ~ lt] [lt ~ ~ ~] ~ [lt lt ~ ~]").gain("1.0 0.6 0.6 0.6").bank(kit)
$: s("~ [~ ~ ~ cp] [cp ~ ~ ~] ~").gain("1.0 0.6").bank(kit)
$: s("[bd ~]*2 [~ bd bd ~] [~ ~ bd bd] [~ ~ bd bd]").gain("0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_13
**Source:** drum-patterns

```js
// Title: TB03_PTN3_13
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[cp ~ ~ ~] ~ ~ ~").bank(bank_cp),
  s("~ ~ [~ ~ bd bd] [_ bd ~ bd]").bank(bank_bd),
  s("[~ x _ x] [~ x x _] ~ ~").note(bass_key).octave(bass_octave).transpose(2).decay(0.2).sustain(0).sound(bass_synth),
  s("~ ~ [x ~ ~ ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_13
const kit = "RolandTR808";

$: s("[cp ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ bd bd] [_ bd ~ bd]").bank(kit)
$: s("[~ x _ x] [~ x x _] ~ ~").note("c").octave(1).transpose(2).decay(0.2).sustain(0).sound("sawtooth")
$: s("~ ~ [x ~ ~ ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN3_14
**Source:** drum-patterns

```js
// Title: TB03_PTN3_14
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

stack(
  s("[bd _ _ bd] [_ _ bd _] [_ bd _ _] [bd _ bd bd]").gain("1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_14
const kit = "RolandTR808";

$: s("[bd _ _ bd] [_ _ bd _] [_ bd _ _] [bd _ bd bd]").gain("1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_15
**Source:** drum-patterns

```js
// Title: TB03_PTN3_15
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;

stack(
  s("~ [~ ~ ht ~] [ht ~ ~ _] [ht ~ ~ ~]").gain("0.6 1.0 0.6 0.6").bank(bank_ht),
  s("[oh _ _ oh] [_ _ ~ ~] [~ _ oh ~] [~ _ oh oh]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 1.0").bank(bank_oh)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_15
const kit = "RolandTR808";

$: s("~ [~ ~ ht ~] [ht ~ ~ _] [ht ~ ~ ~]").gain("0.6 1.0 0.6 0.6").bank(kit)
$: s("[oh _ _ oh] [_ _ ~ ~] [~ _ oh ~] [~ _ oh oh]").gain("1.0 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 1.0 1.0").bank(kit)
```
</details>

### TB03_PTN3_16
**Source:** drum-patterns

```js
// Title: TB03_PTN3_16
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ [~ ~ ht ~] ~").bank(bank_ht),
  s("[lt _ lt _] [_ lt _ _] [lt _ ~ ~] [~ ~ lt lt]").gain("0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6 0.6 1.0").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_16
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ht ~] ~").bank(kit)
$: s("[lt _ lt _] [_ lt _ _] [lt _ ~ ~] [~ ~ lt lt]").gain("0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN3_17
**Source:** drum-patterns

```js
// Title: TB03_PTN3_17
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ ht] [~ ~ _ ~] [~ ~ _ ~] ~").gain("1.0 0.6 0.6").bank(bank_ht),
  s("~ [~ hh ~ ~] ~ ~").gain("0.85").bank(bank_hh),
  s("[lt ~ ~ ~] [~ ~ ~ lt] ~ [~ lt ~ ~]").gain("1.0 0.6 0.6").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ cp]").bank(bank_cp),
  s("[~ ~ bd ~] ~ [~ bd]*2 ~").gain("0.6 1.0 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_17
const kit = "RolandTR808";

$: s("[~ ~ ~ ht] [~ ~ _ ~] [~ ~ _ ~] ~").gain("1.0 0.6 0.6").bank(kit)
$: s("~ [~ hh ~ ~] ~ ~").gain("0.85").bank(kit)
$: s("[lt ~ ~ ~] [~ ~ ~ lt] ~ [~ lt ~ ~]").gain("1.0 0.6 0.6").bank(kit)
$: s("~ ~ ~ [~ ~ ~ cp]").bank(kit)
$: s("[~ ~ bd ~] ~ [~ bd]*2 ~").gain("0.6 1.0 1.0").bank(kit)
```
</details>

### TB03_PTN3_18
**Source:** drum-patterns

```js
// Title: TB03_PTN3_18
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ lt ~ ~] [lt ~ ~ lt]").gain("0.6 0.6 1.0").bank(bank_lt),
  s("[bd ~ ~ bd] [~ ~ bd ~] ~ ~").gain("1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_18
const kit = "RolandTR808";

$: s("~ ~ [~ lt ~ ~] [lt ~ ~ lt]").gain("0.6 0.6 1.0").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] ~ ~").gain("1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN3_19
**Source:** drum-patterns

```js
// Title: TB03_PTN3_19
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [oh ~ ~ ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ ~ hh ~] [~ hh ~ ~] ~ ~").gain("0.6 1.0").bank(bank_hh),
  s("~ ~ [~ ~ ~ bd] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_19
const kit = "RolandTR808";

$: s("~ ~ [oh ~ ~ ~] [~ ~ oh ~]").bank(kit)
$: s("[~ ~ hh ~] [~ hh ~ ~] ~ ~").gain("0.6 1.0").bank(kit)
$: s("~ ~ [~ ~ ~ bd] [~ ~ ~ bd]").bank(kit)
```
</details>

### TB03_PTN3_20
**Source:** drum-patterns

```js
// Title: TB03_PTN3_20
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ oh]*2").bank(bank_oh),
  s("~ ~ [~ ~ hh hh] ~").gain("0.6 1.0").bank(bank_hh),
  s("~ [~ ~ lt lt] [lt ~ ~ ~] ~").gain("0.6 0.6 1.0").bank(bank_lt),
  s("[bd ~]*2 [bd ~ ~ ~] ~ [~ ~ bd ~]").gain("1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_20
const kit = "RolandTR808";

$: s("~ ~ ~ [~ oh]*2").bank(kit)
$: s("~ ~ [~ ~ hh hh] ~").gain("0.6 1.0").bank(kit)
$: s("~ [~ ~ lt lt] [lt ~ ~ ~] ~").gain("0.6 0.6 1.0").bank(kit)
$: s("[bd ~]*2 [bd ~ ~ ~] ~ [~ ~ bd ~]").gain("1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_21
**Source:** drum-patterns

```js
// Title: TB03_PTN3_21
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ ~ lt] ~").bank(bank_lt),
  s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_21
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ lt] ~").bank(kit)
$: s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN3_22
**Source:** drum-patterns

```js
// Title: TB03_PTN3_22
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [oh ~]*2 ~").bank(bank_oh),
  s("~ [~ ~ hh hh] ~ ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ lt] [lt lt ~ ~] ~ [~ ~ lt ~]").gain("1.0 1.0 0.6 0.6").bank(bank_lt),
  s("[bd bd bd ~] ~ [~ bd]*2 [bd bd ~ bd]").gain("1.0 1.0 0.6 1.0 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_22
const kit = "RolandTR808";

$: s("~ ~ [oh ~]*2 ~").bank(kit)
$: s("~ [~ ~ hh hh] ~ ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ lt] [lt lt ~ ~] ~ [~ ~ lt ~]").gain("1.0 1.0 0.6 0.6").bank(kit)
$: s("[bd bd bd ~] ~ [~ bd]*2 [bd bd ~ bd]").gain("1.0 1.0 0.6 1.0 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_23
**Source:** drum-patterns

```js
// Title: TB03_PTN3_23
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ [~ ~ lt ~] [~ lt ~ ~] [lt ~ ~ ~]").gain("1.0 1.0 0.6").bank(bank_lt),
  s("[bd ~ ~ bd] [~ bd ~ ~] ~ ~").gain("1.0 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_23
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ [~ ~ lt ~] [~ lt ~ ~] [lt ~ ~ ~]").gain("1.0 1.0 0.6").bank(kit)
$: s("[bd ~ ~ bd] [~ bd ~ ~] ~ ~").gain("1.0 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN3_24
**Source:** drum-patterns

```js
// Title: TB03_PTN3_24
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ ht]").bank(bank_ht),
  s("[~ ~ oh ~] [~ oh ~ ~] ~ ~").bank(bank_oh),
  s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ lt] ~").bank(bank_lt),
  s("~ [bd ~]*2 [bd ~]*2 [~ bd ~ ~]").gain("1.0 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN3_24
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ ht]").bank(kit)
$: s("[~ ~ oh ~] [~ oh ~ ~] ~ ~").bank(kit)
$: s("[hh ~ ~ ~] ~ ~ ~").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ lt] ~").bank(kit)
$: s("~ [bd ~]*2 [bd ~]*2 [~ bd ~ ~]").gain("1.0 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN4_01
**Source:** drum-patterns

```js
// Title: TB03_PTN4_01
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ ht] [_ ~ ~ ~] ~").gain("1.0 0.6").bank(bank_ht),
  s("~ [~ ~ oh ~] ~ ~").bank(bank_oh),
  s("~ ~ ~ [lt _ _ _]").gain("1.0 0.6 0.6 0.6").bank(bank_lt),
  s("~ ~ [~ ~ lt _] ~").gain("1.0 0.6").bank(bank_lt),
  s("~ ~ [~ cp ~ ~] ~").bank(bank_cp),
  s("[bd bd _ bd] [bd _ ~ ~] ~ ~").gain("1.0 0.6 0.6 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_01
const kit = "RolandTR808";

$: s("~ [~ ~ ~ ht] [_ ~ ~ ~] ~").gain("1.0 0.6").bank(kit)
$: s("~ [~ ~ oh ~] ~ ~").bank(kit)
$: s("~ ~ ~ [lt _ _ _]").gain("1.0 0.6 0.6 0.6").bank(kit)
$: s("~ ~ [~ ~ lt _] ~").gain("1.0 0.6").bank(kit)
$: s("~ ~ [~ cp ~ ~] ~").bank(kit)
$: s("[bd bd _ bd] [bd _ ~ ~] ~ ~").gain("1.0 0.6 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN4_02
**Source:** drum-patterns

```js
// Title: TB03_PTN4_02
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ [~ ~ bd ~] ~").bank(bank_bd),
  s("[x _ _ x] [_ x ~ ~] ~ [x x _ ~]").gain("1.0 0.6 0.6 0.6 0.6 1.0 1.0 1.0 0.6").note(bass_key).octave(bass_octave).transpose(3).decay(0.2).sustain(0).sound(bass_synth),
  s("~ [~ ~ ~ x] [_ ~ ~ ~] [~ ~ ~ x]").note(bass_key).octave(bass_octave).transpose(1).decay(0.2).sustain(0).sound(bass_synth),
  s("~ ~ [~ x ~ ~] ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_02
const kit = "RolandTR808";

$: s("~ ~ [~ ~ bd ~] ~").bank(kit)
$: s("[x _ _ x] [_ x ~ ~] ~ [x x _ ~]").gain("1.0 0.6 0.6 0.6 0.6 1.0 1.0 1.0 0.6").note("c").octave(1).transpose(3).decay(0.2).sustain(0).sound("sawtooth")
$: s("~ [~ ~ ~ x] [_ ~ ~ ~] [~ ~ ~ x]").note("c").octave(1).transpose(1).decay(0.2).sustain(0).sound("sawtooth")
$: s("~ ~ [~ x ~ ~] ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_03
**Source:** drum-patterns

```js
// Title: TB03_PTN4_03
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ lt _ ~] [~ ~ lt ~]").gain("0.6 0.6 1.0").bank(bank_lt),
  s("[sd _ _ ~] [~ ~ sd _] ~ ~").gain("1.0 0.6 0.6 1.0 0.6").bank(bank_sd),
  s("[~ ~ ~ bd] [_ bd ~ ~] [bd ~ ~ bd] [bd _ ~ bd]").gain("0.6 0.6 1.0 1.0 1.0 0.6 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_03
const kit = "RolandTR808";

$: s("~ ~ [~ lt _ ~] [~ ~ lt ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("[sd _ _ ~] [~ ~ sd _] ~ ~").gain("1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ bd] [_ bd ~ ~] [bd ~ ~ bd] [bd _ ~ bd]").gain("0.6 0.6 1.0 1.0 1.0 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN4_04
**Source:** drum-patterns

```js
// Title: TB03_PTN4_04
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("~ ~ [~ ~ x _] ~").note(bass_key).octave(bass_octave).transpose(7).decay(0.2).sustain(0).sound(bass_synth),
  s("~ ~ ~ [~ ~ x _]").note(bass_key).octave(bass_octave).transpose(3).decay(0.2).sustain(0).sound(bass_synth),
  s("[~ ~ x _] [~ ~ x _] ~ ~").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_04
const kit = "RolandTR808";

$: s("~ ~ [~ ~ x _] ~").note("c").octave(1).transpose(7).decay(0.2).sustain(0).sound("sawtooth")
$: s("~ ~ ~ [~ ~ x _]").note("c").octave(1).transpose(3).decay(0.2).sustain(0).sound("sawtooth")
$: s("[~ ~ x _] [~ ~ x _] ~ ~").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_05
**Source:** drum-patterns

```js
// Title: TB03_PTN4_05
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"

stack(
  s("[lt _ _ lt] [_ _ ~ lt] [lt _ _ ~] [lt _ ~ ~]").gain("1.0 0.6 0.6 1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0 0.6").bank(bank_lt),
  s("~ ~ ~ [~ ~ cp ~]").bank(bank_cp),
  s("~ [~ ~ bd ~] [~ ~ ~ bd] ~").bank(bank_bd),
  s("~ ~ ~ [~ ~ ~ x]").note(bass_key).octave(bass_octave).decay(0.2).sustain(0).sound(bass_synth)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_05
const kit = "RolandTR808";

$: s("[lt _ _ lt] [_ _ ~ lt] [lt _ _ ~] [lt _ ~ ~]").gain("1.0 0.6 0.6 1.0 0.6 0.6 1.0 1.0 0.6 0.6 1.0 0.6").bank(kit)
$: s("~ ~ ~ [~ ~ cp ~]").bank(kit)
$: s("~ [~ ~ bd ~] [~ ~ ~ bd] ~").bank(kit)
$: s("~ ~ ~ [~ ~ ~ x]").note("c").octave(1).decay(0.2).sustain(0).sound("sawtooth")
```
</details>

### TB03_PTN4_06
**Source:** drum-patterns

```js
// Title: TB03_PTN4_06
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh ~ hh] [hh ~ ~ ~] ~ ~").gain("1.0 0.6 1.0 0.6").bank(bank_hh),
  s("~ [~ lt]*2 [lt ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_lt),
  s("~ ~ ~ [~ ~ ~ _]").bank(bank_lt),
  s("[~ ~ _ ~] [~ ~ _ ~] [~ bd _ bd] [bd _ bd ~]").gain("0.6 0.6 0.6 0.6 1.0 1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_06
const kit = "RolandTR808";

$: s("[hh hh ~ hh] [hh ~ ~ ~] ~ ~").gain("1.0 0.6 1.0 0.6").bank(kit)
$: s("~ [~ lt]*2 [lt ~ ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ ~ _]").bank(kit)
$: s("[~ ~ _ ~] [~ ~ _ ~] [~ bd _ bd] [bd _ bd ~]").gain("0.6 0.6 0.6 0.6 1.0 1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN4_07
**Source:** drum-patterns

```js
// Title: TB03_PTN4_07
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_cr = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ cb _] [_ ~ ~ ~]").bank(bank_cb),
  s("~ [~ cr ~ ~] ~ ~").bank(bank_cr),
  s("[bd _ _ bd] [~ ~ bd _] [bd _ ~ ~] [~ bd]*2").gain("1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_07
const kit = "RolandTR808";

$: s("~ ~ [~ ~ cb _] [_ ~ ~ ~]").bank(kit)
$: s("~ [~ cr ~ ~] ~ ~").bank(kit)
$: s("[bd _ _ bd] [~ ~ bd _] [bd _ ~ ~] [~ bd]*2").gain("1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN4_08
**Source:** drum-patterns

```js
// Title: TB03_PTN4_08
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_rd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ sd ~]").bank(bank_sd),
  s("~ ~ ~ [~ sd ~ ~]").bank(bank_sd),
  s("~ [rd _ ~ ~] ~ ~").gain("1.0 0.6").bank(bank_rd),
  s("[bd _ _ bd] [~ ~ bd _] [bd bd ~ bd] [_ ~ ~ bd]").gain("1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_08
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ sd ~]").bank(kit)
$: s("~ ~ ~ [~ sd ~ ~]").bank(kit)
$: s("~ [rd _ ~ ~] ~ ~").gain("1.0 0.6").bank(kit)
$: s("[bd _ _ bd] [~ ~ bd _] [bd bd ~ bd] [_ ~ ~ bd]").gain("1.0 0.6 0.6 0.6 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN4_09
**Source:** drum-patterns

```js
// Title: TB03_PTN4_09
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ lt lt lt]").gain("1.0 0.6 1.0").bank(bank_lt),
  s("~ [bd ~ ~ bd] [_ bd ~ bd] [_ ~ ~ ~]").gain("1.0 0.6 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_09
const kit = "RolandTR808";

$: s("~ ~ ~ [~ lt lt lt]").gain("1.0 0.6 1.0").bank(kit)
$: s("~ [bd ~ ~ bd] [_ bd ~ bd] [_ ~ ~ ~]").gain("1.0 0.6 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN4_10
**Source:** drum-patterns

```js
// Title: TB03_PTN4_10
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;

stack(
  s("hh*4 [_ hh hh ~] [hh hh hh ~] [hh ~ hh hh]").gain("0.6 1.0 1.0 0.6 0.6 0.6 0.6 1.0 1.0 0.6 1.0 0.6 0.6").bank(bank_hh),
  s("~ ~ [~ ~ ~ _] ~").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_10
const kit = "RolandTR808";

$: s("hh*4 [_ hh hh ~] [hh hh hh ~] [hh ~ hh hh]").gain("0.6 1.0 1.0 0.6 0.6 0.6 0.6 1.0 1.0 0.6 1.0 0.6 0.6").bank(kit)
$: s("~ ~ [~ ~ ~ _] ~").bank(kit)
```
</details>

### TB03_PTN4_11
**Source:** drum-patterns

```js
// Title: TB03_PTN4_11
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("~ ~ ~ [lt ~ ~ ~]").bank(bank_lt),
  s("~ [sd _ _ sd] [~ ~ sd _] [~ sd sd sd]").gain("1.0 0.6 0.6 0.6 1.0 0.6 1.0 0.6 1.0").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_11
const kit = "RolandTR808";

$: s("~ ~ ~ [lt ~ ~ ~]").bank(kit)
$: s("~ [sd _ _ sd] [~ ~ sd _] [~ sd sd sd]").gain("1.0 0.6 0.6 0.6 1.0 0.6 1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN4_12
**Source:** drum-patterns

```js
// Title: TB03_PTN4_12
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(bank_hh),
  s("~ [~ lt ~ ~] ~ ~").bank(bank_lt),
  s("[~ ~ sd ~] [sd ~ ~ sd] [sd ~ ~ ~] [~ ~ sd sd]").gain("0.6 1.0 0.6 0.6 0.6 0.6").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_12
const kit = "RolandTR808";

$: s("~ ~ [~ ~ ~ hh] ~").gain("0.85").bank(kit)
$: s("~ [~ lt ~ ~] ~ ~").bank(kit)
$: s("[~ ~ sd ~] [sd ~ ~ sd] [sd ~ ~ ~] [~ ~ sd sd]").gain("0.6 1.0 0.6 0.6 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN4_13
**Source:** drum-patterns

```js
// Title: TB03_PTN4_13
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ lt] ~ [lt ~ ~ ~] ~").bank(bank_lt),
  s("~ ~ ~ [cp ~ ~ ~]").bank(bank_cp),
  s("[bd ~ ~ ~] [~ bd bd ~] [~ ~ bd ~] [~ bd bd ~]").gain("1.0 0.6 1.0 0.6 1.0 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_13
const kit = "RolandTR808";

$: s("~ ~ [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("[~ ~ ~ lt] ~ [lt ~ ~ ~] ~").bank(kit)
$: s("~ ~ ~ [cp ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] [~ ~ bd ~] [~ bd bd ~]").gain("1.0 0.6 1.0 0.6 1.0 1.0").bank(kit)
```
</details>

### TB03_PTN4_14
**Source:** drum-patterns

```js
// Title: TB03_PTN4_14
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [_ ~ ~ ~] [_ ~ ~ ~] [_ ~ ~ ht]").gain("0.6 0.6 0.6 1.0").bank(bank_ht),
  s("~ ~ ~ [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[lt ~ ~ ~] ~ [~ ~ ~ lt] ~").bank(bank_lt),
  s("[~ ~ cp ~] ~ ~ ~").bank(bank_cp),
  s("[~ ~ ~ bd] [~ bd]*2 [~ bd ~ ~] ~").gain("1.0 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_14
const kit = "RolandTR808";

$: s("~ [_ ~ ~ ~] [_ ~ ~ ~] [_ ~ ~ ht]").gain("0.6 0.6 0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("[lt ~ ~ ~] ~ [~ ~ ~ lt] ~").bank(kit)
$: s("[~ ~ cp ~] ~ ~ ~").bank(kit)
$: s("[~ ~ ~ bd] [~ bd]*2 [~ bd ~ ~] ~").gain("1.0 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN4_15
**Source:** drum-patterns

```js
// Title: TB03_PTN4_15
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [hh _ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ ~ ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[bd ~]*2 [bd _ bd ~] [~ ~ bd ~] [bd _ bd ~]").gain("0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_15
const kit = "RolandTR808";

$: s("~ ~ [hh _ ~ ~] ~").gain("0.85").bank(kit)
$: s("~ ~ ~ [~ ~ ~ lt]").bank(kit)
$: s("[bd ~]*2 [bd _ bd ~] [~ ~ bd ~] [bd _ bd ~]").gain("0.6 1.0 0.6 0.6 1.0 0.6 1.0 0.6 0.6").bank(kit)
```
</details>

### TB03_PTN4_16
**Source:** drum-patterns

```js
// Title: TB03_PTN4_16
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;

stack(
  s("[cp _ cp _] [cp ~ cp _] [cp ~ cp cp] [_ cp ~ cp]").gain("1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 1.0 1.0").bank(bank_cp)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_16
const kit = "RolandTR808";

$: s("[cp _ cp _] [cp ~ cp _] [cp ~ cp cp] [_ cp ~ cp]").gain("1.0 0.6 0.6 0.6 0.6 1.0 0.6 0.6 0.6 0.6 0.6 1.0 1.0").bank(kit)
```
</details>

### TB03_PTN4_17
**Source:** drum-patterns

```js
// Title: TB03_PTN4_17
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ht ht]").gain("1.0 0.6").bank(bank_ht),
  s("~ ~ ~ [oh oh ~ ~]").gain("0.6 1.0").bank(bank_oh),
  s("~ [~ ~ ~ lt] ~ ~").bank(bank_lt),
  s("[~ ~ bd ~] [~ bd ~ ~] [~ ~ bd ~] ~").gain("1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_17
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ht ht]").gain("1.0 0.6").bank(kit)
$: s("~ ~ ~ [oh oh ~ ~]").gain("0.6 1.0").bank(kit)
$: s("~ [~ ~ ~ lt] ~ ~").bank(kit)
$: s("[~ ~ bd ~] [~ bd ~ ~] [~ ~ bd ~] ~").gain("1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN4_18
**Source:** drum-patterns

```js
// Title: TB03_PTN4_18
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_cp = bank_default;

stack(
  s("[~ ~ ~ ht] [ht ~ ~ ~] [~ ht ~ ~] [ht ~ ~ ~]").gain("0.6 1.0 1.0 0.6").bank(bank_ht),
  s("[~ ~ lt ~] [~ lt]*2 [~ ~ lt ~] [~ lt]*2").gain("0.6 1.0 0.6 0.6 1.0 1.0").bank(bank_lt),
  s("[cp cp ~ ~] [~ ~ cp ~] [cp ~ ~ cp] [~ ~ cp ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_cp)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_18
const kit = "RolandTR808";

$: s("[~ ~ ~ ht] [ht ~ ~ ~] [~ ht ~ ~] [ht ~ ~ ~]").gain("0.6 1.0 1.0 0.6").bank(kit)
$: s("[~ ~ lt ~] [~ lt]*2 [~ ~ lt ~] [~ lt]*2").gain("0.6 1.0 0.6 0.6 1.0 1.0").bank(kit)
$: s("[cp cp ~ ~] [~ ~ cp ~] [cp ~ ~ cp] [~ ~ cp ~]").gain("0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN4_19
**Source:** drum-patterns

```js
// Title: TB03_PTN4_19
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bon = bank_default;
let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [bon ~ ~ ~]").bank(bank_bon),
  s("~ ~ ~ [~ ~ rd rd]").bank(bank_rd),
  s("~ ~ [~ ~ ht ht] [~ _ ~ ~]").gain("1.0 0.6 0.6").bank(bank_ht),
  s("~ [~ ~ ~ oh] [~ oh ~ ~] ~").gain("0.6 1.0").bank(bank_oh),
  s("~ [lt ~ ~ ~] ~ ~").bank(bank_lt),
  s("[bd ~ bd _] [~ bd ~ ~] ~ ~").gain("0.6 0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_19
const kit = "RolandTR808";

$: s("~ ~ ~ [bon ~ ~ ~]").bank(kit)
$: s("~ ~ ~ [~ ~ rd rd]").bank(kit)
$: s("~ ~ [~ ~ ht ht] [~ _ ~ ~]").gain("1.0 0.6 0.6").bank(kit)
$: s("~ [~ ~ ~ oh] [~ oh ~ ~] ~").gain("0.6 1.0").bank(kit)
$: s("~ [lt ~ ~ ~] ~ ~").bank(kit)
$: s("[bd ~ bd _] [~ bd ~ ~] ~ ~").gain("0.6 0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN4_20
**Source:** drum-patterns

```js
// Title: TB03_PTN4_20
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ht ~]").bank(bank_ht),
  s("~ ~ [~ ~ oh _] [oh ~ ~ ~]").gain("0.6 0.6 1.0").bank(bank_oh),
  s("~ [~ ~ lt _] ~ ~").gain("1.0 0.6").bank(bank_lt),
  s("[~ ~ ~ bd] [~ bd ~ ~] [bd ~ ~ ~] ~").gain("0.6 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_20
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ht ~]").bank(kit)
$: s("~ ~ [~ ~ oh _] [oh ~ ~ ~]").gain("0.6 0.6 1.0").bank(kit)
$: s("~ [~ ~ lt _] ~ ~").gain("1.0 0.6").bank(kit)
$: s("[~ ~ ~ bd] [~ bd ~ ~] [bd ~ ~ ~] ~").gain("0.6 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN4_21
**Source:** drum-patterns

```js
// Title: TB03_PTN4_21
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_bon = bank_default;
let bank_rd = bank_default;
let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ bon ~ ~]").bank(bank_bon),
  s("~ ~ ~ [~ ~ rd ~]").bank(bank_rd),
  s("~ ~ [~ ~ ht ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ ~ oh] [_ oh ~ ~] ~").gain("1.0 0.6 1.0").bank(bank_oh),
  s("[~ ~ ~ lt] [_ ~ ~ ~] ~ ~").gain("1.0 0.6").bank(bank_lt),
  s("[bd bd ~ ~] [~ bd ~ ~] ~ ~").gain("1.0 0.6 1.0").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_21
const kit = "RolandTR808";

$: s("~ ~ ~ [~ bon ~ ~]").bank(kit)
$: s("~ ~ ~ [~ ~ rd ~]").bank(kit)
$: s("~ ~ [~ ~ ht ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ ~ oh] [_ oh ~ ~] ~").gain("1.0 0.6 1.0").bank(kit)
$: s("[~ ~ ~ lt] [_ ~ ~ ~] ~ ~").gain("1.0 0.6").bank(kit)
$: s("[bd bd ~ ~] [~ bd ~ ~] ~ ~").gain("1.0 0.6 1.0").bank(kit)
```
</details>

### TB03_PTN4_22
**Source:** drum-patterns

```js
// Title: TB03_PTN4_22
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ ~ ht]").bank(bank_ht),
  s("~ [~ ~ ~ oh] [_ _ _ _] [_ oh _ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(bank_oh),
  s("[~ ~ ~ lt] [_ ~ ~ ~] ~ ~").gain("1.0 0.6").bank(bank_lt),
  s("[bd _ bd ~] [~ bd _ ~] ~ ~").gain("0.6 0.6 0.6 1.0 0.6").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_22
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ ~ ht]").bank(kit)
$: s("~ [~ ~ ~ oh] [_ _ _ _] [_ oh _ ~]").gain("0.6 0.6 0.6 0.6 0.6 0.6 1.0 0.6").bank(kit)
$: s("[~ ~ ~ lt] [_ ~ ~ ~] ~ ~").gain("1.0 0.6").bank(kit)
$: s("[bd _ bd ~] [~ bd _ ~] ~ ~").gain("0.6 0.6 0.6 1.0 0.6").bank(kit)
```
</details>

### TB03_PTN4_23
**Source:** drum-patterns

```js
// Title: TB03_PTN4_23
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;

stack(
  s("[~ ~ ~ ht] [ht ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ oh ~] [oh ~ ~ ~] [_ _ ~ ~]").gain("1.0 1.0 0.6 0.6").bank(bank_oh),
  s("~ ~ [~ hh]*2 ~").gain("0.6 1.0").bank(bank_hh),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_23
const kit = "RolandTR808";

$: s("[~ ~ ~ ht] [ht ~ ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ oh ~] [oh ~ ~ ~] [_ _ ~ ~]").gain("1.0 1.0 0.6 0.6").bank(kit)
$: s("~ ~ [~ hh]*2 ~").gain("0.6 1.0").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
```
</details>

### TB03_PTN4_24
**Source:** drum-patterns

```js
// Title: TB03_PTN4_24
// Category: TB03 Patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_lt = bank_default;
let bank_bd = bank_default;

stack(
  s("[ht ht ~ ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[~ ~ oh oh] [_ ~ ~ ~] ~ ~").gain("1.0 1.0 0.6").bank(bank_oh),
  s("~ [~ hh hh _] ~ ~").gain("0.6 1.0 0.6").bank(bank_hh),
  s("~ ~ [lt lt _ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ ~ [~ ~ ~ bd] [_ bd _ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TB03_PTN4_24
const kit = "RolandTR808";

$: s("[ht ht ~ ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ oh oh] [_ ~ ~ ~] ~ ~").gain("1.0 1.0 0.6").bank(kit)
$: s("~ [~ hh hh _] ~ ~").gain("0.6 1.0 0.6").bank(kit)
$: s("~ ~ [lt lt _ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ ~ bd] [_ bd _ bd]").bank(kit)
```
</details>

---

## Techno

### OffBeat clap
**BPM:** 128
**Source:** DrumBeatRepo

```js
// Title: OffBeat clap
// Category: Techno
setcpm(128 / 4);
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ [cp ~ ~ ~] [~ ~ ~ cp] [cp ~ ~ ~]] [~ [cp ~ ~ ~] [~ ~ ~ cp] [cp ~ ~ ~]]").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - OffBeat clap
setcpm(128 / 4);
const kit = "RolandTR808";

$: s("[~ [cp ~ ~ ~] [~ ~ ~ cp] [cp ~ ~ ~]] [~ [cp ~ ~ ~] [~ ~ ~ cp] [cp ~ ~ ~]]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### 4 on the floor
**BPM:** 128
**Source:** DrumBeatRepo

```js
// Title: 4 on the floor
// Category: Techno
setcpm(128 / 4);
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - 4 on the floor
setcpm(128 / 4);
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

---

## Tidal patterns

### Afro6a
**Source:** drum-patterns

```js
// Title: Afro6a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ rim] [~ ~ rim ~] ~ [rim ~ ~ ~]").bank(bank_rim),
  s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro6a
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("[~ ~ ~ rim] [~ ~ rim ~] ~ [rim ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### Afro6b
**Source:** drum-patterns

```js
// Title: Afro6b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ht ~] ~ ~").bank(bank_ht),
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ rim] ~ ~ [rim ~ ~ ~]").bank(bank_rim),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro6b
const kit = "RolandTR808";

$: s("~ [~ ~ ht ~] ~ ~").bank(kit)
$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("[hh ~ hh hh] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("[~ ~ ~ rim] ~ ~ [rim ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Afro6c
**Source:** drum-patterns

```js
// Title: Afro6c
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ cr cr] [cr ~]*2 [cr ~]*2 [cr ~]*2").bank(bank_cr),
  s("~ ~ [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ ~ [~ ~ lt ~]").bank(bank_lt),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Afro6c
const kit = "RolandTR808";

$: s("[cr ~ cr cr] [cr ~]*2 [cr ~]*2 [cr ~]*2").bank(kit)
$: s("~ ~ [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt ~]").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [~ ~ rim ~] ~ ~").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### Ageispolis
**Source:** drum-patterns

```js
// Title: Ageispolis
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Ageispolis
const kit = "RolandTR808";

$: s("~ ~ [~ ~ oh ~] ~").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Amen
**Source:** drum-patterns

```js
// Title: Amen
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").bank(bank_sd),
  s("[bd ~]*2 ~ [~ ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Amen
const kit = "RolandTR808";

$: s("~ ~ [~ ~ oh ~] ~").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd bd] ~").bank(kit)
```
</details>

### AmenBrother
**Source:** drum-patterns

```js
// Title: AmenBrother
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("hh*8").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]] [~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]] [~ [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]] [~ [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]]").bank(bank_sd),
  s("[[bd ~]*2 ~ [~ ~ bd bd] ~] [[bd ~]*2 ~ [~ ~ bd ~] ~] [[bd ~]*2 ~ [~ ~ bd ~] ~] [[bd ~]*2 ~ [~ ~ bd ~] ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AmenBrother
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ [~ ~ oh ~] ~]").bank(kit)
$: s("hh*8").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]] [~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]] [~ [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]] [~ [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]]").bank(kit)
$: s("[[bd ~]*2 ~ [~ ~ bd bd] ~] [[bd ~]*2 ~ [~ ~ bd ~] ~] [[bd ~]*2 ~ [~ ~ bd ~] ~] [[bd ~]*2 ~ [~ ~ bd ~] ~]").gain("1.0 0.8").bank(kit)
```
</details>

### AshleysRoachClip
**Source:** drum-patterns

```js
// Title: AshleysRoachClip
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ht]*2 [~ ht]*2 [~ ht]*2 [~ ht]*2").bank(bank_ht),
  s("~ ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("lt*8").bank(bank_lt),
  s("[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - AshleysRoachClip
const kit = "RolandTR808";

$: s("[~ ht]*2 [~ ht]*2 [~ ht]*2 [~ ht]*2").bank(kit)
$: s("~ ~ [~ ~ oh ~] ~").bank(kit)
$: s("lt*8").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ bd bd ~] ~").bank(kit)
```
</details>

### Autobahn1a
**Source:** drum-patterns

```js
// Title: Autobahn1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*8").gain("0.9 0.6").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[cp ~]*2 [cp ~ cp cp] [~ cp]*2 [cp ~]*2").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("[rim ~]*2 [rim ~ rim rim] [~ rim]*2 [rim ~]*2").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~]*2 ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Autobahn1a
const kit = "RolandTR808";

$: s("oh*8").gain("0.9 0.6").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[cp ~]*2 [cp ~ cp cp] [~ cp]*2 [cp ~]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[rim ~]*2 [rim ~ rim rim] [~ rim]*2 [rim ~]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Autobahn1b
**Source:** drum-patterns

```js
// Title: Autobahn1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*8").gain("0.9 0.6").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[cp ~]*2 [cp ~ cp cp] [~ cp]*2 [cp ~]*2").gain("1.0 0.5 0.7 0.5").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("[rim ~]*2 [rim ~ rim rim] [~ rim]*2 [rim ~]*2").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~]*2 ~ [bd ~]*2 [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Autobahn1b
const kit = "RolandTR808";

$: s("oh*8").gain("0.9 0.6").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[cp ~]*2 [cp ~ cp cp] [~ cp]*2 [cp ~]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[rim ~]*2 [rim ~ rim rim] [~ rim]*2 [rim ~]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 ~ [bd ~]*2 [~ bd ~ ~]").bank(kit)
```
</details>

### BigBeat
**Source:** drum-patterns

```js
// Title: BigBeat
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BigBeat
const kit = "RolandTR808";

$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### BillyJean
**Source:** drum-patterns

```js
// Title: BillyJean
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BillyJean
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### BlueMonday1a
**Source:** drum-patterns

```js
// Title: BlueMonday1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BlueMonday1a
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### BlueMonday2a
**Source:** drum-patterns

```js
// Title: BlueMonday2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~ ~ hh] [hh ~ ~ hh] [hh ~ ~ hh] [hh ~ ~ hh]").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BlueMonday2a
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh ~ ~ hh] [hh ~ ~ hh] [hh ~ ~ hh] [hh ~ ~ hh]").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### BookOfMoses
**Source:** drum-patterns

```js
// Title: BookOfMoses
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2] [[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] ~] [[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BookOfMoses
const kit = "RolandTR808";

$: s("[[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2] [[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ bd] ~] [[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] ~]").bank(kit)
```
</details>

### Break1
**Source:** drum-patterns

```js
// Title: Break1
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh hh hh ~] [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Break1
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh hh hh ~] [hh ~]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Break2
**Source:** drum-patterns

```js
// Title: Break2
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ hh hh] [hh ~]*2 [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Break2
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ hh hh] [hh ~]*2 [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Breakbeat1
**Source:** drum-patterns

```js
// Title: Breakbeat1
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Breakbeat1
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Breakbeat2
**Source:** drum-patterns

```js
// Title: Breakbeat2
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Breakbeat2
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Breakbeat3
**Source:** drum-patterns

```js
// Title: Breakbeat3
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Breakbeat3
const kit = "RolandTR808";

$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### BritHouse
**Source:** drum-patterns

```js
// Title: BritHouse
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~]").bank(bank_cr),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - BritHouse
const kit = "RolandTR808";

$: s("[~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~] [~ ~ cr ~]").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh] [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### ChaChaCha1a
**Source:** drum-patterns

```js
// Title: ChaChaCha1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[~ ~ ht ~] [~ ~ ht ~] ~ ~").bank(bank_ht),
  s("~ ~ ~ [lt ~]*2").bank(bank_lt),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChaChaCha1a
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[~ ~ ht ~] [~ ~ ht ~] ~ ~").bank(kit)
$: s("~ ~ ~ [lt ~]*2").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### ChaChaCha1b
**Source:** drum-patterns

```js
// Title: ChaChaCha1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[~ ~ ht ht] ~ [~ ~ ht ht] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ lt lt] ~ [~ ~ lt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChaChaCha1b
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[~ ~ ht ht] ~ [~ ~ ht ht] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ lt lt] ~ [~ ~ lt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### ChugChugChugaLug
**Source:** drum-patterns

```js
// Title: ChugChugChugaLug
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~]*2 [hh hh hh ~] [hh hh hh ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ sd sd ~] [sd ~ ~ sd] [~ sd sd ~] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ bd]*2 [~ bd]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ChugChugChugaLug
const kit = "RolandTR808";

$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[hh ~]*2 [hh hh hh ~] [hh hh hh ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ sd sd ~] [sd ~ ~ sd] [~ sd sd ~] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ bd]*2 [~ bd]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### CissyStrutLong
**Source:** drum-patterns

```js
// Title: CissyStrutLong
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ [oh ~]*2] [~ ~ ~ [oh ~]*2]").bank(bank_oh),
  s("[~ [sd ~ ~ sd] [~ sd sd ~] ~] [[~ ~ sd ~] [~ sd sd ~] [sd sd ~ ~] ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[[bd ~ ~ bd] [~ bd ~ ~] [~ bd]*2 [bd ~]*2] [[bd ~ ~ bd] [~ ~ ~ bd] [~ bd]*2 [bd ~]*2]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - CissyStrutLong
const kit = "RolandTR808";

$: s("[~ ~ ~ [oh ~]*2] [~ ~ ~ [oh ~]*2]").bank(kit)
$: s("[~ [sd ~ ~ sd] [~ sd sd ~] ~] [[~ ~ sd ~] [~ sd sd ~] [sd sd ~ ~] ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[[bd ~ ~ bd] [~ bd ~ ~] [~ bd]*2 [bd ~]*2] [[bd ~ ~ bd] [~ ~ ~ bd] [~ bd]*2 [bd ~]*2]").gain("1.0 0.8").bank(kit)
```
</details>

### CissyStrutShort
**Source:** drum-patterns

```js
// Title: CissyStrutShort
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [oh ~]*2").bank(bank_oh),
  s("[hh hh hh ~] [hh ~ hh hh] [~ hh hh ~] [hh ~]*2").gain("0.85").bank(bank_hh),
  s("[sd sd sd ~] [sd ~ sd sd] [~ sd sd ~] [sd ~]*2").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ bd ~ ~] [bd bd ~ bd] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - CissyStrutShort
const kit = "RolandTR808";

$: s("~ ~ ~ [oh ~]*2").bank(kit)
$: s("[hh hh hh ~] [hh ~ hh hh] [~ hh hh ~] [hh ~]*2").gain("0.85").bank(kit)
$: s("[sd sd sd ~] [sd ~ sd sd] [~ sd sd ~] [sd ~]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ bd ~ ~] [bd bd ~ bd] [~ bd ~ ~]").bank(kit)
```
</details>

### ColdSweat
**Source:** drum-patterns

```js
// Title: ColdSweat
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] ~ [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ColdSweat
const kit = "RolandTR808";

$: s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(kit)
$: s("[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### ColdSweatOpening
**Source:** drum-patterns

```js
// Title: ColdSweatOpening
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*8").gain("0.9 0.6").bank(bank_oh),
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ sd]").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ColdSweatOpening
const kit = "RolandTR808";

$: s("oh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ sd]").bank(kit)
$: s("[bd ~]*2 ~ [bd ~]*2 ~").bank(kit)
```
</details>

### ComeDancing
**Source:** drum-patterns

```js
// Title: ComeDancing
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*32").gain("0.85").bank(bank_hh),
  s("[~ sd sd ~] [sd sd sd ~] [~ sd sd ~] [sd sd sd ~] [~ sd ~ ~] [sd sd ~ ~] [~ sd ~ ~] [sd sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ bd]*2 [bd ~ ~ ~] [~ ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ComeDancing
const kit = "RolandTR808";

$: s("hh*32").gain("0.85").bank(kit)
$: s("[~ sd sd ~] [sd sd sd ~] [~ sd sd ~] [sd sd sd ~] [~ sd ~ ~] [sd sd ~ ~] [~ sd ~ ~] [sd sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ bd]*2 [bd ~ ~ ~] [~ ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### ContemporaryKick1a
**Source:** drum-patterns

```js
// Title: ContemporaryKick1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] ~ [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporaryKick1a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] ~ [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### ContemporaryKick1b
**Source:** drum-patterns

```js
// Title: ContemporaryKick1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ ~ bd ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporaryKick1b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[~ ~ bd ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### ContemporaryKick2a
**Source:** drum-patterns

```js
// Title: ContemporaryKick2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[~ ~ bd ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporaryKick2a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[~ ~ bd ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### ContemporaryKick2b
**Source:** drum-patterns

```js
// Title: ContemporaryKick2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ ~ bd ~] ~ [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporaryKick2b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[~ ~ bd ~] ~ [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### ContemporaryKick3b
**Source:** drum-patterns

```js
// Title: ContemporaryKick3b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporaryKick3b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### ContemporaryKick4
**Source:** drum-patterns

```js
// Title: ContemporaryKick4
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporaryKick4
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### ContemporarySnare1a
**Source:** drum-patterns

```js
// Title: ContemporarySnare1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ sd ~ ~] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporarySnare1a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ sd ~ ~] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### ContemporarySnare1b
**Source:** drum-patterns

```js
// Title: ContemporarySnare1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ sd ~] [~ sd ~ ~] [~ sd ~ ~]").bank(bank_sd),
  s("[~ ~ bd ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporarySnare1b
const kit = "RolandTR808";

$: s("~ [~ ~ sd ~] [~ sd ~ ~] [~ sd ~ ~]").bank(kit)
$: s("[~ ~ bd ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### ContemporarySnare2b
**Source:** drum-patterns

```js
// Title: ContemporarySnare2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[~ ~ bd ~] ~ [~ ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporarySnare2b
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[~ ~ bd ~] ~ [~ ~ bd bd] ~").bank(kit)
```
</details>

### ContemporarySnare3a
**Source:** drum-patterns

```js
// Title: ContemporarySnare3a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ ~ sd ~] [~ sd]*2").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporarySnare3a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ ~ sd ~] [~ sd]*2").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(kit)
```
</details>

### ContemporarySnare3b
**Source:** drum-patterns

```js
// Title: ContemporarySnare3b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ContemporarySnare3b
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(kit)
```
</details>

### CowdBell
**Source:** drum-patterns

```js
// Title: CowdBell
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~ cb cb] [cb ~ cb cb] [cb ~ cb cb] [cb ~ cb cb]").bank(bank_cb),
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd bd] [~ ~ bd bd] [~ bd]*2").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - CowdBell
const kit = "RolandTR808";

$: s("[cb ~ cb cb] [cb ~ cb cb] [cb ~ cb cb] [cb ~ cb cb]").bank(kit)
$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd bd] [~ ~ bd bd] [~ bd]*2").gain("1.0 0.8").bank(kit)
```
</details>

### DasModel1b
**Source:** drum-patterns

```js
// Title: DasModel1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ [sd ~]*2").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DasModel1b
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ [sd ~ ~ ~] ~ [sd ~]*2").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### DeepHouse
**Source:** drum-patterns

```js
// Title: DeepHouse
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("~ cp ~ cp").bank(bank_cp),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ hh ~ ~] [~ ~ ~ hh] [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DeepHouse
const kit = "RolandTR808";

$: s("~ cp ~ cp").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[~ hh ~ ~] [~ ~ ~ hh] [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### DeeperHouse
**Source:** drum-patterns

```js
// Title: DeeperHouse
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ hh] ~ [hh ~ ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[~ cp ~ ~] ~ [~ cp ~ ~] ~").bank(bank_cp),
  s("[~ ~ mt ~] [~ ~ ~ mt] [~ ~ mt ~] ~").bank(bank_mt),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh oh] [~ ~ oh ~]").bank(bank_oh),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DeeperHouse
const kit = "RolandTR808";

$: s("[~ ~ ~ hh] ~ [hh ~ ~ ~] ~").gain("0.85").bank(kit)
$: s("[~ cp ~ ~] ~ [~ cp ~ ~] ~").bank(kit)
$: s("[~ ~ mt ~] [~ ~ ~ mt] [~ ~ mt ~] ~").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh oh] [~ ~ oh ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### DirtyHouse
**Source:** drum-patterns

```js
// Title: DirtyHouse
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ cp ~] [cp ~ ~ ~] [cp ~]*2 [cp ~ ~ ~]").bank(bank_cp),
  s("[~ ~ oh ~] ~ [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [~ ~ hh ~] [~ ~ ~ hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [bd ~ ~ ~] [bd ~]*2 [bd ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DirtyHouse
const kit = "RolandTR808";

$: s("[~ ~ cp ~] [cp ~ ~ ~] [cp ~]*2 [cp ~ ~ ~]").bank(kit)
$: s("[~ ~ oh ~] ~ [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ ~ [~ ~ hh ~] [~ ~ ~ hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [bd ~ ~ ~] [bd ~]*2 [bd ~ ~ bd]").bank(kit)
```
</details>

### Disco2a
**Source:** drum-patterns

```js
// Title: Disco2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco2a
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco2b
**Source:** drum-patterns

```js
// Title: Disco2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[hh ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco2b
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[hh ~ hh hh] [~ ~ hh hh] [~ ~ hh hh] [~ ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Disco3c
**Source:** drum-patterns

```js
// Title: Disco3c
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cb ~ cb cb]").bank(bank_cb),
  s("~ ~ [mt ~ ~ mt] ~").bank(bank_mt),
  s("hh*4 ~ ~ ~").gain("0.85").bank(bank_hh),
  s("~ [sd ~ sd sd] [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Disco3c
const kit = "RolandTR808";

$: s("~ ~ ~ [cb ~ cb cb]").bank(kit)
$: s("~ ~ [mt ~ ~ mt] ~").bank(kit)
$: s("hh*4 ~ ~ ~").gain("0.85").bank(kit)
$: s("~ [sd ~ sd sd] [~ sd sd ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Dnb1a
**Source:** drum-patterns

```js
// Title: Dnb1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd bd ~] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dnb1a
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd bd ~] [~ ~ ~ bd]").bank(kit)
```
</details>

### Dnb1b
**Source:** drum-patterns

```js
// Title: Dnb1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [bd bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dnb1b
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [bd bd bd ~] ~").bank(kit)
```
</details>

### Dnb2a
**Source:** drum-patterns

```js
// Title: Dnb2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dnb2a
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Dnb3
**Source:** drum-patterns

```js
// Title: Dnb3
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ oh oh] [oh oh ~ ~] ~").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dnb3
const kit = "RolandTR808";

$: s("~ [~ ~ oh oh] [oh oh ~ ~] ~").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Dnb4a
**Source:** drum-patterns

```js
// Title: Dnb4a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dnb4a
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Dnb4b
**Source:** drum-patterns

```js
// Title: Dnb4b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("~ [bd ~ ~ ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dnb4b
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("~ [bd ~ ~ ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Drumroll1
**Source:** drum-patterns

```js
// Title: Drumroll1
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ [ht ht ht ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("~ ~ [~ ~ ~ mt] [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll1
const kit = "RolandTR808";

$: s("~ ~ [ht ht ht ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ [~ ~ ~ mt] [mt mt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Drumroll10
**Source:** drum-patterns

```js
// Title: Drumroll10
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ht ~ ~] ~ ~ [~ ht ~ ~]").bank(bank_ht),
  s("~ [mt ~ ~ mt] ~ ~").bank(bank_mt),
  s("~ ~ [~ ~ lt ~] [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[sd ~ ~ sd] [~ ~ sd ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll10
const kit = "RolandTR808";

$: s("[~ ht ~ ~] ~ ~ [~ ht ~ ~]").bank(kit)
$: s("~ [mt ~ ~ mt] ~ ~").bank(kit)
$: s("~ ~ [~ ~ lt ~] [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd ~ ~ sd] [~ ~ sd ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[~ ~ bd ~] [~ bd ~ ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Drumroll11
**Source:** drum-patterns

```js
// Title: Drumroll11
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] ~ [~ ht ~ ~] ~").bank(bank_ht),
  s("~ [cr ~]*2 ~ ~").bank(bank_cr),
  s("~ ~ [~ ~ mt ~] [mt ~ ~ ~]").bank(bank_mt),
  s("~ ~ [~ ~ ~ lt] [~ lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[sd sd ~ ~] ~ [sd ~ ~ ~] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ [bd ~]*2 ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll11
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ [~ ht ~ ~] ~").bank(kit)
$: s("~ [cr ~]*2 ~ ~").bank(kit)
$: s("~ ~ [~ ~ mt ~] [mt ~ ~ ~]").bank(kit)
$: s("~ ~ [~ ~ ~ lt] [~ lt lt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd ~ ~] ~ [sd ~ ~ ~] [sd ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [bd ~]*2 ~ ~").bank(kit)
```
</details>

### Drumroll12
**Source:** drum-patterns

```js
// Title: Drumroll12
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ht ~ ~] ~ ~ ~").bank(bank_ht),
  s("~ [~ mt ~ ~] [~ mt ~ ~] ~").bank(bank_mt),
  s("~ ~ ~ [~ lt ~ ~]").bank(bank_lt),
  s("sd*4").bank(bank_sd),
  s("[~ ~ bd bd] [~ ~ bd bd] [~ ~ bd bd] [~ ~ bd bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll12
const kit = "RolandTR808";

$: s("[~ ht ~ ~] ~ ~ ~").bank(kit)
$: s("~ [~ mt ~ ~] [~ mt ~ ~] ~").bank(kit)
$: s("~ ~ ~ [~ lt ~ ~]").bank(kit)
$: s("sd*4").bank(kit)
$: s("[~ ~ bd bd] [~ ~ bd bd] [~ ~ bd bd] [~ ~ bd bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Drumroll13
**Source:** drum-patterns

```js
// Title: Drumroll13
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;

stack(
  s("~ ~ [~ ht ht ht] [ht ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("[~ ~ ~ mt] mt*4 [mt ~ ~ ~] [~ mt mt ~]").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[lt lt lt ~] ~ ~ [~ ~ ~ lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll13
const kit = "RolandTR808";

$: s("~ ~ [~ ht ht ht] [ht ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ mt] mt*4 [mt ~ ~ ~] [~ mt mt ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[lt lt lt ~] ~ ~ [~ ~ ~ lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Drumroll14
**Source:** drum-patterns

```js
// Title: Drumroll14
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ht ~ ~] ~ [~ ht ~ ~] ~").bank(bank_ht),
  s("[~ ~ ~ lt] [~ ~ ~ lt] [~ ~ ~ lt] [~ ~ ~ lt]").bank(bank_lt),
  s("sd*4").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll14
const kit = "RolandTR808";

$: s("[~ ht ~ ~] ~ [~ ht ~ ~] ~").bank(kit)
$: s("[~ ~ ~ lt] [~ ~ ~ lt] [~ ~ ~ lt] [~ ~ ~ lt]").bank(kit)
$: s("sd*4").bank(kit)
```
</details>

### Drumroll15
**Source:** drum-patterns

```js
// Title: Drumroll15
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [cr ~ ~ ~] [~ ~ cr ~] ~").bank(bank_cr),
  s("[~ ~ hh ~] ~ [hh ~ ~ ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[sd sd ~ ~] [~ ~ sd sd] ~ [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll15
const kit = "RolandTR808";

$: s("~ [cr ~ ~ ~] [~ ~ cr ~] ~").bank(kit)
$: s("[~ ~ hh ~] ~ [hh ~ ~ ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[sd sd ~ ~] [~ ~ sd sd] ~ [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Drumroll16
**Source:** drum-patterns

```js
// Title: Drumroll16
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ~ ht ht] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [cr ~ ~ ~] [~ ~ cr ~] ~").bank(bank_cr),
  s("~ ~ [mt mt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[sd sd ~ ~] [sd ~ sd sd] [~ ~ sd ~] sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll16
const kit = "RolandTR808";

$: s("[~ ~ ht ht] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [cr ~ ~ ~] [~ ~ cr ~] ~").bank(kit)
$: s("~ ~ [mt mt ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd ~ ~] [sd ~ sd sd] [~ ~ sd ~] sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Drumroll17
**Source:** drum-patterns

```js
// Title: Drumroll17
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] [~ ~ cr ~] ~ [cr ~ ~ ~]").bank(bank_cr),
  s("[sd ~ ~ ~] [~ ~ sd ~] ~ ~").bank(bank_sd),
  s("[~ ~ bd ~] [bd ~ ~ ~] [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll17
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] [~ ~ cr ~] ~ [cr ~ ~ ~]").bank(kit)
$: s("[sd ~ ~ ~] [~ ~ sd ~] ~ ~").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### Drumroll18
**Source:** drum-patterns

```js
// Title: Drumroll18
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ cr ~] [cr ~ ~ ~] [cr ~]*2 [~ ~ cr ~]").bank(bank_cr),
  s("[sd sd ~ ~] [~ ~ sd sd] ~ [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ bd ~] [bd ~ ~ ~] [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll18
const kit = "RolandTR808";

$: s("[~ ~ cr ~] [cr ~ ~ ~] [cr ~]*2 [~ ~ cr ~]").bank(kit)
$: s("[sd sd ~ ~] [~ ~ sd sd] ~ [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### Drumroll19
**Source:** drum-patterns

```js
// Title: Drumroll19
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ht ~] [ht ~ ~ ~] ~ ~").bank(bank_ht),
  s("~ ~ [cr ~ ~ ~] ~").bank(bank_cr),
  s("~ [~ ~ mt ~] ~ [~ ~ mt ~]").bank(bank_mt),
  s("~ ~ ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[sd ~ ~ ~] ~ [sd ~]*2 [~ sd ~ ~]").bank(bank_sd),
  s("[~ bd]*2 [~ bd]*2 [~ bd]*2 [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll19
const kit = "RolandTR808";

$: s("[~ ~ ht ~] [ht ~ ~ ~] ~ ~").bank(kit)
$: s("~ ~ [cr ~ ~ ~] ~").bank(kit)
$: s("~ [~ ~ mt ~] ~ [~ ~ mt ~]").bank(kit)
$: s("~ ~ ~ [~ ~ ~ lt]").bank(kit)
$: s("[sd ~ ~ ~] ~ [sd ~]*2 [~ sd ~ ~]").bank(kit)
$: s("[~ bd]*2 [~ bd]*2 [~ bd]*2 [bd ~ ~ ~]").bank(kit)
```
</details>

### Drumroll2
**Source:** drum-patterns

```js
// Title: Drumroll2
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd ~ sd sd] [sd ~ sd sd] [~ sd sd sd] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("~ ~ ~ [bd ~]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll2
const kit = "RolandTR808";

$: s("[sd ~ sd sd] [sd ~ sd sd] [~ sd sd sd] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [bd ~]*2").bank(kit)
```
</details>

### Drumroll3
**Source:** drum-patterns

```js
// Title: Drumroll3
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;

stack(
  s("[sd sd sd ~] [sd sd sd ~] [sd ~]*2 sd*4").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll3
const kit = "RolandTR808";

$: s("[sd sd sd ~] [sd sd sd ~] [sd ~]*2 sd*4").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Drumroll4
**Source:** drum-patterns

```js
// Title: Drumroll4
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] [~ ~ cr ~] ~ [cr ~ ~ ~]").bank(bank_cr),
  s("[~ ~ ~ sd] [sd ~ ~ sd] [sd ~ ~ ~] [~ ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll4
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] [~ ~ cr ~] ~ [cr ~ ~ ~]").bank(kit)
$: s("[~ ~ ~ sd] [sd ~ ~ sd] [sd ~ ~ ~] [~ ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### Drumroll5
**Source:** drum-patterns

```js
// Title: Drumroll5
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;

stack(
  s("[ht ~ ~ ~] ~ ~ ~").bank(bank_ht),
  s("~ [mt ~ ~ ~] [mt ~]*2 ~").bank(bank_mt),
  s("~ ~ ~ [lt ~]*2").bank(bank_lt)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll5
const kit = "RolandTR808";

$: s("[ht ~ ~ ~] ~ ~ ~").bank(kit)
$: s("~ [mt ~ ~ ~] [mt ~]*2 ~").bank(kit)
$: s("~ ~ ~ [lt ~]*2").bank(kit)
```
</details>

### Drumroll6
**Source:** drum-patterns

```js
// Title: Drumroll6
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ~ ht ~] ~ ~ ~").bank(bank_ht),
  s("[~ ~ ~ mt] [~ ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ [~ ~ lt lt] [~ lt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("sd*4").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll6
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ ~ ~").bank(kit)
$: s("[~ ~ ~ mt] [~ ~ mt mt] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [~ ~ lt lt] [~ lt ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("sd*4").bank(kit)
```
</details>

### Drumroll7
**Source:** drum-patterns

```js
// Title: Drumroll7
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ~ ht ~] ~ ~ ~").bank(bank_ht),
  s("~ [mt ~ ~ ~] [mt ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[sd ~ ~ ~] [~ ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll7
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ ~ ~").bank(kit)
$: s("~ [mt ~ ~ ~] [mt ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd ~ ~ ~] [~ ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
```
</details>

### Drumroll8
**Source:** drum-patterns

```js
// Title: Drumroll8
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ~ ht ~] ~ ~ ~").bank(bank_ht),
  s("~ [mt ~ ~ ~] [~ ~ mt ~] ~").bank(bank_mt),
  s("~ ~ ~ [lt ~]*2").bank(bank_lt),
  s("[sd sd ~ ~] [~ ~ sd ~] [sd sd ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll8
const kit = "RolandTR808";

$: s("[~ ~ ht ~] ~ ~ ~").bank(kit)
$: s("~ [mt ~ ~ ~] [~ ~ mt ~] ~").bank(kit)
$: s("~ ~ ~ [lt ~]*2").bank(kit)
$: s("[sd sd ~ ~] [~ ~ sd ~] [sd sd ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Drumroll9
**Source:** drum-patterns

```js
// Title: Drumroll9
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_ht = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_sd = bank_default;

stack(
  s("[~ ~ ht ht] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("~ [~ ~ mt mt] [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(bank_lt),
  s("[sd sd ~ ~] [sd sd ~ ~] [sd sd ~ ~] [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Drumroll9
const kit = "RolandTR808";

$: s("[~ ~ ht ht] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ [~ ~ mt mt] [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [~ ~ lt lt]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[sd sd ~ ~] [sd sd ~ ~] [sd sd ~ ~] [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
```
</details>

### Dubstep1a
**Source:** drum-patterns

```js
// Title: Dubstep1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [oh ~ ~ ~] ~ [~ oh ~ ~]").bank(bank_oh),
  s("[~ hh hh ~] [~ ~ hh ~] [~ ~ ~ hh] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dubstep1a
const kit = "RolandTR808";

$: s("~ [oh ~ ~ ~] ~ [~ oh ~ ~]").bank(kit)
$: s("[~ hh hh ~] [~ ~ hh ~] [~ ~ ~ hh] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Dubstep1b
**Source:** drum-patterns

```js
// Title: Dubstep1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [oh ~ ~ ~] ~ [~ oh ~ ~]").bank(bank_oh),
  s("[~ hh hh ~] [~ ~ hh ~] [~ ~ ~ hh] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Dubstep1b
const kit = "RolandTR808";

$: s("~ [oh ~ ~ ~] ~ [~ oh ~ ~]").bank(kit)
$: s("[~ hh hh ~] [~ ~ hh ~] [~ ~ ~ hh] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### DubstepRatcheted
**Source:** drum-patterns

```js
// Title: DubstepRatcheted
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[~ ~ oh oh] [oh oh ~ ~] [oh ~ ~ ~] ~] ~").bank(bank_oh),
  s("[~ hh hh ~] [~ ~ hh ~] [~ ~ ~ hh] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd sd] [sd ~]*2 ~ [~ ~ sd ~] [[~ sd ~ ~] ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - DubstepRatcheted
const kit = "RolandTR808";

$: s("[[~ ~ oh oh] [oh oh ~ ~] [oh ~ ~ ~] ~] ~").bank(kit)
$: s("[~ hh hh ~] [~ ~ hh ~] [~ ~ ~ hh] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ sd sd] [sd ~]*2 ~ [~ ~ sd ~] [[~ sd ~ ~] ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Electro1a
**Source:** drum-patterns

```js
// Title: Electro1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Electro1a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Electro1b
**Source:** drum-patterns

```js
// Title: Electro1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Electro1b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Electro2b
**Source:** drum-patterns

```js
// Title: Electro2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Electro2b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Electro3b
**Source:** drum-patterns

```js
// Title: Electro3b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ ~ bd] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Electro3b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ ~ bd] [~ bd ~ ~]").bank(kit)
```
</details>

### ExpensiveShit
**Source:** drum-patterns

```js
// Title: ExpensiveShit
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ [~ ~ ~ oh] ~] [[~ ~ ~ oh] ~ ~ ~]").bank(bank_oh),
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~]*2 [hh ~ hh hh] [hh ~]*2 [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[sd sd ~ sd] [~ sd ~ ~] [sd sd ~ ~] [sd sd ~ ~] [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ ~] [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ ~ bd] [~ ~ bd ~] ~ [~ ~ bd ~] [~ ~ ~ bd] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ExpensiveShit
const kit = "RolandTR808";

$: s("[~ ~ [~ ~ ~ oh] ~] [[~ ~ ~ oh] ~ ~ ~]").bank(kit)
$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~]*2 [hh ~ hh hh] [hh ~]*2 [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[sd sd ~ sd] [~ sd ~ ~] [sd sd ~ ~] [sd sd ~ ~] [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ ~] [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ bd] [~ ~ bd ~] ~ [~ ~ bd ~] [~ ~ ~ bd] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(kit)
```
</details>

### ExpressYourself
**Source:** drum-patterns

```js
// Title: ExpressYourself
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[hh ~ hh hh] hh*4 hh*4 hh*4] [[hh ~ hh hh] hh*4 hh*4 hh*4]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ sd] [~ sd]*2 [~ sd]*2] [~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ ~]]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [bd ~ ~ bd] ~ [bd ~ ~ bd] [~ ~ bd ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ExpressYourself
const kit = "RolandTR808";

$: s("[[hh ~ hh hh] hh*4 hh*4 hh*4] [[hh ~ hh hh] hh*4 hh*4 hh*4]").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ sd] [~ sd]*2 [~ sd]*2] [~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ ~]]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [bd ~ ~ bd] ~ [bd ~ ~ bd] [~ ~ bd ~]").gain("1.0 0.8").bank(kit)
```
</details>

### Footwork1
**Source:** drum-patterns

```js
// Title: Footwork1
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cp ~ ~ ~]").bank(bank_cp),
  s("[~ ~ hh ~] ~ [~ ~ hh ~] ~").gain("0.85").bank(bank_hh),
  s("rim*16").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Footwork1
const kit = "RolandTR808";

$: s("~ ~ ~ [cp ~ ~ ~]").bank(kit)
$: s("[~ ~ hh ~] ~ [~ ~ hh ~] ~").gain("0.85").bank(kit)
$: s("rim*16").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(kit)
```
</details>

### Footwork2
**Source:** drum-patterns

```js
// Title: Footwork2
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ ~ [cp ~ ~ ~]").bank(bank_cp),
  s("[~ ~ hh ~] [~ ~ ~ hh] [hh ~]*2 [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("rim*16").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Footwork2
const kit = "RolandTR808";

$: s("~ ~ ~ [cp ~ ~ ~]").bank(kit)
$: s("[~ ~ hh ~] [~ ~ ~ hh] [hh ~]*2 [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("rim*16").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~]").bank(kit)
```
</details>

### FourOnTheFloor
**Source:** drum-patterns

```js
// Title: FourOnTheFloor
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FourOnTheFloor
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### FrenchHouse
**Source:** drum-patterns

```js
// Title: FrenchHouse
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh hh ~] [hh ~ hh hh] hh*4 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("oh*8").gain("0.9 0.6").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FrenchHouse
const kit = "RolandTR808";

$: s("[hh hh hh ~] [hh ~ hh hh] hh*4 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("oh*8").gain("0.9 0.6").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### FunkyDrummer
**Source:** drum-patterns

```js
// Title: FunkyDrummer
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkyDrummer
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### FunkyDrummerAlt
**Source:** drum-patterns

```js
// Title: FunkyDrummerAlt
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ oh] ~ [~ oh ~ ~]").bank(bank_oh),
  s("hh*4 [hh hh hh ~] hh*4 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkyDrummerAlt
const kit = "RolandTR808";

$: s("~ [~ ~ ~ oh] ~ [~ oh ~ ~]").bank(kit)
$: s("hh*4 [hh hh hh ~] hh*4 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### FunkyPresident
**Source:** drum-patterns

```js
// Title: FunkyPresident
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [oh ~ ~ ~] [~ ~ oh ~] ~").bank(bank_oh),
  s("[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - FunkyPresident
const kit = "RolandTR808";

$: s("~ [oh ~ ~ ~] [~ ~ oh ~] ~").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd bd ~] ~").bank(kit)
```
</details>

### GenericBossaNova
**Source:** drum-patterns

```js
// Title: GenericBossaNova
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*16").gain("0.9 0.5 0.7 0.5").bank(bank_oh),
  s("[rim ~ ~ rim] [~ ~ rim ~] [~ ~ rim ~] [rim ~ ~ ~]").bank(bank_rim),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GenericBossaNova
const kit = "RolandTR808";

$: s("oh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[rim ~ ~ rim] [~ ~ rim ~] [~ ~ rim ~] [rim ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### GenericGahu
**Source:** drum-patterns

```js
// Title: GenericGahu
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GenericGahu
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### GenericRock
**Source:** drum-patterns

```js
// Title: GenericRock
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [bd ~]*2 [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GenericRock
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [bd ~]*2 [~ ~ bd ~]").bank(kit)
```
</details>

### GenericRumba
**Source:** drum-patterns

```js
// Title: GenericRumba
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*16").gain("0.9 0.5 0.7 0.5").bank(bank_oh),
  s("[rim ~ ~ rim] [~ ~ ~ rim] [~ ~ rim ~] [rim ~ ~ ~]").bank(bank_rim),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GenericRumba
const kit = "RolandTR808";

$: s("oh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[rim ~ ~ rim] [~ ~ ~ rim] [~ ~ rim ~] [rim ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### GenericShiko
**Source:** drum-patterns

```js
// Title: GenericShiko
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ ~] [hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GenericShiko
const kit = "RolandTR808";

$: s("[hh ~ ~ ~] [hh ~]*2 [~ ~ hh ~] [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim] [~ ~ rim rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [bd ~]*2 [bd ~ ~ ~] [bd ~]*2").bank(kit)
```
</details>

### GenericSoukous
**Source:** drum-patterns

```js
// Title: GenericSoukous
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh hh ~] ~").gain("0.85").bank(bank_hh),
  s("[rim ~ ~ rim] [~ ~ rim ~] [rim ~ ~ rim] [~ ~ rim ~]").bank(bank_rim),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GenericSoukous
const kit = "RolandTR808";

$: s("[hh ~ ~ hh] [~ ~ hh ~] [~ hh hh ~] ~").gain("0.85").bank(kit)
$: s("[rim ~ ~ rim] [~ ~ rim ~] [rim ~ ~ rim] [~ ~ rim ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2").bank(kit)
```
</details>

### GetUp
**Source:** drum-patterns

```js
// Title: GetUp
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[hh ~ ~ ~] [hh ~ hh hh] [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ [sd ~ sd sd] [~ sd ~ ~] [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GetUp
const kit = "RolandTR808";

$: s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(kit)
$: s("[hh ~ ~ ~] [hh ~ hh hh] [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(kit)
$: s("~ [sd ~ sd sd] [~ sd ~ ~] [sd ~ ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### GhostSnare1a
**Source:** drum-patterns

```js
// Title: GhostSnare1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;

stack(
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GhostSnare1a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]").bank(kit)
```
</details>

### GhostSnare1b
**Source:** drum-patterns

```js
// Title: GhostSnare1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;

stack(
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GhostSnare1b
const kit = "RolandTR808";

$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
```
</details>

### GhostSnare2a
**Source:** drum-patterns

```js
// Title: GhostSnare2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;

stack(
  s("[~ sd ~ ~] [sd ~ ~ sd] ~ [sd ~ ~ sd]").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GhostSnare2a
const kit = "RolandTR808";

$: s("[~ sd ~ ~] [sd ~ ~ sd] ~ [sd ~ ~ sd]").bank(kit)
```
</details>

### GhostSnare2b
**Source:** drum-patterns

```js
// Title: GhostSnare2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;

stack(
  s("[~ sd ~ ~] [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ sd]").bank(bank_sd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GhostSnare2b
const kit = "RolandTR808";

$: s("[~ sd ~ ~] [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ sd]").bank(kit)
```
</details>

### GoodToGo
**Source:** drum-patterns

```js
// Title: GoodToGo
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GoodToGo
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### GrooveMe
**Source:** drum-patterns

```js
// Title: GrooveMe
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd bd ~ bd] [~ bd]*2").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - GrooveMe
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd bd ~ bd] [~ bd]*2").gain("1.0 0.8").bank(kit)
```
</details>

### HaitianDivorce
**Source:** drum-patterns

```js
// Title: HaitianDivorce
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[hh hh ~ ~] hh*4 [hh hh ~ ~] hh*4").gain("0.85").bank(bank_hh),
  s("[~ sd ~ ~] [sd ~ sd sd] [~ sd ~ ~] [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HaitianDivorce
const kit = "RolandTR808";

$: s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(kit)
$: s("[hh hh ~ ~] hh*4 [hh hh ~ ~] hh*4").gain("0.85").bank(kit)
$: s("[~ sd ~ ~] [sd ~ sd sd] [~ sd ~ ~] [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~]").bank(kit)
```
</details>

### HalfDrop
**Source:** drum-patterns

```js
// Title: HalfDrop
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HalfDrop
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Haus
**Source:** drum-patterns

```js
// Title: Haus
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Haus
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### HipHop
**Source:** drum-patterns

```js
// Title: HipHop
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd bd] ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HipHop
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ bd bd] ~ [~ ~ bd ~]").bank(kit)
```
</details>

### Hiphop1a
**Source:** drum-patterns

```js
// Title: Hiphop1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop1a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ bd] [~ ~ bd ~]").bank(kit)
```
</details>

### Hiphop1b
**Source:** drum-patterns

```js
// Title: Hiphop1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop1b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Hiphop1c
**Source:** drum-patterns

```js
// Title: Hiphop1c
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop1c
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Hiphop2a
**Source:** drum-patterns

```js
// Title: Hiphop2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd bd ~ ~] [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop2a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd bd ~ ~] [~ bd]*2").bank(kit)
```
</details>

### Hiphop2b
**Source:** drum-patterns

```js
// Title: Hiphop2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop2b
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Hiphop3a
**Source:** drum-patterns

```js
// Title: Hiphop3a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop3a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Hiphop3b
**Source:** drum-patterns

```js
// Title: Hiphop3b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 ~ [bd bd ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop3b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 ~ [bd bd ~ bd] ~").bank(kit)
```
</details>

### Hiphop4a
**Source:** drum-patterns

```js
// Title: Hiphop4a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd bd ~] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop4a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ bd bd ~] [~ ~ ~ bd]").bank(kit)
```
</details>

### Hiphop4b
**Source:** drum-patterns

```js
// Title: Hiphop4b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [bd bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop4b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [bd bd bd ~] ~").bank(kit)
```
</details>

### Hiphop5
**Source:** drum-patterns

```js
// Title: Hiphop5
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop5
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd]").bank(kit)
```
</details>

### Hiphop6
**Source:** drum-patterns

```js
// Title: Hiphop6
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 ~ [~ ~ ~ bd] [bd ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop6
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ ~ bd] [bd ~ ~ bd]").bank(kit)
```
</details>

### Hiphop7
**Source:** drum-patterns

```js
// Title: Hiphop7
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd]*2").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop7
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] [~ bd]*2").bank(kit)
```
</details>

### Hiphop8
**Source:** drum-patterns

```js
// Title: Hiphop8
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh ~ hh] [hh ~ hh hh] [hh hh ~ hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [bd ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Hiphop8
const kit = "RolandTR808";

$: s("[hh hh ~ hh] [hh ~ hh hh] [hh hh ~ hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ bd bd] ~").bank(kit)
```
</details>

### HiphopAlt
**Source:** drum-patterns

```js
// Title: HiphopAlt
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd bd ~ ~] [bd ~ ~ ~] [bd bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HiphopAlt
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh] [~ ~ ~ oh]").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd bd ~ ~] [bd ~ ~ ~] [bd bd ~ ~]").bank(kit)
```
</details>

### HookAndSling
**Source:** drum-patterns

```js
// Title: HookAndSling
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ [~ ~ oh ~]]").bank(bank_oh),
  s("[[hh ~ hh hh] [~ hh ~ ~] [hh hh ~ hh] ~] [[hh hh ~ hh] [~ ~ hh ~] [hh hh ~ ~] [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ sd sd] [~ ~ sd ~] [sd ~ ~ ~]] [sd ~ ~ ~] [sd sd ~ sd] [~ ~ sd sd] [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~]*2 ~ [~ bd ~ ~] [~ bd bd ~] [~ ~ ~ [~ bd ~ ~]]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HookAndSling
const kit = "RolandTR808";

$: s("~ [~ ~ ~ [~ ~ oh ~]]").bank(kit)
$: s("[[hh ~ hh hh] [~ hh ~ ~] [hh hh ~ hh] ~] [[hh hh ~ hh] [~ ~ hh ~] [hh hh ~ ~] [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ [sd ~ sd sd] [~ ~ sd ~] [sd ~ ~ ~]] [sd ~ ~ ~] [sd sd ~ sd] [~ ~ sd sd] [~ ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 ~ [~ bd ~ ~] [~ bd bd ~] [~ ~ ~ [~ bd ~ ~]]").bank(kit)
```
</details>

### HotSweat
**Source:** drum-patterns

```js
// Title: HotSweat
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 [[hh ~ hh hh] [hh ~]*2 [hh ~ hh hh] [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ sd] [sd sd ~ ~] [sd ~ sd sd]] [~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [~ ~ bd bd] ~ [~ ~ bd bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HotSweat
const kit = "RolandTR808";

$: s("hh*8 [[hh ~ hh hh] [hh ~]*2 [hh ~ hh hh] [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ sd] [sd sd ~ ~] [sd ~ sd sd]] [~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [~ ~ bd bd] ~ [~ ~ bd bd] [~ ~ bd ~]").bank(kit)
```
</details>

### House1a
**Source:** drum-patterns

```js
// Title: House1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ ~] ~ ~ ~").bank(bank_cr),
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - House1a
const kit = "RolandTR808";

$: s("[cr ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### House1b
**Source:** drum-patterns

```js
// Title: House1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ oh ~ ~] [~ ~ oh ~] [~ oh ~ ~]").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - House1b
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ oh ~ ~] [~ ~ oh ~] [~ oh ~ ~]").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### HybridKick1a
**Source:** drum-patterns

```js
// Title: HybridKick1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HybridKick1a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### HybridKick1b
**Source:** drum-patterns

```js
// Title: HybridKick1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HybridKick1b
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### HybridKick1c
**Source:** drum-patterns

```js
// Title: HybridKick1c
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HybridKick1c
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### HybridKick1d
**Source:** drum-patterns

```js
// Title: HybridKick1d
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HybridKick1d
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### HybridKick1e
**Source:** drum-patterns

```js
// Title: HybridKick1e
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HybridKick1e
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ bd ~ ~] ~").bank(kit)
```
</details>

### HybridKick1g
**Source:** drum-patterns

```js
// Title: HybridKick1g
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd]*2 [~ bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HybridKick1g
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ bd]*2 [~ bd bd ~] ~").bank(kit)
```
</details>

### HybridKick2b
**Source:** drum-patterns

```js
// Title: HybridKick2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - HybridKick2b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### IGotTheFeelin
**Source:** drum-patterns

```js
// Title: IGotTheFeelin
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ sd ~ ~] [~ ~ sd ~]] [~ sd ~ ~] [sd sd ~ sd] [~ sd sd sd] [~ sd sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[[bd ~]*2 ~ [~ ~ bd ~] ~] [[~ ~ bd ~] ~ [bd ~ ~ ~] [bd ~]*2]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - IGotTheFeelin
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ sd ~ ~] [~ ~ sd ~]] [~ sd ~ ~] [sd sd ~ sd] [~ sd sd sd] [~ sd sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[[bd ~]*2 ~ [~ ~ bd ~] ~] [[~ ~ bd ~] ~ [bd ~ ~ ~] [bd ~]*2]").bank(kit)
```
</details>

### IGotYou
**Source:** drum-patterns

```js
// Title: IGotYou
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[~ ~ oh ~] ~ [~ ~ oh ~] ~] [[~ ~ oh ~] ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("[[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~]*2] [[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - IGotYou
const kit = "RolandTR808";

$: s("[[~ ~ oh ~] ~ [~ ~ oh ~] ~] [[~ ~ oh ~] ~ [~ ~ oh ~] ~]").bank(kit)
$: s("[[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~]*2] [[hh ~ ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] ~ [~ ~ bd ~] ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### ImpeachThePresident
**Source:** drum-patterns

```js
// Title: ImpeachThePresident
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[hh ~]*2 [hh ~ hh hh] [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ImpeachThePresident
const kit = "RolandTR808";

$: s("~ ~ [~ ~ oh ~] ~").bank(kit)
$: s("[hh ~]*2 [hh ~ hh hh] [hh ~ ~ ~] [hh ~]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Irregular1a
**Source:** drum-patterns

```js
// Title: Irregular1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ sd] ~ [sd ~ ~ sd]").bank(bank_sd),
  s("[bd ~ bd bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Irregular1a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ sd] ~ [sd ~ ~ sd]").bank(kit)
$: s("[bd ~ bd bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Irregular1b
**Source:** drum-patterns

```js
// Title: Irregular1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] ~ [sd ~ ~ sd]").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Irregular1b
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] ~ [sd ~ ~ sd]").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Irregular2a
**Source:** drum-patterns

```js
// Title: Irregular2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ sd] ~ ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Irregular2a
const kit = "RolandTR808";

$: s("[~ ~ ~ sd] ~ ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Irregular2b
**Source:** drum-patterns

```js
// Title: Irregular2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ sd] ~ [sd ~ ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Irregular2b
const kit = "RolandTR808";

$: s("[~ ~ ~ sd] ~ [sd ~ ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Irregular3
**Source:** drum-patterns

```js
// Title: Irregular3
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ sd ~ ~] [sd ~ ~ ~] [~ ~ sd ~] [~ sd ~ ~]").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Irregular3
const kit = "RolandTR808";

$: s("[~ sd ~ ~] [sd ~ ~ ~] [~ ~ sd ~] [~ sd ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] ~ [bd ~ ~ ~] [~ ~ bd ~]").bank(kit)
```
</details>

### ItaloDisco1a
**Source:** drum-patterns

```js
// Title: ItaloDisco1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~ ~ cb] [~ ~ cb ~] [cb ~ ~ ~] ~").bank(bank_cb),
  s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("cr*4").bank(bank_cr),
  s("[~ mt ~ ~] [~ ~ mt ~] [~ ~ mt ~] ~").bank(bank_mt),
  s("oh*16").gain("0.9 0.5 0.7 0.5").bank(bank_oh),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim] ~").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ItaloDisco1a
const kit = "RolandTR808";

$: s("[cb ~ ~ cb] [~ ~ cb ~] [cb ~ ~ ~] ~").bank(kit)
$: s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("cr*4").bank(kit)
$: s("[~ mt ~ ~] [~ ~ mt ~] [~ ~ mt ~] ~").bank(kit)
$: s("oh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[~ ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### ItaloDisco1b
**Source:** drum-patterns

```js
// Title: ItaloDisco1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_ht = bank_default;
let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~ ~ cb] [~ ~ cb ~] [cb ~]*2 [cb cb ~ ~]").bank(bank_cb),
  s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_ht),
  s("cr*4").bank(bank_cr),
  s("[~ mt ~ ~] [~ ~ mt ~] [~ ~ mt ~] ~").bank(bank_mt),
  s("oh*16").gain("0.9 0.5 0.7 0.5").bank(bank_oh),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("[~ ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim] ~").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ItaloDisco1b
const kit = "RolandTR808";

$: s("[cb ~ ~ cb] [~ ~ cb ~] [cb ~]*2 [cb cb ~ ~]").bank(kit)
$: s("~ ~ ~ [ht ht ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("cr*4").bank(kit)
$: s("[~ mt ~ ~] [~ ~ mt ~] [~ ~ mt ~] ~").bank(kit)
$: s("oh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[~ ~ ~ rim] [rim ~ ~ ~] [rim ~ ~ rim] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### ItsANewDay
**Source:** drum-patterns

```js
// Title: ItsANewDay
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 ~ [~ ~ bd bd] [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - ItsANewDay
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd bd] [~ ~ ~ bd]").bank(kit)
```
</details>

### Juke
**Source:** drum-patterns

```js
// Title: Juke
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ ~ [cp ~ ~ ~] ~").bank(bank_cp),
  s("[sd ~ sd sd] [~ sd]*2 [~ sd sd ~] [sd ~]*2").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Juke
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ ~ [cp ~ ~ ~] ~").bank(kit)
$: s("[sd ~ sd sd] [~ sd]*2 [~ sd sd ~] [sd ~]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Jungle
**Source:** drum-patterns

```js
// Title: Jungle
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ oh] [~ ~ oh ~] [~ ~ ~ oh] [~ ~ oh ~]").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [~ sd ~ ~] [~ sd]*2").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd ~ ~] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jungle
const kit = "RolandTR808";

$: s("[~ ~ ~ oh] [~ ~ oh ~] [~ ~ ~ oh] [~ ~ oh ~]").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [~ sd ~ ~] [~ sd]*2").bank(kit)
$: s("[bd ~ ~ ~] [~ bd ~ ~] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Jungle1a
**Source:** drum-patterns

```js
// Title: Jungle1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~]*2 ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jungle1a
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]").bank(kit)
$: s("[bd ~]*2 ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Jungle1b
**Source:** drum-patterns

```js
// Title: Jungle1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ ~] [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]").bank(bank_sd),
  s("[~ bd bd ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Jungle1b
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[~ sd ~ ~] [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]").bank(kit)
$: s("[~ bd bd ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### JungleAlt
**Source:** drum-patterns

```js
// Title: JungleAlt
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd ~ ~] [bd ~ ~ ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - JungleAlt
const kit = "RolandTR808";

$: s("~ [~ ~ oh ~] ~ [~ ~ oh ~]").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ bd ~ ~] [bd ~ ~ ~] [~ bd ~ ~]").bank(kit)
```
</details>

### Kick
**Source:** drum-patterns

```js
// Title: Kick
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_bd = bank_default;

stack(
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Kick
const kit = "RolandTR808";

$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### KissingMyLove
**Source:** drum-patterns

```js
// Title: KissingMyLove
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ [~ ~ oh ~]] [~ ~ ~ [~ ~ oh ~]]").bank(bank_oh),
  s("[hh*4 hh*4 hh*4 [hh hh ~ ~]] [hh*4 hh*4 hh*4 [hh hh ~ ~]]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]] [~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]]").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~ [~ ~ ~ bd] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - KissingMyLove
const kit = "RolandTR808";

$: s("[~ ~ ~ [~ ~ oh ~]] [~ ~ ~ [~ ~ oh ~]]").bank(kit)
$: s("[hh*4 hh*4 hh*4 [hh hh ~ ~]] [hh*4 hh*4 hh*4 [hh hh ~ ~]]").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]] [~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]]").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~ [~ ~ ~ bd] [~ bd ~ ~]").bank(kit)
```
</details>

### KnocksOffMyFeet
**Source:** drum-patterns

```js
// Title: KnocksOffMyFeet
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(bank_oh),
  s("[hh ~ ~ ~] [~ ~ hh hh] [~ hh ~ ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~]*2 [bd ~ ~ bd] [bd ~]*2 [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - KnocksOffMyFeet
const kit = "RolandTR808";

$: s("[~ ~ oh ~] ~ [~ ~ oh ~] ~").bank(kit)
$: s("[hh ~ ~ ~] [~ ~ hh hh] [~ hh ~ ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~]*2 [bd ~ ~ bd] [bd ~]*2 [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Lady
**Source:** drum-patterns

```js
// Title: Lady
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[~ ~ oh ~] [~ ~ oh ~] ~ ~] [[~ ~ oh ~] [~ ~ oh ~] ~ ~]").bank(bank_oh),
  s("[[~ ~ hh ~] [~ ~ hh ~] ~ ~] [[~ ~ hh ~] [~ ~ hh ~] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [sd sd ~ ~] ~ ~] [~ [sd sd ~ ~] [sd ~ ~ ~] ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~ [~ ~ ~ bd] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Lady
const kit = "RolandTR808";

$: s("[[~ ~ oh ~] [~ ~ oh ~] ~ ~] [[~ ~ oh ~] [~ ~ oh ~] ~ ~]").bank(kit)
$: s("[[~ ~ hh ~] [~ ~ hh ~] ~ ~] [[~ ~ hh ~] [~ ~ hh ~] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [sd sd ~ ~] ~ ~] [~ [sd sd ~ ~] [sd ~ ~ ~] ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] ~ [~ ~ ~ bd] [~ ~ bd ~]").bank(kit)
```
</details>

### LadyMarmalade
**Source:** drum-patterns

```js
// Title: LadyMarmalade
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ [sd ~ ~ ~] [sd ~ ~ ~] ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] [~ ~ ~ [bd ~ ~ ~]]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - LadyMarmalade
const kit = "RolandTR808";

$: s("~ [~ ~ [~ ~ oh ~] ~]").bank(kit)
$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ [sd ~ ~ ~] [sd ~ ~ ~] ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] [~ ~ ~ [bd ~ ~ ~]]").bank(kit)
```
</details>

### LetAWomanBeAWomanLetAManBeAMan
**Source:** drum-patterns

```js
// Title: LetAWomanBeAWomanLetAManBeAMan
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ ~ [~ ~ oh ~]] [~ ~ ~ [~ ~ oh ~]]").bank(bank_oh),
  s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ sd] [~ sd sd ~] [sd sd ~ ~]] [~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ ~]]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ bd ~] ~ [bd ~ bd bd] [~ bd bd ~] [~ ~ bd ~] ~ [~ ~ bd ~] [~ ~ bd ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - LetAWomanBeAWomanLetAManBeAMan
const kit = "RolandTR808";

$: s("[~ ~ ~ [~ ~ oh ~]] [~ ~ ~ [~ ~ oh ~]]").bank(kit)
$: s("[hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2 [hh ~]*2 [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ sd] [~ sd sd ~] [sd sd ~ ~]] [~ [sd ~ ~ sd] [~ sd]*2 [sd ~ ~ ~]]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd ~] ~ [bd ~ bd bd] [~ bd bd ~] [~ ~ bd ~] ~ [~ ~ bd ~] [~ ~ bd ~]").gain("1.0 0.8").bank(kit)
```
</details>

### LookingForThePerfectBeat1a
**Source:** drum-patterns

```js
// Title: LookingForThePerfectBeat1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~]*2 [~ cb]*2 [~ ~ ~ cb] [~ ~ cb ~]").bank(bank_cb),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("rim*4 [rim rim ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - LookingForThePerfectBeat1a
const kit = "RolandTR808";

$: s("[cb ~]*2 [~ cb]*2 [~ ~ ~ cb] [~ ~ cb ~]").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("rim*4 [rim rim ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ bd ~ ~]").bank(kit)
```
</details>

### LookingForThePerfectBeat1b
**Source:** drum-patterns

```js
// Title: LookingForThePerfectBeat1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~]*2 [~ cb]*2 [~ ~ ~ cb] [~ ~ cb ~]").bank(bank_cb),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("rim*4 [rim rim ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - LookingForThePerfectBeat1b
const kit = "RolandTR808";

$: s("[cb ~]*2 [~ cb]*2 [~ ~ ~ cb] [~ ~ cb ~]").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("rim*4 [rim rim ~ ~] ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Lookkapypy
**Source:** drum-patterns

```js
// Title: Lookkapypy
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ [~ ~ oh ~] ~] [~ ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("[[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2] [[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ ~] [sd ~ ~ sd] [sd ~]*2 [~ ~ sd ~] [~ sd ~ ~] [sd sd ~ sd] [sd ~]*2 [~ ~ sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ bd ~ ~] [~ ~ bd ~] [~ bd bd ~] [bd ~ ~ bd] [~ bd]*2 [bd ~]*2 [~ bd bd ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Lookkapypy
const kit = "RolandTR808";

$: s("[~ ~ [~ ~ oh ~] ~] [~ ~ [~ ~ oh ~] ~]").bank(kit)
$: s("[[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2] [[hh ~]*2 [hh ~]*2 [hh ~ ~ ~] [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ sd ~ ~] [sd ~ ~ sd] [sd ~]*2 [~ ~ sd ~] [~ sd ~ ~] [sd sd ~ sd] [sd ~]*2 [~ ~ sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ bd ~ ~] [~ ~ bd ~] [~ bd bd ~] [bd ~ ~ bd] [~ bd]*2 [bd ~]*2 [~ bd bd ~]").gain("1.0 0.8").bank(kit)
```
</details>

### MiamiBass1
**Source:** drum-patterns

```js
// Title: MiamiBass1
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MiamiBass1
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### MiamiBass2
**Source:** drum-patterns

```js
// Title: MiamiBass2
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MiamiBass2
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### MoreBounceToTheOunce
**Source:** drum-patterns

```js
// Title: MoreBounceToTheOunce
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ cr ~ cr").bank(bank_cr),
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("[~ ~ hh ~] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MoreBounceToTheOunce
const kit = "RolandTR808";

$: s("~ cr ~ cr").bank(kit)
$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[~ ~ hh ~] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd bd ~ ~] ~").bank(kit)
```
</details>

### MotherPopcorn
**Source:** drum-patterns

```js
// Title: MotherPopcorn
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*4 hh*4").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]] [~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[[bd ~]*2 ~ [~ ~ bd ~] ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MotherPopcorn
const kit = "RolandTR808";

$: s("hh*4 hh*4").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ sd] [~ sd ~ ~] [~ ~ sd ~]] [~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[[bd ~]*2 ~ [~ ~ bd ~] ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### MusicNonStop1a
**Source:** drum-patterns

```js
// Title: MusicNonStop1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*8").gain("0.9 0.6").bank(bank_oh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MusicNonStop1a
const kit = "RolandTR808";

$: s("oh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### MusicNonStop2a
**Source:** drum-patterns

```js
// Title: MusicNonStop2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*8").gain("0.9 0.6").bank(bank_oh),
  s("[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[rim rim rim ~] [~ rim ~ ~] [rim ~ ~ rim] [~ rim rim ~]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MusicNonStop2a
const kit = "RolandTR808";

$: s("oh*8").gain("0.9 0.6").bank(kit)
$: s("[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[rim rim rim ~] [~ rim ~ ~] [rim ~ ~ rim] [~ rim rim ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### MusicNonStop2b
**Source:** drum-patterns

```js
// Title: MusicNonStop2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("oh*8").gain("0.9 0.6").bank(bank_oh),
  s("[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[rim ~]*2 [rim rim ~ ~] [rim ~ ~ rim] [~ rim rim rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - MusicNonStop2b
const kit = "RolandTR808";

$: s("oh*8").gain("0.9 0.6").bank(kit)
$: s("[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[rim ~]*2 [rim rim ~ ~] [rim ~ ~ rim] [~ rim rim rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ ~] [~ ~ bd bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### NewWave
**Source:** drum-patterns

```js
// Title: NewWave
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[~ ~ oh ~] ~ ~ ~").bank(bank_oh),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [bd bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - NewWave
const kit = "RolandTR808";

$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[~ ~ oh ~] ~ ~ ~").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [bd bd ~ ~] ~").bank(kit)
```
</details>

### Nico
**Source:** drum-patterns

```js
// Title: Nico
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ hh ~ hh").gain("0.85").bank(bank_hh),
  s("[~ ~ rim rim] [~ rim rim rim] [rim ~ ~ rim] [~ rim rim rim]").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd bd ~ ~] ~ [~ bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Nico
const kit = "RolandTR808";

$: s("~ hh ~ hh").gain("0.85").bank(kit)
$: s("[~ ~ rim rim] [~ rim rim rim] [rim ~ ~ rim] [~ rim rim rim]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ ~] ~ [~ bd bd ~] ~").bank(kit)
```
</details>

### Numbers1a
**Source:** drum-patterns

```js
// Title: Numbers1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] hh*4 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Numbers1a
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] hh*4 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Numbers1b
**Source:** drum-patterns

```js
// Title: Numbers1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh hh ~ hh] hh*4 [hh hh ~ hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Numbers1b
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh hh ~ hh] hh*4 [hh hh ~ hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### OneDrop
**Source:** drum-patterns

```js
// Title: OneDrop
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("~ ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - OneDrop
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("~ ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### OneSevenFiveThirteen
**Source:** drum-patterns

```js
// Title: OneSevenFiveThirteen
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] ~ [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - OneSevenFiveThirteen
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] ~ [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### OohChild
**Source:** drum-patterns

```js
// Title: OohChild
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd] [[~ sd]*2 [sd sd ~ sd] [~ sd ~ ~] [sd ~]*2]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[[bd ~]*2 ~ [bd ~ bd bd] ~] [[bd ~ bd bd] ~ [bd ~ bd bd] ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - OohChild
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("[hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~] [hh hh ~ ~]").gain("0.85").bank(kit)
$: s("[~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd] [[~ sd]*2 [sd sd ~ sd] [~ sd ~ ~] [sd ~]*2]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[[bd ~]*2 ~ [bd ~ bd bd] ~] [[bd ~ bd bd] ~ [bd ~ bd bd] ~]").gain("1.0 0.8").bank(kit)
```
</details>

### PalmGrease
**Source:** drum-patterns

```js
// Title: PalmGrease
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ [~ ~ oh ~] ~] ~").bank(bank_oh),
  s("[hh*4 [~ hh hh ~] [hh ~ hh hh] [~ hh hh ~]] [[hh ~]*2 ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]] [~ sd ~ ~] [~ ~ sd ~] ~ [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ ~ bd] [[~ ~ bd ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PalmGrease
const kit = "RolandTR808";

$: s("[~ ~ [~ ~ oh ~] ~] ~").bank(kit)
$: s("[hh*4 [~ hh hh ~] [hh ~ hh hh] [~ hh hh ~]] [[hh ~]*2 ~ ~ ~]").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]] [~ sd ~ ~] [~ ~ sd ~] ~ [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [bd ~ ~ ~] [~ ~ ~ bd] [[~ ~ bd ~] ~ ~ ~]").bank(kit)
```
</details>

### PapaWasToo
**Source:** drum-patterns

```js
// Title: PapaWasToo
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [lt ~ ~ ~] ~ ~").bank(bank_lt),
  s("~ [hh ~ ~ ~] [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PapaWasToo
const kit = "RolandTR808";

$: s("~ [lt ~ ~ ~] ~ ~").bank(kit)
$: s("~ [hh ~ ~ ~] [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd]").bank(kit)
```
</details>

### Pattern00
**Source:** drum-patterns

```js
// Title: Pattern00
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern00
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern01
**Source:** drum-patterns

```js
// Title: Pattern01
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern01
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern02
**Source:** drum-patterns

```js
// Title: Pattern02
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern02
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern03
**Source:** drum-patterns

```js
// Title: Pattern03
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern03
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern04
**Source:** drum-patterns

```js
// Title: Pattern04
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern04
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern05
**Source:** drum-patterns

```js
// Title: Pattern05
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern05
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern06
**Source:** drum-patterns

```js
// Title: Pattern06
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern06
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern07
**Source:** drum-patterns

```js
// Title: Pattern07
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern07
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern08
**Source:** drum-patterns

```js
// Title: Pattern08
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern08
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern09
**Source:** drum-patterns

```js
// Title: Pattern09
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern09
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern10
**Source:** drum-patterns

```js
// Title: Pattern10
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern10
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern11
**Source:** drum-patterns

```js
// Title: Pattern11
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern11
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern12
**Source:** drum-patterns

```js
// Title: Pattern12
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern12
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern13
**Source:** drum-patterns

```js
// Title: Pattern13
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern13
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern14
**Source:** drum-patterns

```js
// Title: Pattern14
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern14
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern15
**Source:** drum-patterns

```js
// Title: Pattern15
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern15
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern16
**Source:** drum-patterns

```js
// Title: Pattern16
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern16
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern17
**Source:** drum-patterns

```js
// Title: Pattern17
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern17
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern18
**Source:** drum-patterns

```js
// Title: Pattern18
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern18
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern19
**Source:** drum-patterns

```js
// Title: Pattern19
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern19
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern20
**Source:** drum-patterns

```js
// Title: Pattern20
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern20
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern21
**Source:** drum-patterns

```js
// Title: Pattern21
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern21
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern22
**Source:** drum-patterns

```js
// Title: Pattern22
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern22
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern23
**Source:** drum-patterns

```js
// Title: Pattern23
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern23
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern24
**Source:** drum-patterns

```js
// Title: Pattern24
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern24
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern25
**Source:** drum-patterns

```js
// Title: Pattern25
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern25
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern26
**Source:** drum-patterns

```js
// Title: Pattern26
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern26
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern27
**Source:** drum-patterns

```js
// Title: Pattern27
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern27
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### Pattern28
**Source:** drum-patterns

```js
// Title: Pattern28
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern28
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern29
**Source:** drum-patterns

```js
// Title: Pattern29
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern29
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern30
**Source:** drum-patterns

```js
// Title: Pattern30
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern30
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern31
**Source:** drum-patterns

```js
// Title: Pattern31
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern31
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] ~ ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### Pattern32
**Source:** drum-patterns

```js
// Title: Pattern32
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern32
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern33
**Source:** drum-patterns

```js
// Title: Pattern33
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern33
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern34
**Source:** drum-patterns

```js
// Title: Pattern34
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern34
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern35
**Source:** drum-patterns

```js
// Title: Pattern35
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern35
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern36
**Source:** drum-patterns

```js
// Title: Pattern36
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern36
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern37
**Source:** drum-patterns

```js
// Title: Pattern37
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern37
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern38
**Source:** drum-patterns

```js
// Title: Pattern38
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern38
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern39
**Source:** drum-patterns

```js
// Title: Pattern39
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern39
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern40
**Source:** drum-patterns

```js
// Title: Pattern40
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern40
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern41
**Source:** drum-patterns

```js
// Title: Pattern41
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern41
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern42
**Source:** drum-patterns

```js
// Title: Pattern42
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern42
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern43
**Source:** drum-patterns

```js
// Title: Pattern43
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern43
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern44
**Source:** drum-patterns

```js
// Title: Pattern44
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern44
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern45
**Source:** drum-patterns

```js
// Title: Pattern45
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern45
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern46
**Source:** drum-patterns

```js
// Title: Pattern46
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern46
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern47
**Source:** drum-patterns

```js
// Title: Pattern47
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern47
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern48
**Source:** drum-patterns

```js
// Title: Pattern48
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern48
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern49
**Source:** drum-patterns

```js
// Title: Pattern49
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern49
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern50
**Source:** drum-patterns

```js
// Title: Pattern50
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern50
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern51
**Source:** drum-patterns

```js
// Title: Pattern51
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern51
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern52
**Source:** drum-patterns

```js
// Title: Pattern52
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern52
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern53
**Source:** drum-patterns

```js
// Title: Pattern53
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern53
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern54
**Source:** drum-patterns

```js
// Title: Pattern54
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern54
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern55
**Source:** drum-patterns

```js
// Title: Pattern55
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern55
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").bank(kit)
```
</details>

### Pattern56
**Source:** drum-patterns

```js
// Title: Pattern56
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern56
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern57
**Source:** drum-patterns

```js
// Title: Pattern57
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern57
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern58
**Source:** drum-patterns

```js
// Title: Pattern58
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern58
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern59
**Source:** drum-patterns

```js
// Title: Pattern59
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern59
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### Pattern60
**Source:** drum-patterns

```js
// Title: Pattern60
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern60
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] ~ ~ ~]").bank(kit)
```
</details>

### Pattern61
**Source:** drum-patterns

```js
// Title: Pattern61
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern61
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ ~ bd] ~ ~]").bank(kit)
```
</details>

### Pattern62
**Source:** drum-patterns

```js
// Title: Pattern62
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern62
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd ~] ~ ~]").bank(kit)
```
</details>

### Pattern63
**Source:** drum-patterns

```js
// Title: Pattern63
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Pattern63
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [~ hh hh ~] [hh hh ~ hh] [hh ~ hh hh] [[~ hh hh ~] [hh hh ~ hh] ~ ~]").gain("0.85").bank(kit)
$: s("[~ [~ ~ sd ~] [~ ~ sd ~] ~] [[~ ~ sd ~] [~ ~ sd ~] ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd bd] [bd ~ ~ ~] [[bd ~ ~ ~] [~ ~ bd bd] ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### PlanetRock
**Source:** drum-patterns

```js
// Title: PlanetRock
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_cp = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~]*2 [cb ~ cb cb] [~ cb]*2 [cb ~]*2").bank(bank_cb),
  s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] hh*4").gain("0.85").bank(bank_hh),
  s("~ cp ~ cp").bank(bank_cp),
  s("~ sd ~ sd").bank(bank_sd),
  s("[rim ~]*2 [rim ~ rim rim] [~ rim]*2 [rim ~]*2").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - PlanetRock
const kit = "RolandTR808";

$: s("[cb ~]*2 [cb ~ cb cb] [~ cb]*2 [cb ~]*2").bank(kit)
$: s("[hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh] hh*4").gain("0.85").bank(kit)
$: s("~ cp ~ cp").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[rim ~]*2 [rim ~ rim rim] [~ rim]*2 [rim ~]*2").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Poly1a
**Source:** drum-patterns

```js
// Title: Poly1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ sd ~] [sd ~ ~ sd] [sd sd ~ sd] [sd sd ~ sd] [[sd ~ ~ ~] ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Poly1a
const kit = "RolandTR808";

$: s("[~ ~ sd ~] [sd ~ ~ sd] [sd sd ~ sd] [sd sd ~ sd] [[sd ~ ~ ~] ~ ~ ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Poly1b
**Source:** drum-patterns

```js
// Title: Poly1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~]*2 [~ ~ sd ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[~ ~ bd ~] ~ [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Poly1b
const kit = "RolandTR808";

$: s("~ [sd ~]*2 [~ ~ sd ~] [sd ~ ~ ~]").bank(kit)
$: s("[~ ~ bd ~] ~ [bd ~ ~ ~] ~").bank(kit)
```
</details>

### Poptech2010
**Source:** drum-patterns

```js
// Title: Poptech2010
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[oh ~ ~ ~] ~ ~ ~] ~").bank(bank_oh),
  s("[~ ~ [hh ~ ~ ~] ~] [hh ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ sd] [~ sd ~ sd]").bank(bank_sd),
  s("[[bd ~ ~ ~] ~ ~ ~] [~ bd ~ ~] ~ ~ [~ bd bd bd]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Poptech2010
const kit = "RolandTR808";

$: s("[[oh ~ ~ ~] ~ ~ ~] ~").bank(kit)
$: s("[~ ~ [hh ~ ~ ~] ~] [hh ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ sd ~ sd] [~ sd ~ sd]").bank(kit)
$: s("[[bd ~ ~ ~] ~ ~ ~] [~ bd ~ ~] ~ ~ [~ bd bd bd]").bank(kit)
```
</details>

### Reggae4a
**Source:** drum-patterns

```js
// Title: Reggae4a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[~ ~ ~ oh] ~ [~ oh ~ ~] ~").bank(bank_oh),
  s("[~ ~ ~ hh] ~ [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("[sd sd sd ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[rim ~ ~ ~] [~ ~ rim ~] ~ ~").bank(bank_rim),
  s("[~ ~ ~ bd] ~ [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggae4a
const kit = "RolandTR808";

$: s("~ [~ ~ mt mt] [mt ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ ~ oh] ~ [~ oh ~ ~] ~").bank(kit)
$: s("[~ ~ ~ hh] ~ [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("[sd sd sd ~] ~ ~ ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[rim ~ ~ ~] [~ ~ rim ~] ~ ~").bank(kit)
$: s("[~ ~ ~ bd] ~ [~ bd ~ ~] ~").bank(kit)
```
</details>

### Reggaeton
**Source:** drum-patterns

```js
// Title: Reggaeton
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("[~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~]").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Reggaeton
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("[~ ~ ~ sd] [~ ~ sd ~] [~ ~ ~ sd] [~ ~ sd ~]").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### RespectYourself
**Source:** drum-patterns

```js
// Title: RespectYourself
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8 hh*8").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~]] [~ [sd ~ ~ ~] [sd ~]*2 [sd ~ ~ ~]]").bank(bank_sd),
  s("bd*4 bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RespectYourself
const kit = "RolandTR808";

$: s("hh*8 hh*8").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~]] [~ [sd ~ ~ ~] [sd ~]*2 [sd ~ ~ ~]]").bank(kit)
$: s("bd*4 bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### RockSteady
**Source:** drum-patterns

```js
// Title: RockSteady
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ ~ oh] [~ ~ oh ~] [~ ~ ~ oh] [[~ oh ~ ~] ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("[[~ hh ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~]*2] [hh ~ ~ ~] [hh ~ hh hh] [hh ~ ~ ~] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ ~] [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockSteady
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ ~ oh] [~ ~ oh ~] [~ ~ ~ oh] [[~ oh ~ ~] ~ [~ ~ oh ~] ~]").bank(kit)
$: s("[[~ hh ~ ~] [hh ~]*2 [hh ~ ~ ~] [hh ~]*2] [hh ~ ~ ~] [hh ~ hh hh] [hh ~ ~ ~] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[~ sd ~ ~] [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ sd] [~ sd ~ ~] [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~] [~ ~ bd ~] [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~]").gain("1.0 0.8").bank(kit)
```
</details>

### RockThePlanet
**Source:** drum-patterns

```js
// Title: RockThePlanet
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ hh hh] [hh hh ~ hh] hh*4").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ ~] ~ ~").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RockThePlanet
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ hh hh] [hh hh ~ hh] hh*4").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ ~] ~ ~").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### RollinBreak
**Source:** drum-patterns

```js
// Title: RollinBreak
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - RollinBreak
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Rolling11
**Source:** drum-patterns

```js
// Title: Rolling11
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ bd bd ~] [~ bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling11
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ bd bd ~] [~ bd bd ~] ~").bank(kit)
```
</details>

### Rolling3a
**Source:** drum-patterns

```js
// Title: Rolling3a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling3a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### Rolling3b
**Source:** drum-patterns

```js
// Title: Rolling3b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ ~ sd ~] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling3b
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ ~ sd ~] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### Rolling4a
**Source:** drum-patterns

```js
// Title: Rolling4a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] ~ ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling4a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] ~ ~ ~").bank(kit)
```
</details>

### Rolling4b
**Source:** drum-patterns

```js
// Title: Rolling4b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [~ bd bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling4b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [~ bd bd ~] ~").bank(kit)
```
</details>

### Rolling5b
**Source:** drum-patterns

```js
// Title: Rolling5b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling5b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Rolling6a
**Source:** drum-patterns

```js
// Title: Rolling6a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling6a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ ~ bd] ~").bank(kit)
```
</details>

### Rolling7a
**Source:** drum-patterns

```js
// Title: Rolling7a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling7a
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ bd] ~").bank(kit)
```
</details>

### Rolling7b
**Source:** drum-patterns

```js
// Title: Rolling7b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Rolling7b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ ~ bd] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Sally
**Source:** drum-patterns

```js
// Title: Sally
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[lt ~ ~ ~] [~ ~ lt ~] [~ ~ lt ~] [~ ~ lt ~]").bank(bank_lt),
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Sally
const kit = "RolandTR808";

$: s("[lt ~ ~ ~] [~ ~ lt ~] [~ ~ lt ~] [~ ~ lt ~]").bank(kit)
$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] [~ ~ bd ~]").bank(kit)
```
</details>

### Samba1a
**Source:** drum-patterns

```js
// Title: Samba1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_mt = bank_default;
let bank_lt = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("cb*4").bank(bank_cb),
  s("[~ ~ ~ mt] ~ ~ ~").bank(bank_mt),
  s("~ [~ ~ ~ lt] ~ [~ ~ ~ lt]").bank(bank_lt),
  s("[~ hh hh ~] [~ hh hh ~] [~ hh hh ~] [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba1a
const kit = "RolandTR808";

$: s("cb*4").bank(kit)
$: s("[~ ~ ~ mt] ~ ~ ~").bank(kit)
$: s("~ [~ ~ ~ lt] ~ [~ ~ ~ lt]").bank(kit)
$: s("[~ hh hh ~] [~ hh hh ~] [~ hh hh ~] [~ hh hh ~]").gain("0.85").bank(kit)
$: s("~ ~ [~ ~ ~ sd] ~").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### Samba1b
**Source:** drum-patterns

```js
// Title: Samba1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~]*2 [cb cb ~ cb] [~ cb cb ~] [cb cb ~ cb]").bank(bank_cb),
  s("~ ~ [~ ~ ~ mt] ~").bank(bank_mt),
  s("[~ hh]*2 [~ ~ hh ~] [hh ~ ~ ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Samba1b
const kit = "RolandTR808";

$: s("[cb ~]*2 [cb cb ~ cb] [~ cb cb ~] [cb cb ~ cb]").bank(kit)
$: s("~ ~ [~ ~ ~ mt] ~").bank(kit)
$: s("[~ hh]*2 [~ ~ hh ~] [hh ~ ~ ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd] [bd ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### SlowDeepHouse
**Source:** drum-patterns

```js
// Title: SlowDeepHouse
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("[~ ~ oh oh] [~ ~ oh oh] [~ oh oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("hh*4").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SlowDeepHouse
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[~ ~ oh oh] [~ ~ oh oh] [~ oh oh ~] [~ ~ oh ~]").bank(kit)
$: s("hh*4").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Steppers
**Source:** drum-patterns

```js
// Title: Steppers
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Steppers
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Strbtsdcgogo100
**Source:** drum-patterns

```js
// Title: Strbtsdcgogo100
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [oh ~ ~ ~] ~").bank(bank_oh),
  s("[~ hh hh ~] [hh hh ~ hh] ~ [~ hh hh ~]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ ~] [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Strbtsdcgogo100
const kit = "RolandTR808";

$: s("~ ~ [oh ~ ~ ~] ~").bank(kit)
$: s("[~ hh hh ~] [hh hh ~ hh] ~ [~ hh hh ~]").gain("0.85").bank(kit)
$: s("[~ sd ~ ~] [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### Supersonic2a
**Source:** drum-patterns

```js
// Title: Supersonic2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~ cb cb] [cb ~ ~ ~] ~ ~").bank(bank_cb),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ ~ ~ [sd ~ ~ ~]").bank(bank_sd),
  s("rim*16").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Supersonic2a
const kit = "RolandTR808";

$: s("[cb ~ cb cb] [cb ~ ~ ~] ~ ~").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ ~ ~ [sd ~ ~ ~]").bank(kit)
$: s("rim*16").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Supersonic2b
**Source:** drum-patterns

```js
// Title: Supersonic2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cb = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("[cb ~ cb cb] [cb ~]*2 [cb ~ ~ ~] ~").bank(bank_cb),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~]").bank(bank_sd),
  s("rim*16").gain("1.0 0.5 0.7 0.5").bank(bank_rim),
  s("[bd ~]*2 [~ ~ bd ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Supersonic2b
const kit = "RolandTR808";

$: s("[cb ~ cb cb] [cb ~]*2 [cb ~ ~ ~] ~").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ [sd ~ ~ ~] [~ ~ sd ~] [sd ~ ~ ~]").bank(kit)
$: s("rim*16").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] ~ ~").bank(kit)
```
</details>

### Superstition
**Source:** drum-patterns

```js
// Title: Superstition
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ hh hh] [hh hh hh ~] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Superstition
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ hh hh] [hh hh hh ~] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### Swing3a
**Source:** drum-patterns

```js
// Title: Swing3a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_mt = bank_default;
let bank_oh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cr ~ ~ cr] [~ ~ cr ~] [~ cr ~ ~] ~").bank(bank_cr),
  s("~ [mt mt ~ ~] [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(bank_mt),
  s("[oh ~ ~ oh] [~ ~ oh ~] [~ oh ~ ~] ~").bank(bank_oh),
  s("[~ sd sd ~] [~ ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Swing3a
const kit = "RolandTR808";

$: s("[cr ~ ~ cr] [~ ~ cr ~] [~ cr ~ ~] ~").bank(kit)
$: s("~ [mt mt ~ ~] [~ ~ mt mt] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[oh ~ ~ oh] [~ ~ oh ~] [~ oh ~ ~] ~").bank(kit)
$: s("[~ sd sd ~] [~ ~ ~ sd] [sd ~ ~ ~] ~").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### SynthWave
**Source:** drum-patterns

```js
// Title: SynthWave
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SynthWave
const kit = "RolandTR808";

$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### SynthethicSubstitution
**Source:** drum-patterns

```js
// Title: SynthethicSubstitution
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [[~ ~ oh ~] ~ ~ ~]").bank(bank_oh),
  s("hh*8 [[hh ~ ~ ~] [hh ~]*2 [hh ~]*2 [hh ~]*2]").gain("0.85").bank(bank_hh),
  s("[~ [~ sd ~ ~] ~ [~ sd ~ ~]] [~ [~ sd ~ ~] ~ [~ sd ~ ~]]").bank(bank_sd),
  s("[bd ~]*2 [~ ~ ~ bd] [~ bd bd bd] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd] [~ bd bd bd] [~ ~ ~ bd]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - SynthethicSubstitution
const kit = "RolandTR808";

$: s("~ [[~ ~ oh ~] ~ ~ ~]").bank(kit)
$: s("hh*8 [[hh ~ ~ ~] [hh ~]*2 [hh ~]*2 [hh ~]*2]").gain("0.85").bank(kit)
$: s("[~ [~ sd ~ ~] ~ [~ sd ~ ~]] [~ [~ sd ~ ~] ~ [~ sd ~ ~]]").bank(kit)
$: s("[bd ~]*2 [~ ~ ~ bd] [~ bd bd bd] [~ ~ ~ bd] [bd ~]*2 [~ ~ ~ bd] [~ bd bd bd] [~ ~ ~ bd]").gain("1.0 0.8").bank(kit)
```
</details>

### TakeMeToMardiGras
**Source:** drum-patterns

```js
// Title: TakeMeToMardiGras
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_cr = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cp ~]*2 [~ cp ~ ~] [~ cp ~ ~] [cp ~ ~ ~]").bank(bank_cp),
  s("~ [cr ~ ~ cr] [~ ~ cr ~] [~ cr]*2").bank(bank_cr),
  s("[hh ~]*2 [hh ~ hh hh] [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ bd ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TakeMeToMardiGras
const kit = "RolandTR808";

$: s("[cp ~]*2 [~ cp ~ ~] [~ cp ~ ~] [cp ~ ~ ~]").bank(kit)
$: s("~ [cr ~ ~ cr] [~ ~ cr ~] [~ cr]*2").bank(kit)
$: s("[hh ~]*2 [hh ~ hh hh] [hh ~]*2 [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] [~ bd ~ ~]").bank(kit)
```
</details>

### TakeMeToMardiGrasAlt
**Source:** drum-patterns

```js
// Title: TakeMeToMardiGrasAlt
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_cr = bank_default;
let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[cp ~]*2 [~ cp ~ ~] [~ cp ~ ~] [cp ~ ~ ~]").bank(bank_cp),
  s("~ [cr ~ ~ cr] [~ ~ cr ~] [~ cr]*2").bank(bank_cr),
  s("~ ~ ~ [~ ~ oh ~]").bank(bank_oh),
  s("[hh ~ ~ ~] [hh ~ hh hh] [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ bd] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TakeMeToMardiGrasAlt
const kit = "RolandTR808";

$: s("[cp ~]*2 [~ cp ~ ~] [~ cp ~ ~] [cp ~ ~ ~]").bank(kit)
$: s("~ [cr ~ ~ cr] [~ ~ cr ~] [~ cr]*2").bank(kit)
$: s("~ ~ ~ [~ ~ oh ~]").bank(kit)
$: s("[hh ~ ~ ~] [hh ~ hh hh] [hh ~]*2 [hh ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### Techno
**Source:** drum-patterns

```js
// Title: Techno
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(bank_oh),
  s("~ ~ [~ hh ~ ~] ~").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("bd*4").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Techno
const kit = "RolandTR808";

$: s("[~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~] [~ ~ oh ~]").bank(kit)
$: s("~ ~ [~ hh ~ ~] ~").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("bd*4").gain("1.0 0.8").bank(kit)
```
</details>

### TheFez
**Source:** drum-patterns

```js
// Title: TheFez
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ bd ~] [bd ~ ~ ~] ~ [bd ~ ~ bd] [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TheFez
const kit = "RolandTR808";

$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd] [~ sd]*2 [sd sd ~ sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ bd ~] [bd ~ ~ ~] ~ [bd ~ ~ bd] [bd ~ ~ ~]").bank(kit)
```
</details>

### TheSameBlood
**Source:** drum-patterns

```js
// Title: TheSameBlood
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~]*2 [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[~ ~ ~ sd] [~ sd sd ~] ~ [sd sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd bd ~ ~] ~ [bd bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TheSameBlood
const kit = "RolandTR808";

$: s("[hh ~]*2 [hh ~ hh hh] [hh ~ hh hh] [hh ~ hh hh]").gain("0.85").bank(kit)
$: s("[~ ~ ~ sd] [~ sd sd ~] ~ [sd sd sd ~]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd bd ~ ~] ~ [bd bd ~ ~] ~").bank(kit)
```
</details>

### TheTrillsGone
**Source:** drum-patterns

```js
// Title: TheTrillsGone
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2").gain("0.85").bank(bank_hh),
  s("sd*4").bank(bank_sd),
  s("~ [~ ~ ~ bd] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TheTrillsGone
const kit = "RolandTR808";

$: s("[~ hh]*2 [~ hh]*2 [~ hh]*2 [~ hh]*2").gain("0.85").bank(kit)
$: s("sd*4").bank(kit)
$: s("~ [~ ~ ~ bd] [bd ~]*2 ~").bank(kit)
```
</details>

### TransEuroExpress
**Source:** drum-patterns

```js
// Title: TransEuroExpress
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh ~ hh hh] [hh ~ ~ hh] [hh ~ hh hh] [hh ~ ~ hh]").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TransEuroExpress
const kit = "RolandTR808";

$: s("[hh ~ hh hh] [hh ~ ~ hh] [hh ~ hh hh] [hh ~ ~ hh]").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] ~ [bd ~]*2 ~").bank(kit)
```
</details>

### Trap1a
**Source:** drum-patterns

```js
// Title: Trap1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Trap1a
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [~ sd ~ ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### Trap1b
**Source:** drum-patterns

```js
// Title: Trap1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[hh hh hh ~] [hh ~]*2 [hh ~]*2 [hh ~ hh hh] [[hh ~]*2 ~ ~ ~]").gain("0.85").bank(bank_hh),
  s("~ ~ [~ sd ~ ~] ~").bank(bank_sd),
  s("[~ ~ bd ~] [bd ~ ~ ~] ~ ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - Trap1b
const kit = "RolandTR808";

$: s("[hh hh hh ~] [hh ~]*2 [hh ~]*2 [hh ~ hh hh] [[hh ~]*2 ~ ~ ~]").gain("0.85").bank(kit)
$: s("~ ~ [~ sd ~ ~] ~").bank(kit)
$: s("[~ ~ bd ~] [bd ~ ~ ~] ~ ~").bank(kit)
```
</details>

### TwoDrop
**Source:** drum-patterns

```js
// Title: TwoDrop
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ ~ [sd ~ ~ ~] ~").bank(bank_sd),
  s("bd ~ bd ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - TwoDrop
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ ~ [sd ~ ~ ~] ~").bank(kit)
$: s("bd ~ bd ~").bank(kit)
```
</details>

### UkGarage1a
**Source:** drum-patterns

```js
// Title: UkGarage1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ cp ~ cp").bank(bank_cp),
  s("~ [~ mt ~ ~] [~ ~ ~ mt] ~").bank(bank_mt),
  s("[~ ~ hh hh] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh hh]").gain("0.85").bank(bank_hh),
  s("[~ rim ~ ~] [~ ~ ~ rim] ~ [~ rim ~ ~]").bank(bank_rim),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UkGarage1a
const kit = "RolandTR808";

$: s("~ cp ~ cp").bank(kit)
$: s("~ [~ mt ~ ~] [~ ~ ~ mt] ~").bank(kit)
$: s("[~ ~ hh hh] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh hh]").gain("0.85").bank(kit)
$: s("[~ rim ~ ~] [~ ~ ~ rim] ~ [~ rim ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### UkGarage1b
**Source:** drum-patterns

```js
// Title: UkGarage1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_mt = bank_default;
let bank_hh = bank_default;
let bank_rim = bank_default;
let bank_bd = bank_default;

stack(
  s("~ cp ~ cp").bank(bank_cp),
  s("~ [~ mt ~ ~] [~ ~ ~ mt] ~").bank(bank_mt),
  s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(bank_hh),
  s("[~ rim ~ ~] [~ ~ ~ rim] ~ [~ rim ~ ~]").bank(bank_rim),
  s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UkGarage1b
const kit = "RolandTR808";

$: s("~ cp ~ cp").bank(kit)
$: s("~ [~ mt ~ ~] [~ ~ ~ mt] ~").bank(kit)
$: s("[~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~] [~ ~ hh ~]").gain("0.85").bank(kit)
$: s("[~ rim ~ ~] [~ ~ ~ rim] ~ [~ rim ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### UnconventionalSnare1a
**Source:** drum-patterns

```js
// Title: UnconventionalSnare1a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [sd ~ ~ ~] [~ ~ sd ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UnconventionalSnare1a
const kit = "RolandTR808";

$: s("~ ~ [sd ~ ~ ~] [~ ~ sd ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### UnconventionalSnare1b
**Source:** drum-patterns

```js
// Title: UnconventionalSnare1b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UnconventionalSnare1b
const kit = "RolandTR808";

$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### UnconventionalSnare2a
**Source:** drum-patterns

```js
// Title: UnconventionalSnare2a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [sd ~ ~ sd] ~").bank(bank_sd),
  s("[bd ~ ~ ~] ~ ~ [bd ~ ~ ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UnconventionalSnare2a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [sd ~ ~ sd] ~").bank(kit)
$: s("[bd ~ ~ ~] ~ ~ [bd ~ ~ ~]").bank(kit)
```
</details>

### UnconventionalSnare2b
**Source:** drum-patterns

```js
// Title: UnconventionalSnare2b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [~ ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UnconventionalSnare2b
const kit = "RolandTR808";

$: s("~ [~ ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] [bd ~]*2 ~").bank(kit)
```
</details>

### UnconventionalSnare3a
**Source:** drum-patterns

```js
// Title: UnconventionalSnare3a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UnconventionalSnare3a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ bd ~] ~ [~ ~ bd ~]").bank(kit)
```
</details>

### UnconventionalSnare4a
**Source:** drum-patterns

```js
// Title: UnconventionalSnare4a
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(bank_sd),
  s("[bd ~]*2 [~ ~ bd ~] [~ bd ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UnconventionalSnare4a
const kit = "RolandTR808";

$: s("~ [sd ~ ~ ~] [~ ~ sd ~] ~").bank(kit)
$: s("[bd ~]*2 [~ ~ bd ~] [~ bd ~ ~] ~").bank(kit)
```
</details>

### UnconventionalSnare4b
**Source:** drum-patterns

```js
// Title: UnconventionalSnare4b
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[sd ~ ~ ~] [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(bank_sd),
  s("[~ ~ bd ~] ~ [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UnconventionalSnare4b
const kit = "RolandTR808";

$: s("[sd ~ ~ ~] [sd ~ ~ ~] [~ sd ~ ~] [sd ~ ~ ~]").bank(kit)
$: s("[~ ~ bd ~] ~ [~ ~ bd ~] ~").bank(kit)
```
</details>

### UnknownDrummer
**Source:** drum-patterns

```js
// Title: UnknownDrummer
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("~ ~ [oh ~ ~ ~] [~ ~ oh ~]").bank(bank_oh),
  s("[~ hh hh ~] [hh hh ~ hh] ~ [~ hh ~ ~]").gain("0.85").bank(bank_hh),
  s("[~ sd ~ ~] [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(bank_sd),
  s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UnknownDrummer
const kit = "RolandTR808";

$: s("~ ~ [oh ~ ~ ~] [~ ~ oh ~]").bank(kit)
$: s("[~ hh hh ~] [hh hh ~ hh] ~ [~ hh ~ ~]").gain("0.85").bank(kit)
$: s("[~ sd ~ ~] [sd ~ ~ sd] ~ [sd ~ ~ ~]").bank(kit)
$: s("[bd ~ ~ bd] [~ ~ bd ~] [~ ~ bd ~] ~").bank(kit)
```
</details>

### UseMe
**Source:** drum-patterns

```js
// Title: UseMe
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[~ ~ [~ oh]*2 [~ oh ~ ~]] [~ ~ [~ oh]*2 [~ oh ~ ~]]").bank(bank_oh),
  s("hh*16 [hh*4 hh*4 [hh ~ ~ ~] [~ ~ ~ hh]]").gain("0.85").bank(bank_hh),
  s("[~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]] [~ [sd ~ ~ sd] ~ [~ ~ ~ sd]]").bank(bank_sd),
  s("[[bd ~]*2 [~ bd]*2 [bd ~ bd bd] [~ bd]*2] [[bd ~]*2 [~ bd ~ ~] [bd bd ~ bd] [~ bd]*2]").gain("1.0 0.8").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UseMe
const kit = "RolandTR808";

$: s("[~ ~ [~ oh]*2 [~ oh ~ ~]] [~ ~ [~ oh]*2 [~ oh ~ ~]]").bank(kit)
$: s("hh*16 [hh*4 hh*4 [hh ~ ~ ~] [~ ~ ~ hh]]").gain("0.85").bank(kit)
$: s("[~ [sd ~ ~ sd] [~ sd ~ ~] [sd ~ ~ sd]] [~ [sd ~ ~ sd] ~ [~ ~ ~ sd]]").bank(kit)
$: s("[[bd ~]*2 [~ bd]*2 [bd ~ bd bd] [~ bd]*2] [[bd ~]*2 [~ bd ~ ~] [bd bd ~ bd] [~ bd]*2]").gain("1.0 0.8").bank(kit)
```
</details>

### UseMeAlt
**Source:** drum-patterns

```js
// Title: UseMeAlt
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[[~ ~ oh ~] ~ [~ ~ oh ~] ~] [[~ ~ oh ~] ~ [~ ~ oh ~] ~]").bank(bank_oh),
  s("[[hh ~ ~ ~] hh*4 [hh hh ~ ~] hh*4] [[hh hh ~ ~] hh*4 [hh hh ~ ~] hh*4]").gain("0.85").bank(bank_hh),
  s("[~ ~ sd ~] [sd ~ sd sd] [~ sd sd ~] [sd ~ sd sd] [~ sd sd ~] [sd ~ sd sd] [~ sd sd ~] [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(bank_sd),
  s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [~ [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~]]").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - UseMeAlt
const kit = "RolandTR808";

$: s("[[~ ~ oh ~] ~ [~ ~ oh ~] ~] [[~ ~ oh ~] ~ [~ ~ oh ~] ~]").bank(kit)
$: s("[[hh ~ ~ ~] hh*4 [hh hh ~ ~] hh*4] [[hh hh ~ ~] hh*4 [hh hh ~ ~] hh*4]").gain("0.85").bank(kit)
$: s("[~ ~ sd ~] [sd ~ sd sd] [~ sd sd ~] [sd ~ sd sd] [~ sd sd ~] [sd ~ sd sd] [~ sd sd ~] [sd ~ sd sd]").gain("1.0 0.5 0.7 0.5").bank(kit)
$: s("[bd ~ ~ ~] [bd ~ ~ ~] ~ [bd ~ ~ ~] [~ [bd ~ ~ bd] [~ ~ bd ~] [bd ~ ~ ~]]").bank(kit)
```
</details>

### WalkThisWay
**Source:** drum-patterns

```js
// Title: WalkThisWay
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_oh = bank_default;
let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("[oh ~ ~ ~] ~ ~ ~").bank(bank_oh),
  s("[~ ~ hh ~] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - WalkThisWay
const kit = "RolandTR808";

$: s("[oh ~ ~ ~] ~ ~ ~").bank(kit)
$: s("[~ ~ hh ~] [hh ~]*2 [hh ~]*2 [hh ~]*2").gain("0.85").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~]*2 ~").bank(kit)
```
</details>

### WeWillRockYou
**Source:** drum-patterns

```js
// Title: WeWillRockYou
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cp = bank_default;
let bank_bd = bank_default;

stack(
  s("~ cp ~ cp").bank(bank_cp),
  s("[bd ~]*2 ~ [bd ~]*2 ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - WeWillRockYou
const kit = "RolandTR808";

$: s("~ cp ~ cp").bank(kit)
$: s("[bd ~]*2 ~ [bd ~]*2 ~").bank(kit)
```
</details>

### WhenTheLeveeBreaks
**Source:** drum-patterns

```js
// Title: WhenTheLeveeBreaks
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_hh = bank_default;
let bank_sd = bank_default;
let bank_bd = bank_default;

stack(
  s("hh*8").gain("0.9 0.6").bank(bank_hh),
  s("~ sd ~ sd").bank(bank_sd),
  s("[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd bd] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - WhenTheLeveeBreaks
const kit = "RolandTR808";

$: s("hh*8").gain("0.9 0.6").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("[bd bd ~ ~] [~ ~ ~ bd] [~ ~ bd bd] ~").bank(kit)
```
</details>

### YaMama
**Source:** drum-patterns

```js
// Title: YaMama
// Category: Tidal patterns
let bank_default = "RolandTR808";

let bank_cr = bank_default;
let bank_bd = bank_default;

stack(
  s("~ cr ~ cr").bank(bank_cr),
  s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(bank_bd)
)
```

<details><summary>View Live Channel Mode ($:)</summary>

```js
// Live Channel Mode - YaMama
const kit = "RolandTR808";

$: s("~ cr ~ cr").bank(kit)
$: s("[bd ~ ~ ~] [~ ~ ~ bd] [bd ~ ~ ~] ~").bank(kit)
```
</details>

---
