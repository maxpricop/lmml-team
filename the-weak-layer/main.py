from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

test_mode = Path("test-input.csv").is_file()
input_file = "test-input.csv" if test_mode else "data/train-input.csv"
output_file = "test-output.txt" if test_mode else "data/train-output.txt"

input = pd.read_csv(input_file)
X = input.drop(columns="slab_released")
y = input["slab_released"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)

tree = model.tree_
pending_nodes = [0]
word = ""

# Depth-First-Search algorithm
while pending_nodes:
    node = pending_nodes.pop()
    left = tree.children_left[node]
    right = tree.children_right[node]

    if left == -1: continue

    word += X.columns[tree.feature[node]][0]
    pending_nodes.append(right)
    pending_nodes.append(left)

Path(output_file).write_text(f"SIGMOID_{word.upper()}")
