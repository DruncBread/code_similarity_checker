import re
import difflib


class SimilarityComparer:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.similarity = 0

    def compare(self):
        # 读取文件内容
        with open(self.file1, 'r') as f1:
            content1 = f1.read()
        with open(self.file2, 'r') as f2:
            content2 = f2.read()

        # 去除注释
        content1 = self._remove_comments(content1)
        content2 = self._remove_comments(content2)

        # 计算相似度
        self.similarity = self._calculate_similarity(content1, content2)

        return self.similarity

    def _remove_comments(self, content):
        # 去除单行注释
        content = re.sub(r'#.*', '', content)
        # 去除多行注释
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        return content

    def _calculate_similarity(self, content1, content2):
        # 使用 difflib 库计算两个字符串的相似度
        similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
        return similarity


