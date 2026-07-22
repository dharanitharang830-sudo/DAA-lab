def bin_packing(items, capacity):
    items.sort(reverse=True)
    bins = []

    for item in items:
        placed = False

        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                placed = True
                break

        if not placed:
            bins.append(item)

    return bins

items = [4, 8, 1, 4, 2, 1, 3]
capacity = 10

bins = bin_packing(items, capacity)

print("Number of bins required:", len(bins))
print("Bin capacities used:", bins)