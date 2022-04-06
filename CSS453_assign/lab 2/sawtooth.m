fs = 1e3;
t = 0:1/1e3:1;
d = 0:1/3:1;
x = tripuls(t,0.2,-1);
y = pulstran(t,d,x,fs);
plot(t,y)
#hold off
xlabel('Time (s)')
ylabel('Waveform')