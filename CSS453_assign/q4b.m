t = -5:0.2:20;
x = zeros(size(t));
h = zeros(size(t));
%% Generating x(t)
k = 0;
for i = t
if i == -2
x(k+1) = 3;
elseif i == 1
x(k+1) = -1;
elseif i == 3
x(k+1) = 2;
else
x(k+1) = 0;
end
k=k+1;
end
subplot(2, 2,1)
plot(t,x,'r','LineWidth',2)
xlim([min(t) max(t)])
ylim([min(x)-0.5 max(x)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t)')
%% Generating h(t)
k = 0;
for i = t
if i >= -4 && i < 4
h(k+1) = 1;
else
h(k+1) = 0;
end
k = k+1;
end
subplot(2, 2,2)
plot(t,h,'r','LineWidth',2)
xlim([min(t) max(t)])
ylim([min(h)-0.5 max(h)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('h(t)')
%% Generating Y(t) for Y(t) = x(t)*h(t)
t1=-10:0.2:40;
n=length(x);
m=length(h);
H=[x,zeros(1,m)];
X=[h,zeros(1,n)];
for i = 1 : n + m - 1
y(i)=0;
for j=1:m
if(i-j+1 > 0)
y(i) = y(i) + X(j) * H(i-j+1);
end
end
end
subplot(2, 2, 3)
plot(t1,y ,'r','LineWidth',2)
xlim([min(t1) max(t1)])
ylim([min(y) - 0.5 max(y) + 0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Y(t) = X(t)*H(t)')
%% Generating Y(t) for Y(t) = h(t)*x(t)
t1=-10:0.2:40;
n=length(x);
m=length(h);
H=[x,zeros(1,m)];
X=[h,zeros(1,n)];
for i = 1 : n + m - 1
y(i)=0;
for j=1:m
if(i-j+1 > 0)
y(i) = y(i) + X(j) * H(i-j+1);
end
end
end
subplot(2, 2, 4)
plot(t1,y ,'r','LineWidth',2)
xlim([min(t1) max(t1)])
ylim([min(y) - 0.5 max(y) + 0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Y(t) = H(t)*X(t)')