print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,plot_tree

#Parameters
n_classes = 3
plot_colors = 'ryb'
plot_step = 0.02

#Load data
iris = load_iris()

for pairidx,pair in enumerate([[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]):
    #We only take the two corresponding features  选取两个属性，每个节点分成两个叉
    x = iris.data[:,pair] #样例
    y = iris.target  #类别

    #Train
    clf = DecisionTreeClassifier().fit(x,y)

    #plot the decision boundary #绘制决策树
    plt.subplot(2,3,pairidx + 1)

    x_min,x_max = x[:,0].min()-1,x[:,0].max()+1
    y_min,y_max = x[:,1].min()-1,x[:,1].max()+1
    xx,yy = np.meshgrid(np.arange(x_min,x_max,plot_step),
                        np.arange(y_min,y_max,plot_step))
    plt.tight_layout(h_pad=0.5,w_pad=0.5,pad=2.5)

    z = clf.predict(np.c_[xx.ravel(),yy.ravel()])
    z = z.reshape(xx.shape)
    cs = plt.contourf(xx,yy,z,cmap=plt.cm.RdYlBu)

    plt.xlabel(iris.feature_names[pair[0]])
    plt.ylabel(iris.feature_names[pair[1]])

    #Plot the trainning points
    for i,color in zip(range(n_classes),plot_colors):
        idx = np.where(y==i)
        plt.scatter(x[idx,0],x[idx,1],c=color,label=iris.target_names[i],
                    cmap=plt.cm.RdYlBu,edgecolor='black',s=15)

plt.suptitle("Decision surface of a decision tree using paired features")
plt.legend(loc='lower right')
plt.axis("tight")

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data,iris.target)
plot_tree(clf,filled=True)
plt.savefig('D:/python/czpython/save_decision_tree.png')#只能保存一张图片
plt.show()