# sharing code between main.ipynb and test_main.ipynb
def median(data):
    return data["Grade"].median()
def mean(data):
    return data["Grade"].mean()
def std(data):
    return data["Grade"].std()