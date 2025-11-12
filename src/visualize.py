import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion(conf_matrix):
    plt.figure(num=1 , figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Purples",
                xticklabels=["Normal", "Mega"], yticklabels=["Normal", "Mega"])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

def plot_roc(fpr, tpr, roc_auc):
    plt.figure(num=2 , figsize=(6, 4))
    plt.plot(fpr, tpr, color='purple', label=f'ROC Curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()
    plt.show()

def plot_pr(precision, recall):
    plt.figure(num=3 , figsize=(6, 4))
    plt.plot(recall, precision, color='purple', label='Precision-Recall Curve')
    plt.title("Precision-Recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.legend()
    plt.show()
