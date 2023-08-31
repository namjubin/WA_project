import subprocess

class Start_pgm:
    def __init__(self, dictloc):
        self.read_pgmdict(dictloc)
    
    def read_pgmdict(self, dictloc):
        self.data = {}
        
        with open(dictloc, 'r', encoding="UTF-8") as file:
            data = file.readlines()
            
        "".join(data)
        for index, line in enumerate(data):
            key, value = line.replace("\n", "").split("=")
            key, value = key.strip(), value.strip()
            self.data[key] = value
        
    def start_pgm(self, cmd):
        print(cmd,"실행")
        
        try:
            subprocess.Popen(self.data[cmd])
        except:
            print("지정돤 파일을 찾을 수 없습니다")
            
    
if __name__ == "__main__":
    proc = Start_pgm("./cmd_ps/pgm_dict.txt")
    proc.start_pgm("메모장")