import serial

class ModbusSerial:
    def __init__(self,baudrate=19200,timeout=0,port='/dev/ttyS4'):
        self.ser=serial.Serial(port,baudrate,timeout)

    def send(self,data,readLength=8):
        try:
            self.ser.write(data)
            data=self.ser.read(readLength)
            return data 
        except serial.SerialException as e:
            raise e 

    def close(self):
        self.close()

class ReadCoilsReq:
    def __init__(self,addr=0x01,startRegister=0x0000,count=6):
        self.addr=addr 
        self.cmd=0x01
        self.startRegister=startRegister
        self.count=count 
        self.crc=0

    def encode(self):
        buf=bytearray()
        buf.extend(self.addr.to_bytes())
        buf.extend(self.cmd.to_bytes())

        buf.extend(self.startRegister.to_bytes(2,byteorder='big'))
        buf.extend(self.count.to_bytes(2,byteorder='big'))
        self.crc=modbus_crc(buf)
        buf.extend(self.crc.to_bytes(2,byteorder='little'))
        return buf 
    
class ReadCoilsResp:
    def __init__(self,addr=0x01,byteCount=0x02,data=0x1300):
        self.addr=addr 
        self.cmd=0x01
        self.byteCount=byteCount
        self.data=data 
        self.crc=0
    
    def decode(self,data):
        if len(data)<7:
            raise ValueError('data too short')
        self.addr=data[0]
        self.cmd=data[1]
        self.byteCount=data[2]
        self.data=int.from_bytes(data[3:5],byteorder='big')
        self.crc=int.from_bytes(data[5:7],byteorder='little')

class WriteSingleCoil:
    def __init__(self,addr=0x01,startRegister=0x0000,switch=True):
        self.addr=addr 
        self.cmd=0x05
        self.startRegister=startRegister
        if switch:
            self.data=0xff00
        else:
            self.data=0x0000
        self.crc=0
    
    def encode(self):
        buf=bytearray()
        buf.extend(self.addr.to_bytes())
        buf.extend(self.cmd.to_bytes())
        buf.extend(self.startRegister.to_bytes(2,byteorder='big'))
        buf.extend(self.data.to_bytes(2,byteorder='big'))
        self.crc=modbus_crc(buf)
        buf.extend(self.crc.to_bytes(2,byteorder='little'))
        return buf
    
    def decode(self,data):
        if len(data)<8:
            raise ValueError('data too short')
        self.addr=data[0]
        self.cmd=data[1]
        self.startRegister=int.from_bytes(data[2:4],byteorder='big')
        self.data=int.from_bytes(data[4:6],byteorder='big')
        self.crc=int.from_bytes(data[6:8],byteorder='little')

def modbus_crc(data: bytes) -> int:
    crc = 0xFFFF  # 初始值
    for byte in data:
        crc ^= byte  # 按位异或
        for _ in range(8):  # 每个字节进行 8 次移位
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001  # 多项式 0xA001
            else:
                crc >>= 1
    return crc        
        

if __name__=='__main__':
    f=WriteSingleCoil(startRegister=1,switch=True)
    print(f.encode())
 

    data=b'\x01\x05\x00\x01\xff\x00\xdd\xfa'
    f.decode(data) 

    readReq=ReadCoilsReq(count=9)
    print(readReq.encode())