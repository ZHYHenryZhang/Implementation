%% ECE271A Homework2
% Author: Hengyuan Zhang
% PID: A53283623
% Dept.: ECE ISRC

load('TrainingSamplesDCT_8_new\TrainingSamplesDCT_8_new.mat')
zig_zag = [0   1   5   6  14  15  27  28;
    2   4   7  13  16  26  29  42;
    3   8  12  17  25  30  41  43;
    9  11  18  24  31  40  44  53;
    10  19  23  32  39  45  52  54;
    20  22  33  38  46  51  55  60;
    21  34  37  47  50  56  59  61;
    35  36  48  49  57  58  62  63];

X_FG = TrainsampleDCT_FG;
X_BG = TrainsampleDCT_BG;

%% compute P(y) 
num_FG = size(X_FG,1);
num_BG = size(X_BG,1);
PY_FG = num_FG / (num_FG + num_BG);
PY_BG = num_BG / (num_FG + num_BG);

%% compute P(x|y)
% get mean and covarian matrix
u_FG = mean(X_FG);
u_BG = mean(X_BG);
cov_FG = cov(X_FG, 1);
cov_BG = cov(X_BG, 1);

% min_FG = min(X_FG(:))
% min_BG = min(X_BG(:))
% max_FG = max(X_FG(:))
% max_BG = max(X_BG(:))
% min_x = min(min_FG,min_BG)
% max_x = max(max_FG,max_BG)
XX = [X_FG; X_BG];
min_XX = min(XX);
max_XX = max(XX);

% plot marginal density
d_FG = std(X_FG, 1);
d_BG = std(X_BG, 1);

n_FG = (X_FG - repmat(u_FG,[size(X_FG,1),1]))./repmat(d_FG,[size(X_FG,1),1]);
n_BG = (X_BG - repmat(u_BG,[size(X_BG,1),1]))./repmat(d_BG,[size(X_BG,1),1]);

% for i=1:64
%     j = mod(i-1,8);
%     if j == 0
%         figure;
%     end
%     x = min_XX(i):0.001:max_XX(i);
%     g_FG = normpdf(x,u_FG(i),d_FG(i));
%     g_BG = normpdf(x,u_BG(i),d_BG(i));
%     subplot(2,4,j+1);
%     plot(x,g_FG);title(num2str(i));
%     hold on
%     plot(x,g_BG);title(num2str(i));
%     hold off
% end

best = [ 1 19 21 25 31 32 40 48];
worst = [ 3 4 5 58 59 62 63 64];
% figure;
% for i=1:8
%     x = min_XX(best(i)):0.001:max_XX(best(i));
%     g_FG = normpdf(x,u_FG(best(i)),d_FG(best(i)));
%     g_BG = normpdf(x,u_BG(best(i)),d_BG(best(i)));
%     subplot(2,4,i);
%     plot(x,g_FG);title(num2str(best(i)));
%     hold on
%     plot(x,g_BG);title(num2str(best(i)));
%     hold off
% end
% figure;
% for i=1:8
%     x = min_XX(worst(i)):0.001:max_XX(worst(i));
%     g_FG = normpdf(x,u_FG(worst(i)),d_FG(worst(i)));
%     g_BG = normpdf(x,u_BG(worst(i)),d_BG(worst(i)));
%     subplot(2,4,i);
%     plot(x,g_FG);title(num2str(worst(i)));
%     hold on
%     plot(x,g_BG);title(num2str(worst(i)));
%     hold off
% end

X_FG_8 = X_FG(:,best);
X_BG_8 = X_BG(:,best);
u_FG_8 = mean(X_FG_8);
u_BG_8 = mean(X_BG_8);
cov_FG_8 = cov(X_FG_8, 1);
cov_BG_8 = cov(X_BG_8, 1);
% 
% % normalization?
% 
%% classification
figure;

cheetah_bmp = imread('cheetah.bmp');
cheetah_db = im2double(cheetah_bmp);
[max_i, max_j] = size(cheetah_bmp);
cheetah = padarray(cheetah_db,[7,7],'post');
subplot(2,2,1);imshow(cheetah_bmp);title('original');

A_64 = zeros(size(cheetah_bmp));
A_8 = zeros(size(cheetah_bmp));
% block = cheetah(1:8,1:8);
% abs(dct2(block));
% vector = zeros([1, 64]);
for i=1:size(cheetah_bmp,1)
    for j=1:size(cheetah_bmp,2)
        % get image block
        block = cheetah(i:i+7,j:j+7);
        frequency = abs(dct2(block));
        vector = zeros([1, 64]);
        for idx_x = 1:8
            for idx_y = 1:8
                %frequency(idx_x, idx_y)
                %zig_zag(idx_x,idx_y)+1
                vector(zig_zag(idx_x,idx_y)+1) = frequency(idx_x, idx_y);
            end
        end
        % [sorted_vec, idx_vec] = sort(vector);
        % x_vec = idx_vec(size(idx_vec,2)-1);
        %2nd max
        %decide
        vector_8 = vector(best);
        prob_x_BG_64 = mvnpdf(vector, u_BG, cov_BG);
        prob_x_BG_8 = mvnpdf(vector_8, u_BG_8, cov_BG_8);
        prob_x_FG_64 = mvnpdf(vector, u_FG, cov_FG);
        prob_x_FG_8 = mvnpdf(vector_8, u_FG_8, cov_FG_8);
        if prob_x_BG_64 * PY_BG < prob_x_FG_64 * PY_FG
            A_64(i,j) = 1;
        end
        if prob_x_BG_8 * PY_BG < prob_x_FG_8 * PY_FG
            A_8(i,j) = 1;
        end
    end
end
mask = imread('cheetah_mask.bmp');
subplot(2,2,2);imshow(A_64);title('cheetah_64');
subplot(2,2,3);imshow(A_8);title('cheetah_8');
subplot(2,2,4);imshow(mask);title('mask');

mask_db = im2double(mask);
s_64=sign(A_64 - mask_db);
fp_64 = sum(s_64(:)==1);
fn_64 = sum(s_64(:)==-1);
m_FG = sum(mask_db(:)==1);
m_BG = sum(mask_db(:)==0);
s_8 = sign(A_8 - mask_db);
fp_8 = sum(s_8(:)==1);
fn_8 = sum(s_8(:)==-1);
POE_64 = PY_BG*fp_64/m_BG+PY_FG*fn_64/m_FG
POE_8 = PY_BG*fp_8/m_BG+PY_FG*fn_8/m_FG

error_rate_64 = nnz(imabsdiff(A_64,mask_db))/(size(A_64,1)*size(A_64,2));
error_rate_8 = nnz(imabsdiff(A_8,mask_db))/(size(A_8,1)*size(A_8,2));