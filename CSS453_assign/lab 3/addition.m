t = -5:0.2:20;
x = zeros(size(t));
y = zeros(size(t));
%% Generate x
k = 0;
for i = t
    if i < 0
        x(k + 1)=0;
    elseif i >= 0 && i < 5
        x(k+1) = 1;
    elseif i >= 5 && i < 8
        x(k+1) =2;
    elseif i >= 8 && i < 12
        x(k+1) = 5;
    else
        x(k+1) = 0;
    end
        k = k+1;
end
subplot(2,4,1)
plot(t,x,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(x)-0.5 max(x)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t)')


%% Generate y
k=0;
for i = t
    if i<0
        y(k+1)=0;
    elseif i>=0 && i<7
        y(k+1)=2;
    elseif i>=7 && i<10
        y(k+1)=0;
    elseif i>=10 && i<15
        y(k+1)=7;
    else
        y(k+1)=0;
    end
        k=k+1;
    end
subplot(2,4,2)
plot(t,y,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(y)-0.5 max(y)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t)')

%% Addition
z=x+y;
subplot(2,4,3)
plot(t,z,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(z)-0.5 max(z)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t)+y(t)')