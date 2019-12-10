import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error

print("Loading data...")

#load or create your dataset
df_train = pd.read_csv('data/regression.train',header=None,sep='\t')
df_test = pd.read_csv('data/regression.test',header=None,sep='\t')

y_train = df_train[0]
y_test = df_test[0]
x_train = df_train.drop(0,axis=1)
x_test = df_test.drop(0,axis=1)

#create dataset for lightgbm
lgb_train = lgb.Dataset(x_train,x_test)
lgb_eval = lgb.Dataset(x_test,y_test,reference=lgb_train)

#specify your configurations as a dict
params = {
    'boosting_type':'gbdt',
    'objective':'regression',
    'metric':{'12','l1'},
    'num_leaves':31,
    'learning_rate':0.05,
    'feature_fraction':0.9,
    'bagging_fraction':0.8,
    'bagging_freq':5,
    'verbose':0
}
print("Starting training...")
#train
gbm = lgb.train(params,lgb_train,num_boost_round=20,valid_sets=lgb_eval,early_stopping_rounds=5)

print('Saving model...')
#save model to file
gbm.save_model('model.txt')

print('Saving model...')
#save model to file
gbm.save_model('model.txt')

print('Starting predicting...')
#predict
y_pred = gbm.predict(x_test,num_iteration=gbm.best_iteration)
#eval
print('The rmse of prediction is:',mean_squared_error(y_test,y_pred)**0.5)
