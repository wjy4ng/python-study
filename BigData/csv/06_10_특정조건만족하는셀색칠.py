from tkinter import *
import csv

class App():
    def __init__(self):
        self.window = Tk()
        self.result_list = []
        self.csv_list = []

    def run(self, csv_file_path="../10주차/singer1.csv"):
        try:
            with open(csv_file_path, "r") as singer1:
                # header
                csv_reader = csv.reader(singer1)
                header_list = next(csv_reader)
                self.csv_list.append(header_list)

                # body
                for row_list in csv_reader:
                    self.csv_list.append(row_list)
                
                # row, col
                row = len(self.csv_list)
                col = len(self.csv_list[0])

                # Create sheet
                self.make_empty_sheet(row, col)
                
                # height index
                try:
                    idx = self.csv_list[0].index("키") 
                except ValueError:
                    print("경고: '키' 컬럼을 CSV 헤더에서 찾을 수 없습니다. 기본 인덱스 6을 사용합니다.")
                    idx = 6 

                # Insert data
                for i in range(row):
                    for j in range(col):
                        if(self.csv_list[i][idx].isnumeric()):
                            if(int(self.csv_list[i][idx])>=167):
                                ent = self.result_list[i][j]
                                ent.configure(bg='yellow')
                        self.result_list[i][j].insert(0, self.csv_list[i][j])

                self.window.mainloop()

        except FileNotFoundError:
            print("오류: '{}' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.".format(csv_file_path))
            self.window.destroy()

    def make_empty_sheet(self, row, col):
        for i in range(row):
            tmp = []
            for j in range(col):
                ent = Entry(self.window, text="", width=10)
                ent.grid(row=i, column=j)
                tmp.append(ent)
            self.result_list.append(tmp)
    
if __name__=="__main__":
    app = App()
    app.run()
