#!/usr/bin/env python3
"""Safe dry-run launch planner. No secrets, signing, or network writes."""

import argparse
import json
import re
from dataclasses import asdict, dataclass


@dataclass
class LaunchPlan:
    name: str
    symbol: str
    decimals: int
    mode: str = "dry-run"


def build_plan(name: str, symbol: str, decimals: int = 9) -> LaunchPlan:
    name = name.strip()
    symbol = symbol.strip().upper()
    if not 1 <= len(name) <= 32:
        raise ValueError("name must be 1-32 characters")
    if not re.fullmatch(r"[A-Z0-9]{1,10}", symbol):
        raise ValueError("symbol must be 1-10 letters or numbers")
    if not 0 <= decimals <= 18:
        raise ValueError("decimals must be between 0 and 18")
    return LaunchPlan(name=name, symbol=symbol, decimals=decimals)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a safe dry-run launch plan")
    parser.add_argument("--name", required=True)
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--decimals", type=int, default=9)
    args = parser.parse_args()
    print(json.dumps(asdict(build_plan(args.name, args.symbol, args.decimals)), indent=2))


if __name__ == "__main__":
    main()
