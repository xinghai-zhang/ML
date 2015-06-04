function min = findmin( input )
%FINDMIN Summary of this function goes here
%   Detailed explanation goes here
syms x;
f(x)= (x-3)^2+exp(x);
g(x)= diff(f(x));
alpha = 0.2;

temp = input+1;

while abs(input-temp) > 0.001
    temp = input;
    input = input - alpha*g(input);  
end

min = eval(input);

end

