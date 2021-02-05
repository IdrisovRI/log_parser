# Read logs from date which was set
from datetime import datetime

FILENAME = "test_data.log"
print(len(
    '2017-01-01 13:38;{"data": "JQ3SI4ATZ1M2GTM9PK9TTQJLXGBT9JH262QEG7WB86ZI9UQTFGS5D12DP5DKI91SFWE8KAC33620YUIMUSE76NOY7N6S9OAJREGE"}'))
ROWLEN = 130


def get_date_from_str(date_str: str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M')


print(get_date_from_str("2017-01-04 20:05").day)


def get_file_length():
    with open(FILENAME, "r") as f:
        return f.seek(0, 2)


print(f"file len={get_file_length()}")


def get_string_by_row_num(row_num: int):
    row = ""
    with open(FILENAME, "r") as f:
        f.seek(row_num * (ROWLEN))
        row = f.read(ROWLEN + 2)
    return row


print(get_string_by_row_num(5))


def get_data_from_file(date1: datetime):
    file_len = int(get_file_length() / ROWLEN)

    row_num = int(file_len / 2)
    step = int(file_len / 2)

    while (step > 1):
        row = get_string_by_row_num(row_num)
        row_date = get_date_from_str(row[0:16])
        step = int((step + 1) / 2)

        print(f"row_num={row_num} step={step}")
        if row_date >= date1:
            print(f"1. rowdate={row_date} > date1={date1}")
            row_num = int(row_num - step)
        else:
            print(f"2. rowdate={row_date} < date1={date1}")
            row_num = int(row_num + step)
        print(" ")

    result = list()
    with open(FILENAME, "r") as f:
        for i in range(file_len - row_num):
            f.seek((row_num + i) * (ROWLEN))
            row = f.read(ROWLEN + 2)
            # print(f"add row={row}")
            result.append(row)

    print(f"total_len={get_file_length()}")
    print(f"result_len={len(result)}")
    print(f"first_element={result[0]}")
    print(f"last_element={result[len(result) - 1]}")


print("")
print("Start main")
get_data_from_file(get_date_from_str("2017-01-15 00:00"))
