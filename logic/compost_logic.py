"""Compost recommendations and simple keyword-based help logic."""

from data.materials import MATERIALS

def make_recommendations(entries):
    green = sum(q for m, q in entries if MATERIALS[m][0] == "Green")
    brown = sum(q for m, q in entries if MATERIALS[m][0] == "Brown")
    unsuitable = [m for m, q in entries if q > 0 and MATERIALS[m][0] == "Unsuitable"]
    tips = []

    if unsuitable:
        tips.append("Remove unsuitable materials: " + ", ".join(unsuitable) + ".")
    if green == 0 and brown == 0:
        tips.append("Add suitable green or brown materials to create a compost plan.")
    elif brown == 0:
        tips.append("Add brown materials such as dry leaves or shredded cardboard.")
    elif green == 0:
        tips.append("Add green materials such as fruit peels or vegetable scraps.")
    elif green / brown > 2:
        tips.append("The mixture has more green material. Add brown materials gradually.")
    elif green / brown < 0.5:
        tips.append("The mixture has more brown material. Add green materials gradually.")
    else:
        tips.append("The initial green/brown balance looks reasonable. Keep checking moisture and airflow.")

    tips.append("This balance is an estimate based on the quantities entered.")
    return green, brown, unsuitable, tips
