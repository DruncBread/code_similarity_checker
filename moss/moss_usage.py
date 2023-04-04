import requests

import mosspy


def get_sim(path1: str, path2: str):
    try:
        userid = 604014254  # add your userid here

        m = mosspy.Moss(userid, "python")

        # m.addBaseFile("submission/a01.py")
        # m.addBaseFile("submission/test_student.py")

        # Submission Files
        m.addFile(path1)
        m.addFilesByWildcard(path2)

        # progress function optional, run on every file uploaded
        # result is submission URL
        url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
        print()
        print("Report URL: " + url)

        sim = get_similarity_index(url)
        print("___df_sim__: " + str(sim))
        return sim
    except Exception as e:
        return -1
    # mosspy.download_report(url, "submission/report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True))
    # log_level=logging.DEBUG (20 to disable)
    # on_read function run for every downloaded file


def get_similarity_index(url):
    if len(url) == 0:
        raise Exception("Empty url supplied")

    print(url)
    content = requests.get(url).content.decode()
    if content.__contains__("No matches"):
        return 0
    print(content)
    import re
    regex = re.compile(r'[(](.*?)[)]', re.S)
    similarity_index = re.findall(regex, content)
    similarity_index = str(similarity_index[0]).split("%")[0]
    return similarity_index

# get_sim("D:\\coding\\pycharmWorkspace\\CODE_SIM\\GUI\\trash.py",
#         "D:\\coding\\pycharmWorkspace\\CODE_SIM\\GUI\\start.py")
