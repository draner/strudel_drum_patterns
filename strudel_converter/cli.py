"""Command-line interface for strudel_converter."""

import argparse
import sys
from .library_builder import build_library


def main():
    parser = argparse.ArgumentParser(description="Convert drum pattern repositories to a Strudel.cc code library.")
    parser.add_argument(
        "--drum-patterns-dir",
        default="drum-patterns",
        help="Path to the drum-patterns repository directory."
    )
    parser.add_argument(
        "--drum-beat-repo-dir",
        default="DrumBeatRepo",
        help="Path to the DrumBeatRepo repository directory."
    )
    parser.add_argument(
        "--output-dir",
        default="dist",
        help="Output directory for generated library files."
    )
    parser.add_argument(
        "--bank",
        default="RolandTR808",
        help="Default drum bank name for generated snippets."
    )
    
    args = parser.parse_args()
    
    print("Starting Strudel Drum Pattern Converter...")
    build_library(
        drum_patterns_dir=args.drum_patterns_dir,
        drum_beat_repo_dir=args.drum_beat_repo_dir,
        output_dir=args.output_dir,
        default_bank=args.bank
    )
    print("Conversion completed successfully!")


if __name__ == "__main__":
    main()
