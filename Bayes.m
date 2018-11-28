%% ECE271A Homework3
% Author: Hengyuan Zhang
% PID: A53283623
% Dept.: ECE ISRC

load('hw3Data/TrainingSamplesDCT_subsets_8.mat')
load('hw3Data/Alpha.mat')
load('hw3Data/Prior_1.mat')
load('hw3Data/Prior_2.mat')

zig_zag = [0   1   5   6  14  15  27  28;
    2   4   7  13  16  26  29  42;
    3   8  12  17  25  30  41  43;
    9  11  18  24  31  40  44  53;
    10  19  23  32  39  45  52  54;
    20  22  33  38  46  51  55  60;
    21  34  37  47  50  56  59  61;
    35  36  48  49  57  58  62  63];

%% 
% a) for each class, compute the covariance of class conditional and the
% posterior mean and covariance of P_{u|T}(u|D_1)

% covariance of class conditional
mean_BG = zeros(size(D1_FG,2), 1, 4);
mean_FG = zeros(size(D1_FG,2), 1, 4);
cov_FG = zeros(size(D1_FG,2), size(D1_FG,2), 4);
cov_BG = zeros(size(D1_FG,2), size(D1_FG,2), 4);
num_FG = zeros(4);
num_BG = zeros(4);

mean_BG(:,:,1) = transpose(mean(D1_BG));
mean_FG(:,:,1) = transpose(mean(D1_FG));
cov_FG(:,:,1) = cov(D1_FG, 1);
cov_BG(:,:,1) = cov(D1_BG, 1);
num_FG(1)= size(D1_FG, 1);
num_BG(1) = size(D1_BG, 1);

mean_BG(:,:,2) = transpose(mean(D2_BG));
mean_FG(:,:,2) = transpose(mean(D2_FG));
cov_FG(:,:,2) = cov(D2_FG, 1);
cov_BG(:,:,2) = cov(D2_BG, 1);
num_FG(2)= size(D2_FG, 1);
num_BG(2) = size(D2_BG, 1);

mean_BG(:,:,3) = transpose(mean(D3_BG));
mean_FG(:,:,3) = transpose(mean(D3_FG));
cov_FG(:,:,3) = cov(D3_FG, 1);
cov_BG(:,:,3) = cov(D3_BG, 1);
num_FG(3)= size(D3_FG, 1);
num_BG(3) = size(D3_BG, 1);

mean_BG(:,:,4) = transpose(mean(D4_BG));
mean_FG(:,:,4) = transpose(mean(D4_FG));
cov_FG(:,:,4) = cov(D4_FG, 1);
cov_BG(:,:,4) = cov(D4_BG, 1);
num_FG(4)= size(D4_FG, 1);
num_BG(4) = size(D4_BG, 1);

% ML prior
sum_D = zeros(4);
py_BG = zeros(4);
py_FG = zeros(4);


cheetah_bmp = imread('cheetah.bmp');
cheetah_db = im2double(cheetah_bmp);
[max_i, max_j] = size(cheetah_bmp);
cheetah = padarray(cheetah_db,[7,7],'post');
mask = imread('cheetah_mask.bmp');
mask_db = im2double(mask);

cheetah_zz = zeros([ 64, max_j, max_i ]);
tic
for j=1: max_j
    for i=1: max_i
        block = cheetah(i:i+7,j:j+7);
        frequency = abs(dct2(block));
        vector = zeros([1, 64]);
        for idx_x = 1:8
            for idx_y = 1:8
                cheetah_zz(zig_zag(idx_x,idx_y)+1,j,i) = frequency(idx_x, idx_y);
            end
        end
    end
end
toc




Res_bayes = zeros([size(cheetah_bmp),size(alpha, 2),4,2]);
Res_map = zeros([size(cheetah_bmp),size(alpha, 2),4,2]);
Res_ml = zeros([size(cheetah_bmp),4]);

POE_bayes = zeros(size(alpha,2),4,2);
POE_map = zeros(size(alpha,2),4,2);
POE_ml = zeros(4);
error_rate_bayes = zeros(size(alpha,2),4,2);
error_rate_map = zeros(size(alpha,2),4,2);
error_rate_ml = zeros(4);

