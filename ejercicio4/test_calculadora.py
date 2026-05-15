from ejercicio3.calc import *
import pytest
@pytest.fixture
def numEnteros():
    return 18, 9

@pytest.fixture
def numFlotantes():
    return 0.1, 0.2

def testSuma():
    assert Sumar(5,5) == 10, "Resultado no esperado"

def testSuma1():
    assert Sumar("a",4) == 2, "Valor no esperado"

def testResta():
    assert Restar(8,9) == -1, "Resultado no esperado"

def testResta1():    
    assert Restar(10,5) == 9, "Resultado no esperado"
@pytest.mark.exception
def testDividir():
    assert Dividir(10, 0) == 0, "Resultado no esperado"

def testDividir1():
    assert Dividir(10, 2) == 5, "Resultado no esperado"

def testMultiplicar():
    assert Multiplicar(10,3) == 30, "Resultado no esperado"

def testMultiplicar1():
    assert Multiplicar(19,5) == 154, "Resultado no esperado"

def testSuma2(numEnteros):
    x, y = numEnteros
    assert Sumar(x, y) == 27, "Resultado no esperado"

def testResta2(numEnteros):
    x, y = numEnteros
    assert Sumar(x, y) == 27, "Resultado no esperado"

def testDividir2(numFlotantes):
    x, y = numFlotantes
    assert Dividir(x,y) == 2, "Resultado no esperado"

def testSuma3(x, y, resultado):
    assert Sumar(x , y) == resultado, "Resultado no esperado"

@pytest.mark.parametrize("x,y,resultado",[
    (2,8,10),
    (6,3,2),
    (2.5,5.3,9.0)
])

@pytest.mark.smoke
def testSuma3(x, y, resultado):
    assert Sumar(x , y) == resultado, "Resultado no esperado"

@pytest.mark.parametrize("x,y,resultado",[
    (20,10,10),
    (6,3,3),
    (2.5,2.5,10)
])
def testResta3(x,y, resultado):
    assert Restar(x, y) == resultado, "Resultado no esperado"
