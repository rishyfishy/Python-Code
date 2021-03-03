    %% Boundary Condition --> Q_in = -q''b*A
    vector(1) = 2 * A_c * h(1) * T_air + q_b * A(1);
    matrix(1,1) = k * A(2) / dx + 2 * A_c * h(1);
    matrix(1,2) = -k * A(2) / dx;
    
    %% Heat transfer Balance: Q_cond_in = Q_cond_out + Q_conv_out
    for i=2:n-1
        vector(i) = 2 * A_c * h(i) * T_air;
        matrix(i,i-1) = -k * A(i) / dx;
        matrix(i,i) = k * (A(i) + A(i+1)) / dx + 2 * A_c * h(i);
        matrix(i,i+1) = -k * A(i+1) / dx;
    end
    
    %% Boundary Condition --> Q_cond_in = Q_conv_out
    vector(n)= 2 * A_c * h(n) * T_air;
    matrix(n,n-1) = -k * A(n) / dx;
    matrix(n,n) = k * (A(n) + A(n+1)) / dx + 2 * A_c * h(n);