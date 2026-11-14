# Golden Tonkotsu Ramen

A steaming bowl of tonkotsu ramen, photographed as a hero shot: springy
noodles lifted high by wooden chopsticks, seared chashu pork, a halved
soft-boiled egg with a jammy orange yolk, and chili-oil swirls glistening
on the rich creamy broth. A sheet of nori and a scatter of spring onions
finish the bowl, lit by warm window light on a dark rustic wood table.

`main.py` copies the bundled `entry.png` (a JPEG) to `/output/entry.png`,
validating it first: it must exist, be a whole JPEG under 1 MiB and
1024x1024, and the copy must match byte for byte. The program is
deterministic — every run writes the same bytes.
