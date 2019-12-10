import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier

#Load data from https://www.openml.org/d/554
x,y = fetch_openml('mnist_784',version=1,return_X_y=True)
x= x/255

#rescale the data, use the traditional train/test split
x_train,x_test = x[:60000],x[60000:]
y_train,y_test = y[:60000],y[60000:]

#mlp = MLPClassifier(hidden_layer_sizes=(100,100),max_iter=400,alpha=1e-4,
#                   solver='sgd',verbose=10,tol=1e-4,random_state=1)
mlp = MLPClassifier(hidden_layer_sizes=(100,100),max_iter=10,alpha=1e-4,
                  solver='sgd',verbose=10,tol=1e-4,random_state=1,learning_rate_init=.1)
mlp.fit(x_train,y_train)
print("Training set score: %f" % mlp.score(x_train,y_train))
print("Test set score: %f" %mlp.score(x_test,y_test))

fig,axes = plt.subplots(4,4)
#use global min/max to ensure all weights are shown on the same scale
vmin,vmax = mlp.coefs_[0].min(),mlp.coefs_[0].max()
for coef,ax in zip(mlp.coefs_[0].T,axes.ravel()):
    ax.matshow(coef.reshape(28,28),cmap=plt.cm.gray,vmin=.5*vmin,
    vmax=.5*vmax)
    ax.set_xticks(())
    ax.set_yticks(())
plt.show()
