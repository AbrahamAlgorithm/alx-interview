#!/usr/bin/python3
"""Log Parsing"""


status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
count = 0
size = 0


def collect_status(dic: dict, size: int) -> None:
    '''print the output'''
    print("File size: {}".format(size))
    dic = dict(sorted(dic.items()))
    for k, v in dic.items():
        if v > 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    import sys

    try:
        for line in sys.stdin:
            count += 1
            lin = line.split(" ")
            try:
                code = lin[-2]
                size += int(lin[-1])
                if code in status:
                    status[code] += 1
            except BaseException:
                pass
            if count == 10:
                collect_status(status, size)
                count = 0

    except KeyboardInterrupt:
        collect_status(status, size)
    collect_status(status, size)
