# 읽어들인 csv 파일에서 .를 /로 수정하여 새로운 파일로 저장하기
class App():
    def __init__(self):
        pass

    def run(self):
        with open("../10주차/singer.csv", "r") as in_file:
            with open("../10주차/singer1.csv", "w") as out_file:
                # header
                header = in_file.readline()
                header = header.strip()
                out_file.writelines(header)
                out_file.write("\n")

                # body
                for row in in_file:
                    row = row.strip()
                    data_list = row.split(',')
                    data_list[-1] = data_list[-1].replace('.', '/')
                    data_list[-2] = f"{int(data_list[-2]):0.2f}"
                    data_str = ','.join(data_list)
                    out_file.writelines(data_str)
                    out_file.write("\n")

    def print_list(self, list):
        pass

if __name__=="__main__":
    app = App()
    app.run()

