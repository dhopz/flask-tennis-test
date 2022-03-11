from tennisapp.helpers import age, points_logic
import datetime


def test_age():
    age_string = "14/01/2000"
    age_calc = age(datetime.datetime.strptime(age_string, '%d/%m/%Y'))   
    assert age_calc == 22