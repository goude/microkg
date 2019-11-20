import re
from pathlib import Path
from pprint import pprint

from . import meta


def parse(file: Path) -> dict:
    with open(file) as fh:
        lines = fh.readlines()

    metadata = {}

    data = []
    for line in lines:
        in_header = re.search(r"^# (\w+): (.+)$", line)
        if in_header:
            key, val = in_header.groups()
            metadata[key] = meta.get_meta_value(key, val)
        else:
            delimiter = meta.get_delimiter(metadata["delimiter"])
            line_vals = line.strip().split(delimiter)
            data_row = {}
            for val, col, typ, reg in zip(
                line_vals,
                metadata["columns"],
                metadata["types"],
                metadata["validations"],
            ):
                if not re.match(reg, val):
                    raise RuntimeError(f"Val fail {reg} {val}")

                data_row[col] = meta.get_type(typ)(val)

            data.append(data_row)

    return dict(meta=metadata, data=data)


def main() -> None:
    file = Path("sources/rout.txt")
    output = parse(file)
    pprint(output)


if __name__ == "__main__":
    main()
