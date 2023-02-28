#! /home/aaron/miniconda3/envs/cheese/bin/python
import os
import re
import fire


def convert_to_ipynb(in_file: str):
    abs_file = os.path.abspath(in_file)

    in_dir = os.path.dirname(abs_file)
    sub = re.sub(r".*/docs/", "", in_dir)

    stem = os.path.splitext( os.path.basename(in_file))[0]
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(out_dir, "docs/code", sub)
    
    out_file = os.path.join(out_dir, f"{stem}.ipynb")
    print(f"converting {in_file} to {out_file}")

    os.system(f"notedown --match=python {in_file} > {out_file}")

if __name__ == "__main__":
    fire.Fire({
        "ipynb": convert_to_ipynb
    })
