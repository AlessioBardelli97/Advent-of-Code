from sys import argv
from collections import namedtuple


global tree_map


Tree = namedtuple("Tree", "is_visible viewing_distance")


def top_view(i: int, j: int) -> Tree:
    ii, visible, viewing_distance = i-1, True, 0
    while ii >= 0 and visible:
        viewing_distance += 1
        if tree_map[ii][j] >= tree_map[i][j]:
            visible = False
        else:
            ii -= 1
    return Tree(visible, viewing_distance)


def bottom_view(i: int, j: int) -> Tree:
    ii, visible, viewing_distance = i+1, True, 0
    while ii < len(tree_map) and visible:
        viewing_distance += 1
        if tree_map[ii][j] >= tree_map[i][j]:
            visible = False
        else:
            ii += 1
    return Tree(visible, viewing_distance)


def left_view(i: int, j: int) -> Tree:
    jj, visible, viewing_distance = j-1, True, 0
    while jj >= 0 and visible:
        viewing_distance += 1
        if tree_map[i][jj] >= tree_map[i][j]:
            visible = False
        else:
            jj -= 1
    return Tree(visible, viewing_distance)


def right_view(i: int, j: int) -> Tree:
    jj, visible, viewing_distance = j+1, True, 0
    while jj < len(tree_map[i]) and visible:
        viewing_distance += 1
        if tree_map[i][jj] >= tree_map[i][j]:
            visible = False
        else:
            jj += 1
    return Tree(visible, viewing_distance)


def view(i: int, j: int) -> Tree:
    t = top_view(i, j)
    r = right_view(i, j)
    b = bottom_view(i, j)
    l = left_view(i, j)    
    return Tree(any([t.is_visible, r.is_visible, b.is_visible, l.is_visible]), t.viewing_distance * r.viewing_distance * b.viewing_distance * l.viewing_distance)


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        tree_map = file.read().split("\n")
        trees: list[Tree] = []
        for i in range(1, len(tree_map)-1):
            for j in range(1, len(tree_map[i])-1):
                tree = view(i, j)
                if tree.is_visible:
                    trees.append(tree)
        sum(tree.viewing_distance for tree in trees if tree.is_visible)
        print("Part One:", (len(tree_map) * 4 - 4) + len(trees))
        print("Part Two:", max(tree.viewing_distance for tree in trees))
