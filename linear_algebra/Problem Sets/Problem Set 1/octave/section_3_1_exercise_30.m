v = [0; 1]; 
A= [.8 .3; .2 .7];
x = v; k = [0 : 7];
for j = 1 : 7
  v = A*v; 
  x = [x v];
end
x
plot(k, x)