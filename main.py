import os
from src.preprocessing import load_data, preprocess_data
from src.model_train import train_model
from src.evaluation import evaluate_model
from src.visualize import plot_confusion, plot_roc, plot_pr
import pandas as pd

# Loading of the data
data_path = os.path.join("data", "raw_data.csv")
df = load_data(data_path)

# Data Preprocessing
X, y = preprocess_data(df)

# Model Training
model, X_train, X_test, y_train, y_test = train_model(X, y)

# Evaluating
accuracy, conf_matrix, roc_data, pr_data = evaluate_model(model, X_test, y_test)

# Visualizing 
plot_confusion(conf_matrix)
plot_roc(*roc_data)
plot_pr(*pr_data)

# Saving Predictions
output_df = X.copy()
output_df["Mega_Evolution_Predicted"] = model.predict(X)
output_df["Mega_Evolution_Predicted"] = output_df["Mega_Evolution_Predicted"].apply(lambda x: "Yes" if x == 1 else "No")

os.makedirs("results", exist_ok=True)
output_path = os.path.join("results", "mega_predictions.csv")
output_df.to_csv(output_path, index=False)
print(f"\nPredictions saved to {output_path}")


