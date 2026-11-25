# Make the AI Judge Laugh

![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![make.fun](https://img.shields.io/badge/make.fun-entry-orange)

A make.fun entry for **Make the AI Judge Laugh**: a program that writes a
single one-line joke about office life to `/output/entry.txt`.

## How it works

`main.py` writes one joke line (under 200 characters, single line, no
trailing newline) to the output directory named by `MAKEFUN_OUTPUT_DIR`
(default `/output`), with mode `0644` so the grader can read it.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
