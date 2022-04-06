### Name: NIKHIL KUMAR

### Roll no: 19CS8013

### Reg no: 19U10042

<hr>

### Subject: Signal and Systems Laboratory

### Subject Code: CSS453 

### Lab 4: Convolution

<hr>

$$
x(t) =
  \begin{cases}
    3,       & \quad t = -2\\
    -1,  	 & \quad t = 1\\
    2, 		 & \quad t = 3\\
    0,   	 & \quad t \ne {-2, 1, 3}
  \end{cases}
$$

$$
h(t) =
  \begin{cases}
    1,       & \quad -4 \le t < 4\\
    0,  	 & \quad t > 4 \quad \text{or} \quad t < -4 \\
  \end{cases}
$$

#### 1. Write a program to convolve two discrete time sequences. Plot all the sequences.

```matlab
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
subplot(3,4,1)
plot(t,x,'LineWidth',2)
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
subplot(3,4,2)
plot(t,h,'LineWidth',2)
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
subplot(3, 4, 3)
plot(t1,y,'LineWidth',2)
xlim([min(t1) max(t1)])
ylim([min(y) - 0.5 max(y) + 0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Y(t)')
```

![lab4-1](/home/kumnik/Documents/4th sem/SAS/lab4/lab4-1.png)



#### 2. Write a program to convolve two discrete time sequences. Plot all the sequences. Hence verify

$$
x(t) * h(t) = h(t) * x(t)
$$

```matlab
t = -5:0.2:20;
x = zeros(size(t));
h = zeros(size(t));
%% Generating x(t)
k = 0;
for i = t
    if i==-2
        x(k+1)=3;
    elseif i == 1
        x(k+1) = -1;
    elseif i == 3
        x(k+1)=2;
    else
        x(k+1)=0;
    end
    k=k+1;
end
subplot(3,4,1)
plot(t,x,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(x)-0.5 max(x)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('x(t)')
%% Generating h(t)
k = 0;
for i = t
    if i>=-4 && i<4
        h(k+1)=1;
    else
        h(k+1)=0;
    end
    k=k+1;
end
subplot(3,4,2)
plot(t,h,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(h)-0.5 max(h)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('h(t)')
%% Generating Y(t) = x(t)*h(t)
t1=-10:0.2:40;
m = length(x);
n = length(h);
X = [x,zeros(1,n)];
H = [h,zeros(1,m)];
for i = 1:n+m-1
    y(i)=0;
    for j=1:m
        if(i-j+1>0)
            y(i)=y(i)+X(j)*H(i-j+1);
        end
    end
end
subplot(3,4,3)
plot(t1,y,'LineWidth',2)
xlim([min(t1) max(t1)])
ylim([min(y)-0.5 max(y)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Y(t) = x(t)*h(t)')
%% Generating Y'(t) = h(t)*x(t)
n=length(x);
m=length(h);
H=[x,zeros(1,m)];
X=[h,zeros(1,n)];
for i=1:n+m-1
    y(i)=0;
    for j=1:m
        if(i-j+1>0)
            y(i)=y(i)+X(j)*H(i-j+1);
        end
    end
end
subplot(3,4,4)
plot(t1,y,'LineWidth',2)
xlim([min(t1) max(t1)])
ylim([min(y)-0.5 max(y)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Y(t) = h(t)*x(t)')
```

![lab4-2](/home/kumnik/Documents/4th sem/SAS/lab4/lab4-2.png)



#### 3. Find the convolution of two Non Causal Signal 

$$
x(n) = 3 \delta (n+2) - \delta (n-1) + 2 \delta (n-3) \\
\text{and} \\
g(n) = u( n+4) - u(n-3)
$$

```matlab
n0 = -2;
n1 = 1;
n2 = 3;
n3 = -4;
n = -5:5;
%% generating x(n)
xn = 3*((n-n0)==0)-((n-n1)==0)+2*((n-n2)==0);
%% generating h(n)
yn = ((n-n3)==0) - ((n-n2)==0);
%% convolution
h = conv(xn, yn, 'same');
%% plot
figure
subplot(3,4,1)
stem(n,xn,'linewidth',1,'color','b')
a= title('x(n)');
set(a,'fontsize',9);
a= xlabel('Time(s)-->');
set(a,'fontsize',9);
a = ylabel('Waveform-->');
set(a,'fontsize',9);
grid
subplot(3,4,2)
stem(n,yn,'linewidth',1,'color','r')
a= title('h(n)');
set(a,'fontsize',9);
a= xlabel('Time(s)-->');
set(a,'fontsize',9);
a = ylabel('Waveform-->');
set(a,'fontsize',9);
grid
subplot(3,4,3)
stem(n,h,'linewidth',1,'color','g')
xlim([-5,5]);
ylim([-3,3]);
a= title('x(n)*h(n)');
set(a,'fontsize',9);
a= xlabel('Time(s)-->');
set(a,'fontsize',9);
a = ylabel('Waveform-->');
set(a,'fontsize',9);
grid
```

![lab4-3](/home/kumnik/Documents/4th sem/SAS/lab4/lab4-3.png)



#### 5. Write a program to find the response of the given system below. Plot all the sequences.

![image-20210606105551059](/home/kumnik/.config/Typora/typora-user-images/image-20210606105551059.png)

###### We assume all the individual systems to be able to take the input signal and reverse it 

```matlab
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
subplot(2,4,1)
plot(t,x,'LineWidth',2)
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
subplot(2,4,2)
plot(t,w,'LineWidth',2)
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
subplot(2,4,3)
plot(t,z,'LineWidth',2)
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
subplot(2,4,4)
plot(t,o1,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(o1)-0.5 max(o1)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Output1(t)=x(-t)*w(t)')
subplot(2,4,5)
plot(t,o2,'LineWidth',2)
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
subplot(2,4,7)
plot(t,Y,'LineWidth',2)
xlim([min(t) max(t)])
ylim([min(Y)-0.5 max(Y)+0.5])
xlabel('Time (s)-->')
ylabel('waveform-->')
title('Y(t)=Output1(-t)*Output2(-t)')
```

![lab4_5](/home/kumnik/Documents/4th sem/SAS/lab4/lab4_5.png)
