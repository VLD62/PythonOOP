bands_dict = {}
input_string = input().split("; ")
while not input_string[0] == "start of concert":
    command = input_string[0]
    band = input_string[1]
    if command == "Add":
        members = input_string[2].split(", ")
        if not band in bands_dict:
            bands_dict[band] = {"Members": members,
                                "Minutes" : 0}
        else:
            for key, value in bands_dict.items():
                if key == band:
                    for member in members:
                        if member not in value["Members"]:
                            value["Members"].append(member)
    if command == "Play":
        minutes = int(input_string[2])
        if not band in bands_dict:
            bands_dict[band] = {"Members": [],
                                "Minutes" : minutes}
        else:
            bands_dict[band]["Minutes"] += minutes
    input_string = input().split("; ")

input_band = input()
total_time = 0
for band, value in bands_dict.items():
    total_time += value["Minutes"]
print(f"Total time: {total_time}")

for band, value in sorted(bands_dict.items(), key = lambda x: (-x[1]["Minutes"],x[0])):
    print(f"{band} -> {value['Minutes']}")

for band, value in bands_dict.items():
    if band == input_band:
        print(band)
        for member in value["Members"]:
            print(f"=> {member}")
"""

Play; The Beatles; 2584
Add; The Beatles; John Lennon, Paul McCartney, George Harrison, Ringo Starr
Add; Eagles; Glenn Frey, Don Henley, Bernie Leadon, Randy Meisner
Play; Eagles; 1869
Add; The Rolling Stones; Brian Jones, Mick Jagger, Keith Richards
Add; The Rolling Stones; Brian Jones, Mick Jagger, Keith Richards, Bill Wyman, Charlie Watts, Ian Stewart
Play; The Rolling Stones; 4239
start of concert
The Rolling Stones

"""