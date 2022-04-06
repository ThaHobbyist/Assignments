### Name: NIKHIL KUMAR

### Roll no: 19CS8013

### Reg no: 19U10042

<hr>

### Subject: Signal and Systems Laboratory

### Subject Code: CSS453 

### Lab 2: Basic Plotting of Signals

<hr>

##### 1. Unit Step Function



$$
U(t) =
  \begin{cases}
    1       & \quad \text{if } t \ge\ 0\\
    0  		& \quad \text{if } t < 0
  \end{cases}
$$



```matlab
t = -20:0.2:20;
u_t = zeros(size(t));
k = 0;
for i = t
    if i > 0
        u_t(k+1) = 1;
    else
        u_t(k+1) = 0;
    end
    k = k + 1;
end
plot(t,u_t)
xlabel('t-->')
ylabel('u(t)-->')
xlim([-20 20])
ylim([-0.2 1.2])
title('Unit Step Function')
```

![Screenshot from 2021-06-02 03-21-09](/home/kumnik/Pictures/Screenshot from 2021-06-02 03-21-09.png)



##### 2. Unit Impulse

$$
\delta(t) =
  \begin{cases}
    1       & \quad \text{if } t = 0\\
    0  		& \quad \text{if } t \ne\ 0
  \end{cases}
$$

​     				                 													```Or ```
$$
\delta(t) = \frac {du(t)}{dt}
$$

```matlab
t = -20:0.2:20;
delta_t = zeros(size(t));
k = 0;
for i = t
    if i == 0
        delta_t(k+1)=1;
    else
        delta_t(k+1)=0;
    end
    k=k+1;
end

plot(t,delta_t)
xlabel('t-->')
ylabel('\delta(t)-->')
xlim([-20 20])
ylim([-0.2 1.2])
title('Unit Impulse')
```

![Screenshot from 2021-06-02 03-14-39](/home/kumnik/Pictures/Screenshot from 2021-06-02 03-14-39.png)

###### Using Difference Function 

$$
\delta(t) = \frac {du(t)}{dt} = \lim\limits_{\Delta t \to 0} \frac{u(t+\Delta t)-u(t)}{\Delta t}
$$

```matlab
deltat = 0.2;
t = -20:deltat:20;
u_t = zeros(size(t));
k = 0;
for i = t
    if i >= 0
        u_t(k+1) = 1;
    else
        u_t(k+1) = 0;
    end
    k = k+1;
end
k = 0;
delta_t = [];
for i = t(2:end)
    delta_t(k+1) = (u_t(k+2)-u_t(k+1));
    k = k+1;
end

plot(t(1:end-1),delta_t)
xlabel('t-->')
ylabel('\delta(t)-->')
xlim([-20 20])
ylim([-0.2 1.2])
title('Unit Impulse Using Diff')
```

![Screenshot from 2021-06-02 03-15-15](/home/kumnik/Pictures/Screenshot from 2021-06-02 03-15-15.png)



##### 3.  Ramp Function 

$$
\gamma(t) = 
    \begin{cases}
        t       & \quad \text{if } t \ge\ 0\\
        0  		& \quad \text{if } t < 0
    \end{cases}
$$

​											               							    ```Or```
$$
\gamma(t) = \int\limits_{-\infty}^{t} u(t) dt
$$

```matlab
t = -20:0.2:20;
r_t = zeros(size(t));
k = 0;
for i = t
    if i>=0
        r_t(k+1) = i;
    else
        r_t(k+1) = 0;
    end
    k=k+1;
end

plot(t,r_t)
xlabel('t-->')
ylabel('r(t)-->')
xlim([-20 20])
ylim([-1.2 20])
title('Ramp Function')
```

![Screenshot from 2021-06-02 03-15-48](/home/kumnik/Pictures/Screenshot from 2021-06-02 03-15-48.png)



##### 4. Periodic Sinusoidal  Sequences

- $ y = \sin{\omega t}$ or  $ y = \cos{\omega t}$

- $y = \sin{\omega t + \phi}$ or $y = \sin{\omega t - \phi}$ 

```matlab
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
```

![Screenshot from 2021-06-02 03-16-23](/home/kumnik/Pictures/Screenshot from 2021-06-02 03-16-23.png)



##### 5. Periodic Rectangular Pulse

###### Generates a pulse train using the default rectangular pulse of unit width. The repetition frequency is 0.5 Hz, the signal length is 60 s, and the sample rate is 1 kHz. The gain factor is a sinusoid of frequency 0.05 Hz.

```matlab
t = 0:1/1e3:60;
d = [0:2:60;sin(2*pi*0.05*(0:2:60))]';
x = @rectpuls;
y = pulstran(t,d,x);

plot(t,y)
hold off
xlabel('Time (s)')
ylabel('Waveform')
```

![Screenshot from 2021-06-02 03-16-51](/home/kumnik/Pictures/Screenshot from 2021-06-02 03-16-51.png)



##### 6. Asymmetric Saw-Tooth Waveform

###### Generates an asymmetric sawtooth waveform with a repetition frequency of 3 Hz. The sawtooth has width 0.2 s and skew factor –1. The signal length is 1 s, and the sample rate is 1 kHz. Plot the pulse train.

````matlab
fs = 1e3;
t = 0:1/1e3:1;
d = 0:1/3:1;
x = tripuls(t,0.2,-1);
y = pulstran(t,d,x,fs);
plot(t,y)
hold off
xlabel('Time (s)')
ylabel('Waveform')
````

![Screenshot from 2021-06-02 03-17-16](/home/kumnik/Pictures/Screenshot from 2021-06-02 03-17-16.png)



##### 7. Periodic Gaussian Pulse

###### Plot a 10 kHz Gaussian RF pulse with 50% bandwidth, sampled at a rate of 10 MHz. Truncate the pulse where the envelope falls 40 dB below the peak.

```matlab
fs = 1e7;
tc = gauspuls('cutoff', 10e3, 0.5, [], -40);
t = -tc:1/fs:tc;
x = gauspuls(t, 1000, 0.5)
plot(t, x)
xlabel('Time (s)')
ylabel('Waveform')
```

![image-20210602031148857](/home/kumnik/.config/Typora/typora-user-images/image-20210602031148857.png)

