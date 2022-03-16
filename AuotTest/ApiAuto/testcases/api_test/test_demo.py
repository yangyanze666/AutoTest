import pytest_ordering,pytest



class TestA():

    @pytest.mark.run(order=1)
    def testb(self):
        print("1")

    @pytest.mark.run(order=3)
    def testa(self):
        print("2")

    @pytest.mark.run(order=2)
    def testc(self):
        print("3")