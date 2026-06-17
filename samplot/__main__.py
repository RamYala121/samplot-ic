#!/usr/bin/env python
import argparse
import logging
import sys

from .__init__ import __version__
from .samplot import add_plot
from .samplot_vcf import add_vcf


def main(args=None):
    logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                        format="%(module)s - %(levelname)s: %(message)s")
    
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="samplot", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-v",
        "--version",
        help="Installed version",
        action="version",
        version="%(prog)s " + str(__version__),
    )
    sub = parser.add_subparsers(title="[sub-commands]", dest="command")
    sub.required = True

    add_plot(sub)
    add_vcf(sub)

    args, extra_args = parser.parse_known_args(args)

    # =========================================================================
    # PATCH FOR INTERCHROMOSOMAL & BACKWARDS COMPATIBILITY
    # =========================================================================
    # Check if the user is running the 'plot' command and has location flags
    if args.command == "plot" and hasattr(args, "chrom") and args.chrom is not None:
        # Validate that the number of chromosomes, starts, and ends match up
        if not (len(args.chrom) == len(args.start) == len(args.end)):
            print("Error: The number of -c, -s, and -e arguments must be equal.", file=sys.stderr)
            sys.exit(1)

        # For normal single-region runs, turn the single-item lists back into regular 
        # strings/integers so the rest of Samplot's unpatched backend functions don't crash.
        if len(args.chrom) == 1:
            args.chrom = args.chrom[0]
            args.start = args.start[0]
            args.end = args.end[0]
    # =========================================================================

    args.func(parser, args, extra_args)


if __name__ == "__main__":
    sys.exit(main() or 0)
