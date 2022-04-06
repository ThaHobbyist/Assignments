t=-2:0.05:2;
f=1; % frequency = 1Hz
omega=2*pi*f;

y = sin(omega*t);
subplot(2,2,1)
plot(t,y)
xlabel('t-->')
ylabel('amplitude')
title('sin(\omega(t))')

y = cos(omega*t);
subplot(2,2,2)
plot(t,y)
xlabel('t-->')
ylabel('amplitude')
title('cos(\omega(t))')

y = sin(omega*t-pi/3);
subplot(2,2,3)
plot(t,y)
xlabel('t-->')
ylabel('amplitude')
title('sin(\omega(t)-\phi/3)')

y = sin(omega*t+pi/6);
subplot(2,2,4)
plot(t,y)
xlabel('t-->')
ylabel('amplitude')
title('sin(\omega(t)+\phi/6)')
