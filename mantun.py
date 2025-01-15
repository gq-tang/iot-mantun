import modbus

class MantunSwitch(modbus.WriteSingleCoil):
    def __init__(self,addr=0x01,startRegister=0x0000,switch=True):
        super().__init__(addr=addr,startRegister=startRegister,switch=switch)

    def state(self):
        switch=self.data&0xff00>0
        return {
            'switchNo':self.startRegister,
            'switch':switch
        }    

class MantunSwitchResp(modbus.ReadCoilsResp):
    def __init__(self, addr=1, byteCount=2, data=0):
        super().__init__(addr, byteCount, data)
    
    def decode(self,data):
        super().decode(data)

    def states(self):
        results=[]
        for i in range(16):
            switch=False
            if self.data&(1<<i)>0:
                switch=True 
            results.append({
                'switchNo':i,
                'switch':switch
            })    
        return results     


class MantunModbus(modbus.ModbusSerial):
    def __init__(self,baudrate=19200,timeout=0,port='/dev/ttyS4',bytesize=8):
        super().__init__(baudrate=baudrate,timeout=timeout,port=port,bytesize=bytesize)
    
    def switch(self,addr=0x01,startRegister=0x0000,switch=True):
        f=MantunSwitch(addr=addr,startRegister=startRegister,switch=switch)
        try:
            resp=self.send(f.encode())
            f.decode(resp)
            return f.state()
        except Exception as e:
            raise e 

    def readSwitchState(self,addr=0x01,startRegister=0x0000,count=6):
        f=modbus.ReadCoilsReq(addr=addr,startRegister=startRegister,count=count)    
        try:
            resp=self.send(f.encode())
            respF=MantunSwitchResp()
            respF.decode(resp)
            return respF.states()
        except Exception as e:
            raise e 
