# serial_to_csv
This is a simple set of code to log serial data (e.g. from an arduino) and store to .csv in a default location.

For use with Python 2.7 and Windows.

Example:
```import data_logger
import datetime

logger = data_logger.DataLogger(header_list=['Date-Time', 'Voltage', 'Current'], 'C:\\ThisDirectory\\')
time_now = datetime.datetime.now()
logger.write_result(result_list=[time_now, 5.0, 1.25])
```
On initialization, creates a new file in either a default location or path specified, using the current timestamp as a filename. Then proceeds to save a new row of data for each call to "write_result", taking a list as input.
