# Smart Recipe Ingredient Scaler & Grocery Budgeter

pr = {
    "rice": 0.08,
    "flour": 0.06,
    "sugar": 0.05,
    "salt": 0.02,
    "oil": 0.15,
    "milk": 0.06,
    "onion": 0.04,
    "tomato": 0.05,
    "potato": 0.03,
    "carrot": 0.05,
    "chicken": 0.35,
    "egg": 7,
    "butter": 0.50,
    "cheese": 0.60,
    "bread": 0.08
}
def show():
    print("\nAvailable Ingredients:")
    for x in pr:
        print(x)
def add():
    rn = input("\nEnter recipe name: ")
    os = int(input("Enter original servings: "))
    n = int(input("Enter number of ingredients: "))
    ing = []

    for i in range(n):

        print("\nIngredient", i + 1)

        nm = input("Enter ingredient: ").lower()

        while nm not in pr:
            print("Ingredient not available.")
            nm = input("Enter ingredient again: ").lower()
        q = float(input("Enter quantity: "))
        u = input("Enter unit (g/ml/unit): ").lower()
        ing.append((nm, q, u))
    return (rn, os, ing)


def scale(r):
    rn = r[0]
    os = r[1]
    ing = r[2]
    ns = int(input("\nEnter required servings: "))
    f = ns / os

    print("\nRecipe:", rn)
    print("Servings:", ns)
    print("-" * 35)
    si = []

    for x in ing:
        nm = x[0]
        q = x[1]
        u = x[2]
        nq = q * f
        print(nm, "=", round(nq, 2), u)
        si.append((nm, nq, u))
    return si


def cost(ing):
    t = 0
    for x in ing:
        nm = x[0]
        q = x[1]
        t = t + q * pr[nm]
    return t


def grocery(ing):
    gl = {}
    for x in ing:
        nm = x[0]
        q = x[1]
        u = x[2]
        if nm in gl:
            gl[nm] = (gl[nm][0] + q, u)
        else:
            gl[nm] = (q, u)
    return gl


def show_grocery(gl):
    t = 0
    print("\n")
    print("=" * 40)
    print("GROCERY SHOPPING LIST")
    print("=" * 40)
    for nm in gl:
        q = gl[nm][0]
        u = gl[nm][1]
        c = q * pr[nm]
        t = t + c
        print(
            nm.title(),
            "-",
            round(q, 2),
            u,
            "- ₹",
            round(c, 2)
        )
    print("-" * 40)
    print("Total Budget = ₹", round(t, 2))

rl = []
al = []
print("=" * 45)
print("SMART RECIPE INGREDIENT SCALER")
print("       & GROCERY BUDGETER")
print("=" * 45)

while True:
    print("\n1. Show Ingredients")
    print("2. Add Recipe")
    print("3. Scale Recipe")
    print("4. View Grocery List")
    print("5. Exit")

    ch = input("\nEnter choice: ")
    if ch == "1":
        show()

    elif ch == "2":
        r = add()
        rl.append(r)
        print("Recipe added.")

    elif ch == "3":
        if len(rl) == 0:
            print("No recipe added.")

        else:
            print("\nRecipes:")
            for i in range(len(rl)):
                print(i + 1, ".", rl[i][0])

            no = int(input("Enter recipe number: "))
            if no >= 1 and no <= len(rl):
                si = scale(rl[no - 1])
                for x in si:
                    al.append(x)
                c = cost(si)

                print("\nEstimated cost = ₹", round(c, 2))
            else:
                print("Wrong recipe number.")

    elif ch == "4":
        if len(al) == 0:
            print("Grocery list is empty.")

        else:
            gl = grocery(al)
            show_grocery(gl)

    elif ch == "5":
        print("Thank you!")
        break

    else:
        print("Wrong choice.")