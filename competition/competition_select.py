# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'competition_select.ui'
#
# Created: Mon Dec  8 22:39:57 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys
from PySide.QtGui import *
from PySide.QtCore import *
from competition.new_compdialog import *
from utils.utils import *
from competition.competition_members import *
from competition.resultswindow import *
from utils.db_classes import *
import subprocess, os

class Ui_comp_win(object):

    def setupUi(self, comp_win, compid):
        self.comp_win = comp_win
        comp_win.setObjectName("comp_win")
        comp_win.resize(600, 500)
        self.centralwidget = QtGui.QWidget(comp_win)
        self.centralwidget.setObjectName("centralwidget")
        self.newComp_butt = QtGui.QPushButton(self.centralwidget)
        self.newComp_butt.setGeometry(QtCore.QRect(70, 40, 131, 51))
        self.newComp_butt.setObjectName("newComp_butt")
        self.quick_butt = QtGui.QPushButton(self.centralwidget)
        self.quick_butt.setGeometry(QtCore.QRect(230, 40, 131, 51))
        self.quick_butt.setObjectName("quick_butt")
        self.update_exist_butt = QtGui.QPushButton(self.centralwidget)
        self.update_exist_butt.setGeometry(QtCore.QRect(390, 40, 131, 51))
        self.update_exist_butt.setObjectName("update_exist_butt")
        self.list_comps_lbl = QtGui.QLabel(self.centralwidget)
        self.list_comps_lbl.setGeometry(QtCore.QRect(70, 150, 261, 16))
        self.list_comps_lbl.setObjectName("list_comps_lbl")
        self.comps_list = QtGui.QListView(self.centralwidget)
        self.comps_list.setGeometry(QtCore.QRect(70, 200, 461, 211))
        self.comps_list.setObjectName("comps_list")
        self.filter_butt = QtGui.QPushButton(self.centralwidget)
        self.filter_butt.setGeometry(QtCore.QRect(440, 170, 80, 23))
        self.filter_butt.setObjectName("filter_butt")
        self.year_edit = QtGui.QLineEdit(self.centralwidget)
        self.year_edit.setGeometry(QtCore.QRect(310, 170, 113, 23))
        self.year_edit.setText("")
        yearvalidator = QIntValidator(1900, 2099, comp_win)
        self.year_edit.setValidator(yearvalidator)
        self.year_edit.setObjectName("year_edit")
        comp_win.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(comp_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        comp_win.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(comp_win)
        self.statusbar.setObjectName("statusbar")
        comp_win.setStatusBar(self.statusbar)
        self.newComp_butt.clicked.connect(self.new_btn_clicked)
        self.update_exist_butt.clicked.connect(comp_win.open_comp_mem_win)
        self.quick_butt.clicked.connect(self.quick_btn_clicked)


        self.session = session
        self.data = []
        self.dataStringList = []
        self.model = QStringListModel()
        list = ["one", "two", "three"]
        for instance in self.session.query(Competition).all():
            self.data.append((instance.id,instance.name,instance.year))
            self.dataStringList.append(instance.name + "     " + str(instance.year))


        self.model.setStringList(self.dataStringList)
        self.comps_list.setModel(self.model)
        self.retranslateUi(comp_win)
        QtCore.QMetaObject.connectSlotsByName(comp_win)
        self.filter_butt.clicked.connect(self.filter_btn_clicked)




    def retranslateUi(self, comp_win):
        comp_win.setWindowTitle(QtGui.QApplication.translate("comp_win", "Competition", None, QtGui.QApplication.UnicodeUTF8))
        self.newComp_butt.setText(QtGui.QApplication.translate("comp_win", "New Competition", None, QtGui.QApplication.UnicodeUTF8))
        self.quick_butt.setText(QtGui.QApplication.translate("comp_win", "Quick Import", None, QtGui.QApplication.UnicodeUTF8))
        self.update_exist_butt.setText(QtGui.QApplication.translate("comp_win", "Update Existing", None, QtGui.QApplication.UnicodeUTF8))
        self.list_comps_lbl.setText(QtGui.QApplication.translate("comp_win", "List of existing competitions", None, QtGui.QApplication.UnicodeUTF8))
        self.filter_butt.setText(QtGui.QApplication.translate("comp_win", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.year_edit.setPlaceholderText(QtGui.QApplication.translate("comp_win", "Enter a Year", None, QtGui.QApplication.UnicodeUTF8))



    def quick_btn_clicked(self):
        self.fileimportdiag = ControlFileImportDialog(self.gen_import_file, self.add_from_file)
        self.fileimportdiag.show()


    # def add_from_file(self, file=False):
    #
    #     comp = self.session.query(Competition).filter(Competition.year==text).first()
    #     if comp is None:
    #         okorcancel = QMessageBox.information(self.comp_win, "New Competition", "There are no results for the current competition year, do you wish to create a new one?", QMessageBox.Ok|QMessageBox.Cancel)
    #         if not okorcancel:
    #             return;
    #         else:
    #             comp = Competition(name=text, year=text)
    #     return;

    def add_from_file(self, filetoopen=False):
        if not filetoopen:
            filetoopen = QFileDialog.getOpenFileName(self.comp_win, 'Open file', os.getcwd())
            filetoopen = filetoopen[0]
            if filetoopen == "":
                QMessageBox.critical(self.comp_win, "Failure", "Please choose a valid directory", QMessageBox.Ok)
        workbook = xlrd.open_workbook(filetoopen)
        worksheet = workbook.sheet_by_name('Sheet1')
        num_rows = worksheet.nrows - 1
        num_cells = worksheet.ncols -1
        curr_row = -1
        counter = 0
        rowstart = curr_row = 1
        comp_text = worksheet.cell_value(rowstart, 0)
        comp_text = str(comp_text).split(" ")
        comp_year = False;
        if len(comp_text) < 2:
            QMessageBox.critical(self.comp_win, "Bad Format", "File given has an unexpected format.\n Hint: Please use the generate file for import function. Only input weight values. \n DO NOT CHANGE THE FORMAT.", QMessageBox.Ok)
            return False
        try:
            comp_year = int(comp_text[1])
            if comp_year < 1950 or comp_year > 3000:
                QMessageBox.critical(self.comp_win, "Invalid Year", "Invalid year given.", QMessageBox.Ok)
                return False;
        except ValueError as ve:
            QMessageBox.critical(self.comp_win, "Invalid Year", "Invalid year given.", QMessageBox.Ok)
            return False;

        curr_row += 3
        coeffs_defined_header = ["No", "Gender", "Lift Type", "Year", "A", "B",	"C", "D", "E", "F"]
        row = worksheet.row_slice(curr_row, 1)
        same = True;
        for i in range(len(row)):
            if row[i].value != coeffs_defined_header[i]:
                same = False
        if not same:
            QMessageBox.critical(self.comp_win, "Bad Format", "File given has an unexpected format.\n Hint: Please use the generate file for import function. Only input weight values. \n DO NOT CHANGE THE FORMAT.", QMessageBox.Ok)
            return False;

        print(row)
        return;



        fvalidator = QDoubleValidator(self.comp_win)
        progress = QProgressDialog("Importing Records...", "Abort Import", 0, num_rows, self.comp_win)
        defined_header = ["Id", "First Name", "Last Name", "Gender", "DOB", "Lift Type", "Lift Name",	"Body Weight", "Lift Weight", "Date"]
        key_names = ["id", "fname", "lname", "gender", "dob", "lift_type", "lift_name", "body_weight", "lift_weight", "date"]
        header_data = []

        curr_cell = 0
        value_list = []
        curr_row += 1
        ##get the header data to validate that the file matches the preexisting format
        while curr_cell < num_cells:
            curr_cell += 1
            # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
            cell_type = worksheet.cell_type(curr_row, curr_cell)
            cell_value = worksheet.cell_value(curr_row, curr_cell)
            print('	', cell_type, ':', cell_value)
            val = ""
            header_data.append(cell_value)

        #match the predefined format
        print header_data, defined_header
        for i in range(len(header_data)):
            if header_data[i] != defined_header[i]:
                QMessageBox.critical(self.ResultsWindow, "Error!", "Format of the file is incorrect! Please generate the skeleton file using the program.", QMessageBox.Ok)
                return



        ##get the actual values...
        while curr_row < num_rows:
            progress.setValue(curr_row)
            if progress.wasCanceled():
                QMessageBox.information(self.ResultsWindow, "Operation Cancelled", str(counter) + " records imported!", QMessageBox.Ok)
                return

            curr_row += 1
            row = worksheet.row(curr_row)
            curr_cell = 0
            value_list = {}
            while curr_cell < num_cells:
                curr_cell += 1
                # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                cell_type = worksheet.cell_type(curr_row, curr_cell)
                cell_value = worksheet.cell_value(curr_row, curr_cell)
                print('	', cell_type, ':', cell_value)
                val = ""
                if curr_row == 0:
                    header_data.append(cell_value)
                    continue
                # if curr_cell == 1:
                #     val = cell_value.split(" ")
                #     value_list.append(val[0])
                #     if len(val) >1:
                #         value_list.append(" ".join(val[1:]))
                #     else:
                #         value_list.append("")

                ##store the values in the dictionary value_list using the key from the key_names list
                else:
                    value_list[key_names[curr_cell-1]] = cell_value
            print(value_list)
            if curr_row == 0:
                counter += 1
                continue

            if len(value_list) == 0:
                counter += 1
                continue

            #get the member whose id is equal to that present in the excel file..
            mem = self.session.query(Member).filter(Member.id == value_list["id"]).first()
            if mem is None:
                mem = self.session.query(Member).filter(Member.fname == value_list['fname']).filter(Member.lname == value_list['lname']).first()
                if mem is None:
                    c = QMessageBox.information(self.ResultsWindow, "Member does not exist", "Member " + value_list["fname"] + " " + value_list["lname"] + " does not exist, do you want to create this member? \n Cancelling this box, will continue importing others.", QMessageBox.Ok|QMessageBox.Cancel )
                    if c == QMessageBox.Cancel:
                        continue
                else:
                    c = QMessageBox.information(self.ResultsWindow, "Member exists", "Member " + value_list["fname"] + " " + value_list["lname"] + " already exists, please change either his first name or last name? \n Click on OK to continue importing others.", QMessageBox.Ok|QMessageBox.Cancel )
                    continue
                ##still need to perform validity checks on gender and dob..
                mem = Member(fname=value_list["fname"], lname=value_list["lname"], gender=value_list["gender"], dob=value_list["dob"])
                try:
                    self.session.add(mem)
                    self.session.commit()
                except:
                    self.session.rollback()
                    QMessageBox.critical(self.ResultsWindow, "Failure", "Unforseen error has occurred, aborting current operation! " + str(counter) + " records have been added!", QMessageBox.Ok)
                    progress.cancel()
                    raise
            if mem not in self.comp.members:
                self.comp.members.append(mem)
                try:
                    self.session.add(self.comp)
                    self.session.commit()
                except:
                    self.session.rollback()
                    QMessageBox.critical(self.ResultsWindow, "Failure", "Unforseen error has occurred, aborting current operation! " + str(counter) + " records have been added!", QMessageBox.Ok)
                    progress.cancel()
                    raise
            print(value_list)
            b_weight = None
            if type(value_list["body_weight"]) == float:
                b_weight = value_list["body_weight"]
            elif type(value_list["body_weight"]) == str:
                res = fvalidator.validate(value_list["body_weight"],0)
                if res[0] == QValidator.State.Acceptable:
                    b_weight = float(value_list["body_weight"])

            if b_weight is None:
                ##also tell the user about the bad float value...
                QMessageBox.critical(self.ResultsWindow, "Error", "In the record of " + value_list["fname"] + " " + value_list["lname"] + "Bad value given for body weight. Click OK to continue to import other records.", QMessageBox.Ok)
                continue

            l_weight = None
            if type(value_list["lift_weight"]) == float:
                l_weight = value_list["lift_weight"]
            elif type(value_list["lift_weight"]) == str:
                res = fvalidator.validate(value_list["lift_weight"],0)
                if res[0] == QValidator.State.Acceptable:
                    l_weight = float(value_list["lift_weight"])

            if l_weight is None:
                    ##also tell the user about the bad float value...
                    QMessageBox.critical(self.ResultsWindow, "Error", "In the record of " + value_list["fname"] + " " + value_list["lname"] + "Bad value given for lift weight. Click OK to continue to import other records.", QMessageBox.Ok)
                    continue



            ltype = self.session.query(Lift_Type).filter(Lift_Type.liftName == value_list["lift_name"]).first()
            if ltype is None:
                QMessageBox.critical(self.ResultsWindow, "Error", "In the record of " + value_list["fname"] + " " + value_list["lname"] + "Bad value given for lift type or name. Click OK to continue to import other records.", QMessageBox.Ok)
                continue
            lift = self.session.query(Lift).filter(Lift.mem_id == mem.id).filter(Lift.lift_type == ltype).filter(Competition.year == self.comp.year).first()
            if lift is not None:
                QMessageBox.critical(self.ResultsWindow, "Error", "In the record of " + value_list["fname"] + " " + value_list["lname"] + " ,the record for " + value_list["lift_name"] + " for the competition year " + str(self.comp.year) + " already exists. Click OK to continue to import other records.", QMessageBox.Ok)
                continue
            lift = Lift(body_weight=b_weight, lift_weight=l_weight, lift_type=ltype, member=mem, competition=self.comp)
            try:
                self.session.add(lift)
                self.session.commit()

            except:
                self.session.rollback()
                QMessageBox.critical(self.ResultsWindow, "Failure", "Unforseen error has occurred, aborting current operation! " + str(counter) + " records have been added!", QMessageBox.Ok)
                progress.cancel()
                raise
            i += 1

            counter += 1
            # try:
            #     self.session.add(mem)
            #     self.session.commit()
            #     counter += 1;
            # except:
            #     self.session.rollback()

            print(row)
        progress.setValue(num_rows)
        QMessageBox.information(self.ResultsWindow, "Success", str(counter) + " records imported!", QMessageBox.Ok)

    def gen_import_file(self):
        print("Hi I am gen_import_file()")
        text,ok = QInputDialog.getText(self.fileimportdiag, "Input year", "Competition Year")
        if ok == False:
            return False;
        try:
            if int(text) > 3000 or int(text) < 1900:
                return False;
        except:
            QMessageBox.critical(self.comp_win, "Error!", "Invalid year input!", QMessageBox.Ok)
            return False;
        ltypes = self.session.query(Lift_Type).distinct().all()
        lnames = [];
        for l in ltypes:
            lnames.append(l.liftName);

        lift_name,ok = QInputDialog.getItem(self.fileimportdiag, "Choose Lift", "Lift Name", lnames)
        if ok == False:
            return False;
        print (lift_name)
        lift_type = self.session.query(Lift_Type).filter(Lift_Type.liftName == lift_name).first().liftType

        savedir = QFileDialog.getExistingDirectory(self.comp_win, 'Choose Output Directory', os.getcwd())

        if savedir == "":
            QMessageBox.critical(self.comp_win, "Failure", "Please choose a valid directory", QMessageBox.Ok)

        comp = self.session.query(Competition).filter(Competition.year==str(text)).first()
        if comp is None:
            #global comp
            comp = Competition(name=str(text), year=str(text))
            try:
                self.session.add(comp)
                self.session.commit()
            except:
                self.session.rollback()
                QMessageBox.critical(self.comp_win, "Failure", "Unforseen error has occurred! ", QMessageBox.Ok)
                raise
                return;

        members = comp.members;
        coeffs = comp.coefficients;

        outdir = os.path.join(savedir, "results-"+text+".xls")
        print(savedir)
        workbook = xlsxwriter.Workbook(outdir)
        worksheet = workbook.add_worksheet()
        pdata = []
        pheader_data = ["No","Id", "First Name", "Last Name", "Gender", "DOB", "Lift Type", "Lift Name", "Body Weight", "Lift Weight", "Date"];

        i=0;
        for member in members:
            i = i + 1;
            body_weight = self.session.query(Lift).filter(Competition.year==str(text)).filter(Lift.mem_id==member.id).filter(Lift_Type.liftType == lift_type).first();
            if body_weight is None:
                body_weight = ""
            else:
                body_weight = body_weight.body_weight;
            pdata.append([i, member.id, member.fname, member.lname, member.gender, member.dob, lift_type, lift_name, body_weight])

        rowstart = 0
        colstart = 0
        rowno = rowstart+1
        colno = colstart
        format = workbook.add_format({'bold': True, 'font_color': 'red'})
        worksheet.merge_range(rowno, colstart, rowno, len(pheader_data)+colstart, "Competition " + str(text), format)
        # worksheet.write(rowno, colno, "Competition", format)
        # worksheet.write(rowno, colno+1, str(text), format)
        ## write the coefficients for that year
        rowno += 1
        worksheet.merge_range(rowno, colstart, rowno, len(pheader_data)+colstart, "Please verify the coefficients given here against the competition year.", format)
        rowno += 1
        worksheet.merge_range(rowno, colstart, rowno, len(pheader_data)+colstart, "Coefficients", format)
        rowno += 1
        row = ["No","Gender", "Lift Type", "Year", "A", "B", "C", "D", "E", "F"];
        worksheet.write_row(rowno, colstart+1, row, format)
        rowno += 1
        if len(coeffs)==0:
            #global coeffs
            last_year = self.session.query(Coefficient).order_by(Coefficient.year.desc()).first()
            if last_year is None:
                coeffs = [[1,"Male", "Olympic Lift", str(text),],[2,"Female", "Olympic Lift", str(text),],[3,"Male", "Power Lift", str(text),], [4,"Female", "Power Lift", str(text),]]
            else:
                last_year = last_year.year;
                coeffs = self.session.query(Competition).filter(Competition.year==str(last_year)).first().coefficients;

        i = 1
        format = workbook.add_format({'bold': False, 'font_color': 'black'})
        for c in coeffs:
            #global i;
            row = [i,c.gender, c.liftType, c.year, c.a, c.b, c.c, c.d, c.e, c.f]
            worksheet.write_row(rowno, colstart+1, row, format)
            rowno += 1
            i+=1

        rowno += 4
        format = workbook.add_format({'bold': True, 'font_color': 'red'})
        for h in pheader_data:
            worksheet.write(rowno, colno, h, format)
            colno += 1
        rowno += 1
        colno = colstart
        columnswidth = []
        format = workbook.add_format({'bold': False, 'font_color': 'black'})
        for item in pheader_data:
            columnswidth.append(len(str(item)) + 1)
        for rowitem in pdata:
            for item in rowitem:
                worksheet.write(rowno, colno, item)
                if len(str(item)) + 1 > columnswidth[colno]:
                    columnswidth[colno] = len(str(item)) + 1
                colno += 1
            colno = colstart
            rowno += 1

        colno = colstart
        for width in columnswidth:
            worksheet.set_column(colno,colno,width)
            colno += 1
        workbook.close()
        QMessageBox.information(self.comp_win, "Success!", "Done file generated successfully!", QMessageBox.Ok)

        ret_val = 0;
        if sys.platform.startswith('darwin'):
            #global ret_val;
            ret_val = subprocess.call(('open', outdir))
        elif os.name == 'nt':
            #global ret_val;
            ret_val = os.startfile(outdir)
        elif os.name == 'posix':
            #global ret_val;
            ret_val = subprocess.call(('xdg-open', outdir))

        if ret_val != 0:
            QMessageBox.critical(self.comp_win, "Error!", "Previous application quit unexpectedly...!", QMessageBox.Ok)
            return False;


        add_from_file(self, file=False)









    def filter_btn_clicked(self):
        yr = self.year_edit.text()
        if yr != "" and yr.isdigit():
            year = int(yr)
            self.data = []
            self.dataStringList = []
            for instance in self.session.query(Competition).filter(Competition.year == year):
                self.data.append((instance.id,instance.name,instance.year))
                self.dataStringList.append(instance.name + "     " + str(instance.year))
            self.model = QStringListModel()
            self.model.setStringList(self.dataStringList)
            self.comps_list.setModel(self.model)


    def refresh_table(self):
        self.data = []
        self.dataStringList = []
        self.model = QStringListModel()
        for instance in self.session.query(Competition).all():
            self.data.append((instance.id,instance.name,instance.year))
            self.dataStringList.append(instance.name + "     " + str(instance.year))


        self.model.setStringList(self.dataStringList)
        self.comps_list.setModel(self.model)


    def new_btn_clicked(self):
        self.newWin = ControlNewCompDialog()
        result = self.newWin.exec_()
        if result == 1:
            self.refresh_table()
        else:
            print("")
            # msgBox = QMessageBox()
            # msgBox.setText("You cancelled the last operation")
            # msgBox.exec_()
        #self.newWin.raise_()



class ControlCompetitionSelectWindow(QMainWindow):

    currentInstance = None
    win_ui_stack = []

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = ControlCompetitionSelectWindow()
            print("I was here")
            return cls.currentInstance
        return cls.currentInstance

    def __init__(self, parent=None):
        super(ControlCompetitionSelectWindow, self).__init__(parent)
        self.ui =  Ui_comp_win()
        self.ui.setupUi(self, 8)
        #self.ui.back.clicked.connect()
        self.session = session

    def open_comp_mem_win(self):
        self.win_ui_stack.append(self.ui)
        rowno = self.ui.comps_list.currentIndex().row()
        if rowno == -1:
            QMessageBox.critical(self, "No Selection", "Please select a competition to update!", QMessageBox.Ok).show()

        else:
            comp_id = self.ui.data[rowno][0]
            self.comp = self.session.query(Competition).filter(Competition.id == comp_id).first()
            self.ui = Ui_competitionMembers()
            self.ui.setupUi(self,self.comp)
            self.show()

    def open_results_win(self):
        if len(self.ui.comp.members) == 0:
            QMessageBox.critical(self, "Not Enough Members", "At least one member should be enrolled!", QMessageBox.Ok).show()
        comp = self.ui.comp;
        self.win_ui_stack.append(self.ui)
        self.ui = Ui_ResultsWindow()
        self.ui.setupUi(self, comp)
        self.show()

    def go_back(self):
        self.ui = self.win_ui_stack.pop()
        self.ui.setupUi(self, self.comp)
        self.show()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    mySW = ControlCompetitionSelectWindow()
    mySW.show()
    sys.exit(app.exec_())

