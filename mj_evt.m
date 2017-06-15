%==================        Set Directiory        ===============
cd('/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/')

%==================      Read and clean data     ===============
filename='/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx';
sheet = 2;
xlrange = 'A:UA';
DATA = xlsread(filename,sheet,xlrange);

[r,c] = find(isnan(DATA));
DATA(:,c) = []; %now data is complete

%==================      Order Data     ===============
data_mat = DATA(:,5:end);
data_vec = data_mat(:);
order_vec = sort(data_vec,'ascend');
threshold = unique(order_vec);

%==================      Mean Excess    ===============

me = threshold*0;

for t=1:length(threshold)
    me(t) = (sum(order_vec(order_vec>threshold(t)))/length(order_vec(order_vec>threshold(t)))) - threshold(t);   
end

k = threshold*0;
for t=1:length(threshold)
    k(t) = length(order_vec(order_vec>threshold(t)));   
end


plot(threshold,me,'k.')
ylim([0.35 1])

plot(k,me,'k.')
ylim([0.35 1])
xlim([0 100000])
%==================      max/sum ratio of weekly max     ===============
filename='/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/weekly_max.csv';
wm = csvread(filename);

wm_vec = wm(:);
sum_vec = wm_vec*0;
max_vec = wm_vec*0;
p = 10;
for i=1:length(wm_vec)
    sum_vec(i) = sum(wm_vec(1:i).^p);
    max_vec(i) = max(wm_vec(1:i).^p);
end
plot(max_vec./sum_vec)

%==================      max/sum ratio of exceedances     ===============