def solution(m, musicinfos):
    m = m.replace('C#','0')
    m = m.replace('D#','1')
    m = m.replace('F#','2')
    m = m.replace('G#','3')
    m = m.replace('A#','4')
    answer={}
    for info in musicinfos:
        start, end, name, melody = info.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        time = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        print(time)
        melody = melody.replace('C#','0')
        melody = melody.replace('D#','1')
        melody = melody.replace('F#','2')
        melody = melody.replace('G#','3')
        melody = melody.replace('A#','4')
        melody_len = len(melody)
        melody = melody*(time//melody_len) + melody[:time%melody_len]
        answer[name] = melody
    answers=[]
    for name, melody in answer.items():
        if m in melody:
            answers.append([name, len(melody)])
    answers.sort(key = lambda x : x[1], reverse=True)
    if answers:
        answer = answers[0][0]
    else:
        answer = '(None)'
    return answer