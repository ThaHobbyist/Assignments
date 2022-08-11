t = -5:0.2:20;
x = zeros(size(t));
w = zeros(size(t));
z = zeros(size(t));
%% Generate x(t)
k = 0;
for i = t
if i<0
x(k+1) = 0;
elseif i >= 0 && i<5
x(k+1) = 1;
elseif i >= 5 && i<8
x(k+1) = 2;
elseif i >= 8 && i < 12
x(k+1) = 5;
else
x(k+1) = 0;
end
k = k+1;
end
subplot(3,2,1)
plot(t,x,'r','LineWidth',2)
xlim([min(t) max(t)])
ylim([min(x)-0.5 max(x)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t)')
%% Generate w(t)
k=0;
for i = t
if i<0
w(k+1)=0;
elseif i>=0 && i<7
w(k+1)=2;
elseif i>=7 && i<10
w(k+1)=0;
elseif i>=10 && i<15
w(k+1)=7;
else
w(k+1)=0;
end
k=k+1;
end
subplot(3,2,2)
plot(t,w,'r','LineWidth',2)
xlim([min(t) max(t)])
ylim([min(w)-0.5 max(w)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('w(t)')
%% generate z(t)
k=0;
for i = t
if i==-2
z(k+1)=3;
elseif i==1
z(k+1)=-1;
elseif i==3
z(k+1)=2;
else
z(k+1)=0;
end
k=k+1;
end
subplot(3,2,3)
plot(t,z,'r','LineWidth',2)
xlim([min(t) max(t)])
ylim([min(z)-0.5 max(z)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('z(t)')
%% x(t)->x(-t)
c=fliplr(x);
%% x(-t)*w(t); x(-t)*z(t)
o1 = conv(c,w,'same');
o2 = conv(c,z,'same');
subplot(3,2,4)
plot(t,o1,'r','LineWidth',2)
xlim([min(t) max(t)])
ylim([min(o1)-0.5 max(o1)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Output1(t)=x(-t)*w(t)')
subplot(3,2,5)
plot(t,o2,'r','LineWidth',2)
xlim([min(t) max(t)])
ylim([min(o2)-0.5 max(o2)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Output2(t)=x(-t)*z(t)')
%% o1(t)->o1(-t); o2(t)->o2(-t)
o1flip = fliplr(o1);
o2flip = fliplr(o2);
%% Y(t)=o1flip(t)*o2flip(t)
Y = conv(o1flip,o2flip,'same');
%% plot Y(t)
subplot(3,2,6)
plot(t,Y,'r','LineWidth',2)
xlim([min(t) max(t)])
ylim([min(Y)-0.5 max(Y)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Y(t)=Output1(-t)*Output2(-t)')