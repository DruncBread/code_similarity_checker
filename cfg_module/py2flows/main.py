#  Copyright 2022 Layne Liu
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import argparse
import ast
import logging
import os.path

from cfg import comments, flows

# def construct_CFG(file_name) -> flows.CFG:
#     with open(file_name) as handler:
#         source = handler.read()
#         comments_cleaner = comments.CommentsCleaner(source)
#         visitor = flows.CFGVisitor(not_in_function=True)
#         base_name = os.path.basename(file_name)
#         cfg = visitor.build(base_name, ast.parse(comments_cleaner.source))
#         logging.debug("Previous edges: {}".format(sorted(cfg.edges.keys())))
#         logging.debug("Refactored flows: {}".format(visitor.cfg.flows))
#         logging.debug(
#             "Refactored inter flows: {}".format(visitor.cfg.call_return_flows)
#         )
#         cfg.show()
#
#         return cfg
from py2flows.cfg.flows import CFG


def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(
        description="compute flows of control flow graphs. "
                    "But of course you can use it to examine cfgs only"
    )
    parser.add_argument(
        "-cp",
        "--code_path", default="../examples/12_listcomp.py",
        help="path to the Python file"
    )
    parser.add_argument(
        "-f",
        "--format",
        default="png",
        help="Specify the format of output graph. Basically three formats: png(default), svg and pdf",
    )
    parser.add_argument(
        "-op",
        "--output_path",
        default="../images",
        help="Specify the path of output graph. The default is current directory",
    )
    parser.add_argument(
        "-pn",
        "--pic_name",
        default="output",
        help="Specify the name of the output file. The default is output",
    )
    args = parser.parse_args()
    logging.debug(args.code_path)
    file = open(args.code_path, "r", encoding="utf-8")
    source = file.read()
    file.close()

    comments_cleaner = comments.CommentsCleaner(source)
    logging.debug(comments_cleaner.source)

    visitor = flows.CFGVisitor(not_in_function=True)
    base_name = os.path.basename(args.code_path)
    cfg = visitor.build(base_name, ast.parse(comments_cleaner.source))
    logging.debug("Previous edges: {}".format(sorted(cfg.edges.keys())))
    logging.debug("Refactored flows: {}".format(visitor.cfg.flows))
    logging.debug("Refactored inter flows: {}".format(visitor.cfg.call_return_flows))
    cfg.show(fmt=args.format, filepath=args.output_path + "/" + args.pic_name, name=base_name,show=False)

    return cfg


if __name__ == "__main__":
    main()
