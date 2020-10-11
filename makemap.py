#!/usr/bin/env python3
import random

def vec2str(vec):
    return " ".join([str(x) for x in vec])

def make_meshbox(position, size, rotation=0):
    return f"""meshbox
 position {vec2str(position)}
 size {vec2str(size)}
 rotation {rotation}
end"""

def make_shield(name, position, rotation, size, border):
    return f"""teleporter {name}
 position {vec2str(position)}
 rotation {rotation}
 size {vec2str(size)}
 border {border}
end
link
 name ln_{name}
 from {name}:b
 to {name}:b
end"""


shields = [
    make_shield("red_bottom_north", [400, 300, 0], 0, [0.125, 150, 10], 1.12),
    make_shield("red_bottom_south", [400, -300, 0], 0, [0.125, 150, 10], 1.12),
    make_shield("red_top_north", [400, 300, 15], 0, [0.125, 150, 10], 1.12),
    make_shield("red_top_mid", [400, 0, 15], 0, [0.125, 75, 10], 1.12),
    make_shield("red_top_south", [400, -300, 15], 0, [0.125, 150, 10], 1.12),

    make_shield("blue_bottom_north", [-400, 300, 0], 180, [0.125, 150, 10], 1.12),
    make_shield("blue_bottom_south", [-400, -300, 0], 180, [0.125, 150, 10], 1.12),
    make_shield("blue_top_north", [-400, 300, 15], 180, [0.125, 150, 10], 1.12),
    make_shield("blue_top_mid", [-400, 0, 15], 180, [0.125, 75, 10], 1.12),
    make_shield("blue_top_south", [-400, -300, 15], 180, [0.125, 150, 10], 1.12)
]


print("#shields")
for s in shields:
    print(s)

print("")

print("#Islands")
for xpos in range(-350, 400, 50):
    print(make_meshbox([xpos, 0, 15], [20, 20, 1]))

for xpos in range(-300, 350, 50):
    for ypos in range(-350, 420, 70):
        print(make_meshbox([xpos + random.uniform(-4, 4),
                            ypos + random.uniform(-4, 4),
                            0],
                        size=[20+random.uniform(-15, 0),
                              20+random.uniform(-15, 2),
                              5 + random.uniform(-3, 15)],
                        rotation=random.uniform(0, 360))
            )

print(make_meshbox([0, 300, 5], [230, 20, 1]))
print(make_meshbox([0, -300, 5], [230, 20, 1]))

print(make_meshbox([0, 450, 5], [400, 30, 1]))
print(make_meshbox([0, -450, 5], [400, 30, 1]))
