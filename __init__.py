from pymodbus.client.sync import ModbusSerialClient
from pymodbus.constants import Defaults
import json

Defaults.UnitId = 1

def join_msb_lsb(msb, lsb):
    return (msb << 16) | lsb

def fetch(port, baudrate, parity, stopbits, timeout):

    vals = {}

    try:
        client = ModbusSerialClient(method="rtu", port=port, baudrate=9600, parity="N", stopbits=1, timeout=1)

        result = client.read_input_registers(0X400, 53)

        vals['Pv1 input voltage'] = result.getRegister(0) / 10
        vals['Pv2 input voltage'] = result.getRegister(1) / 10
        vals['Pv1 input current'] = result.getRegister(2) / 10
        vals['Pv2 input current'] = result.getRegister(3) / 10
        vals['Grid Voltage Phase 1'] = result.getRegister(4) / 10
        vals['Grid Voltage Phase 2'] = result.getRegister(5) / 10
        vals['Grid Voltage Phase 3'] = result.getRegister(6) / 10
        vals['Grid Frequency Phase 1'] = result.getRegister(7) / 100
        vals['Grid Frequency Phase 2'] = result.getRegister(8) / 100
        vals['Grid Frequency Phase 3'] = result.getRegister(9) / 100
        vals['Output Current Phase 1'] = result.getRegister(10) / 10
        vals['Output Current Phase 2'] = result.getRegister(11) / 10
        vals['Output Current Phase 3'] = result.getRegister(12) / 10
        vals['Temperature'] = result.getRegister(13)
        vals['Inverter Power'] = result.getRegister(14)
        vals['RunMode'] = result.getRegister(15)
        vals['Output Power Phase 1'] = result.getRegister(16)
        vals['Output Power Phase 2'] = result.getRegister(17)
        vals['Output Power Phase 3'] = result.getRegister(18)
        vals['Total DC Power'] = result.getRegister(19)
        vals['PV1 DC Power'] = result.getRegister(20)
        vals['PV2 DC Power'] = result.getRegister(21)
        vals['Fault value of Phase 1 Voltage'] = result.getRegister(22) / 10
        vals['Fault value of Phase 2 Voltage'] = result.getRegister(23) / 10
        vals['Fault value of Phase 3 Voltage'] = result.getRegister(24) / 10
        vals['Fault value of Phase 1 Frequency'] = result.getRegister(25) / 100
        vals['Fault value of Phase 2 Frequency'] = result.getRegister(26) / 100
        vals['Fault value of Phase 3 Frequency'] = result.getRegister(27) / 100
        vals['Fault value of Phase 1 DCI'] = result.getRegister(28) / 1000
        vals['Fault value of Phase 2 DCI'] = result.getRegister(29) / 1000
        vals['Fault value of Phase 3 DCI'] = result.getRegister(30) / 1000
        vals['Fault value of PV1 Voltage'] = result.getRegister(31) / 10
        vals['Fault value of PV2 Voltage'] = result.getRegister(32) / 10
        vals['Fault value of Temperature'] = result.getRegister(33)
        vals['Fault value of GFCI'] = result.getRegister(34) / 1000
        vals['Total Yield'] = join_msb_lsb(result.getRegister(36), result.getRegister(35)) / 1000
        vals['Yield Today'] = join_msb_lsb(result.getRegister(38), result.getRegister(37)) / 1000

    except:

        vals['Pv1 input voltage'] = 0
        vals['Pv2 input voltage'] = 0
        vals['Pv1 input current'] = 0
        vals['Pv2 input current'] = 0
        vals['Grid Voltage Phase 1'] = 0
        vals['Grid Voltage Phase 2'] = 0
        vals['Grid Voltage Phase 3'] = 0
        vals['Grid Frequency Phase 1'] = 0
        vals['Grid Frequency Phase 2'] = 0
        vals['Grid Frequency Phase 3'] = 0
        vals['Output Current Phase 1'] = 0
        vals['Output Current Phase 2'] = 0
        vals['Output Current Phase 3'] = 0
        vals['Temperature'] = 0
        vals['Inverter Power'] = 0
        vals['RunMode'] = 0
        vals['Output Power Phase 1'] = 0
        vals['Output Power Phase 2'] = 0
        vals['Output Power Phase 3'] = 0
        vals['Total DC Power'] = 0
        vals['PV1 DC Power'] = 0
        vals['PV2 DC Power'] = 0
        vals['Fault value of Phase 1 Voltage'] = 0
        vals['Fault value of Phase 2 Voltage'] = 0
        vals['Fault value of Phase 3 Voltage'] = 0
        vals['Fault value of Phase 1 Frequency'] = 0
        vals['Fault value of Phase 2 Frequency'] = 0
        vals['Fault value of Phase 3 Frequency'] = 0
        vals['Fault value of Phase 1 DCI'] = 0
        vals['Fault value of Phase 2 DCI'] = 0
        vals['Fault value of Phase 3 DCI'] = 0
        vals['Fault value of PV1 Voltage'] = 0
        vals['Fault value of PV2 Voltage'] = 0
        vals['Fault value of Temperature'] = 0
        vals['Fault value of GFCI'] = 0
        vals['Total Yield'] = 0
        vals['Yield Today'] = 0
    
    print(json.dumps(vals))

fetch("/dev/ttyUSBBBBBB, 9600, "N", 1, 1)
