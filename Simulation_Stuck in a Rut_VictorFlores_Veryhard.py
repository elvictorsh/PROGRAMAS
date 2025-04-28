def main():
    n = int(input())
    cows = []
    for _ in range(n):
        line = input().strip()
        direction = line[0]
        x, y = map(int, line[1:].split())
        cows.append({
            'direction': direction,
            'x': x,
            'y': y,
            'eaten': 1,
            'stopped': False,
            'infinite': False
        })

    pasture = dict()
    for idx, cow in enumerate(cows):
        pos = (cow['x'], cow['y'])
        pasture[pos] = idx

    while True:
        moved = False
        next_positions = {}

        for idx, cow in enumerate(cows):
            if cow['stopped'] or cow['infinite']:
                continue

            if cow['direction'] == 'N':
                next_pos = (cow['x'], cow['y'] + 1)
            else:
                next_pos = (cow['x'] + 1, cow['y'])

            next_positions[idx] = next_pos

        collision = dict()
        for idx, pos in next_positions.items():
            if pos not in collision:
                collision[pos] = []
            collision[pos].append(idx)

        for pos, idxs in collision.items():
            if len(idxs) > 1:
                for idx in idxs:
                    cows[idx]['infinite'] = True

        for idx, cow in enumerate(cows):
            if cow['stopped'] or cow['infinite']:
                continue

            pos = next_positions[idx]

            if pos in pasture:
                cows[idx]['stopped'] = True
            else:
                cow['x'], cow['y'] = pos
                pasture[pos] = idx
                cow['eaten'] += 1
                moved = True

        if not moved:
            break

    for cow in cows:
        if cow['infinite']:
            print("Infinity")
        else:
            print(cow['eaten'])

if __name__ == "__main__":
    main()

