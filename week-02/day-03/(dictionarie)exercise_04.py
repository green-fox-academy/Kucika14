watchlist = []

# security_alcohol_loot = 0

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

def festivalgoers(queue):
    security_alcohol = 0
    gun_check(queue)
    for member in queue:
        security_alcohol += alcohol_check(member)

    print(security_alcohol)
def alcohol_check(member):
    temp_alcohol = member['alcohol']
    if member['alcohol'] > 0:
        member['alcohol'] = 0
    return temp_alcohol
#         # if alcohol['alcohol'] == alcohol['alcohol']:

def gun_check(member):
    for gun in member:
        if gun['guns'] > 0:
            watchlist.append(gun['name'])
            gun['guns'] = 0
    return watchlist

print(festivalgoers(queue))
print(watchlist)
# print(security_alchol_loot)