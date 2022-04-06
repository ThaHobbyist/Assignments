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