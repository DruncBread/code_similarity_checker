import os

import networkx
from similarity_index_of_label_graph_package import similarity_index_of_label_graph_class

from py2flows.cfg.flows import CFG
from py2flows import generator


def build_directed_graph(cfg: CFG):
    import networkx
    g1 = networkx.Graph()
    for edge in cfg.edges.keys():
        g1.add_edge(edge[0], edge[1])  # it automatically changes to (small num, big num)

    return g1


def compute_similarity(cfg1: CFG, cfg2: CFG):
    main_sim_index = compute_similarity_of_main_cfg(cfg1, cfg2)

    sub_graphs1 = []
    sub_graphs2 = []
    for sub_cfg in cfg1.sub_cfgs.values():
        sub_graph = build_directed_graph(sub_cfg)
        sub_graphs1.append(sub_graph)

    for sub_cfg in cfg2.sub_cfgs.values():
        sub_graph = build_directed_graph(sub_cfg)
        sub_graphs2.append(sub_graph)

    return main_sim_index


def compute_similarity_of_main_cfg(cfg1, cfg2):
    graph1 = build_directed_graph(cfg1)
    graph2 = build_directed_graph(cfg2)
    similarity_index_of_label_graph = similarity_index_of_label_graph_class()
    sim_index = similarity_index_of_label_graph(graph1, graph2)
    return sim_index


def compute_similarity_of_sub_cfgs():
    return 1


def get_sim(code_path1:str, code_path2:str):
    code_path = "./examples/06_if_copy.py"
    output_path = "./images"
    pic_name = "12_listcomp"

    cfg1 = generator.generate_cfg(code_path1, "png", output_path, pic_name)

    code_path = "./examples/06_if.py"
    output_path = "./images"
    pic_name = "06"

    cfg2 = generator.generate_cfg(code_path2, "png", output_path, pic_name)

    graph= build_directed_graph(cfg1)

    similarity = compute_similarity(cfg1, cfg2)
    return similarity


# code_path1 = "D:\coding\pycharmWorkspace\CODE_SIM\samples\classA.py"
# code_path2 = "D:\coding\pycharmWorkspace\CODE_SIM\samples\classB.py"
# get_sim(code_path2,code_path1)