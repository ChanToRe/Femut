from sklearn.linear_model import LinearRegression

def LinearReg(X, Y, graph=True or False):
    X = X
    Y = Y
    LM = LinearRegression()
    LM.fit(X.values.reshape(-1,1), Y)
