import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)


def can_fill_with_rotation(tiles, h, w):
    # Calculate total area of tiles and the grid
    total_tiles_area = 0
    for tile in tiles:
        total_tiles_area += tile[0] * tile[1]
    grid_area = h * w

    # If total area of tiles is less than the grid area, it's impossible to fill
    if total_tiles_area < grid_area:
        return False

    # Attempt to place each tile on a 5x5 grid
    grid = [[0 for _ in range(w)] for _ in range(h)]

    # Check if a tile can be placed at a specific position
    def can_place(tile, row, col):
        tile_rows, tile_cols = tile
        for r in range(tile_rows):
            for c in range(tile_cols):
                if row + r >= h or col + c >= w or grid[row + r][col + c] != 0:
                    return False
        return True

    # Place a tile on the grid
    def place_tile(tile, row, col, tile_id):
        tile_rows, tile_cols = tile
        for r in range(tile_rows):
            for c in range(tile_cols):
                grid[row + r][col + c] = tile_id

    # Recursive function to try placing tiles
    def try_place_tiles(tiles, tile_id):
        if tile_id > len(tiles):
            # If all tiles have been placed, check if the grid is fully covered
            return all(all(cell != 0 for cell in row) for row in grid)

        for row in range(h):
            for col in range(w):
                # Try both orientations of the tile
                for orientation in [
                    (tiles[tile_id - 1][0], tiles[tile_id - 1][1]),
                    (tiles[tile_id - 1][1], tiles[tile_id - 1][0]),
                ]:
                    if can_place(orientation, row, col):
                        place_tile(orientation, row, col, tile_id)
                        if try_place_tiles(tiles, tile_id + 1):
                            return True
                        # Reset placed tiles for backtracking
                        place_tile(orientation, row, col, 0)
        return False

    # ０から(1<<n)-1まで全探索。
    for i in range(1 << n):
        tile_to_use = []
        for j in range(n):
            wari = 1 << j
            if (i // wari) % 2 == 1:
                tile_to_use.append(tiles[j])
        total_tiles_area_to_use = 0
        for tile in tile_to_use:
            total_tiles_area_to_use += tile[0] * tile[1]
        if total_tiles_area_to_use != h * w:
            continue
        if try_place_tiles(tile_to_use, 1):
            return True
    # Start placing tiles from the first one
    return False


n, h, w = map(int, input().split())
tiles = []
for i in range(n):
    a, b = map(int, input().split())
    tiles.append([a, b])

# Check if the tiles can fill the 5x5 grid
if can_fill_with_rotation(tiles, h, w):
    print("Yes")
else:
    print("No")
