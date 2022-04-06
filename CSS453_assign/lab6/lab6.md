### Name: NIKHIL KUMAR

### Roll no: 19CS8013

### Reg no: 19U10042

<hr>

### Subject: Signal and Systems Laboratory


### Subject Code: CSS453 

### Lab 6: Convolution in transform domain

<hr>

##### 1. Find the Fourier transform of the following in symbolic form

**(a)** $f=a|t|$

```matlab
syms t a
f = a*abs(t);
fourier(f)
```

###### Output:

```
ans =
 
-(2*a)/w^2
```

**(b)** $f=a \cos(\omega t)$

```matlab
syms t
f = a*cos(w0*t);
fourier(f)
```

###### Output:

```
ans =
 
pi*a*(dirac(t - w) + dirac(t + w))
```

**(c)** $f=e^{-t \mod{a}} u(t)$

```matlab
syms t a
f = exp(-t*abs(a))*heaviside(t);
fourier(f)
```

###### Output:

```
ans =
 
1/(abs(a) + w*1i) - (sign(abs(a))/2 - 1/2)*fourier(exp(-t*abs(a)), t, w)
```

**(d)** $f=e^{-t^2-x^2}$

```matlab
syms t x
f = exp(-t^2-x^2);
fourier(f)
```

###### Output:

```
ans =
 
pi^(1/2)*exp(- t^2 - w^2/4)
```

##### 2. Find the Inverse Fourier transform of the following in symbolic form:

**(a)** $F=e^{\frac{-\omega^2}{4}}$

```matlab
syms w
F = exp(-w^2/4);
ifourier(F)
```

###### Output:

```
ans =
 
exp(-x^2)/pi^(1/2)
```

**(b)** $F=e^{\omega^2 - a^2}$

```matlab
syms a w t
F = exp(-w^2-a^2);
ifourier(F)
```

###### Output:

```
ans =
 
exp(- a^2 - x^2/4)/(2*pi^(1/2))
```

##### 3. Find the Z- transform of the following in symbolic form:

**(a)** $f=\sin{k}$

```matlab
syms k x
f = sin(k);
ztrans(f, k, x)
```

###### Output:

```
ans =
 
(x*sin(1))/(x^2 - 2*cos(1)*x + 1)
```

**(b)** $f(n)=a^n$

```matlab
syms a n x
f = a^n;
ztrans(f, x)
```

###### Output:

```
ans =
 
-x/(a - x)
```

**(c)** $f(n)=u(n-3)$

```matlab
syms n z
ztrans(heaviside(n - 3), n, z)
```

###### Output:

```
ans =
 
(1/(z - 1) + 1/2)/z^3
```

**(d)** $f[n] = (\frac{1}{4})^n u[n]$

```matlab
syms z n;
ztrans(1/4^n)
```

###### Output:

```
ans =
 
z/(z - 1/4)
```

**(f)** $f(n)=2^{n+1}+4(\frac{1}{2})^n$

```matlab
syms z n
ztrans(2*2^n+4*(1/2)^n)
```

###### Output:

```
ans =
 
(2*z)/(z - 2) + (4*z)/(z - 1/2)
```

##### 4. **Find the inverse Z- transform of the following in symbolic form** 

**(a)** $x(z)=\frac{2z}{2z-1}$

```matlab
syms z n;
iztrans(2*z/(2*z-1))
```

###### Output:

```
ans =
 
(1/2)^n
```

**(b)** $x(z) = \frac{6-9z^{-1}}{1-2.5z^{-1}+z^{-2}}$

```matlab
syms z n;
iztrans((6-9*z^-1)/(1-2.5*z^-1+z^-2))
```

###### Output:

```
ans =
 
2*2^n + 4*(1/2)^n
```

**(c)** $x(z)=(\frac{1}{6-5z^{-1}+z^{-2}})(\frac{4z}{4z-1} - z^{-1} + 5z^{-1})$

```matlab
syms z n;
iztrans((1/(6-5*z^-1+z^-2))*((4*z/(4*z-1))-z^-1+5*z^-1))
```

###### Output:

```
ans =
 
5*(1/2)^n - (16*(1/3)^n)/3 + (1/4)^n/2
```

##### 6. Verification of convolution property of 

##### **(a)** Fourier Transform: $Z[x1(n)*x2(n)] = X1(z)X2(z)$

```matlab
function [ w ] = convmat(x1,x2)
n=0:100;
x1=[1 2 3 4 5];
x2=[6 7 8 9 10];
lengthofx1=length(x1);
lengthofx2=length(x2);
X1=[x1,zeros(1,lengthofx2)];
X2=[x2,zeros(1,lengthofx1)];
for k=1:(lengthofx1+lengthofx2-1)
w(k)=0;
for j=1:lengthofx1
if(k-j+1)>0
w(k)=w(k)+X1(j)*X2(k-j+1);
end
end
end
subplot(2,4,2)
r=x1.*x2;
f=abs(fft(r));
stem(f)
title('fourier transform of two multiplied signals')
subplot(2,4,6)
a1=abs(fft(x1));
a2=abs(fft(x2));
b=conv(a1,a2);
stem(b)
title('convolution of two fourier transformed signals')
end
```

###### Output:

```
ans =

     6    19    40    70   110   114   106    85    50
```

![image-20210610110359879](/home/kumnik/.config/Typora/typora-user-images/image-20210610110359879.png)

