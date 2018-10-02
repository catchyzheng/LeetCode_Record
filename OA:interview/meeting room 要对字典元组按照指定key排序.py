

# Expected output:

# find_available_time(schedules)
#  => [    0,  845 ],
#     [  915,  930 ],
#     [ 1200, 1230 ],
#     [ 1500, 1515 ],
#     [ 1545, 1600 ]
# 
def Cmp(self, other):
     if self['start'] != other['start']:
         cmp(self['start'], other['start'])
     else:
         cmp(self['end'], other['end'])


def find_available_time(schedules):
    p1_meetings = [
    {"start": 1230, "end": 1300},
    {"start":  845, "end":  900},
    {"start": 1300, "end": 1500},
    ]
    p2_meetings = [
    {"start":  930, "end": 1200},
    {"start": 1600, "end": 2359},
    ]
    p3_meetings = [
    {"start":  845, "end":  915},
    {"start": 1515, "end": 1545},
    ]
    schedules = [p1_meetings, p2_meetings, p3_meetings]
    
    total = []
    for ele in schedules:
        total += ele
    for ele in total:
        print ele
    
    total = sorted(total, cmp = Cmp)
    
    init = 0
    end_all = 2359
    res = []
    for schedule in schedules:
        if len(res) == 0:
            res.append(schedule)
        else:
            x, y = schedule[0], schedule[1]
            if res[-1][1] < x:
                res.append(schedule)
            else:
                res[-1][1] = y
    ans = []
    ans.append([0, res[0][0]])
    for i in range(len(res) - 1):
        ans.append(res[i][1], res[i+1][0])
    
    #ans.append(res[-1][1], )
    for inter in ans:
        print inter[0], inter[1]
    