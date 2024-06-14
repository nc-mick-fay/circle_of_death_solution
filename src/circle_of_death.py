def circle(num=None, li=None):
    if not num:
        people = li
    else:
        people = list(range(1, num+1))

    start = len(people)
    for i in range(len(people)):
        try:
            del people[i+1]
        except:
            break

    if start % 2 == 1 and len(people) > 1:
        del people[0]
    if len(people) != 1:
        return circle(li=people)
    return people[0]
