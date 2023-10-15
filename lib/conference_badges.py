# def badge_maker(name):
#     return None

def badge_maker(name):
    return f"Hello, my name is {name}."


# def batch_badge_creator(names):
#     return None

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]


# def assign_rooms(names):
#     return None

def assign_rooms(speakers):
    return [f"Hello, {name}! You'll be assigned to room {room}!" for room, name in enumerate(speakers, start=1)]


# def printer(names):
#     return None

def printer(speakers):
    badges = batch_badge_creator(speakers)
    assignments = assign_rooms(speakers)

    for badge in badges:
        print(badge)

    for assignment in assignments:
        print(assignment)
