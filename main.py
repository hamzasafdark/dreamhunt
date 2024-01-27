print('Welcome to DreamTrek')

sword_damage = 10
player_health = 100
health_after_attack = player_health - sword_damage

print(f"Lollilfred's health is: {player_health}")
print(f"Lollilfred's is hit by a sword for {sword_damage} damege...")
print(f"Lollilfred's health is now : {health_after_attack}")

print("Use the arrow keys to move")

print("Jax: B-Kaw!")
print("Hero: ...")
print("Jax: Where are you off to this morning? Bkaw...")
print("Hero: Where did an owl learn to speak??")

name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")


player_health = 100

player_has_magic = True

# don't touch below this line
print(f"player_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")


def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
axe_length = 0.5
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
axe_area = area_of_circle(axe_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Axe length:", axe_length, "meters.")
print("Axe attack area:", axe_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")


def calculate_damage(opening_attack, core_damage, finishing_move):
    return opening_attack + core_damage + finishing_move


# Don't touch below this line

dmg_one = 2
dmg_two = 4
dmg_three = 3
print("Getting damage for", dmg_one, dmg_two, "and", dmg_three, "...")
print(calculate_damage(dmg_one, dmg_two, dmg_three), "points of damage dealt!")
print("=====================================")

dmg_four = -1
dmg_five = 10
dmg_six = 5
print("Getting damage for", dmg_four, dmg_five, "and", dmg_six, "...")
print(calculate_damage(dmg_four, dmg_five, dmg_six), "points of damage dealt!")
print("=====================================")


def to_celsius(f):
    return 5/9 * (f-32)


## Don't touch below this line


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)



def hours_to_seconds(hours):
    return hours * 3600


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)


def become_warrior(first_name, last_name, power):
    title = first_name + " " + last_name + " the warrior"
    power_plus_one = power + 1
    return title, power_plus_one 


# Don't edit below this line


def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)


def test(first_name, last_name, power_level):
    title_string, power = become_warrior(first_name, last_name, power_level)
    print(title_string, "has a power level of:", power)


main()


def get_punched(health, armor=0):
    damage = 50 - armor
    return health - damage 

def get_slashed(health, armor=0):
    damage = 100 - armor
    return health - damage 
    


# Don't touch below this line


def test(health, armor):
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("=====================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}\n")
    print("=====================================")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("=====================================")


test(400, 5)
test(300, 3)
test(200, 1)


def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")


