def main():
    from itertools import permutations

    logos = list(map(int, input().split()))
    rects = [(logos[i], logos[i+1]) for i in range(0, 6, 2)]

    total_area = sum(x * y for x, y in rects)
    side = int(total_area ** 0.5)

    if side * side != total_area:
        print(-1)
        return

    for perm in permutations([0, 1, 2]):
        for r1 in [(rects[perm[0]][0], rects[perm[0]][1]), (rects[perm[0]][1], rects[perm[0]][0])]:
            for r2 in [(rects[perm[1]][0], rects[perm[1]][1]), (rects[perm[1]][1], rects[perm[1]][0])]:
                for r3 in [(rects[perm[2]][0], rects[perm[2]][1]), (rects[perm[2]][1], rects[perm[2]][0])]:
                    if r1[0] == side and r2[0] == side and r3[0] == side and r1[1] + r2[1] + r3[1] == side:
                        grid = []
                        for _ in range(side):
                            grid.append([''] * side)

                        idx = 0
                        for ch, (w, h) in zip(['A', 'B', 'C'], [r1, r2, r3]):
                            for i in range(h):
                                for j in range(w):
                                    grid[i][idx + j] = ch
                            idx += h

                        print(side)
                        for row in grid:
                            print(''.join(row))
                        return

                    if r1[1] == side and r2[1] == side and r3[1] == side and r1[0] + r2[0] + r3[0] == side:
                        grid = []
                        for _ in range(side):
                            grid.append([''] * side)

                        idx = 0
                        for ch, (w, h) in zip(['A', 'B', 'C'], [r1, r2, r3]):
                            for i in range(h):
                                for j in range(w):
                                    grid[idx + i][j] = ch
                            idx += w

                        print(side)
                        for row in grid:
                            print(''.join(row))
                        return

    print(-1)

if __name__ == "__main__":
    main()
