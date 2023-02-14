from src.bob import bob


def test_call_bob_by_name():
    assert bob("bob") == "okay be soo"


def test_call_bob_by_scream_question():
    assert bob("BOB?") == "relax, i know  what I`m doing"


def test_call_bob_by_question():
    assert bob("are you okay?") == "Of course"


def test_call_bob_by_without_meaning():
    assert bob("ok") == "wot hewer"


def test_call_bob_by_scream():
    assert bob("YOU") == "wow relax"
