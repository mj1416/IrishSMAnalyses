%==================        Set Directiory        ===============
cd('/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/')

%==================      Read and clean data     ===============
filename='/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx';
sheet = 2;
xlrange = 'A:UA';
DATA = xlsread(filename,sheet,xlrange);

[r,c] = find(isnan(DATA));
DATA(:,c) = []; %now data is complete

%==================         Daily total per customer        ===============
[aa,~,cc]= unique(DATA(:,2));
tot_daily = zeros(length(aa),504);
[~,n] = size(DATA);
tot_daily(:,1) = aa;
for p=5:n
    out = [aa,accumarray(cc,DATA(:,p),size(aa),@sum)];
    tot_daily(:,p-5+2) = out(:,2);
end
plot(tot_daily(:,1),tot_daily(:,2:end),'.')
xlim([min(aa)-1 max(aa)+1])
xlabel('Day')
ylabel('Daily Demand (kWh)')
filename = 'tot_daily_per_customer.png';
saveas(gcf,filename)
boxplot(transpose(tot_daily(:,2:end)))
xlabel('Day')
ylabel('Total Daily Electric Load (kWh)')
xticks([1 5 10 15 20 25 30 35 40 45 49])
xticklabels({593,597,602,607,612,616,622,627,632,637,641})
%==================      Prediction based on unweighted mean     ===============

%isolate first 5 weeks and actual sixth week
A = DATA(:,1)<22;
Weeks5 = DATA(A,:);

%calculate half hourly mean for each person
[~,n] = size(Weeks5);
[a,~,c]= unique(Weeks5(:,3));
MEAN = zeros(48,504);
MEAN(:,1) = a;
for p=5:n
    out = [a,accumarray(c,Weeks5(:,p),size(a),@mean)];
    MEAN(:,p-5+2) = out(:,2);
end

%compare sixth week reading to new matrix
AA = DATA(:,1)==22;
Week6 = DATA(AA,:);
[aa,~,cc] = unique(Week6(:,3));
ACT = zeros(48,504);
ACT(:,1) = aa;
for p=5:n
    out = [aa,accumarray(cc,Week6(:,p),size(aa),@mean)];
    ACT(:,p-5+2) = out(:,2);
end 



%==================      Plotting and saving the prediction and observed     ===============

%we have the actual (ACT) and the benchmark prediction (MEAN), now we
%compare
% for P=1:480
%     if mod(P,30) ~= 0
%         PP = mod(P,30);
%     else
%         PP = 30;
%     end
%     subplot(10,3,PP)
%     plot(MEAN(:,1),MEAN(:,2+P-1))
%     hold on
%     plot(ACT(:,1),ACT(:,2+P-1))
%     if mod(P,30)==0
%         filename=['compare_' num2str(P-30) '_' num2str(P) '.png'];
%         saveas(gcf,filename)
%         clf
%     end
% end
% 
% for P=481:503
%     subplot(10,3,mod(P,10))
%     plot(MEAN(:,1),MEAN(:,2+P-1))
%     hold on
%     plot(ACT(:,1),ACT(:,2+P-1))
%     if mod(P,30)==23
%         filename='compare_481_503.png';
%         saveas(gcf,filename)
%         clf
%     end
% end


%============================     mean error     ==========================

%mean square error
SE = zeros(48,504);
SE(:,1) = MEAN(:,1);
SE(:,2:504) = (MEAN(:,2:504) - ACT(:,2:504)).^2;

MSE = zeros(503,1);
for i=1:503
    MSE(i,1)= mean(SE(:,i+1));
end
%plotting the mean square error
clf
plot(MSE)
xlabel('Customer ID')
ylabel('Mean Square Error')
xlim([0 504])
filename = 'mse_means.png';
saveas(gcf,filename)

clf
plot(sort(MSE,'descend'))
xlabel('Household')
ylabel('Mean square Error (ordered)');
xlim([0 504])
filename = 'mse_sorted.png';
saveas(gcf,filename)

%mean error (power of 4)

SE4 = zeros(48,504);
SE4(:,1) = MEAN(:,1);
SE4(:,2:504) = (MEAN(:,2:504) - ACT(:,2:504)).^4;

MSE4 = zeros(503,1);
for i=1:503
    MSE4(i,1)= mean(SE4(:,i+1));
end
%plotting the mean square error
clf
plot(MSE4)
xlabel('Customer ID')
ylabel('Mean Quartic Error')
xlim([0 504])
filename = 'mse_fourth_power.png';
saveas(gcf,filename)

clf
plot(sort(MSE4,'descend'))
xlabel('Household')
ylabel('Mean Quartic Error (ordered)');
xlim([0 504])
filename = '4mse_sorted.png';
saveas(gcf,filename)

%relative error
RE = zeros(48,504);
RE(:,1) = 1:48;
RE(:,2:504) = ((MEAN(:,2:504) - ACT(:,2:504)).^2)./ACT(:,2:504);

MRE = zeros(503,1);
for i = 1:503
    MRE(i,1) = mean(RE(:,i+1));
