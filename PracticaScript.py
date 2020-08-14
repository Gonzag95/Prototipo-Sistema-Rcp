import matplotlib.pyplot as plt
import serial
import matplotlib.animation as animation
import numpy as np
import threading
gData= []
gData.append([0.0])
gData.append([0.0])
def getData(out_data):
    with serial.Serial("\\.\COM3", 9600) as ser:
        while True:
            line = ser.readline().decode('utf-8')
            try:
               out_data[1].append(float(line))#se convierten datos a float y se guardan en gdata1
               if len(out_data[1]) > 1300:#esta condicion la podemos usar para limitar hasta donde hace el muestreo
                   out_data[1].pop(0)

            except:
                 pass

dataCollector = threading.Thread(target = getData, args = (gData,))
dataCollector.start()

def update_line(num, hl, data):
    dx=np.array(range(len(data[1])))
    dy=np.array(data[1])
    hl.set_data(dx, dy)
    return hl,

fig= plt.figure(figsize=(10,8))
plt.ylim(2,15)
plt.xlim(0,1300)
hl, = plt.plot(gData[0],gData[1])
print(gData[1],gData[0])
line_ani= animation.FuncAnimation(fig,update_line,fargs=(hl,gData),interval=50,blit=False)

plt.show()
dataCollector.join()