for m = 1:4
    sum_D(m) = num_FG(m) + num_BG(m);
    py_BG(m) = num_BG(m) / sum_D(m);
    py_FG(m) = num_FG(m) / sum_D(m);
    
    figure(1+2*(m-1))
    subplot(3,4,1);imshow(cheetah_bmp);title('original');
    subplot(3,4,2);imshow(mask);title('mask');
    figure(1+2*(m-1)+8)
    subplot(3,4,1);imshow(cheetah_bmp);title('original');
    subplot(3,4,2);imshow(mask);title('mask');
    
    tic
    for j=1:max_j
        for i=1:max_i
            %decide
            prob_ml_BG = mvnpdf(cheetah_zz(:,j,i), mean_BG(:,:,m), cov_BG(:,:,m));
            prob_ml_FG = mvnpdf(cheetah_zz(:,j,i), mean_FG(:,:,m), cov_FG(:,:,m));
            if prob_ml_BG * py_BG(m) < prob_ml_FG * py_FG(m)
                Res_ml(i,j,m) = 1;
            end
        end
    end
    s_64_ml=sign(Res_ml(:,:,m)- mask_db);
    fp_64_ml = sum(s_64_ml(:)==1);
    fn_64_ml = sum(s_64_ml(:)==-1);
    m_FG_ml = sum(mask_db(:)==1);
    m_BG_ml = sum(mask_db(:)==0);
    POE_ml(m) = py_BG(m)*fp_64_ml/m_BG_ml+py_FG(m)*fn_64_ml/m_FG_ml;
    error_rate_ml(m) = nnz(imabsdiff(Res_ml(:,:,m),mask_db))/(max_i*max_j);
    figure(1+2*(m-1))
    subplot(3,4,3);imshow(Res_ml(:,:,m));title(strcat('ML ', num2str(m), 'POE: ', num2str(round(POE_ml(m),4))));
    figure(2+2*(m-1))
    subplot(2,5,1);imshow(Res_ml(:,:,m));title(strcat('ML ', num2str(m), 'POE: ', num2str(round(POE_ml(m),4))));
    figure(1+2*(m-1)+8)
    subplot(3,4,3);imshow(Res_ml(:,:,m));title(strcat('ML ', num2str(m), 'POE: ', num2str(round(POE_ml(m),4))));
    figure(2+2*(m-1)+8)
    subplot(2,5,1);imshow(Res_ml(:,:,m));title(strcat('ML ', num2str(m), 'POE: ', num2str(round(POE_ml(m),4))));
    toc
    
    mu_BG = zeros(size(D1_FG,2), 1, 2);
    mu_FG = zeros(size(D1_FG,2), 1, 2);
    
    mu_BG(:,:,1) = transpose(mu0_BG);
    mu_BG(:,:,2) = transpose(mu0_BG);
    mu_BG(1,1,1) = 1;
    mu_BG(1,1,2) = 2;
    mu_FG(:,:,1) = transpose(mu0_FG);
    mu_FG(:,:,2) = transpose(mu0_FG);
    mu_FG(1,1,1) = 3;
    mu_FG(1,1,2) = 2;
    
   for n = 1:2     
        for k=1:size(alpha,2)
            tic
            % compute parameters
            al = alpha(k);
            covmu_BG = diag(al*W0);
            covmu_FG = diag(al*W0);
            
            covsuminv_BG = inv( 1/num_BG(m) * cov_BG(:,:,m) + covmu_BG);
            covsuminv_FG = inv( 1/num_FG(m) * cov_FG(:,:,m) + covmu_FG);
            
            % alpha_BG = covmu1_BG * covsuminv_BG;
            % alpha_FG = covmu1_FG * covsuminv_FG;
            % posterior parameters
            mupos1_BG = covmu_BG * covsuminv_BG * mean_BG(:,:,m) + ...
                cov_BG(:,:,m) / num_BG(m) * covsuminv_BG * mu_BG(:,:,n);
            mupos1_FG = covmu_FG * covsuminv_FG * mean_FG(:,:,m) + ...
                cov_FG(:,:,m) / num_FG(m) * covsuminv_FG * mu_FG(:,:,n);
            % temp1 = covmu1_FG * covsuminv_FG / num1_FG * mean1_FG;
            % temp2 = cov1_FG / num1_FG * covsuminv_FG * mu1_FG;
            % mupos1_FG = temp1 + temp2;
            covpos_BG = cov_BG(:,:,m) / num_BG(m) * covsuminv_BG * covmu_BG;
            covpos_FG = cov_FG(:,:,m) / num_FG(m) * covsuminv_FG * covmu_FG;
            
            % predictive distribution
            covpre_BG = covpos_BG + cov_BG(:,:,m);
            covpre_FG = covpos_FG + cov_FG(:,:,m);
            
            % classification
            for j=1:max_j
                for i=1:max_i
                    %decide Bayes
                    prob_bayes_BG = mvnpdf(cheetah_zz(:,j,i), mupos1_BG, covpre_BG);
                    prob_bayes_FG = mvnpdf(cheetah_zz(:,j,i), mupos1_FG, covpre_FG);
                    if prob_bayes_BG * py_BG(m) < prob_bayes_FG * py_FG(m)
                        Res_bayes(i,j,k,m,n) = 1;
                    end
                    
                    %decide MAP
                    prob_map_BG = mvnpdf(cheetah_zz(:,j,i), mupos1_BG, cov_BG(:,:,m));
                    prob_map_FG = mvnpdf(cheetah_zz(:,j,i), mupos1_FG, cov_FG(:,:,m));
                    if prob_map_BG * py_BG(m) < prob_map_FG * py_FG(m)
                        Res_map(i,j,k,m,n) = 1;
                    end
                end
            end
            
            % subplot(2,2,2);imshow(A_64);title('cheetah_64');
            % subplot(2,2,3);imshow(A_8);title('cheetah_8');
            
            
            
            s_64=sign(Res_bayes(:,:,k,m,n)- mask_db);
            fp_64 = sum(s_64(:)==1);
            fn_64 = sum(s_64(:)==-1);
            m_FG = sum(mask_db(:)==1);
            m_BG = sum(mask_db(:)==0);
            POE_bayes(k,m,n) = py_BG(m)*fp_64/m_BG+py_FG(m)*fn_64/m_FG;
            error_rate_bayes(k,m,n) = nnz(imabsdiff(Res_bayes(:,:,k,m,n),mask_db))/(max_i*max_j);
            figure(1+2*(m-1)+8*(n-1))
            subplot(3,4,k+3);imshow(Res_bayes(:,:,k,m,n));title(strcat('Bayes ', num2str([k,m,n]), 'POE: ', num2str(round(POE_bayes(k,m,n),4))));
            
            s_64_map=sign(Res_map(:,:,k,m,n)- mask_db);
            fp_64_map = sum(s_64_map(:)==1);
            fn_64_map = sum(s_64_map(:)==-1);
            m_FG_map = sum(mask_db(:)==1);
            m_BG_map = sum(mask_db(:)==0);
            POE_map(k,m,n) = py_BG(m)*fp_64_map/m_BG_map+py_FG(m)*fn_64_map/m_FG_map;
            error_rate_map(k,m,n) = nnz(imabsdiff(Res_map(:,:,k),mask_db))/(max_i*max_j);
            figure(2+2*(m-1)+8*(n-1))
            subplot(2,5,k+1);imshow(Res_map(:,:,k,m,n));title(strcat('MAP ', num2str([k,m,n]), 'POE: ', num2str(round(POE_map(k,m,n),4))));
            
            toc
        end
    end
