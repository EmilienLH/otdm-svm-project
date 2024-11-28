import numpy as np

def convert_to_ampl_format(input_file, output_file):
    # Read raw data
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Count dimensions
    total_samples = len(lines)
    n = len(lines[0].strip().split()) - 1  # number of features
    
    # Calculate split sizes
    train_size = total_samples // 2
    # test_size = total_samples - train_size
    
    # Parse data
    A = []  # features
    y = []  # labels
    for line in lines:
        values = line.strip().split()
        A.append([float(x) for x in values[:-1]])
        y_value = values[-1].rstrip('*')
        y.append(float(y_value))
    
    # Random split indices
    indices = np.random.permutation(total_samples)
    train_indices = indices[:train_size]
    test_indices = indices[train_size:]
    
    # Split data
    A_train = [A[i] for i in train_indices]
    y_train = [y[i] for i in train_indices]
    A_test = [A[i] for i in test_indices]
    y_test = [y[i] for i in test_indices]
    
    # Write AMPL format
    with open(output_file, 'w') as f:
        # Write parameters
        f.write(f"param n := {n};\n")
        f.write(f"param m := {train_size};\n")
        f.write("param nu := 1.0;\n\n")
        
        # Write y_train
        f.write("param y_train :=\n")
        for i, val in enumerate(y_train, 1):
            f.write(f"{i} {val}\n")
        f.write(";\n\n")
        
        # Write A_train
        f.write("param A_train : ")
        f.write(" ".join(str(j) for j in range(1, n+1)))
        f.write(" :=\n")
        for i, row in enumerate(A_train, 1):
            f.write(f"{i} {' '.join(str(x) for x in row)}\n")
        f.write(";\n\n")
        
        # Write y_test
        f.write("param y_test :=\n")
        for i, val in enumerate(y_test, 1):
            f.write(f"{i} {val}\n")
        f.write(";\n\n")
        
        # Write A_test
        f.write("param A_test : ")
        f.write(" ".join(str(j) for j in range(1, n+1)))
        f.write(" :=\n")
        for i, row in enumerate(A_test, 1):
            f.write(f"{i} {' '.join(str(x) for x in row)}\n")
        f.write(";\n")

if __name__ == "__main__":
    np.random.seed(42)  # For reproducibility
    dataset_number = input("Enter the dataset number: ")
    print(f"Getting file raw_data/dataset{dataset_number}-raw.dat")
    input_file = f"raw_data/dataset{dataset_number}-raw.dat"
    print(f"Writing to file data/dataset{dataset_number}.dat")
    output_file = f"data/dataset{dataset_number}.dat"
    convert_to_ampl_format(input_file, output_file)