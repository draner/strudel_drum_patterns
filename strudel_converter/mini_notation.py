"""Mini-notation optimizer and expressive accent generator for Strudel drum patterns."""

from typing import List, Tuple, Dict, Any, Optional


def optimize_beat_group(steps_4: str, sample_name: str) -> str:
    """
    Optimize a 4-step sixteenth-note group for a single quarter-note beat.
    
    steps_4: 4-character string of 'x', 'f', '_', '-'
    sample_name: Strudel sample name (e.g. 'bd', 'sd', 'hh')
    """
    if len(steps_4) != 4:
        return "~"
        
    if steps_4 == "----":
        return "~"
    if steps_4 in ("xxxx", "ffff"):
        return f"{sample_name}*4"
    if steps_4 in ("x-x-", "f-f-"):
        return f"[{sample_name} ~]*2"
    if steps_4 in ("-x-x", "-f-f"):
        return f"[~ {sample_name}]*2"
    if steps_4 in ("x---", "f---"):
        return f"[{sample_name} ~ ~ ~]"
    if steps_4 in ("-x--", "-f--"):
        return f"[~ {sample_name} ~ ~]"
    if steps_4 in ("--x-", "--f-"):
        return f"[~ ~ {sample_name} ~]"
    if steps_4 in ("---x", "---f"):
        return f"[~ ~ ~ {sample_name}]"
        
    # Mixed pattern: convert symbol by symbol
    tokens = []
    for char in steps_4:
        if char in ("x", "f"):
            tokens.append(sample_name)
        elif char == "_":
            tokens.append("_")
        else:
            tokens.append("~")
    return "[" + " ".join(tokens) + "]"


def optimize_track_pattern(steps: str, sample_name: str) -> str:
    """
    Convert a full track step string (16, 32, etc.) into idiomatic Strudel mini-notation.
    Formats 4-bar patterns into bracketed bar subgroups [bar0] [bar1] [bar2] [bar3]
    so Strudel plays them at the correct tempo and duration.
    """
    if not steps or set(steps) == {"-"}:
        return "~"

    length = len(steps)
    
    # Check whole-track global repetition shortcuts
    if set(steps) in ({"x"}, {"f"}, {"x", "f"}):
        return f"{sample_name}*{length}"
        
    # Check alternating 8th notes across 16 steps
    if length == 16:
        if steps == "x-x-x-x-x-x-x-x-":
            return f"{sample_name}*8"
        if steps == "x---x---x---x---":
            return f"{sample_name}*4"
        if steps == "----x-------x---":
            return f"~ {sample_name} ~ {sample_name}"
        if steps == "x-------x-------":
            return f"{sample_name} ~ {sample_name} ~"
            
    # Process bar by bar (16 steps per bar)
    bars = []
    chunk_size = 16
    
    # Pad steps if not multiple of 16
    remainder = length % chunk_size
    if remainder != 0:
        steps = steps + ("-" * (chunk_size - remainder))
        length = len(steps)
        
    # Process 16-step bars
    for bar_start in range(0, length, chunk_size):
        bar_steps = steps[bar_start : bar_start + chunk_size]
        
        # Check bar-level shortcuts
        if bar_steps == "x-x-x-x-x-x-x-x-":
            bar_notation = f"{sample_name}*8"
        elif bar_steps == "x---x---x---x---":
            bar_notation = f"{sample_name}*4"
        elif bar_steps == "----x-------x---":
            bar_notation = f"~ {sample_name} ~ {sample_name}"
        elif bar_steps == "x-------x-------":
            bar_notation = f"{sample_name} ~ {sample_name} ~"
        elif set(bar_steps) in ({"x"}, {"f"}, {"x", "f"}):
            bar_notation = f"{sample_name}*16"
        elif set(bar_steps) == {"-"}:
            bar_notation = "~"
        else:
            # Divide 16 steps into 4 quarter-note beats
            beat_groups = []
            for b in range(4):
                beat_4 = bar_steps[b * 4 : (b + 1) * 4]
                beat_groups.append(optimize_beat_group(beat_4, sample_name))
            bar_notation = " ".join(beat_groups)
            
        bars.append(bar_notation)
        
    # Combine bars: if all bars are identical, return single bar
    if len(bars) == 4 and bars[0] == bars[1] == bars[2] == bars[3]:
        return bars[0]
        
    if len(bars) > 1:
        wrapped_bars = [f"[{b}]" if " " in b and not (b.startswith("[") and b.endswith("]")) else b for b in bars]
        return " ".join(wrapped_bars)
        
    return " ".join(bars)


def get_expressive_gain(sample_name: str, steps: str, accent_grid: Optional[str] = None) -> Optional[str]:
    """
    Generate an expressive gain pattern string for a track to enhance feel and dynamics.
    
    Returns:
        String gain pattern e.g. "0.9 0.5 0.7 0.5" or None if default gain is fine.
    """
    if not steps or set(steps) == {"-"}:
        return None

    # 1. Explicit accent grid from .pat AC line
    if accent_grid and len(accent_grid) == len(steps) and set(accent_grid) != {"-"}:
        gains = []
        for i, char in enumerate(steps):
            if char in ("x", "f", "_"):
                ac = accent_grid[i] if i < len(accent_grid) else "-"
                if ac in ("x", "1"):
                    gains.append("1.0" if char == "x" else "1.1")
                else:
                    gains.append("0.6")
        if gains and len(set(gains)) > 1:
            return " ".join(gains)

    # 2. Hi-Hat Expression
    if sample_name in ("hh", "oh", "hc"):
        if "x*16" in optimize_track_pattern(steps, sample_name) or steps == "x" * 16:
            return "0.9 0.5 0.7 0.5"
        elif "x*8" in optimize_track_pattern(steps, sample_name) or steps == "x-x-x-x-x-x-x-x-":
            return "0.9 0.6"
        elif "f" in steps:
            return "1.0 0.7"
        elif sample_name == "hh":
            return "0.85"

    # 3. Snare & Percussion Rolls / Ghost Notes
    if sample_name in ("sd", "rim", "cp", "lt", "mt", "ht"):
        if "xx" in steps or "ff" in steps or "sd sd" in optimize_track_pattern(steps, sample_name):
            return "1.0 0.5 0.7 0.5"
        elif "f" in steps:
            return "1.1 0.7"

    # 4. Kick Expression
    if sample_name == "bd":
        if steps.count("x") >= 8 or "bd*4" in optimize_track_pattern(steps, sample_name):
            return "1.0 0.8"

    return None
