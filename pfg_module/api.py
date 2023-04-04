# Copyright (C) 2021 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example generating a complete program graph from a Python function.

Generates an image visualizing the complete program graph for each function
in classA.py. Saves the resulting images to the directory
`out`.

Usage:
python -m examples.program_graph_example
"""

import inspect
import os

from absl import app

from python_graphs import program_graph
from python_graphs import program_graph_graphviz
from python_graphs import program_graph_test_components as tc
from similarity_index_of_label_graph_package import similarity_index_of_label_graph_class


# def main(argv) -> None:
#     del argv  # Unused

def get_sim(code_path1: str, code_path2: str):
    # Create the output directory.
    os.makedirs('out', exist_ok=True)
    # For each function in classA.py, visualize its
    # program graph. Save the results in the output directory.

    basename1 = os.path.basename(code_path1)
    filename1 = basename1.split(".")[0]
    dirname1 = os.path.dirname(code_path1)

    basename2 = os.path.basename(code_path2)
    filename2 = basename2.split(".")[0]
    dirname2 = os.path.dirname(code_path2)

    import sys
    sys.path.append(dirname1)
    sys.path.append(dirname2)
    try:
        a = __import__(filename1)
        b = __import__(filename2)
    except:
        return '/'

    graph_a = None
    graph_b = None

    for name, fn in inspect.getmembers(a, predicate=inspect.isclass):
        graph_a = program_graph.get_program_graph(fn)
        directed_graph = build_directed_graph(graph_a)
        print(directed_graph.edges)

    for name, fn in inspect.getmembers(b, predicate=inspect.isclass):
        graph_b = program_graph.get_program_graph(fn)
        directed_graph = build_directed_graph(graph_b)
        print(directed_graph.edges)

    for name, fn in inspect.getmembers(a, predicate=inspect.isfunction):
        graph_a = program_graph.get_program_graph(fn)
        directed_graph = build_directed_graph(graph_a)
        print(directed_graph.edges)

    for name, fn in inspect.getmembers(b, predicate=inspect.isfunction):
        graph_b = program_graph.get_program_graph(fn)
        directed_graph = build_directed_graph(graph_b)
        print(directed_graph.edges)

    # graph_a = program_graph.get_program_graph(f_a)
    # graph_b = program_graph.get_program_graph(f_b)
    if  graph_a is None or graph_b is None:
        return '/'

    # program flows always have sth in common, so divided by 4
    sim = compute_similarity_of_main_cfg(graph_b,graph_a)

    print(sim)
    return sim

    directed_graph_a = build_directed_graph(graph_a)
    directed_graph_b = build_directed_graph(graph_b)

    # for name, fn in inspect.getmembers(tc, predicate=inspect.isfunction):
    #     path = f'out/{name}-program-graph.png'
    #     print(type(fn))
    #     graph = program_graph.get_program_graph(fn)
    #     directed_graph = build_directed_graph(graph)
    #     # print(directed_graph.edges)
    # # program_graph_graphviz.render(graph, path=path)

    print('Done. See the `out` directory for the results.')


def build_directed_graph(pg: program_graph):
    import networkx
    graph = networkx.Graph()
    for edge in pg.edges:
        graph.add_edge(edge.id1, edge.id2)  # it automatically changes to (small num, big num)
    return graph


def compute_similarity(pg1: program_graph, pg2: program_graph):
    main_sim_index = compute_similarity_of_main_cfg(pg1, pg2)

    sub_graphs1 = []
    sub_graphs2 = []
    for sub_cfg in pg1.sub_cfgs.values():
        sub_graph = build_directed_graph(sub_cfg)
        sub_graphs1.append(sub_graph)

    for sub_cfg in pg2.sub_cfgs.values():
        sub_graph = build_directed_graph(sub_cfg)
        sub_graphs2.append(sub_graph)

    return main_sim_index


def compute_similarity_of_main_cfg(pg1: program_graph, pg2: program_graph):
    graph1 = build_directed_graph(pg1)
    graph2 = build_directed_graph(pg2)
    similarity_index_of_label_graph = similarity_index_of_label_graph_class()
    sim_index = similarity_index_of_label_graph(graph1, graph2)
    return sim_index

# if __name__ == '__main__':
#     app.run(main)

# get_sim("C:/Users/2146/Desktop/code_sim/classA.py","C:/Users/2146/Desktop/code_sim/classB.py")
