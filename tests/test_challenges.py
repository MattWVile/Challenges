from programs.near import near
from programs.times_tables import times_table
from programs.grade_calculator import grade_calc

def test_near():
    assert near('dragon','dragoon') == False
    assert near('dragoon','dragon') == True
    assert near('dragoin','dragon') == True
    assert near('bigbrian','bigbrain') == False
def test_times_table():
    assert times_table(1) == [1]
    assert times_table(2) == [2 ,4]
    assert times_table(3) == [3, 6, 9]
def test_grade_calc():
    assert grade_calc(20,20,20) == 'You failed'
    assert grade_calc(200,200,200) == 'A'