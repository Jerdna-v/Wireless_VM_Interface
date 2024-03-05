import serial

class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = min(2048, self.s.in_waiting)
            data = self.s.read(i)
            i = data.find(b"\r")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)

ser = serial.Serial("COM10", 9600, timeout=1, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
rl = ReadLine(ser)
with open("60-zlatnakopacka-kafe.txt", 'a') as f:
    while True:
        try:
            f.write(rl.readline().decode("ascii"))
        except Exception as e:
            print(e)