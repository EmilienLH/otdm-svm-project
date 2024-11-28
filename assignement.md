
# Assignment (part I)

1. Implement in AMPL the SVM problem (primal formulation).

2. The provided program "gensvmdat" randomly generates points `x ∈ ℝ⁴`: if `Σ⁴ᵢ₌₁ xᵢ ≥ 2` the point belongs to class +1; otherwise, to class −1.

3. To run the code:

   ```
   gensvmdat file p seed
   ```
   where `file` is the file name where data will be written, `p` is the number of points, and `seed` is a number for the random generator.

4. E.g., "gensvmdat file.dat 100 12345", file "file.dat" contains 100 points:

   ```
   0.553 0.152 0.466 0.136 -1.0
   0.258 0.487 0.655 0.408  1.0
   0.771 0.799 0.610 0.262 -1.0*
   ...
   ```

5. Points marked with "*", randomly distributed, belong to an incorrect class.

6. For a good mark in the assignment: use other datasets too.

# Assignment (part II)

1. Implement in AMPL the SVM problem (dual formulation).

2. Use the "gensvmdat" data generator (as with the primal formulation)

3. Check the primal and dual formulation provide the same separation hyperplane.

4. Highly recommended for a good mark: use also some additional dataset.
