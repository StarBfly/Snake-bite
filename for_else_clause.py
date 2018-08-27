""" for loops have an else clause . The else clause executes after the loop completes normally.
This means that the loop did not encounter a break statement."""

#Inspired by "Horizon:zero dawn".
#Given list of already discovered machines, their weaknesses and level of danger
machines = {"Watcher" : {"weakness": "eye", "danger_level": 2}, "Strider": {"weakness": "blaze container",
                                                                                     "danger_level": 2},
                     "Grazer": {"weakness": "rotor blades", "danger_level": 2}, "Scrapper": {"weakness": "radar",
                                                                                             "danger_level": 2},
                     "Broadhead": {"weakness": "horns", "danger_level": 3} , "Lancehorn": {"weakness": "drill horns",
                                                                                           "danger_level": 3},
                     "Longleg": {"weakness": "wings", "danger_level": 3}, "Trampler": {"weakness": "processor unit",
                                                                                       "danger_level": 3},
                     "Sawtooth": {"weakness": "blaze canister", "danger_level": 5}, "Shell-Walker": {"weakness":
                                                                                                         "shield claw",
                                                                                                     "danger_level": 4}}


def check_machines(machine_name):
    """ Checks if the machine in the list of known info
    :param machine_name: encountered machine
    :return name and weakness if machine is known:"""
    for i in machines:
        if i == machine_name:
            weakness = machines[i]["weakness"]
            print(f"Machine: {i}. Weakness: {weakness}.")
            break
    else:
        print(f"New machine discovered: {machine_name}.")
        return

#Unknown machine
check_machines("Charger")

#Machine, encountered before
check_machines("Watcher")


def check_machines_level(machines_field):
    """Checks if there any dangerous machines on the field
    :param machines_field: list of machines names on the field
    :return warning if there is someone too strong"""
    for i in machines_field:
        if machines[i]["danger_level"] > 4:
            print("There is the Sawtooth among them! Too dangerous! Run away!")
            break
    else:
        print("All machines can be destroyed. Get ready for fight.")
        return

#Field of weak machines
check_machines_level(["Watcher", "Longleg", "Trampler", "Grazer"])

#Dangerous machine field
check_machines_level(["Watcher", "Longleg", "Sawtooth", "Trampler", "Grazer"])