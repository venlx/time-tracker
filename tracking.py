from datetime import datetime
from win10toast import ToastNotifier
import csv

# file location can be adjusted
location = r"time.csv"

# get current time
current_time = datetime.now().strftime("%H:%M:%S")

# get the tracked time slots
with open(location, "r", newline='') as csv_file:
    time_table = [row for row in csv.reader(csv_file, delimiter=";")]

if len(time_table) == 0:
    time_table = [["Start", "End", "Diff"]]

if len(time_table[-1]) == 3:
    time_table.append([current_time])
elif len(time_table[-1]) == 1:
    time_table[-1].append(current_time)
    t1 = datetime.strptime(time_table[-1][1], "%H:%M:%S")
    t2 = datetime.strptime(time_table[-1][0], "%H:%M:%S")
    delta = t1 - t2
    time_table[-1].append(str(delta.total_seconds() / (60 * 60)))
with open(location, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        for row in time_table:
            csv_writer.writerow(row)
print(time_table)

toast = ToastNotifier()

toast.show_toast(
    "Saved Timestamp",
    current_time,
    duration=3,
    threaded=True,
)