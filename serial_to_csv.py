import data_logger
import datetime
import serial

com_port = "COM44" # Change this based on COM port seen in Device Manager
arduino = serial.Serial(port=com_port, baudrate=9600)

header_list = ['Date-Time', 'Voltage_1', 'Voltage_2']
logger = data_logger.DataLogger(header_list=header_list)

print header_list

while True:
    # Waits for newline char before continuing
    voltage_readings = arduino.readline().strip()

    # Turn string into list of voltage values
    voltage_readings = voltage_readings.split(",")

    # Get current time for time stamp
    time_now = datetime.datetime.now()


    result_list = [time_now] + voltage_readings

    print result_list

    # Write result to csv
    logger.write_result(result_list=result_list)
