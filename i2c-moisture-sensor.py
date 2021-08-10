import time
import smbus

i2c_ch = 0   #channel we're running on with i2c
#address on the I2C bus of the ADC
i2c_address = 0x48

bus = smbus.SMBus(i2c_ch)

# Print out temperature every second
while True:
    temperature = bus.read_i2c_block_data(i2c_address, 0)
    print(temperature)
    time.sleep(1)