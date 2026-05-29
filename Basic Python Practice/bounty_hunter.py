def generate_bounty_ledger(target_name, faction, danger_level, base_reward):
    if not isinstance(target_name, str) or not target_name:
        return "Target name must be a valid text string."
    if ' ' in target_name:
        return "Target alias cannot contain spaces for secure indexing."

    if not isinstance(faction, str) or not faction:
        return "Faction assignment must be a valid text string."

    if ' ' in faction:
        return "Target must be linked to a known faction or network."

    if not isinstance(danger_level, int):
        return "Danger metric must be an integer value."

    if danger_level < 1 or danger_level > 100:
        return "Danger rating out of bounds. System scale is 1 to 100."

    if not isinstance(base_reward, (int, float)):
        return "Base reward must be a numerical value."

    if base_reward <= 0:
        return "Bounty contract cannot be zero or negative."

    if danger_level < 40:
        level_class = "LOW RISK"
        total_bounty = base_reward
    elif danger_level > 80:
        level_class = "CRITICAL (OMEGA RISK)"
        total_bounty = base_reward * 1.50
    else:
        level_class = "MODERATE RISK"
        total_bounty = base_reward * 1.15

    line_1 = target_name.upper()
    line_2 = f"FACTION: {faction.title()}"
    line_3 = f"RISK CLASS: {level_class}"
    line_4 = f"PAYOUT: {total_bounty:.2f}"
    line_5 = "[TRANSMISSION END]"

    return (
        f"{line_1}\n"
        f"{line_2}\n"
        f"{line_3}\n"
        f"{line_4}\n"
        f"{line_5}"
    )
print(generate_bounty_ledger('neon_ghost', 'SyntheticSyndicates', 85, 4000))
