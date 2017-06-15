%==================        Set Directiory        ===============
cd('/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/')

%==================      Read and clean data     ===============
filename='/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx';
sheet = 2;
xlrange = 'A:UA';
DATA = xlsread(filename,sheet,xlrange);

[r,c] = find(isnan(DATA));
DATA(:,c) = []; %now data is complete

ncust = length(DATA(1,:)) - 4;

%==================      Percentiles Plots       ===============
% data_mat = DATA(:,5:end);
% Y_97 = prctile(data_mat,97);
% 
% plot(Y_97)
% xlim([0 504])
% xlabel('Customers')
% ylabel('97th Percentile')
% filename = 'percentile_97.pdf';
% saveas(gcf,filename);
% 
% clf
% Y_50 = prctile(data_mat,50);
% plot(Y_50)
% xlim([0 504])
% xlabel('Customers')
% ylabel('50th Percentile')
% filename = 'percentile_50.pdf';
% saveas(gcf,filename);
% 
% clf
% MAX = max(data_mat);
% plot(MAX)
% xlim([0 504])
% xlabel('Customers')
% ylabel('Household maximum')
% filename = 'household_max.pdf';
% saveas(gcf,filename);
% 

%==================        Finding Outliers        ===============
%==================        mean daily usage        ===============

[~,n] = size(DATA);
[a,~,c] = unique(DATA(:,2));
MDU = zeros(length(a),ncust+1);
MDU(:,1) = a;
for p=5:n
   out = [a, accumarray(c,DATA(:,p),size(a),@mean)];
   MDU(:, p-5+2) = out(:,2);
end

%==================        total daily usage       ===============

[~,n] = size(DATA);
[a,~,c] = unique(DATA(:,2));
SDU = zeros(length(a),ncust+1);
SDU(:,1) = a;
for p=5:n
   out = [a, accumarray(c,DATA(:,p),size(a),@sum)];
   SDU(:, p-5+2) = out(:,2);
end

%==================        define outliers          ===============
temp = SDU(:,2:end);
sum_vec = temp(:);

%temp = MDU(:,2:end);
%mean_vec = temp(:);

sum_threshold = prctile(sum_vec,70);
%mean_threshold = prctile(mean_vec,70);

exceedances = sum(SDU(:,2:end)>sum_threshold);
households = 1:ncust;

weird = households(exceedances>20);

outlier_housholds = SDU(:,weird);

normal = households(exceedances<=20);
normal_household = SDU(:,normal);
