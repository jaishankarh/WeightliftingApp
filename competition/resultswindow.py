# -*- coding: utf-8 -*- 9944611954

# Form implementation generated from reading ui file 'resultswindow.ui'
#
# Created: Thu Dec 11 18:54:36 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import *
from PySide.QtGui import *
from utils.db_classes import *
from sqlalchemy.sql import text
from utils.utils import *
from sqlalchemy.orm import *
from datetime import *
from competition.fileimportdialog import *
import xlrd
import os
import xlsxwriter


class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow, comp):
        self.ResultsWindow = ResultsWindow
        self.session = session
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(ResultsWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.back_btn = QtGui.QPushButton(self.centralWidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 30, 80, 23))
        self.back_btn.setObjectName("back_btn")
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(40, 231, 721, 301))
        self.tableView.setObjectName("tableView")
        self.today_results_lbl = QtGui.QLabel(self.centralWidget)
        self.today_results_lbl.setGeometry(QtCore.QRect(50, 210, 111, 16))
        self.today_results_lbl.setObjectName("today_results_lbl")
        self.lift_type = QtGui.QComboBox(self.centralWidget)
        self.lift_type.setGeometry(QtCore.QRect(60, 90, 191, 23))
        self.lift_type.setEditable(False)
        self.lift_type.setObjectName("lift_type")
        # conn = engine.connect()
        # s = text("SELECT DISTINCT LIFT_TYPE.liftType FROM LIFT_TYPE")
        # ls = conn.execute(s).fetchall()
        # conn.close()
        ls = self.session.query(Lift_Type.liftType).distinct()
        print(ls)
        #ls = [("Olympic Lift", "Snatch"), ("Power Lift", "Squat")]
        self.liftypes = []
        for l in ls:
            self.liftypes.append(l[0])
        self.lift_type.insertItems(0, self.liftypes)


        self.lift_name = QtGui.QComboBox(self.centralWidget)
        self.lift_name.setGeometry(QtCore.QRect(390, 90, 191, 23))
        self.lift_name.setEditable(False)
        self.lift_name.setObjectName("lift_name")
        self.lifts = []
        self.liftnames = []
        for instance in  self.session.query(Lift_Type).filter(Lift_Type.liftType == self.liftypes[0]).all():
            self.lifts.append((instance.id, instance))
            self.liftnames.append(instance.liftName)
        self.lift_name.insertItems(0,self.liftnames)

        self.member_box = QtGui.QComboBox(self.centralWidget)
        self.member_box.setGeometry(QtCore.QRect(60, 150, 261, 23))
        self.member_box.setEditable(True)
        self.member_box.setObjectName("member_box")
        self.comp = comp
        self.all_members = self.comp.members
        self.all_members_str = []
        for instance in self.all_members:
            self.all_members_str.append(str(instance.fname) + " " + str(instance.lname))
        self.member_box.insertItems(0, self.all_members_str)

        self.bdy_weight_btn = QtGui.QLineEdit(self.centralWidget)
        self.bdy_weight_btn.setGeometry(QtCore.QRect(340, 150, 91, 23))
        self.bdy_weight_btn.setObjectName("bdy_weight_btn")
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(610, 150, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("dd-MM-yyyy")
        self.dateEdit.setCalendarPopup(True);
        self.comp_name_lbl = QtGui.QLabel(self.centralWidget)
        self.comp_name_lbl.setGeometry(QtCore.QRect(190, 20, 251, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comp_name_lbl.sizePolicy().hasHeightForWidth())
        self.comp_name_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comp_name_lbl.setFont(font)
        self.comp_name_lbl.setObjectName("comp_name_lbl")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(590, 0, 89, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year_val = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.year_val.setFont(font)
        self.year_val.setObjectName("year_val")
        self.horizontalLayout.addWidget(self.year_val)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.add_from_file_btn = QtGui.QPushButton(self.centralWidget)
        self.add_from_file_btn.setGeometry(QtCore.QRect(308, 190, 111, 23))
        self.add_from_file_btn.setObjectName("add_from_file_btn")
        self.save_btn = QtGui.QPushButton(self.centralWidget)
        self.save_btn.setGeometry(QtCore.QRect(449, 190, 111, 23))
        self.save_btn.setObjectName("save_btn")
        self.lift_weight = QtGui.QLineEdit(self.centralWidget)
        self.lift_weight.setGeometry(QtCore.QRect(460, 150, 113, 23))
        self.lift_weight.setObjectName("lift_weight")
        self.del_btn = QtGui.QPushButton(self.centralWidget)
        self.del_btn.setGeometry(QtCore.QRect(590, 190, 141, 23))
        self.del_btn.setObjectName("del_btn")
        self.choose_type_lbl = QtGui.QLabel(self.centralWidget)
        self.choose_type_lbl.setGeometry(QtCore.QRect(60, 70, 131, 16))
        self.choose_type_lbl.setObjectName("choose_type_lbl")
        self.lift_name_lbl = QtGui.QLabel(self.centralWidget)
        self.lift_name_lbl.setGeometry(QtCore.QRect(400, 70, 131, 16))
        self.lift_name_lbl.setObjectName("lift_name_lbl")
        self.mem_lbl = QtGui.QLabel(self.centralWidget)
        self.mem_lbl.setGeometry(QtCore.QRect(60, 130, 57, 15))
        self.mem_lbl.setObjectName("mem_lbl")
        self.bdy_wt_lbl = QtGui.QLabel(self.centralWidget)
        self.bdy_wt_lbl.setGeometry(QtCore.QRect(340, 130, 81, 16))
        self.bdy_wt_lbl.setObjectName("bdy_wt_lbl")
        self.lift_nm_lbl = QtGui.QLabel(self.centralWidget)
        self.lift_nm_lbl.setGeometry(QtCore.QRect(460, 130, 71, 16))
        self.lift_nm_lbl.setObjectName("lift_nm_lbl")
        self.datefilterEdit = QtGui.QDateEdit(self.centralWidget)
        self.datefilterEdit.setGeometry(QtCore.QRect(610, 150, 110, 24))
        self.datefilterEdit.setObjectName("datefilterEdit")
        self.datefilterEdit.setDisplayFormat("dd-MM-yyyy")
        self.datefilterEdit.setCalendarPopup(True);
        ResultsWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ResultsWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menuBar.setObjectName("menuBar")
        ResultsWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ResultsWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        ResultsWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ResultsWindow)
        self.statusBar.setObjectName("statusBar")
        ResultsWindow.setStatusBar(self.statusBar)

        self.header_data = ["Id","Member", "Lift Name", "Lift Type", "Body Weight", "Lift Weight", "Date"]

        self.all_lifts = []
        ls = self.comp.lifts

        for instance in self.session.query(Lift).join(Lift.competition).filter(Competition.year == self.comp.year).all():
            self.all_lifts.append((instance.id, instance.member.fname, instance.lift_type.liftName, instance.lift_type.liftType, instance.body_weight, instance.lift_weight, instance.date))


        print("***************************")
        print(self.all_lifts)
        self.model =  MyTableModel(ResultsWindow, self.all_lifts, self.header_data)
        self.tableView.setModel(self.model)

        #self.tableView.hideColumn(0) #hide column 'id'
        # self.tableView.horizontalHeader().stretchLastSection()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows) #select Row
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection) #disable multiselect
        self.tableView.setSortingEnabled(True)
        self.tableView.sortByColumn(0, Qt.AscendingOrder)
        #self.tableView.resizeColumnsToContents()
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)

        self.back_btn.clicked.connect(ResultsWindow.go_back)
        self.save_btn.clicked.connect(self.save_result)
        self.add_from_file_btn.clicked.connect(self.raiseFileDialog)
        self.lift_type.currentIndexChanged.connect(self.populate_liftnames)
        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

    def retranslateUi(self, ResultsWindow):
        ResultsWindow.setWindowTitle(QtGui.QApplication.translate("ResultsWindow", "ResultsWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.back_btn.setText(QtGui.QApplication.translate("ResultsWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.today_results_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Filter by date", None, QtGui.QApplication.UnicodeUTF8))
        self.bdy_weight_btn.setInputMask(QtGui.QApplication.translate("ResultsWindow", "000.00 Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.comp_name_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Current Competition", None, QtGui.QApplication.UnicodeUTF8))
        self.year_val.setText(QtGui.QApplication.translate("ResultsWindow", "Year:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ResultsWindow", "2009", None, QtGui.QApplication.UnicodeUTF8))
        self.add_from_file_btn.setText(QtGui.QApplication.translate("ResultsWindow", "Import from file", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("ResultsWindow", "Add/Save Result", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_weight.setInputMask(QtGui.QApplication.translate("ResultsWindow", "000.00 Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("ResultsWindow", "Delete Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.choose_type_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Choose Lift Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_name_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Choose Lift Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.mem_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Member", None, QtGui.QApplication.UnicodeUTF8))
        self.bdy_wt_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Body Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_nm_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Lift Weight", None, QtGui.QApplication.UnicodeUTF8))
        #self.checkBox.setText(QtGui.QApplication.translate("ResultsWindow", "Check for viewing today\'s Results", None, QtGui.QApplication.UnicodeUTF8))
        t = date.today()
        self.todaydate = t.strftime("%d-%m-%Y")
        self.datefilterEdit.setDate(QDate.fromString(self.todaydate,"dd-MM-yyyy"))


    def populate_liftnames(self):
        self.lift_name.clear()
        index = self.lift_type.currentIndex()
        sel_type = self.liftypes[index]
        self.lifts = []
        self.liftnames = []
        for instance in  self.session.query(Lift_Type).filter(Lift_Type.liftType == sel_type).all():
            self.lifts.append((instance.id, instance))
            self.liftnames.append(instance.liftName)
        self.lift_name.insertItems(0,self.liftnames)

    def refresh_table(self):
        self.all_lifts = []

        # if self.checkBox.isChecked():
        #     for instance in self.session.query(Lift).join(Lift.competition).filter(Competition.year == self.comp.year).filter(Lift.date == self.todaydate).all():
        #         self.all_lifts.append((instance.id, instance.member.fname, instance.lift_type.liftName, instance.lift_type.liftType, instance.body_weight, instance.lift_weight, instance.date))
        # else:
        for instance in self.session.query(Lift).join(Lift.competition).filter(Competition.year == self.comp.year).all():
                self.all_lifts.append((instance.id, instance.member.fname, instance.lift_type.liftName, instance.lift_type.liftType, instance.body_weight, instance.lift_weight, instance.date))

        print(self.all_lifts)
        self.model =  MyTableModel(self.ResultsWindow, self.all_lifts, self.header_data)
        self.tableView.setModel(self.model)

    def save_result(self):
        mem_ind = self.member_box.currentIndex()
        mem = self.all_members[mem_ind]
        lift_ind = self.lift_name.currentIndex()
        lift_name = self.liftnames[lift_ind]
        lift_type = self.session.query(Lift_Type).filter(Lift_Type.liftName == lift_name).first()
        lift_weight = self.lift_weight.text()[0:-3]
        bdy_weight = self.bdy_weight_btn.text()[0:-3]
        # print(lift_weight)
        # print(bdy_weight)
        lift_date = self.datefilterEdit.text()
        d = datetime.strptime(lift_date, "%d-%m-%Y")
        # print(lift_date)
        y = d.year
        # print(self.comp.year)
        # print(y)
        existing_lifts = self.session.query(Lift).join(Member).join(Competition).join(Lift_Type).filter(Competition.year == self.comp.year).filter(Lift_Type.liftName == lift_name).filter(Member.id == mem.id).all()
        if len(existing_lifts) > 0:
            QMessageBox.critical(self.ResultsWindow, "Duplicate Entries", "Entry for the lift type already exists for this member in this competition. Please change one of the values!",  QMessageBox.Ok)
            return
        if y != self.comp.year:
            QMessageBox.critical(self.ResultsWindow, "Inconsistent date", "Year of the lift should match the year of the competition!", QMessageBox.Ok)
            return
        print(lift_type)
        lift = Lift(body_weight = bdy_weight, date=lift_date, lift_weight=lift_weight, member=mem, competition=self.comp, lift_type=lift_type)
        try:
            self.session.add(lift)
            self.session.commit()
            self.refresh_table()
        except:
            self.session.rollback()
            raise
        # print(lift_type)
        # print(mem)
        # print(lift.id)

    def raiseFileDialog(self):
        self.fileimportdiag = ControlFileImportDialog(self.gen_import_file, self.add_from_file)
        self.fileimportdiag.show()
        print("I was in raise file dialog")

    def gen_import_file(self):
        print("Hi I am gen_import_file()")
        index = self.lift_type.currentIndex()
        lift_type = self.liftypes[index]
        index = self.lift_name.currentIndex()
        lift_name = self.liftnames[index]
        savedir = QFileDialog.getExistingDirectory(self.ResultsWindow, 'Choose Output Directory', os.getcwd())

        if savedir == "":
            QMessageBox.critical(self.ResultsWindow, "Failure", "Please choose a valid directory", QMessageBox.Ok)
        outdir = os.path.join(savedir, "results-for-" + lift_name + "-" + str(self.comp.year) + ".xls")
        print(savedir)
        workbook = xlsxwriter.Workbook(outdir)
        worksheet = workbook.add_worksheet()
        pdata = []
        pheader_data = ["No","Id", "First Name", "Last Name", "Gender", "DOB", "Lift Type", "Lift Name", "Body Weight", "Lift Weight", "Date"];

        i=0;
        for member in self.all_members:
            i = i + 1;
            pdata.append([i, member.id, member.fname, member.lname, member.gender, member.dob, lift_type, lift_name])

        rowstart = 0
        colstart = 0
        rowno = rowstart+1
        colno = colstart
        format = workbook.add_format({'bold': True, 'font_color': 'red'})

        for h in pheader_data:
            worksheet.write(rowstart, colno, h, format)
            colno += 1
        colno = colstart
        columnswidth = []
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
        QMessageBox.information(self.ResultsWindow, "Success!", "Done file generated successfully!", QMessageBox.Ok)


    def add_from_file(self):
        '''
        some action to indicate which button has been clicked
        '''
        filetoopen = QFileDialog.getOpenFileName(self.ResultsWindow, 'Open file', os.getcwd())
        if filetoopen[0] == "":
            QMessageBox.critical(self.ResultsWindow, "Failure", "Please choose a valid directory", QMessageBox.Ok)
        workbook = xlrd.open_workbook(filetoopen[0])
        worksheet = workbook.sheet_by_name('Sheet1')
        num_rows = worksheet.nrows - 1
        num_cells = worksheet.ncols -1
        curr_row = -1
        counter = 0
        fvalidator = QDoubleValidator(self.ResultsWindow)
        progress = QProgressDialog("Importing Records...", "Abort Import", 0, num_rows, self.ResultsWindow)
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
        self.refresh_table()



class ControlResultsWindow(QMainWindow):

    currentInstance = None

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = ControlResultsWindow()
            print("I was here")
            return cls.currentInstance
        return cls.currentInstance

    def __init__(self, parent=None):
        super(ControlResultsWindow, self).__init__(parent)
        self.ui =  ControlResultsWindow()
        self.ui.setupUi(self)