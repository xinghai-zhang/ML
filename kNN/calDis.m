function dis = calDis( a,b,dim )
%CALDIS Summary of this function goes here
%   Detailed explanation goes here
if(dim == 2)
    dis = sumsqr(a - b); %sum of sqaure of the row
end
if(dim == 1)
    dis = sum(a - b);
end

end

