from src.circle_of_death import CircleOfDeath, circle

def test_returns_1_if_passed_1():
    result = circle(1)
    assert result == 1


def test_returns_1_if_passed_2():
    result = circle(2)
    assert result == 1


def test_returns_3_if_passed_3():
    result = circle(3)
    assert result == 3


def test_returns_1_if_passed_4():
    result = circle(4)
    assert result == 1


def test_returns_3_if_passed_5():
    result = circle(5)
    assert result == 3


def test_returns_5_if_passed_6():
    result = circle(6)
    assert result == 5


def test_returns_7_if_passed_7():
    result = circle(7)
    assert result == 7


def test_returns_73_if_passed_100():
    result = circle(100)
    assert result == 73


def test_returns_68929_if_passed_100000():
    result = circle(100000)
    assert result == 68929


# def test_returns_68929_if_passed_100000():
#     result = circle(1000000)
#     assert result == 68929
