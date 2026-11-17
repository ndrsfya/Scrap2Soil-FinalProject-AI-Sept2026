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

def chat_answer(question):
    q = question.lower()
    if any(x in q for x in ["smell", "odour", "odor", "stink"]):
        return "A bad smell may mean the pile is too wet or lacks airflow. Add dry brown materials such as leaves or shredded cardboard, then mix gently to improve airflow."
    if any(x in q for x in ["wet", "moist", "soggy"]):
        return "Add dry brown materials such as dry leaves or shredded cardboard. Mix gently and avoid adding more wet scraps until the mixture is better balanced."
    if any(x in q for x in ["dry", "dusty"]):
        return "Add a little water and mix evenly. Avoid soaking the pile. The moisture should feel similar to a wrung-out sponge."
    if any(x in q for x in ["slow", "decompos", "not breaking"]):
        return "Check moisture, airflow and material size. Chop scraps into smaller pieces, mix gently and review the green/brown balance."
    if any(x in q for x in ["pest", "rat", "fly", "insect"]):
        return "Cover fresh food scraps with brown material, avoid meat and dairy in this beginner plan, and keep the compost area tidy."
    if any(x in q for x in ["green", "brown", "ratio", "balance"]):
        return "Green materials include fruit peels and vegetable scraps. Brown materials include dry leaves and cardboard. Use both and adjust the mixture gradually."
    if any(x in q for x in ["plastic", "glass", "metal", "meat", "fish", "dairy"]):
        return "For this beginner plan, do not add plastic, glass, metal, meat, fish or dairy. Choose suitable plant-based green and dry brown materials."
    return "I can help with bad smells, excess moisture, dry compost, slow decomposition, pests and green/brown balance. Try asking about one of these topics."
