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