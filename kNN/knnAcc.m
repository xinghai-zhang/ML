function result = knnAcc(X ,Y)

testResult = NaN(1,5000);

for n = 5001:10000
   testResult(n-5000) = kNN(X(1:5000,:), X(n,:), 3, Y);
   disp(n);
end
   diff = testResult'-Y(5001:10000);
   n = nnz(diff);
   result = n/5000;

end