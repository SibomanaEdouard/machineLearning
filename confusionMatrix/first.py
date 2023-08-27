import numpy as np
import matplotlib.pyplot as plt
actual=np.random.binomial(1,0.9,size=100)
predictions=np.random.binomial(1,0.9,size=100)
from sklearn import metrics

confusion_matrix = metrics.confusion_matrix(actual, predictions)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])


# print(actual)
# print("..........................................")
# print(predictions)

cm_display.plot()
plt.show()
