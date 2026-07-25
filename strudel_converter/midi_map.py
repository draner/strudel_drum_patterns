"""MIDI note and instrument name mapping to Strudel sample & synth definitions."""

# Standard General MIDI & Roland Drum mapping to Strudel sample names
MIDI_TO_STRUDEL = {
    # Bass Drums / Kicks
    35: "bd",
    36: "bd",
    
    # Snares & Rim/Side-stick
    37: "rim",
    38: "sd",
    40: "sd",
    
    # Hand Clap
    39: "cp",
    
    # Hi-Hats
    42: "hh",  # Closed Hi-Hat
    44: "hh",  # Pedal Hi-Hat
    46: "oh",  # Open Hi-Hat
    
    # Toms
    41: "lt",  # Low Floor Tom
    43: "lt",  # High Floor Tom
    45: "mt",  # Low Tom
    47: "mt",  # Low-Mid Tom
    48: "ht",  # Hi-Mid Tom
    50: "ht",  # High Tom
    
    # Cymbals & Ride
    49: "cr",  # Crash Cymbal 1
    51: "rd",  # Ride Cymbal 1
    52: "cr",  # Chinese Cymbal
    53: "rd",  # Ride Bell
    55: "cr",  # Splash Cymbal
    57: "cr",  # Crash Cymbal 2
    59: "rd",  # Ride Cymbal 2
    
    # Percussion
    54: "tamb", # Tambourine
    56: "cb",   # Cowbell
    60: "bon",  # Hi Bongo
    61: "bon",  # Low Bongo
    62: "hc",   # Mute Hi Conga
    63: "hc",   # Open Hi Conga
    64: "lc",   # Low Conga
    75: "cl",   # Claves
    76: "wb",   # Hi Wood Block
    77: "wb",   # Low Wood Block
}

# String/Name & 2-letter Roland short code mappings
NAME_TO_STRUDEL = {
    "bd": "bd",
    "kick": "bd",
    "bass drum": "bd",
    "bassdrum": "bd",
    
    "sd": "sd",
    "snare": "sd",
    "snaredrum": "sd",
    
    "rim": "rim",
    "rs": "rim",
    "rm": "rim",
    "side stick": "rim",
    "sidestick": "rim",
    "rimshot": "rim",
    
    "cp": "cp",
    "clap": "cp",
    "hand clap": "cp",
    
    "hh": "hh",
    "ch": "hh",
    "hat": "hh",
    "hats": "hh",
    "closed hat": "hh",
    "closed hihat": "hh",
    "closed hi-hat": "hh",
    "hihat": "hh",
    "hi-hat": "hh",
    
    "oh": "oh",
    "ho": "oh",
    "open hat": "oh",
    "open hihat": "oh",
    "open hi-hat": "oh",
    
    "cr": "cr",
    "cc": "cr",
    "crash": "cr",
    "crash cymbal": "cr",
    
    "rd": "rd",
    "rc": "rd",
    "ride": "rd",
    "ride cymbal": "rd",
    
    "ht": "ht",
    "high tom": "ht",
    "hi tom": "ht",
    "mid tom": "mt",
    "mt": "mt",
    "low tom": "lt",
    "floor tom": "lt",
    "lt": "lt",
    "tom": "ht",
    "toms": "ht",
    
    "cb": "cb",
    "perc": "cb",
    "percussion": "cb",
    "cowbell": "cb",
    
    "hc": "hc",
    "lc": "lc",
}


def midi_to_sample(midi_note: int) -> str:
    """Map a MIDI note integer to a Strudel sample name."""
    return MIDI_TO_STRUDEL.get(int(midi_note), "bd")


def name_to_sample(track_name: str) -> str:
    """Map a track name string or short code to a Strudel sample name."""
    clean_name = str(track_name).strip().lower()
    if clean_name in NAME_TO_STRUDEL:
        return NAME_TO_STRUDEL[clean_name]
    
    # Substring search fallbacks
    for key, sample in NAME_TO_STRUDEL.items():
        if key in clean_name:
            return sample
            
    return "sd"  # Default fallback


def is_bass_track(midi_note=None, track_name=None) -> bool:
    """Determine if a track is a bass synth track."""
    if midi_note is not None:
        try:
            val = int(midi_note)
            if val < 35:
                return True
        except (ValueError, TypeError):
            pass
            
    if track_name:
        clean = str(track_name).strip().lower()
        if any(w in clean for w in ("bass", "synth", "sub", "tb303", "303")):
            return True
            
    return False


def get_bass_transpose(midi_note=None) -> int:
    """Calculate semitone transpose interval relative to C1 (MIDI note 24)."""
    if midi_note is not None:
        try:
            val = int(midi_note)
            if val < 35:
                return max(0, val - 24)
        except (ValueError, TypeError):
            pass
    return 0


def resolve_sample(midi_note=None, track_name=None) -> str:
    """Resolve sample name using MIDI note first, then track name fallback."""
    if midi_note is not None:
        try:
            val = int(midi_note)
            if val in MIDI_TO_STRUDEL:
                return MIDI_TO_STRUDEL[val]
        except (ValueError, TypeError):
            pass
            
    if track_name:
        return name_to_sample(track_name)
        
    return "bd"
