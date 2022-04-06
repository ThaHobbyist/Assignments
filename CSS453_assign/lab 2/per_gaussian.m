fs = 1e7;
tc = gauspuls('cutoff', 10e3, 0.5, [], -40);
t = -tc:1/fs:tc;
x = gauspuls(t, 1000, 0.5)
plot(t, x)
xlabel('Time (s)')
ylabel('Waveform')