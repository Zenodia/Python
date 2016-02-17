import sklearn

# Naive Bayes
bayes = GaussianNB().fit(train[features], y)
bayes_predict = bayes.predict(test[features])

# Logistic regression
logistic = LogisticRegression().fit(train[features], y)
logistic_predict = logistic.predict(test[features])

# Random Forest
rf = RandomForestClassifier().fit(train[features], y)
rf_predict = rf.predict(test[features])
"""
# Classification Metrics
print(metrics.classification_report(test.bot, bayes_predict))
print(metrics.classification_report(test.bot, logistic_predict))
print(metrics.classification_report(test.bot, rf_predict))

# construct parameter grid
param_grid = {'max_depth': [1, 3, 6, 9, 12, 15, None],
              'max_features': [1, 3, 6, 9, 12],
              'min_samples_split': [1, 3, 6, 9, 12, 15],
              'min_samples_leaf': [1, 3, 6, 9, 12, 15],
              'bootstrap': [True, False],
              'criterion': ['gini', 'entropy']}

# fit best classifier
grid_search = GridSearchCV(RandomForestClassifier(), param_grid = param_grid).fit(train[features], y)

# assess predictive accuracy
predict = grid_search.predict(test[features])
print(metrics.classification_report(test.bot, predict))
"""
