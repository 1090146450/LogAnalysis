
class LogAnalysis():
    def dmslog(self):
        with open("invo-log.txt", "r") as f:
            for fLine in f:
                if "SYS MEMORY :" in fLine:
                    fileResult1.write(fLine)
                elif 'fps'in fLine:
                    fileResult2.write(fLine)
                elif 'CPU OCCUPY :'in fLine:
                    fileResult3.write(fLine)
                elif 'CAM VOLTAGE:'in fLine:
                    fileResult4.write(fLine)
                fileResult1= open("./Log1_1SYS_MEMORY.txt", 'a')
                fileResult2 = open("./Log2_2ETH帧率.txt", 'a')
                fileResult3 = open("./Log3_3CPU.txt", 'a')
                fileResult4 = open("./Log4_4CAM VOLTAGE.txt", 'a')



LA = LogAnalysis()
LA.dmslog()