end
%plotting relative error
clf
plot(MRE)
xlim([0 504])
xlabel('Customer ID')
ylabel('Relative Mean Square Error')
filename = 'rel_mse.png';
saveas(gcf,filename)

%plotting sorted relative error
clf
plot(sort(MRE,'descend'))
xlim([0 504])
xlabel('Customer ID')
ylabel('Relative Mean Square Error')
filename = 'rel_mse_sorted.png';
saveas(gcf,filename)



%==================      Prediction based on weighted mean     ===============

%mean of weeks 16,17
weeks16_17 = DATA((DATA(:,1)==16 | DATA(:,1)==17),:);
[~,n] = size(weeks16_17);
[a,~,c]= unique(weeks16_17(:,3));
WMean16_17 = zeros(48,504);
WMean16_17(:,1) = a;
for p=5:n
    out = [a,accumarray(c,weeks16_17(:,p),size(a),@mean)];
    WMean16_17(:,p-5+2) = out(:,2);
end

%mean of weeks 18,19
weeks18_19 = DATA((DATA(:,1)==18 | DATA(:,1)==19),:);
[~,n] = size(weeks18_19);
[a,~,c]= unique(weeks18_19(:,3));
WMean18_19 = zeros(48,504);
WMean18_19(:,1) = a;
for p=5:n
    out = [a,accumarray(c,weeks18_19(:,p),size(a),@mean)];
    WMean18_19(:,p-5+2) = out(:,2);
end

%mean of weeks 20,21
weeks20_21 = DATA((DATA(:,1)==20 | DATA(:,1)==21),:);
[~,n] = size(weeks20_21);
[a,~,c]= unique(weeks20_21(:,3));
WMean20_21 = zeros(48,504);
WMean20_21(:,1) = a;
for p=5:n
    out = [a,accumarray(c,weeks20_21(:,p),size(a),@mean)];
    WMean20_21(:,p-5+2) = out(:,2);
end

WMEAN = [a,(0.5*WMean16_17(:,2:end)+WMean18_19(:,2:end)+1.5*WMean20_21(:,2:end))./3];

WSE = zeros(48,504);
WSE(:,1) = WMEAN(:,1);
WSE(:,2:504) = (WMEAN(:,2:504) - ACT(:,2:504)).^2;

WMSE = zeros(503,1);
for i=1:503
    WMSE(i,1)= mean(WSE(:,i+1));
end


%==================     Plotting MSE of the weighted prediction and non-weighted prediction     ===============

clf
plot(MSE)
hold on
plot(WMSE)
xlim([0 504])
hold off
xlabel('Household')
ylabel('Mean Square Error')
filename = '(w)mse_errors.png';
saveas(gcf,filename)


%==================      histogram     ===============

%doing a histogram plot (for whole data)
data_mat = DATA(:,5:end);
data_vec = data_mat(:);

clf
nbins = 500;
hist(data_vec,nbins)
xlabel('Instantaneous Energy Usage per household')
ylabel('Number of time recorded')
filename = 'usage_histogram.png';
saveas(gcf,filename)

% third quartile
sort_data_vec = sort(data_vec);
L = length(sort_data_vec)/4;

third_quartile = sort_data_vec(1:3*L);
clf
hist(third_quartile, nbins)
xlabel('Electricity Usage');
ylabel('Occurences');
filename = 'third_quartile_hist.png';
saveas(gcf,filename)

%calculate the median and median
fprintf('median=%0f', median(sort_data_vec))
fprintf('\n')
fprintf('mode=%0f', mode(sort_data_vec))
fprintf('\n')


%=======================            QQ plot           =====================
%use exponential distribution for the moment.
clf
pd = makedist('exponential');
qqplot(data_vec,pd) % matlab version
filename = 'qq_plot_matlab.png';
saveas(gcf,filename)

%my version
% sort_data_vec = sort(data_vec);
% n = length(sort_data_vec);
% p_val = (1:n)./n;
% std_exp_quant = -log(1-p_val);
% clf
% plot(std_exp_quant,sort_data_vec)
% ylabel('Ordered Electricity usage')
% xlabel('standard exponential distribution quantile')
% filename = 'QQ_plot_from_scratch.png';
% saveas(gcf,filename)

% piecewise QQ plot

%=======================            Auto-correlation           =====================
[~,n] = size(DATA);
[a,~,c] = unique(DATA(:,2));
SDU = zeros(length(a),504);
SDU(:,1) = a;
for p=5:n
   out = [a, accumarray(c,DATA(:,p),size(a),@sum)];
   SDU(:, p-5+2) = out(:,2);
end


SDUWD1 = SDU(1:7:49,:);
SDUWD2 = SDU(2:7:49,:);
SDUWD3 = SDU(3:7:49,:);
SDUWD4 = SDU(4:7:49,:);
SDUWD5 = SDU(5:7:49,:);
SDUWD6 = SDU(6:7:49,:);
SDUWD7 = SDU(7:7:49,:);

