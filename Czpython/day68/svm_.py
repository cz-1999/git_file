import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,datasets

def make_meshgrid(x,y,h=.02):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid,optional

    Returns
    -------
    xx,yy ： ndarray
    """

    x_min,x_max = x.min() - 1,x.max()+1
    y_min,y_max = y.min() - 1,y.max()+1
    xx,yy = np.meshgrid(np.arange(x_min,x_max,h),
                        np.arange(y_min,y_max,h))
    return xx,yy
def plot_contours(ax,clf,xx,yy,**params):
    """plot the decision boundaries for a classifier.

    parameter
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf,optional
    """
    z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
    z = z.reshape(xx.shape)
    out = ax.contourf(xx,yy,z,**params)
    return out


#import some data to play wich
iris = datasets.load_iris()
#Take the first two features.We could avoid this by using a two-dim dataset
x = iris.data[:,:2]
y = iris.target

#we can create an instance of SVM and fit out data.We do not scale our
#data since we want to plot the support vectors
c = 1.0 #SVM regularization parameter
models = (svm.SVC(kernel='linear',C=c),
          svm.LinearSVC(C=c,max_iter=10000),
          svm.SVC(kernel='rbf',gamma=0.7,C=c),
          svm.SVC(kernel='poly',degree=3,gamma='auto',C=c))
models = (clf.fit(x,y)for clf in models)

#title for the lots
titles =('SVC with linear kernel','LinearSVC (linear kernel)','SVC with RBF kernel',
         'SVC with polynomial(degree 3)kernel')

#Set-up 2*2 grid for plotting.
fig,sub = plt.subplots(2,2)
plt.subplots_adjust(wspace=0.4,hspace=0.4)

x0,x1 = x[:,0],x[:,1]
xx,yy = make_meshgrid(x0,x1)

for clf,title,ax in zip(models,titles,sub.flatten()):
    plot_contours(ax,clf,xx,yy,cmap=plt.cm.coolwarm,alpha=0.8)
    ax.scatter(x0,x1,c=y,cmap=plt.cm.coolwarm,s=20,edgecolors='k')
    ax.set_xlim(xx.min(),xx.max())
    ax.set_ylim(yy.min(),yy.max())
    ax.set_xlabel('Sepal length')
    ax.set_ylabel('Sepal width')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)

plt.show()