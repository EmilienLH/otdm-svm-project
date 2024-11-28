def combine_results(output_file):
    files_and_headers = [
        ("out/primal_results.txt", "Primal results:"),
        ("out/computed_w.txt", "Computed w:"),
        ("out/computed_gamma.txt", "Computed gamma:"),
        ("out/dual_results.txt", "Dual results:"),
        ("out/predictions.txt", "Predictions:"),
        ("out/misclassifications.txt", "Misclassifications:"),
        ("out/accuracy.txt", "Accuracy:")
    ]
    
    with open(output_file, 'w') as outfile:
        for file, header in files_and_headers:
            outfile.write(header + "\n")
            try:
                with open(file, 'r') as infile:
                    outfile.write(infile.read() + "\n")
            except FileNotFoundError:
                outfile.write("File not found: " + file + "\n")
            outfile.write("\n")

if __name__ == "__main__":
    dataset_number = input("Enter the dataset number: ")
    combine_results(f"out/combined_results{dataset_number}.txt")