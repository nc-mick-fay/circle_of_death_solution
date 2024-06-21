def circ(num, start=1, step=1, wielder=True):

    people = range(start, num+1, step)
    even = len(people) % 2 == 0

    if len(people) == 1:
        return people[0]
    
    elif even and wielder:
        return circ(people[-1], people[0], step*2, wielder)
    elif even and not wielder:
        return circ(people[-1] + 1, people[1], step*2, wielder)
    elif not even and wielder:
        return circ(people[-1] + 1, people[0], step*2, not wielder)
    elif not even and not wielder:
        return circ(people[-1] + 1, people[1], step*2, not wielder)