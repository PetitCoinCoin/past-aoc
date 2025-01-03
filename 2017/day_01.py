import argparse

from pathlib import Path

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--part", "-p",
        type=int,
        choices={1, 2},
        help="Set puzzle part"
    )
    args = parser.parse_args()
    if not args.part:
        parser.error("Which part are you solving?")
    return args

if __name__ == "__main__":
    args = _parse_args()
    with Path(f"inputs/{Path(__file__).stem}.txt").open("r") as file:
        data = file.read()
    n = len(data)
    if args.part == 1:
        print(sum(int(data[i]) for i in range(n) if data[i] == data[(i + 1) % n]))
    else:
        print(sum(int(data[i]) for i in range(n) if data[i] == data[(i + n // 2) % n]))
