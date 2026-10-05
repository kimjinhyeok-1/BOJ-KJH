from collections import defaultdict

def to_minute(times):
    h, m = map(int, times.split(":"))
    return 60 * h + m

def solution(fees, records):
    answer = []
    in_time = {}
    total_time = defaultdict(int)

    for record in records:
        times, number, status = record.split()
        minute = to_minute(times)

        if status == "IN":
            in_time[number] = minute
        else:
            total_time[number] += minute - in_time[number]
            del in_time[number]

    for number, start in in_time.items():
        total_time[number] += to_minute("23:59") - start

    for number in sorted(total_time):
        time = total_time[number]

        if time <= fees[0]:
            answer.append(fees[1])
        else:
            remain = time - fees[0]
            extra = (remain + fees[2] - 1) // fees[2]

            answer.append(
                fees[1] + extra * fees[3]
            )

    return answer