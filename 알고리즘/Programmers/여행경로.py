from collections import deque
import copy
def solution(tickets):
    final = len(tickets)
    answer = []
    ticket_list = {}
    for ticket in tickets:
        if ticket[0] not in ticket_list:
            ticket_list[ticket[0]] = [ticket[1]]
        else:
            ticket_list[ticket[0]].append(ticket[1])
        if ticket[1] not in ticket_list:
            ticket_list[ticket[1]] = []
    for ticket in ticket_list:
        ticket_list[ticket].sort()
    que = deque([])
    que.append([["ICN"], ticket_list])
    while que:
        line, tickets = que.popleft()
        # print("="*5, line, tickets)
        if len(line) == final + 1:
            return line
        start = line[-1]
        # print(tickets[start])
        for dest in tickets[start]:
            tmp_tickets = copy.deepcopy(tickets)
            tmp_tickets[start].remove(dest)
            # print(line+[dest], tmp_tickets)
            que.append([line+[dest], tmp_tickets])
            
    return answer
