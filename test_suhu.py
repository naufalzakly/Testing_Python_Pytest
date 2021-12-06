import pytest
from  suhu_pytest import Suhuu

class TestSuhu():

    def test_Faranheit(self):
        result_Faranheit = Suhuu.test_CelciusConvertFaranheit(30)
        assert result_Faranheit == 86

    def test_Reamur(self):
        result_Reamur = Suhuu.test_CelciusConvertReamur(30)
        assert result_Reamur == 24
    
    def test_Kelvin(self):
        result_Kelvin = Suhuu.test_CelciusConvertKelvin(30)
        assert result_Kelvin== 303.15