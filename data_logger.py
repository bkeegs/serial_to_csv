import datetime, time, os

class DataLogger():

    def __init__(self, header_list, path=None):
        '''
        Desc:
        On initialization, creates a new file in either a default location or path specified,
        using the current timestamp as a filename.
        Then proceeds to save a new row of data for each call to "write_result", taking a list as input.

        Example:
        import data_logger
        logger = data_logger.DataLogger(header_list=['Voltage', 'Current'], 'C:\\ThisDirectory\\')
        logger.write_result(data=[5.0, 1.25])
        '''

        # Get initial time stamp for .csv filename
        time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
        # Create csv filename from time_stamp
        filename_str = time_stamp + '.csv'

        # If path provided is valid, continue, otherwise make new folder in default location
        try:
            valid_path_detected = os.path.isdir(path)
        except Exception as e:
            print e
            valid_path_detected = False

        if valid_path_detected:
            pass
        else:
            print "Path provided was None or invalid, will use default path for CSV logging."
            path = 'C:\\' + 'test_data_' + time_stamp + '\\'
            print "\nStoring data to {}\n".format(path)
            os.makedirs(path)

        # Open a file object to write header row
        output_file = open(path + filename_str, "w")

        header_str = ""
        for k in header_list:
            header_str += str(k) + ","
        output_file.write(header_str[:-1] + "\n")

        self.log_file_name = path + filename_str

    def write_result(self, result_list):
        result_str = ""

        # Convert string of entries to comma delimited string
        for result in result_list:
            result = str(result)

            # Get rid of \n or \r in the result list entry
            result = result.replace('\r', '')
            result = result.replace('\n', '')
            result_str += result + ","

        # Remove final comma, add \n to mark end of row
        result_str = result_str[:-1] + "\n"

        # Open the output file to append the result_str on a new row
        log_file = open(self.log_file_name, "a")
        log_file.write(result_str)

        # Close file object
        log_file.close()

if __name__ == "__main__":
    import data_logger
    import datetime
    import time

    logger = data_logger.DataLogger(header_list=['Date-Time', 'Voltage', 'Current'])
    time_now = datetime.datetime.now()

    voltage_read = 5.0
    current_read = 1.25
    while True:
        logger.write_result(result_list=[time_now, voltage_read, current_read])
        time.sleep(1)