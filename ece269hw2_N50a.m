% ECE 269 homework2 computer exercise
% orthogonal matching pursuit
% Author: Hengyuan Zhang PID: A53283623

% parameters
tic
N = 50;
smax = N;
mmax = N;
err = zeros( smax, mmax);
for s = 1:smax
    for M = 1:mmax
        toc
        tic
        s_count = 0;
        sign_mtx = 2*randi(2,s,2000)-3;
        rnum_mtx = 9*rand(s,2000)+1;
        x_mtx = sign_mtx .* rnum_mtx;
        randn_mtx = randn(M,N,2000);
        for k = 1:2000
            % testing of matrix generation
            B = randn_mtx(:,:,k);
            % A = B * diag(1./sqrt(sum(B.*B,1)));
            A = normc(B);
            x = zeros(N,1);
            metric_v = zeros(2000,1);
            S = randperm(N,s);
            for i = 1:s
                x(S(i)) = x_mtx(i,k);
            end
%             tic
%             while i <= s
%                 tmp = randi(N);
%                 newrand = true;
%                 for j = 1:i-1
%                     if tmp == S(j)
%                         newrand = false;
%                         break;
%                     end
%                 end
%                 if newrand == false
%                     i = i - 1;
%                 else
%                     S(i) = tmp;
%                     x(tmp) = (2*randi(2) - 3) * (9*rand(1) + 1);
%                 end
%                 i = i + 1;
%             end
            y = A * x;
            [S_est] = myOMP_aprx(y,A,s);
            % metric_v(k) = norm(x - x_est)/norm(x);
            s_correct = true;
            for m = 1:size(S_est,1)
                if x(S_est(m)) == 0
                    s_correct = false;
                    break;
                end
            end
            if s_correct == true
                s_count = s_count + 1;
            end
        end
        % metric = sum(metric_v)/2000.0;
        metric_s = s_count/2000.0;
        [s,M,metric_s]
        err(s,M) = metric_s;
    end
end