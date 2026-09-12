from sklearn.metrics import precision_recall_fscore_support

y_true = [1,1,0,0,1,0]
y_pred = [1,0,0,0,1,1]
p, r, f1, _ = precision_recall_fscore_support(
    y_true, y_pred, average="binary", zero_division=0
)
print({"precision": p, "recall": r, "f1": f1})