end
    
    
% 
% X_FG = TrainsampleDCT_FG;
% X_BG = TrainsampleDCT_BG;
% 
% %% compute P(y) 
% num_FG = size(X_FG,1);
% num_BG = size(X_BG,1);
% PY_FG = num_FG / (num_FG + num_BG);
% PY_BG = num_BG / (num_FG + num_BG);
% 
% %% compute P(x|y)
% % get mean and covarian matrix
% u_FG = mean(X_FG);
% u_BG = mean(X_BG);
% cov_FG = cov(X_FG, 1);
% cov_BG = cov(X_BG, 1);
% 
% % min_FG = min(X_FG(:))
% % min_BG = min(X_BG(:))
% % max_FG = max(X_FG(:))
% % max_BG = max(X_BG(:))
% % min_x = min(min_FG,min_BG)
% % max_x = max(max_FG,max_BG)
% XX = [X_FG; X_BG];
% min_XX = min(XX);
% max_XX = max(XX);
% 
% % plot marginal density
% d_FG = std(X_FG, 1);
% d_BG = std(X_BG, 1);
% 
% n_FG = (X_FG - repmat(u_FG,[size(X_FG,1),1]))./repmat(d_FG,[size(X_FG,1),1]);
% n_BG = (X_BG - repmat(u_BG,[size(X_BG,1),1]))./repmat(d_BG,[size(X_BG,1),1]);
% 
% % for i=1:64
% %     j = mod(i-1,8);
% %     if j == 0
% %         figure;
% %     end
% %     x = min_XX(i):0.001:max_XX(i);
% %     g_FG = normpdf(x,u_FG(i),d_FG(i));
% %     g_BG = normpdf(x,u_BG(i),d_BG(i));
% %     subplot(2,4,j+1);
% %     plot(x,g_FG);title(num2str(i));
% %     hold on
% %     plot(x,g_BG);title(num2str(i));
% %     hold off
% % end
% 
% best = [ 1 19 21 25 31 32 40 48];
% worst = [ 3 4 5 58 59 62 63 64];
% % figure;
% % for i=1:8
% %     x = min_XX(best(i)):0.001:max_XX(best(i));
% %     g_FG = normpdf(x,u_FG(best(i)),d_FG(best(i)));
% %     g_BG = normpdf(x,u_BG(best(i)),d_BG(best(i)));
% %     subplot(2,4,i);
% %     plot(x,g_FG);title(num2str(best(i)));
% %     hold on
% %     plot(x,g_BG);title(num2str(best(i)));
% %     hold off
% % end
% % figure;
% % for i=1:8
% %     x = min_XX(worst(i)):0.001:max_XX(worst(i));
% %     g_FG = normpdf(x,u_FG(worst(i)),d_FG(worst(i)));
% %     g_BG = normpdf(x,u_BG(worst(i)),d_BG(worst(i)));
% %     subplot(2,4,i);
% %     plot(x,g_FG);title(num2str(worst(i)));
% %     hold on
% %     plot(x,g_BG);title(num2str(worst(i)));
% %     hold off
% % end
% 
% X_FG_8 = X_FG(:,best);
% X_BG_8 = X_BG(:,best);
% u_FG_8 = mean(X_FG_8);
% u_BG_8 = mean(X_BG_8);
% cov_FG_8 = cov(X_FG_8, 1);
% cov_BG_8 = cov(X_BG_8, 1);
% % 
% % % normalization?
% % 
% %% classification
% figure;
% 
% cheetah_bmp = imread('cheetah.bmp');
% cheetah_db = im2double(cheetah_bmp);
% [max_i, max_j] = size(cheetah_bmp);
% cheetah = padarray(cheetah_db,[7,7],'post');
% subplot(2,2,1);imshow(cheetah_bmp);title('original');
% 
% A_64 = zeros(size(cheetah_bmp));
% A_8 = zeros(size(cheetah_bmp));
% % block = cheetah(1:8,1:8);
% % abs(dct2(block));
% % vector = zeros([1, 64]);
% for i=1:size(cheetah_bmp,1)
%     for j=1:size(cheetah_bmp,2)
%         % get image block
%         block = cheetah(i:i+7,j:j+7);
%         frequency = abs(dct2(block));
%         vector = zeros([1, 64]);
%         for idx_x = 1:8
%             for idx_y = 1:8
%                 %frequency(idx_x, idx_y)
%                 %zig_zag(idx_x,idx_y)+1
%                 vector(zig_zag(idx_x,idx_y)+1) = frequency(idx_x, idx_y);
%             end
%         end
%         % [sorted_vec, idx_vec] = sort(vector);
%         % x_vec = idx_vec(size(idx_vec,2)-1);
%         %2nd max
%         %decide
%         vector_8 = vector(best);
%         prob_x_BG_64 = mvnpdf(vector, u_BG, cov_BG);
%         prob_x_BG_8 = mvnpdf(vector_8, u_BG_8, cov_BG_8);
%         prob_x_FG_64 = mvnpdf(vector, u_FG, cov_FG);
%         prob_x_FG_8 = mvnpdf(vector_8, u_FG_8, cov_FG_8);
%         if prob_x_BG_64 * PY_BG < prob_x_FG_64 * PY_FG
%             A_64(i,j) = 1;
%         end
%         if prob_x_BG_8 * PY_BG < prob_x_FG_8 * PY_FG
%             A_8(i,j) = 1;
%         end
%     end
% end
% mask = imread('cheetah_mask.bmp');
% subplot(2,2,2);imshow(A_64);title('cheetah_64');
% subplot(2,2,3);imshow(A_8);title('cheetah_8');
% subplot(2,2,4);imshow(mask);title('mask');
% 
% mask_db = im2double(mask);
% s_64=sign(A_64 - mask_db);
% fp_64 = sum(s_64(:)==1);
% fn_64 = sum(s_64(:)==-1);
% m_FG = sum(mask_db(:)==1);
% m_BG = sum(mask_db(:)==0);
% s_8 = sign(A_8 - mask_db);
% fp_8 = sum(s_8(:)==1);
% fn_8 = sum(s_8(:)==-1);
% POE_64 = PY_BG*fp_64/m_BG+PY_FG*fn_64/m_FG
% POE_8 = PY_BG*fp_8/m_BG+PY_FG*fn_8/m_FG
% 
% error_rate_64 = nnz(imabsdiff(A_64,mask_db))/(size(A_64,1)*size(A_64,2));
% error_rate_8 = nnz(imabsdiff(A_8,mask_db))/(size(A_8,1)*size(A_8,2));