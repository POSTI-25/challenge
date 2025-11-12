from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc, precision_recall_curve

def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)
    y_scores = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    fpr, tpr, _ = roc_curve(y_test, y_scores)
    roc_auc = auc(fpr, tpr)
    precision, recall, _ = precision_recall_curve(y_test, y_scores)

    print(f"\nModel Accuracy: {accuracy:.2f}")
    return accuracy, conf_matrix, (fpr, tpr, roc_auc), (precision, recall)
