import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def convert_to_ampl_format(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Remove the ID column
    df = df.drop(columns=['ID'])
    
    # Normalize the feature values
    scaler = MinMaxScaler()
    features = df.drop(columns=['Personal Loan'])
    normalized_features = scaler.fit_transform(features)
    
    # Extract and transform target variable from 0/1 to -1/1
    y = df['Personal Loan'].values
    y = np.where(y == 0, -1, 1)  # Transform labels to -1/1
    
    # Combine normalized features and target variable
    data = np.hstack((normalized_features, y.reshape(-1, 1)))
    
    # Split the data into training and testing sets (50/50 split)
    total_samples = data.shape[0]
    train_size = total_samples // 2
    indices = np.random.permutation(total_samples)
    train_indices = indices[:train_size]
    test_indices = indices[train_size:]
    
    A_train = data[train_indices, :-1]
    y_train = data[train_indices, -1]
    A_test = data[test_indices, :-1]
    y_test = data[test_indices, -1]
    
    # Write AMPL format
    n = A_train.shape[1]
    m_train = A_train.shape[0]
    
    with open(output_file, 'w') as f:
        # Write parameters
        f.write(f"param n := {n};\n")
        f.write(f"param m := {m_train};\n")
        f.write("param nu := 0.1;\n\n")  # Reduced nu value
        
        # Write y_train
        f.write("param y_train :=\n")
        for i, val in enumerate(y_train, 1):
            f.write(f"{i} {int(val)}\n")
        f.write(";\n\n")
        
        # Write A_train
        f.write("param A_train : ")
        f.write(" ".join(str(j) for j in range(1, n+1)))
        f.write(" :=\n")
        for i, row in enumerate(A_train, 1):
            f.write(f"{i} {' '.join(f'{x:.6f}' for x in row)}\n")
        f.write(";\n\n")
        
        # Write y_test
        f.write("param y_test :=\n")
        for i, val in enumerate(y_test, 1):
            f.write(f"{i} {int(val)}\n")
        f.write(";\n\n")
        
        # Write A_test
        f.write("param A_test : ")
        f.write(" ".join(str(j) for j in range(1, n+1)))
        f.write(" :=\n")
        for i, row in enumerate(A_test, 1):
            f.write(f"{i} {' '.join(f'{x:.6f}' for x in row)}\n")
        f.write(";\n")

if __name__ == "__main__":
    np.random.seed(42)  # For reproducibility
    convert_to_ampl_format("raw_data/UniversalBank.csv", "data/universalbank.dat")