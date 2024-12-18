# Parameters
param n; 				# rows
param m; 				# columns
param nu;				# tradeoff

param y_train {1..m};        	# response value
param A_train {1..m,1..n};   	# feature values

param y_test {1..m};        	# response value
param A_test {1..m,1..n};   	# feature values

# Variables
var lambda {1..m} >= 0, <= nu;


# Dual formulation
maximize dual:
	sum{i in {1..m}}lambda[i] 
	-(1/2)*sum{i in {1..m}, j in {1..m}}lambda[i]*y_train[i]*lambda[j]*y_train[j]*(sum{k in {1..n}}A_train[i,k]*A_train[j,k]);
	
subject to c1:
	sum{i in {1..m}}(lambda[i]*y_train[i]) = 0;