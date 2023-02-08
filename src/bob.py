def bob(question: str):
    """

    :param question:
    :return:
    """
    if question.lower() == "bob":
        return "okay be soo"
    elif question.endswith("?") and question.isupper():
        return "relax, i know  what I`m doing"
    elif question.endswith("?"):
        return "Of course"
    elif question.issuper():
        return "wow relax"
    else:
        return "wot hewer"


if __name__ == '__main__':
    print(bob("BOB?"))
