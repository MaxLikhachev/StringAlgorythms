from string_algorithms.first_second_third import open_file


class PArc:
    def __init__(self, i_beg, i_end, p_dest_vert, i_dest_vert):
        self.i_beg = i_beg  # индексы символов метки
        self.i_end = i_end  # в исходной строке
        self.p_dest_vert = p_dest_vert  # вершина, куда входит дуга
        self.i_dest_vert = i_dest_vert  # индекс листа, куда входит дуга


class PNode:
    def __init__(self, ch_arc_idx, p_arc):
        self.arcs = {}
        for i in range(256):
            self.arcs[chr(i)] = 0
        self.arcs[ch_arc_idx] = [p_arc]

    def add(self, ch_arc_idx, p_arc):
        if self.arcs.get(ch_arc_idx) == 0:
            self.arcs[ch_arc_idx] = [p_arc]
        else:
            self.arcs[ch_arc_idx].append(p_arc)

    def display(self, s):
        for i in range(len(self.arcs)):
            curr = self.arcs.get(chr(i))
            if curr != 0:
                for o in range(len(curr)):
                    print(s[curr[o].i_beg:curr[o].i_end + 1])


def find_suffix_tree_arc(s, substr, m, p_tree):
    p_arc = None
    idx_substr, idx_arc = 0, 0
    p_curr_node = p_tree
    b_stopped = 0
    while not b_stopped and p_curr_node:
        p_next_arc = p_curr_node.arcs.get(ord(substr[idx_substr]))
        if p_next_arc:
            p_arc = p_next_arc
            idx_arc = p_arc.i_beg
            while idx_substr < m and idx_arc < p_arc.i_end + 1 and substr[idx_substr] == s[idx_arc]:
                idx_substr += 1
                idx_arc += 1
            if idx_arc <= p_arc.i_end:
                b_stopped = 1
            else:
                p_curr_node = p_arc.p_dest_vert
        else:
            b_stopped = 1
    if idx_substr == m:
        idx_arc += 1
    return p_arc, idx_arc, idx_substr


def st_build_naive(s):
    n = len(s)
    p_uv_arc = PArc(0, n - 1, None, 0)
    p_tree = PNode(s[0], p_uv_arc)
    p_w_node = None
    for i in range(1, n):
        p_uv_arc, idxarc, idxsubstr = find_suffix_tree_arc(s, s[i:], n - i, p_tree)
        if not p_uv_arc:
            p_w_node = p_tree
        elif idxarc <= p_uv_arc.i_end:
            p_w_node = p_tree
            p_w_node.add(s[i], p_uv_arc)
            p_wv_arc = PArc(idxarc, p_uv_arc.i_end, p_uv_arc.p_dest_vert, p_uv_arc.i_dest_vert)
            p_uv_arc.p_dest_vert = p_w_node
            p_uv_arc.i_dest_vert = -1
        else:
            p_w_node = p_uv_arc.p_dest_vert
        p_arc_new = PArc(i + idxsubstr, n - 1, None, i)
        try:
            p_w_node.add(s[i + idxsubstr], p_arc_new)
        except IndexError:
            pass
    return p_w_node


def st_leaves_traversal(p_start_arc, n_alpha):
    if p_start_arc.i_dest_vert >= 0:
        print("Найдена позиция", p_start_arc.i_dest_vert)
    else:
        p_start_node = p_start_arc.p_dest_vert
        for k in range(n_alpha):
            p_arc = p_start_node.arcs[k]
            if p_arc:
                st_leaves_traversal(p_arc, n_alpha)

if __name__ == '__main__':
    input_string = open_file()
    print("Исходная строка", input_string)
    tree = st_build_naive(input_string)
    print('Суффиксное дерево')
    tree.display(input_string)
    for i in range(len(tree.arcs)):
        curr = tree.arcs.get(chr(i))
        if curr != 0:
            for j in range(len(curr)):
                st_leaves_traversal(curr[j], 256)
