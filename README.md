# Strudel Drum Patterns Library & Converter 🥁

An automated Python converter and pattern library that transforms drum pattern repositories ([jcelerier/drum-patterns](https://github.com/jcelerier/drum-patterns) and [Babali42/DrumBeatRepo](https://github.com/Babali42/DrumBeatRepo)) into **1,034 expressive, ready-to-play live-coding snippets** for [Strudel.cc](https://strudel.cc).

---

## 🌟 Key Features

- **1,034 Patterns Across 20 Categories**: Includes Rock, Hip-Hop, Techno, House, Drum & Bass, Dub, Reggae, Dancehall, Jersey Club, Metal, EDM Literature, TB03 Acid Patterns, and more.
- **Idiomatic Strudel Mini-Notation**: Converts raw step grids into concise mini-notation (`hh*16`, `hh*8`, `~ sd ~ sd`, `bd*4`, `[~ ~ sd ~]`).
- **Expressive Dynamics & Accents**: Adds rhythmic velocity gain contours (`.gain("0.9 0.5 0.7 0.5")`) for hi-hats, ghost-note snare rolls, and programmed accent grids (`AC`).
- **Bass Synth Integration**: Automatically detects basslines and synthesizes them using configurable root key (`bass_key`), octave (`bass_octave`), and synth waveforms (`bass_synth`). Relative musical pitch intervals (minor 3rd, 5th, 7th) are preserved via `.transpose()`.
- **Flexible `drumLibrary` ES Module**: Every pattern is exported as a parameterized function `(opts = {}) => stack(...)` allowing live bank, sample index `n`, and bass synth switching.
- **Dual Live-Coding Modes**: Provides both `stack(...)` expressions for preset playback and `$: Channel` mode for live muting/solo (`_$:`).

---

## 🌐 Remote Import in Strudel.cc REPL

To load the library in [Strudel.cc](https://strudel.cc), use top-level **`await import(...)`**:

### 1. Remote Import via jsDelivr CDN (Recommended)
Works immediately once pushed to GitHub (no GitHub Pages setup required):

```js
// Import remotely via jsDelivr CDN
const { drumLibrary } = await import('https://cdn.jsdelivr.net/gh/draner/strudel_drum_patterns@main/dist/strudel_library.js')

// 1. Play with default settings (TR-808, n=0, Key C, Octave 1)
drumLibrary.Dancehall.Reggaeton()

// 2. Play with custom drum bank
drumLibrary.Dancehall.Reggaeton("RolandTR909")

// 3. Play with custom bank, sample variation index (n), and bass synth parameters
drumLibrary.Dub({ bank: "RolandTR909", n: 1, key: "eb", octave: 2, synth: "tb303" })
```

### 2. Remote Import via RawGithack CDN
```js
const { drumLibrary } = await import('https://raw.githack.com/draner/strudel_drum_patterns/main/dist/strudel_library.js')

drumLibrary.Rock.Rock1_MeasureA()
```

### 3. Remote Import via GitHub Pages
If GitHub Pages is enabled in your repository settings (Settings -> Pages -> Branch: `main`):

```js
const { drumLibrary } = await import('https://draner.github.io/strudel_drum_patterns/dist/strudel_library.js')

drumLibrary.Rock.Rock1_MeasureA()
```

> ⚠️ **Troubleshooting `Failed to fetch dynamically imported module`**:
> - Ensure you pushed your commits including `dist/` to GitHub (`git add . && git commit -m "Build dist" && git push`).
> - Ensure the repository name in the URL matches your GitHub repo name (`strudel_drum_patterns`).
> - Use the **jsDelivr** or **RawGithack** CDN URLs above, as they include mandatory CORS headers and work instantly.

---

## 🚀 How to Use Snippets from `dist/CATALOG.md`

Browse [`dist/CATALOG.md`](./dist/CATALOG.md) to find copy-pasteable snippets formatted for standalone execution or live performance:

#### Standalone `stack(...)` Snippet Example
```js
// Title: Dub
// Category: Dub
setcpm(140 / 4);
let bank_default = "RolandTR808";

let bank_bd = bank_default;
let bank_sd = bank_default;
let bank_hh = bank_default;

let n_bd = 0;
let n_sd = 0;
let n_hh = 0;

let bass_key = "c";          // Bass root key
let bass_octave = 1;         // Bass octave
let bass_synth = "sawtooth"; // Synth sound ("sawtooth", "square", "tb303", "sine")

stack(
  s("bd ~ bd ~").gain("1.0 0.8").bank(bank_bd).n(n_bd),
  s("~ sd ~ sd").bank(bank_sd).n(n_sd),
  s("hh*16").gain("0.9 0.5 0.7 0.5").bank(bank_hh).n(n_hh),
  s("[x ~ ~ x] [~ ~ x ~] [x ~ ~ x] [~ ~ ~ ~]").note(bass_key).octave(bass_octave).sound(bass_synth)
)
```

#### Live Channel Mode (`$:`) Example
For live tweaking, muting, or soloing individual drum parts (prefix with `_$:` to mute a track):

```js
// Live Channel Mode - Dub
setcpm(140 / 4);
const kit = "RolandTR808";

$: s("bd ~ bd ~").gain("1.0 0.8").bank(kit)
$: s("~ sd ~ sd").bank(kit)
$: s("hh*16").gain("0.9 0.5 0.7 0.5").bank(kit)
$: s("[x ~ ~ x] [~ ~ x ~] [x ~ ~ x] [~ ~ ~ ~]").note("c").octave(1).sound("sawtooth")
```

---

## 🛠️ Installation & Setup (Cloning Source Repos)

To set up this project locally and convert the pattern repositories:

### 1. Clone the Generator Repository
```bash
git clone https://github.com/draner/strudel_drum_patterns.git
cd strudel_drum_patterns
```

### 2. Clone the Pattern Source Repositories
Clone the two source pattern repositories into the root of `strudel_drum_patterns`:

```bash
# Clone the drum-patterns repo
git clone https://github.com/jcelerier/drum-patterns.git

# Clone the DrumBeatRepo
git clone https://github.com/Babali42/DrumBeatRepo.git
```

---

## ⚙️ Running the Python Converter

To scan the cloned drum pattern repositories and build the output files in `dist/`:

### 1. Execute Default Conversion
```bash
python convert.py
```

### 2. Custom Command-Line Options
```bash
python convert.py --drum-patterns-dir ./drum-patterns --drum-beat-repo-dir ./DrumBeatRepo --output-dir ./dist --bank RolandTR808
```

### 3. Run Unit Tests
```bash
python -m unittest discover -s tests
```

---

## 📁 Repository & Output Artifacts

```
strudel_drum_patterns/
├── drum-patterns/           # Cloned source repo (jcelerier/drum-patterns)
├── DrumBeatRepo/            # Cloned source repo (Babali42/DrumBeatRepo)
├── strudel_converter/       # Python converter package
│   ├── midi_map.py          # General MIDI & drum instrument mapping
│   ├── pat_parser.py        # Parser for .pat ASCII drum pattern files
│   ├── json_parser.py       # Parser for .json beat preset files
│   ├── mini_notation.py     # Mini-notation optimizer & gain accent generator
│   ├── strudel_generator.py # Strudel code snippet & drumLibrary entry generator
│   ├── library_builder.py   # Scans repos and generates dist outputs
│   └── cli.py               # Command-line interface
├── tests/                   # Unit test suite
├── dist/                    # Generated Strudel pattern library files
│   ├── strudel_library.js   # Parameterized ES module exporting drumLibrary object
│   ├── strudel_library.json # Structured JSON dataset of all 1,034 patterns
│   └── CATALOG.md           # Markdown catalog listing all patterns with copyable snippets
├── convert.py               # Main converter runner script
└── README.md                # Documentation & usage guide
```

---

## 📄 License & Credits

- **Pattern Sources**:
  - [drum-patterns](https://github.com/jcelerier/drum-patterns) by Jean-Michaël Celerier
  - [DrumBeatRepo](https://github.com/Babali42/DrumBeatRepo) by Babali42
- **Strudel**: Built for the [Strudel live-coding environment](https://strudel.cc) created by Felix Roos and the TidalCycles community.