SDUWD1_this = SDUWD1(:,2:end);
SDUWD1_last = SDUWD1(:,1:end-1);
SDUWD2_this = SDUWD2(:,2:end);
SDUWD2_last = SDUWD2(:,1:end-1);
SDUWD3_this = SDUWD3(:,2:end);
SDUWD3_last = SDUWD3(:,1:end-1);
SDUWD4_this = SDUWD4(:,2:end);
SDUWD4_last = SDUWD4(:,1:end-1);
SDUWD5_this = SDUWD5(:,2:end);
SDUWD5_last = SDUWD5(:,1:end-1);
SDUWD6_this = SDUWD6(:,2:end);
SDUWD6_last = SDUWD6(:,1:end-1);
SDUWD7_this = SDUWD7(:,2:end);
SDUWD7_last = SDUWD7(:,1:end-1);

[~,n] = size(DATA);
[a,~,c] = unique(DATA(:,2));
MDU = zeros(length(a),504);
MDU(:,1) = a;
for p=5:n
   out = [a, accumarray(c,DATA(:,p),size(a),@mean)];
   MDU(:, p-5+2) = out(:,2);
end

today = MDU(2:end,:);
yesterday = MDU(1:end -1, :);

%==================      Correlating Data and Errors     ===============
good_hombres = MDU(:,MSE4<=0.001);
bad_hombres = MDU(:,MSE4>0.001);

good_today = good_hombres(2:end,:);
good_yesterday = good_hombres(1:end-1,:);

plot(today(:,2:end),yesterday(:,2:end),'g.')
hold on
plot(good_today(:,2:end),good_yesterday(:,2:end),'b.')

clf
plot(today(:,2:end),yesterday(:,2:end),'.')
xlabel('Daily Mean Usage at time t')
ylabel('Daily Mean Usage at time t-1')
filename = 'mean_all_autocorr.png';
saveas(gcf,filename)
clf

MDUWD1 = MDU(1:7:49,:);
MDUWD2 = MDU(2:7:49,:);
MDUWD3 = MDU(3:7:49,:);
MDUWD4 = MDU(4:7:49,:);
MDUWD5 = MDU(5:7:49,:);
MDUWD6 = MDU(6:7:49,:);
MDUWD7 = MDU(7:7:49,:);

MDUWD1_this = MDUWD1(:,2:end);
MDUWD1_last = MDUWD1(:,1:end-1);
MDUWD2_this = MDUWD2(:,2:end);
MDUWD2_last = MDUWD2(:,1:end-1);
MDUWD3_this = MDUWD3(:,2:end);
MDUWD3_last = MDUWD3(:,1:end-1);
MDUWD4_this = MDUWD4(:,2:end);
MDUWD4_last = MDUWD4(:,1:end-1);
MDUWD5_this = MDUWD5(:,2:end);
MDUWD5_last = MDUWD5(:,1:end-1);
MDUWD6_this = MDUWD6(:,2:end);
MDUWD6_last = MDUWD6(:,1:end-1);
MDUWD7_this = MDUWD7(:,2:end);
MDUWD7_last = MDUWD7(:,1:end-1);

clf
subplot(7,2,1)
plot(SDUWD1_this(:,2:end),SDUWD1_last(:,2:end),'.')

subplot(7,2,2)
plot(MDUWD1_this(:,2:end),MDUWD1_last(:,2:end),'.')

subplot(7,2,3)
plot(SDUWD2_this(:,2:end),SDUWD2_last(:,2:end),'.')

subplot(7,2,4)
plot(MDUWD2_this(:,2:end),MDUWD2_last(:,2:end),'.')

subplot(7,2,5)
plot(SDUWD3_this(:,2:end),SDUWD3_last(:,2:end),'.')

subplot(7,2,6)
plot(MDUWD3_this(:,2:end),MDUWD3_last(:,2:end),'.')

subplot(7,2,7)
plot(SDUWD4_this(:,2:end),DUWD4_last(:,2:end),'.')
ylabel('Sum and Mean Daily Usgae on day d of week t-1')

subplot(7,2,8)
plot(MDUWD4_this(:,2:end),MDUWD4_last(:,2:end),'.')
ylabel('Mean Daily Usage on day d of week t-1')

subplot(7,2,9)
plot(SDUWD5_this(:,2:end),SDUWD5_last(:,2:end),'.')

subplot(7,2,10)
plot(MDUWD5_this(:,2:end),MDUWD5_last(:,2:end),'.')

subplot(7,2,11)
plot(SDUWD6_this(:,2:end),SDUWD6_last(:,2:end),'.')

subplot(7,2,12)
plot(MDUWD6_this(:,2:end),MDUWD6_last(:,2:end),'.')

subplot(7,2,13)
plot(SDUWD7_this(:,2:end),SDUWD7_last(:,2:end),'.')
xlabel('Sum of daily usage on day d of week t')

subplot(7,2,14)
plot(MDUWD7_this(:,2:end),MDUWD7_last(:,2:end),'.')
xlabel('Mean daily usage on day d of week t')

filename = 'autocorr_subplots.png';
saveas(gcf,filename)

