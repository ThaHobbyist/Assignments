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