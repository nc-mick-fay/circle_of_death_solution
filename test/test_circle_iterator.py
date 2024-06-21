from src.circle_iterator import CircleIterator
from datetime import datetime
start_time = datetime.now()

def test_circle_class_contains_init_method():
    test_circle = CircleIterator(3)
    assert '__init__' in dir(test_circle)

def test_instantiated_with_people_attribute():
    test_circle = CircleIterator(3)
    assert test_circle.people == range(1, 4, 1)
    assert list(test_circle.people) == [1, 2, 3]

def test_instantiated_with_even_property_representing_if_even_length():
    test_circle = CircleIterator(3)
    assert test_circle.even == False
    test_circle_2 = CircleIterator(4)
    assert test_circle_2.even == True

def test_execute_halves_people_range_when_first_executed_and_even():
    test_circle = CircleIterator(4)
    test_circle.execute()
    assert list(test_circle.people) == [1, 3]
    test_circle_2 = CircleIterator(8)
    test_circle_2.execute()
    assert list(test_circle_2.people) == [1, 3, 5, 7]
    test_circle_2.execute()
    assert list(test_circle_2.people) == [1, 5]

def test_if_even_property_false_execute_flips_even_property():
    test_circle = CircleIterator(7)
    assert test_circle.even == False
    test_circle.execute()
    assert test_circle.even == True


def test_if_even_property_true_execute_maintains_property():
    test_circle = CircleIterator(12)
    assert test_circle.even == True
    test_circle.execute()
    assert test_circle.even == True

def test_execute_removes_people_range_when_first_executed_and_odd():
    test_circle = CircleIterator(5)
    test_circle.execute()
    assert list(test_circle.people) == [1, 3, 5]


def test_removes_first_item_if_odd_on_subsequent_execution():
    test_circle = CircleIterator(11)
    test_circle.execute()
    assert list(test_circle.people) == [1, 3, 5, 7, 9, 11]
    test_circle.execute()
    assert list(test_circle.people) == [3, 7, 11]
    assert test_circle.execute() == 7
    assert list(test_circle.people) == [7]

def test_execute_returns_winner_if_len_of_result_1():
    test_circle = CircleIterator(2)  
    assert test_circle.execute() == 1

def test_execute_returns_winner_after_appropriate_time():
    test_circle = CircleIterator(11)
    test_circle.execute()
    test_circle.execute()
    assert test_circle.execute() == 7
    assert list(test_circle.people) == [7]

def test_return_winner_returns_result():
    test_circle = CircleIterator(11)
    assert test_circle.return_winner() == 7
    hundred_circle = CircleIterator(100)
    assert hundred_circle.return_winner() == 73
    thousand_circle = CircleIterator(100000)
    assert thousand_circle.return_winner() == 68929
    big_ol_circle = CircleIterator(1000000000)
    assert big_ol_circle.return_winner() == 926258177
    hayooooooj_circle = CircleIterator(1000000000000000000)
    assert hayooooooj_circle.return_winner() == 847078495393153025
    end_time = datetime.now()
    print(end_time - start_time)

