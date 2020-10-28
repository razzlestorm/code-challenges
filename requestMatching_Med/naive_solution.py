# if pro_distance <= max_pref_distance,
# then matching score = distance between pro and customer
# otherwise, the non-matching score = distance between pro and customer - max travel distance
#
def requestMatching(pros, distances, travelPreferences):
    matching = {}
    non_matching = {}
    # compare distances/travelPreferences and append to different dicts
    for ii in range(len(pros)):
        if distances[ii] <= travelPreferences[ii]:
            matching[pros[ii]] = distances[ii]
        elif distances[ii] > travelPreferences[ii]:
            non_matching[pros[ii]] = distances[ii] - travelPreferences[ii]
    pros = []

    for k, v in sorted(matching.items(), key=lambda item: item[1]):
        pros.append(k)
    for k, v in sorted(non_matching.items(), key=lambda item: item[1]):
        pros.append(k)
    # but wait, we need to make sure the names are in the right order:

    checked_pros = []
    matching.update(non_matching)
    for ii in range(len(pros[:5])):
        matches = []
        matches.append(pros[ii])

        for k, v in matching.items():
            if v == matching[pros[ii]] and k != pros[ii]:
                matches.append(k)
        for name in sorted(matches):
            if name not in checked_pros:
                checked_pros.append(name)
    return checked_pros



pros = ["Michael",
 "Mary",
 "Ann",
 "Nick",
 "Dan",
 "Mark"]
distances = [12, 10, 19, 15, 5, 20]
travelPreferences = [12, 8, 25, 10, 3, 10]

print(requestMatching(pros, distances, travelPreferences))
