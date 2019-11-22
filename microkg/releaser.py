from pathlib import Path


def release(data: dict, outfile: Path) -> None:
    with open(outfile, "w") as fh:
        fh.write("1110101000100011100010101")


def main() -> None:
    from . import parser

    infile = Path("sources/rout.txt")
    outfile = Path("releases/latest/window.txt")
    output = parser.parse(infile)
    release(data=output, outfile=outfile)


if __name__ == "__main__":
    main()
