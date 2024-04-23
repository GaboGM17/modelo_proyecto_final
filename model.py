import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
from sklearn.model_selection import cross_val_score

# Carga de datos
df = pd.read_csv('housing_df.csv')
y = df['MEDV']
X = df.drop(['MEDV'], axis=1)

# División de los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definición de modelos y pipelines
pipelines = {
    'poly_reg': Pipeline([
        ('scaler', StandardScaler()),
        ('poly_features', PolynomialFeatures(degree=2)),
        ('lin_reg', LinearRegression())
    ]),
    'tree_reg': Pipeline([
        ('scaler', StandardScaler()),
        ('decision_tree', DecisionTreeRegressor(random_state=42))
    ]),
    'forest_reg': Pipeline([
        ('scaler', StandardScaler()),
        ('forest', RandomForestRegressor(random_state=42))
    ])
}

# Parámetros para GridSearchCV
parameters = {
    'poly_reg': {
        'poly_features__degree': [2, 3],
        'lin_reg__fit_intercept': [True, False]
    },
    'tree_reg': {
        'decision_tree__max_depth': [None, 10, 20],
        'decision_tree__min_samples_leaf': [1, 2, 4]
    },
    'forest_reg': {
        'forest__n_estimators': [50, 100, 200],
        'forest__max_depth': [None, 10, 20],
        'forest__min_samples_leaf': [1, 2, 4]
    }
}

# Ejecución de GridSearchCV con validación cruzada anidada para cada modelo
for name, pipeline in pipelines.items():
    grid_search = GridSearchCV(pipeline, parameters[name], cv=5, n_jobs=-1, verbose=1)
    scores = cross_val_score(grid_search, X_train, y_train, cv=5)
    print(f"Mean cross-validated score of the best_estimator for {name}: {scores.mean():.4f}")

# Entrenamiento y evaluación del modelo seleccionado
best_model = grid_search.fit(X_train, y_train)
y_predictions = best_model.predict(X_test)
mae = mean_absolute_error(y_test, y_predictions)
r2 = r2_score(y_test, y_predictions)

print(f"Mean Absolute Error: {mae}")
print(f"R-squared: {r2}")

# Guardar el mejor modelo
filename = 'ensemble_regression_model.pkl'
joblib.dump(best_model, filename)
#%%
