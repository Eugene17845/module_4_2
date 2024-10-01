def test_fukction():
    def inner_function():
        print('Я в области видимости фукции test_function')
    inner_function()

test_fukction()
#inner_function()
# Если этот вызов заключался в том,
# что я должен видеть ошибку, то тогда всё ок