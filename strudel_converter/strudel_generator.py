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
        lines.append('let bass_synth = "sawtooth"; // Synth sound ("sawtooth", "square", "tb303", "sine")')
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
            track_expr = f's("{mini_pat}"){gain_part}.note(bass_key).octave(bass_octave){transpose_part}.sound(bass_synth)'
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
            lines.append(f'$: s("{mini_pat}"){gain_part}.note("c").octave(1){transpose_part}.sound("sawtooth")')
        else:
            s_name = tr["sample"]
            mini_pat = optimize_track_pattern(steps_str, s_name)
            gain_str = get_expressive_gain(s_name, steps_str, accent_grid=accent_grid)
            gain_part = f'.gain("{gain_str}")' if gain_str else ""
            lines.append(f'$: s("{mini_pat}"){gain_part}.bank(kit)')
        
    return "\n".join(lines)


def generate_js_library_entry(pattern_data: Dict[str, Any], default_bank: str = "RolandTR808") -> str:
    """
    Generate a parameterized JS pattern function (opts = {}) => stack(...) for drumLibrary object.
    Bank defaults to undefined so Strudel's default built-in drum samples play automatically.
    """
    tracks = pattern_data.get("tracks", [])
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
            stack_lines.append(f'      s("{mini_pat}"){gain_part}.note(key).octave(oct){transpose_part}.sound(synth)')
        else:
            s_name = tr["sample"]
            mini_pat = optimize_track_pattern(steps_str, s_name)
            gain_str = get_expressive_gain(s_name, steps_str, accent_grid=accent_grid)
            gain_part = f'.gain("{gain_str}")' if gain_str else ""
            n_expr = f'(typeof n === "object" ? (n.{s_name} ?? 0) : n)'
            stack_lines.append(f'      s("{mini_pat}"){gain_part}.n({n_expr}).bank(bank)')
        
    if not stack_lines:
        inner = '      s("bd ~ ~ ~").bank(bank)'
    else:
        inner = ",\n".join(stack_lines)

    lines = [
        "(opts = {}) => {",
        "      const o = typeof opts === 'string' ? { bank: opts } : (opts || {});",
        "      const bank = o.bank || o.kit || undefined;",
        "      const n = o.n ?? 0;",
        "      const key = o.key || o.bassKey || bass_key;",
        "      const oct = o.octave || o.bassOctave || bass_octave;",
        "      const synth = o.synth || o.bassSynth || bass_synth;",
        "      return stack(",
        f"{inner}",
        "      );",
        "    }"
    ]
    
    return "\n".join(lines)
