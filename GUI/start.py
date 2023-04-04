import random
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_MainWindow import Ui_MainWindow
import pymysql


class MainWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.path2 = None
        self.path1 = None
        self.open_main()
        self.threadpool = QThreadPool()

    # Open main window
    def open_main(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.get_file1.clicked.connect(self.get_file1)
        self.ui.get_file2.clicked.connect(self.get_file2)
        self.ui.subit.clicked.connect(self.submit_files)

    # Open dialog window to choose C file
    def get_file1(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "select a .py file", "", "Python Files (*.py)")
        self.path1 = file_name
        self.ui.file_path1.setText(file_name)

    def get_file2(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "select a .py file", "", "Python Files (*.py)")
        self.path2 = file_name
        self.ui.file_path2.setText(file_name)

    def get_overall_rating(self,cfg_sim,dfg_sim,pfg_sim,text_sim):
        if pfg_sim=='/' and dfg_sim=='/':
            return cfg_sim*0.85+text_sim*0.15
        if pfg_sim=='/':
            return max(cfg_sim,dfg_sim)*0.65+min(cfg_sim,dfg_sim)*0.25+text_sim*0.1
        if dfg_sim=='/':
            return cfg_sim*0.75+pfg_sim*0.125+text_sim*0.125
        return max(cfg_sim,dfg_sim)*0.5+min(cfg_sim,dfg_sim)*0.3+pfg_sim*0.1+text_sim*0.1

    def submit_files(self):
        from cfg_module.api import get_sim as get_cfg_sim
        from moss.moss_usage import get_sim as get_dfg_sim
        from pfg_module.api import get_sim as get_pfg_sim
        from text_module.api import get_sim as get_text_sim

        dfg_sim = float(get_dfg_sim(self.path1, self.path2))/100.0
        if dfg_sim==-0.01:
            dfg_sim_show='/'
            dfg_sim='/'
        else: dfg_sim_show=dfg_sim*100
        # dfg_sim = 0
        cfg_sim = get_cfg_sim(self.path1, self.path2)
        # cfg_sim=0
        pfg_sim=get_pfg_sim(self.path1,self.path2)
        if pfg_sim!='/':
            pfg_sim_show=pfg_sim*100.0
        else: pfg_sim_show=pfg_sim
        # pfg_sim=0
        text_sim=get_text_sim(self.path1,self.path2)
        overall_sim= self.get_overall_rating(cfg_sim,dfg_sim,pfg_sim,text_sim)
        if overall_sim<=0.5:
            comment="Low"
        if(overall_sim>0.5) & (overall_sim<=0.75):
            comment="Medium"
        if overall_sim>0.75:
            comment="Critical"

        result = "Text Similarity: {0}\n" \
                 "CFG Similarity: {1}%\n" \
                 "DFG Similarity: {2}%\n" \
                 "PFG Similarity: {3}%\n\n" \
                 "Overall Similarity: {4} ({5})".format(
            text_sim*100.0,
            str(cfg_sim*100.0),
            dfg_sim_show,
            pfg_sim_show,
            overall_sim*100.0,
            comment)

        self.ui.textEdit.setText(result)
        db = pymysql.connect(host="localhost", user= "root",password= "123",database= "sim_tester")
        cursor = db.cursor()
        test_time=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        id=test_time+"_"+str(random.randint(0,10000))
        values=(str(id),
                str(self.path1),
                str(self.path2),
                cfg_sim,
                dfg_sim_show,
                str(pfg_sim),
                str(text_sim),
                str(overall_sim),
                str(test_time))
        query="insert into test_history(id,file_path1,file_path2,cfg_sim,dfg_sim,pfg_sim,text_sim,overall_sim,test_time) "\
                       "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(query,values)
        db.commit()

    # Save converted file as .ll (LLVM file)
    def save(self, result):
        if result:
            fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', "", "LLVM Files (*.ll)")
            if result is not None and fileName != '':
                with open(fileName, "w") as f1:
                    f1.write(result)
        self.ui.linePathForC.setText('')
        self.ui.linePathForLlvm.setText('')
        self.ui.btnConvInLlvm.setEnabled(False)
        self.ui.btnBuildDFG.setEnabled(False)
        self.ui.btnChooseC.setEnabled(True)
        self.ui.btnChooseLlvm.setEnabled(True)

    def reportProgress(self, s):
        self.ui.textPrint.append(s)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
