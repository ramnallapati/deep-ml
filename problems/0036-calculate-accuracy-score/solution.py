# Cell 1
import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    correct = (y_true == y_pred)
    return np.sum(correct)/len(y_true)