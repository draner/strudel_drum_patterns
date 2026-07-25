"""Parser for .pat ASCII drum pattern files (drum-patterns repo)."""

import os
from typing import Dict, List, Any
from .midi_map import resolve_sample, is_bass_track


def normalize_pat_steps(raw_steps: str) -> str:
    """Normalize raw .pat step characters into standard 'x', 'f', '_', '-'."""
    norm = []
    for char in raw_steps:
        if char in ("1", "x", "X"):
            norm.append("x")
        elif char == "2":
            norm.append("_")
        elif char in ("f", "F"):
            norm.append("f")
        else:
            norm.append("-")
    return "".join(norm)


def parse_pat_file(file_path: str, repo_root: str = "") -> Dict[str, Any]:
    """
    Parse a single .pat file into a structured dictionary.
    Filters out completely empty tracks with no hits.
    Calculates bass transposition relative to the pattern's lowest bass note.
    """
    file_basename = os.path.basename(file_path)
    pattern_name, _ = os.path.splitext(file_basename)
    
    category = "General"
    if repo_root:
        abs_file = os.path.abspath(file_path)
        abs_root = os.path.abspath(repo_root)
        if abs_file.startswith(abs_root):
            rel_path = os.path.relpath(abs_file, abs_root)
            parts = os.path.dirname(rel_path).split(os.sep)
            if parts and parts[0]:
                category = " / ".join([p for p in parts if p])

    tracks = []
    accent_grid = None
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            inst_id = parts[0]
            steps = parts[1]
            if inst_id == "AC":
                accent_grid = normalize_pat_steps(steps)

    raw_parsed_tracks = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            inst_id = parts[0]
            raw_steps = parts[1]
            
            if inst_id in ("AC", "SL"):
                continue
                
            norm_steps = normalize_pat_steps(raw_steps)
            
            # Skip completely empty tracks with no hits at all
            if set(norm_steps) == {"-"}:
                continue
                
            sample = resolve_sample(midi_note=inst_id, track_name=inst_id)
            is_bass = is_bass_track(midi_note=inst_id, track_name=inst_id)
            
            raw_parsed_tracks.append({
                "id": inst_id,
                "sample": sample,
                "steps": norm_steps,
                "accent_grid": accent_grid,
                "is_bass": is_bass,
            })
            
    # Calculate bass transposition relative to lowest bass note in the pattern
    bass_notes = []
    for tr in raw_parsed_tracks:
        if tr["is_bass"] and str(tr["id"]).isdigit():
            bass_notes.append(int(tr["id"]))
            
    lowest_bass = min(bass_notes) if bass_notes else 24
    
    for tr in raw_parsed_tracks:
        if tr["is_bass"] and str(tr["id"]).isdigit():
            tr["transpose"] = max(0, int(tr["id"]) - lowest_bass)
        else:
            tr["transpose"] = 0
        tracks.append(tr)
                
    return {
        "name": pattern_name,
        "category": category,
        "source": "drum-patterns",
        "file_path": file_path,
        "tracks": tracks
    }
