"""
CTEC 121
<Grant Parkinson>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main1():
    print()
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear Fred...")
    print("Happy birthday to you!")
    print()


# remove obvious duplicatrion
""" IPO happy()
Input(s): none
Process: prints/outputs "Happy birthday to you!"
Output: prints to terminal screen
"""


def happy():
    print("Happy birthday to you!")


def main2():
    print()
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()
    print()


# generalize for any person
""" IPO happybday()
Input(s): a name
Process: prints verse line of happy birthday song
Output: prints to terminal screen
"""


def happybday(name):
    print("Happy birthday, dear ", name, "...", sep="")


def main3():
    print()
    happy()
    happy()
    happybday("yoshi")
    happy()
    print()


# combine song into a function
""" IPO singhappybday()
Input(s): a name
Process: prints happy birthday song
Output: prints to terminal screen
"""


def singhappybday(name):
    happy()
    happy()
    happybday(name)
    happy()
    print()


def main4():
    print()
    singhappybday("Fred")
    singhappybday("lucy")
    singhappybday("Bill")


main4()
