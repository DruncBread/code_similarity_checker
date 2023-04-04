import argparse
import ast
import logging
import os.path

from py2flows.cfg import comments, flows

from py2flows.cfg.flows import CFG, CFGVisitor


# format: Specify the format of output graph. Basically three formats: png(default), svg and pdf"
# output_path: Specify the path of output graph. The default is current directory
def generate_cfg(
        code_path: str,
        format: str,
        output_path: str,
        pic_name: str):

    logging.basicConfig(level=logging.DEBUG)

    logging.debug(code_path)
    file = open(code_path, "r", encoding="utf-8")
    source = file.read()
    file.close()

    comments_cleaner = comments.CommentsCleaner(source)
    logging.debug(comments_cleaner.source)

    visitor = flows.CFGVisitor(not_in_function=True)

    base_name = os.path.basename(code_path)
    cfg = visitor.build(base_name, ast.parse(comments_cleaner.source))
    logging.debug("Previous edges: {}".format(sorted(cfg.edges.keys())))
    logging.debug("Refactored flows: {}".format(visitor.cfg.flows))
    logging.debug("Refactored inter flows: {}".format(visitor.cfg.call_return_flows))
    cfg.show(fmt=format, filepath=output_path + "/" + pic_name, name=base_name, show=False)

    return cfg


def build_directed_graph(cfg: CFG):
    import networkx
    g1 = networkx.Graph()
    for edge in cfg.edges.keys():
        g1.add_edge(edge[0], edge[1])

    sub_graphs = []
    for sub_cfg in cfg.sub_cfgs.values():
        sub_graph = networkx.Graph()
        for edge in sub_cfg.edges.keys():
            sub_graph.add_edge(edge[0], edge[1])
        sub_graphs.append(sub_graph)

    return g1, sub_graphs


def compute_similarity():
    return 1
