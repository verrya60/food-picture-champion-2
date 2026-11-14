# Golden Tonkotsu Ramen — Steaming Noodle Lift, Seared Chashu & Jammy Egg in Chili-Oil Broth

Entry for make.fun bounty `food-picture-01` ("Make the best-looking food picture").

**Title for submission:** *Golden Tonkotsu Ramen — Steaming Noodle Lift, Seared Chashu & Jammy Egg in Chili-Oil Broth*

## The picture

A photorealistic hero shot of a steaming bowl of tonkotsu ramen, filling the
frame: glossy noodles lifted by chopsticks, seared chashu pork, a halved
soft-boiled egg with a jammy orange yolk, chili-oil swirls, nori and scallions
in a rich golden broth, on a dark rustic wooden table in warm window light.
Single dish, no text, no hands — it reads clearly even at 300 px wide.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) copies
the repo-held image `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output/entry.png`).

`entry.png` is JPEG bytes under the `entry.png` name (allowed by the rules:
the file is told apart by its first bytes), 1024×683 px, 184,211 bytes —
within the ≤1024×1024 px and ≤1 MiB limits.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
