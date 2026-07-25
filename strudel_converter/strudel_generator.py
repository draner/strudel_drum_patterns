"""Generator for Strudel code snippets and library definitions including bass synth configuration."""

import re
from typing import Dict, List, Any
from .mini_notation import optimize_track_pattern, get_expressive_gain


def sanitize_js_identifier(name: str) -> str:
    """Convert a human readable pattern name or category to a valid JS camelCase / snake_case key."""
    clean = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    clean = re.sub(r"_+", "_", clean).strip("_")
    if not clean:
        clean = "pattern"
    if clean[0].isdigit():
        clean = "p_" + clean
    return clean


def generate_strudel_snippet(pattern_data: Dict[str, Any], default_bank: str = "RolandTR808") -> str:
    """
    Generate a full standalone Strudel code snippet string for a drum pattern.
    Includes setcpm, per-instrument bank & n variables, bass synth config, and stack(...).
    """
    name = pattern_data.get("name", "Untitled")
    category = pattern_data.get("category", "General")
    bpm = pattern_data.get("bpm")
    tracks = pattern_data.get("tracks", [])
    
    has_bass = any(tr.get("is_bass") for tr in tracks)
    
    lines = [
        f"// Title: {name}",
        f"// Category: {category}"
    ]
    
    if bpm:
        lines.append(f"setcpm({bpm} / 4);")
        
    lines.append(f'let bank_default = "{default_bank}";')
    lines.append("")
    
    # Collect unique non-bass samples used
    samples_used = []
    seen = set()
    for tr in tracks:
        if not tr.get("is_bass"):
            s_name = tr["sample"]
            if s_name not in seen:
                seen.add(s_name)
                samples_used.append(s_name)
            
    # Declare bank variables
    for s_name in samples_used:
        lines.append(f"let bank_{s_name} = bank_default;")
    if samples_used:
        lines.append("")
    
    # Declare n variables
    for s_name in samples_used:
        lines.append(f"let n_{s_name} = 0;")
    if samples_used:
        lines.append("")
        
    # Declare bass synth variables if pattern contains a bass line
    if has_bass:
        lines.append('let bass_key = "c";          // Bass root key')
        lines.append('let bass_octave = 1;         // Bass octave')
        lines.append('let bass_synth = "sawtooth"; // Valid waveforms: "sawtooth", "square", "sine", "triangle", "supersaw"')
        lines.append("")
    
    # Build stack tracks
    stack_lines = []
    for tr in tracks:
        steps_str = tr["steps"]
        accent_grid = tr.get("accent_grid")
        is_bass = tr.get("is_bass", False)
        transpose = tr.get("transpose", 0)
        
        if is_bass:
            mini_pat = optimize_track_pattern(steps_str, "x")
            transpose_part = f".transpose({transpose})" if transpose > 0 else ""
            gain_str = get_expressive_gain("bd", steps_str, accent_grid=accent_grid)
            gain_part = f'.gain("{gain_str}")' if gain_str else ""
            track_expr = f's("{mini_pat}"){gain_part}.note(bass_key).octave(bass_octave){transpose_part}.decay(0.2).sustain(0).sound(bass_synth)'
        else:
            s_name = tr["sample"]
            mini_pat = optimize_track_pattern(steps_str, s_name)
            gain_str = get_expressive_gain(s_name, steps_str, accent_grid=accent_grid)
            gain_part = f'.gain("{gain_str}")' if gain_str else ""
            track_expr = f's("{mini_pat}"){gain_part}.bank(bank_{s_name}).n(n_{s_name})'
            
        stack_lines.append(f"  {track_expr}")
        
    lines.append("stack(")
    lines.append(",\n".join(stack_lines))
    lines.append(")")
    
    return "\n".join(lines)


def generate_channel_snippet(pattern_data: Dict[str, Any], default_bank: str = "RolandTR808") -> str:
    """
    Generate a $: channel-based Strudel live-coding snippet.
    """
    name = pattern_data.get("name", "Untitled")
    bpm = pattern_data.get("bpm")
    tracks = pattern_data.get("tracks", [])
    
    lines = [f"// Live Channel Mode - {name}"]
    if bpm:
        lines.append(f"setcpm({bpm} / 4);")
    lines.append(f'const kit = "{default_bank}";')
    lines.append("")
    
    for tr in tracks:
        steps_str = tr["steps"]
        accent_grid = tr.get("accent_grid")
        is_bass = tr.get("is_bass", False)
        transpose = tr.get("transpose", 0)
        
        if is_bass:
            mini_pat = optimize_track_pattern(steps_str, "x")
            transpose_part = f".transpose({transpose})" if transpose > 0 else ""
            gain_str = get_expressive_gain("bd", steps_str, accent_grid=accent_grid)
            gain_part = f'.gain("{gain_str}")' if gain_str else ""
            lines.append(f'$: s("{mini_pat}"){gain_part}.note("c").octave(1){transpose_part}.decay(0.2).sustain(0).sound("sawtooth")')
        else:
            s_name = tr["sample"]
            mini_pat = optimize_track_pattern(steps_str, s_name)
            gain_str = get_expressive_gain(s_name, steps_str, accent_grid=accent_grid)
            gain_part = f'.gain("{gain_str}")' if gain_str else ""
            lines.append(f'$: s("{mini_pat}"){gain_part}.bank(kit)')
        
    return "\n".join(lines)


def extract_pattern_tracks_dict(pattern_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract a pure data dictionary of mini-notation tracks and gains for a pattern.
    Uses 'title' instead of 'name' to avoid JS Function.name property collisions.
    """
    title = pattern_data.get("name", "Untitled")
    category = pattern_data.get("category", "General")
    bpm = pattern_data.get("bpm")
    tracks = pattern_data.get("tracks", [])
    
    tracks_dict = {}
    gains_dict = {}
    
    for tr in tracks:
        steps_str = tr["steps"]
        accent_grid = tr.get("accent_grid")
        is_bass = tr.get("is_bass", False)
        
        if is_bass:
            key_name = "bass"
            mini_pat = optimize_track_pattern(steps_str, "x")
            gain_str = get_expressive_gain("bd", steps_str, accent_grid=accent_grid)
        else:
            key_name = tr["sample"]
            mini_pat = optimize_track_pattern(steps_str, key_name)
            gain_str = get_expressive_gain(key_name, steps_str, accent_grid=accent_grid)
            
        tracks_dict[key_name] = mini_pat
        if gain_str:
            gains_dict[key_name] = gain_str
            
    return {
        "title": title,
        "category": category,
        "bpm": bpm,
        "tracks": tracks_dict,
        "gains": gains_dict
    }
