"""Parser for .json drum beat files (DrumBeatRepo)."""

import json
import os
from typing import Dict, List, Any
from .midi_map import resolve_sample, is_bass_track


def parse_json_beat_file(file_path: str) -> Dict[str, Any]:
    """
    Parse a single beat .json file into a structured dictionary.
    Filters out completely empty tracks with no hits.
    Calculates bass transposition relative to the pattern's lowest bass note.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    name = data.get("label") or os.path.splitext(os.path.basename(file_path))[0]
    category = data.get("genre", "General")
    bpm = data.get("bpm")
    
    raw_tracks = data.get("tracks", [])
    raw_parsed_tracks = []
    
    for tr in raw_tracks:
        tr_name = tr.get("name", "")
        midi_note = tr.get("midiNote")
        raw_steps = tr.get("steps", "")
        
        # Normalize step symbols: convert 'X', 'x', 'f', '1' to 'x', ' ' and '_' to '-'
        norm_steps = []
        for char in raw_steps:
            if char in ("X", "x", "f", "1", "o", "*"):
                norm_steps.append("x" if char != "f" else "f")
            elif char == "2":
                norm_steps.append("_")
            elif char in (" ", "-", ".", "0", "~"):
                norm_steps.append("-")
            else:
                norm_steps.append("-")
                
        steps_str = "".join(norm_steps)
        
        # Skip completely empty tracks with no hits
        if set(steps_str) == {"-"}:
            continue
            
        sample = resolve_sample(midi_note=midi_note, track_name=tr_name)
        is_bass = is_bass_track(midi_note=midi_note, track_name=tr_name)
        
        raw_parsed_tracks.append({
            "name": tr_name,
            "midiNote": midi_note,
            "sample": sample,
            "steps": steps_str,
            "is_bass": is_bass,
        })
        
    # Calculate bass transposition relative to lowest bass note in the pattern
    bass_notes = []
    for tr in raw_parsed_tracks:
        if tr["is_bass"] and tr.get("midiNote") is not None:
            bass_notes.append(int(tr["midiNote"]))
            
    lowest_bass = min(bass_notes) if bass_notes else 24
    
    parsed_tracks = []
    for tr in raw_parsed_tracks:
        if tr["is_bass"] and tr.get("midiNote") is not None:
            tr["transpose"] = max(0, int(tr["midiNote"]) - lowest_bass)
        else:
            tr["transpose"] = 0
        parsed_tracks.append(tr)
        
    return {
        "name": name,
        "category": category,
        "bpm": bpm,
        "source": "DrumBeatRepo",
        "file_path": file_path,
        "tracks": parsed_tracks
    }
