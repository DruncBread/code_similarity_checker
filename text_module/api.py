from text_checker import SimilarityComparer

def get_sim(code_path1: str, code_path2: str):
    comparer = SimilarityComparer(code_path1,code_path2)
    similarity =comparer.compare()
    print(similarity)
    return similarity
