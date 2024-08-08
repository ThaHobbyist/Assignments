syms t
%% define f(t)
f = heaviside(t)*heaviside(3-t);
subplot(2,4,1)
fplot(f)
xlabel('t --->')
ylabel('f(t) --->')
%% define g(t)
g = heaviside(t) - heaviside(t-3);
subplot(2,4,3)
fplot(g)
xlabel('t --->')
ylabel('g(t) --->')
%% calculate laplace f(t) and g(t) and plot
F = laplace(f);
G = laplace(g);
subplot(2,4,5)
fplot(F)
xlabel('s --->')
ylabel('F(s) --->')
disp(F)
subplot(2,4,7)
fplot(G)
xlabel('s --->')
ylabel('G(s) --->')
disp(G)