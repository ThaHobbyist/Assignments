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
subplot(3,1,1)
stem(n,xn,'linewidth',2,'color','b')
a= title('x(n)');
set(a,'fontsize',9);a= xlabel('Time(s)-->');
set(a,'fontsize',9);
a = ylabel('Waveform-->');
set(a,'fontsize',9);
grid
subplot(3,1,2)
stem(n,yn,'linewidth',2,'color','r')
a= title('h(n)');
set(a,'fontsize',9);
a= xlabel('Time(s)-->');
set(a,'fontsize',9);
a = ylabel('Waveform-->');
set(a,'fontsize',9);
grid
subplot(3,1,3)
stem(n,h,'linewidth',2,'color','g')
xlim([-5,5]);
ylim([-3,3]);
a= title('x(n)*h(n)');
set(a,'fontsize',9);
a= xlabel('Time(s)-->');
set(a,'fontsize',9);
a = ylabel('Waveform-->');
set(a,'fontsize',9);
grid
