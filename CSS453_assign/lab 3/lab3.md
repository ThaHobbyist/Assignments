### Name: NIKHIL KUMAR

### Roll no: 19CS8013

### Reg no: 19U10042

<hr>

### Subject: Signal and Systems Laboratory

### Subject Code: CSS453 

### Lab 3: 

<hr>


$$
x(t) =
  \begin{cases}
    1,       & \quad 0\le t < 5\\
    2,  	 & \quad 5 \le t < 8\\
    3, 		 & \quad 8 \le t < 12\\
    0,   	 & \quad t < 0 \quad \text{or} \quad t \ge 12\\
  \end{cases}
$$

$$
y(t) =
  \begin{cases}
    2,       & \quad 0\le t < 7\\
    0,  	 & \quad 7 \le t < 10\\
    7, 		 & \quad 10 \le t < 15\\
    0,   	 & \quad t < 0 \quad \text{or} \quad t \ge 15\\
  \end{cases}
$$

###### 1. Generate and Perform:

##### a. $ x(t) + y(t) $

###### b.  $ x(t) - y(t)

##### c. $ x(t)*y(t)$

##### d. $\frac{x(t)}2 + \frac{y(t)}3$

##### e. $x(-t)$

##### f. $y(-t)$

##### g. $y(-t)$

##### h. $x(-t) $

##### g. $x(2t)$

##### h. $x(-2t + 5)$

##### i. $x(0.5t - 5)$

##### j. $x(-0.5t - 5)$

```matlab
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
title('x(t) + y(t)')

%% Substraction
z=x-y;
subplot(2,4,4)
plot(t,z,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(z)-0.5 max(z)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t) - y(t)')

%% Multiplication
z=x.*y;
subplot(2,4,5)
plot(t,z,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(z)-0.5 max(z)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t) * y(t)')

% $\frac{x(t)}{2}+\frac{y(t)}{3}$
z=x/2+y/3;
subplot(2,4,6)
plot(t,z,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(z)-0.5 max(z)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t)/2 + y(t)/3')

%% Time Reversal $x(-t) and y(-t)$
% for Y(t) change z=fliplr(x) to fliplar(y)
z=fliplr(x);
subplot(2,4,7)
plot(-1*fliplr(t),z,'LineWidth',2)
xlim([min(-1*fliplr(t)) max(-1*fliplr(t))])
ylim([min(z)-0.5 max(z)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(-t)')

%% Shifiting, Scaling and Time reversal i.e $x(at+\delta t)$
% $x(2t)$ = change a=2, delta_t=5 and xlim accordingly
% $x(-2t+5):$ = change a=2, delta_t=5 and xlim accordingly
% $x(0.5t-5):$ = change a=0.5, delta_t=-5 and xlim accordingly
% $x(-0.5t-5):$ = change a=-0.5, delta_t=-5 and xlim accordingly
a=2;
delta_t=0;
t_new=(t-delta_t)/a;
k=0;
for i = t_new
if i<(0-delta_t)/a
x(k+1)=0;
elseif i>=(0-delta_t)/a && i<(5-delta_t)/a
x(k+1)=1;
elseif i>=(5-delta_t)/a && i<(8-delta_t)/a
x(k+1)=2;
elseif i>=(8-delta_t)/a && i<(12-delta_t)/a
x(k+1)=5;
else
x(k+1)=0;
end
k=k+1;
end
subplot(2,4,8)
plot(t_new,x,'LineWidth',2)
xlim([-5 20])
ylim([min(x)-0.5 max(x)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(-0.5t - 5)')
```



![Figure_2](/home/kumnik/Downloads/Figure_2.png)

