def calculate_delivery_manifest(pilot_callsign, package_manifest, priority_override):
    if not isinstance(pilot_callsign, str):
        return "Pilot callsign must be a valid text string."
    if pilot_callsign == "":
        return "System requires an active pilot callsign to authenticate flight."
    if not isinstance(package_manifest, list):
        return "Package manifest must be a provided as a structured list."
    if package_manifest == "":
        return "Cannot generate route instructions for an empty cargo bay."
    
    weights = [weight for name, weight in package_manifest]
    total_weight = sum(weights)

    calc_baseline = lambda w: w * 1.12
    if priority_override == "TURBO":
        energy_required = total_weight * 1.5
    else:
        energy_required = calc_baseline(total_weight) 
    
    hazmat_count = 0
    for name, weight in package_manifest:
        if name == "HAZMAT":
            hazmat_count += 1

     
    line1 = f"PILOT LOG: {pilot_callsign.upper()}"
    line2 = f"MANIFEST SIZE: {len(package_manifest)}"
    line3 = f"HAZMAT UNITS: {int(hazmat_count)}"
    line4 = f"REQUIRED ENERGY CELLS: {energy_required:.2f}"
    line5 = " --- ROUTE LOCK ACTIVE ---"

    return f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}"

test_manifest = [
    ("HAZMAT", 4.50), 
    ("MED_KIT", 2.10), 
    ("HAZMAT", 1.40)
]

reciept_output = calculate_delivery_manifest("sky_hawk_9", test_manifest, "STANDARD")
print(reciept_output)


    








    
    



    


    