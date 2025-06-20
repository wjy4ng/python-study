# 읽어들인 csv 파일에서 .를 /로 수정하여 새로운 파일로 저장하기
class App():
    def __init__(self):
        pass

    def run(self):
        with open("../10주차/singer.csv", "r") as in_file:
            with open("../10주차/singer2.csv", "w") as out_file:
                # header
                header = in_file.readline()
                header = header.strip()
                header_list = header.split(',')
                idx1 = header_list.index('이름')
                idx2 = header_list.index('국번')
                idx3 = header_list.index('전화번호')
                
                header_list = [header_list[idx1], header_list[idx2], header_list[idx3]]
                header_str = ','.join(header_list)
                out_file.writelines(header_str)
                out_file.write('\n')

                # body
                for row in in_file:
                    row = row.strip()
                    row_list = row.split(',')
                    row_list = [row_list[idx1], row_list[idx2], row_list[idx3]]
                    if(row_list[1] == "" or row_list[2] == ""):
                        pass
                    else:
                        row_str = ','.join(row_list)
                        out_file.writelines(row_str)
                        out_file.write('\n')

    def print_list(self, list):
        pass

if __name__=="__main__":
    app = App()
    app.run()

