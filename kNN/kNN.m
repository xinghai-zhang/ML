function result = kNN(train,test,k,label)
%KNN Summary of this function goes here
%   Detailed explanation goes here

distance =NaN(2,5000);
for n = 1:5000
   dist = calDis(train(n,:) ,test,2);
   distance(1:2,n)=[dist,label(n)];
end
newDistance = sortrows(distance',1)';% sort array based on the first row
neighbors = newDistance(2,1:k);
result = mode(neighbors,2); % most frequent value

end

