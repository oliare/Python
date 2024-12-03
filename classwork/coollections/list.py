# ------ tuple: fixed size, cannot modify
coord = (1, 10)

# coord[0] += 1

# ------ list: dynamic size, can modify
colors = ["red", "green", "blue"]

for c in colors:
    print(c)

colors[0] = "yellow"

if "purple" not in colors:
    colors.append("purple")

# ---- shallow copy
shallowList = colors
colors[1] = "superpuperwhite"

# ---- deep copy
deepList = colors.copy()
colors[2] = "blablacolor"

print(f"Colors: {colors}")
print(f"Shallow: {shallowList}")
print(f"Deep: {deepList}")

# --- deleting
colors.pop(3)   # remove fourth
colors.pop()    # remove last
colors.pop(-1)  # remove last

if "black" in colors:
    colors.remove("black")