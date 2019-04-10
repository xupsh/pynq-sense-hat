class I2CDevice:
  
    def __init__(self, i2c, device_address, *, debug=False):
        self.i2c = i2c
        self.device_address = device_address
        self._debug = debug

    def readinto(self, buf, **kwargs):
        self.i2c.read(self.device_address, buf, kwargs["end"])
        if self._debug:
            print("i2c_device.readinto:", [hex(i) for i in buf])

    def write(self, buf, **kwargs):
        self.i2c.write(self.device_address, buf, kwargs["end"])
        if self._debug:
            print("i2c_device.write:", [hex(i) for i in buf])
            
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False
