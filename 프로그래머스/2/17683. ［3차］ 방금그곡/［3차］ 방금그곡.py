import math


def time_cal(s, e):
    hr_s, m_s = map(int, s.split(":"))
    hr_e, m_e = map(int, e.split(":"))

    result = (hr_e * 60 + m_e) - (hr_s * 60 + m_s)

    return result


def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for music_info in musicinfos:
        start, end, title, code = music_info.split(",")
        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        
        time = time_cal(start, end)
        code *= math.ceil(time / len(code))
        code = code[:time]

        if m not in code:
            continue

        if answer == None or answer[0] < time or (answer[0] == time and answer[1] > start):
            answer = (time, start, title)

    if answer:
        return answer[-1]

    return "(None)"

