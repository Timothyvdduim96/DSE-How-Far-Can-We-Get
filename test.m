x=[0:1:4];
y=[0:1:4];
[x,y]=meshgrid(x,y)
z=x.^2+y.^2
figure(1)
surf(x,y,z)





x=[0:1:8];
y=[0:1:4];
row=0;
col=0;

z=ones(length(x),length(y));

for i=x
    row=row+1;
    for j=y
        col=col+1
        z(row,col)=i^2+j^2
    end
    col=0
end
figure(2)
surf(x,y,z)
disp(z)
        