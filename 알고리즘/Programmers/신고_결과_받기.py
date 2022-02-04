def solution(id_list, report, k):
    answer = []
    report_dictionary={id : set([]) for id in id_list}
    for rep in report:
        user, bad=rep.split()
        report_dictionary[user]=report_dictionary[user].union([bad])
    result_dictionary={id : 0 for id in id_list}
    for bads in report_dictionary.values():
        for bad in bads:
            result_dictionary[bad]+=1
    for id in id_list:
        count=0
        for bad in report_dictionary[id]:
            if result_dictionary[bad]>=k:
                count+=1
        answer.append(count)
    return answer