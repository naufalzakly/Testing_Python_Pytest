    
class Suhuu:
    
    # fungsi untuk Suhu ke Faranheit
    def test_CelciusConvertFaranheit(C):
        F = (C * (9/5)) + 32 #rumus faranhite
        return F
    faranheit = test_CelciusConvertFaranheit(30)
    print(faranheit)
    # fungsi untuk Suhu ke Kelvin
    def test_CelciusConvertKelvin(C):
        K = C + 273.15 #rumus kelvin
        return K
        
    kelvin = test_CelciusConvertKelvin(30)
    print(kelvin)

    # fungsi untuk Suhu ke Reamur
    def test_CelciusConvertReamur(C):
        Re = C * (4/5) #rumus reamur
        return Re
    reamur = test_CelciusConvertReamur(30)
    print(reamur)    