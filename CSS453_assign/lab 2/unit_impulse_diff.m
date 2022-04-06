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