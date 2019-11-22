from pathlib import Path


def release(data: dict, outfile: Path) -> None:
    with open(outfile, "w") as fh:
        fls = [dd["flags"] for dd in data["data"]]
        fh.write("|".join(fls))


def main() -> None:
    from . import parser

    infile = Path("sources/rout.txt")
    outfile = Path("releases/latest/window.txt")
    output = parser.parse(infile)
    release(data=output, outfile=outfile)


if __name__ == "__main__":
    main()
