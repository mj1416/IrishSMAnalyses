function [output1,output2] = outlier1(DATA)
% This function gives us the household that can be considered outliers, output1, 
% and those that aren't, output2. The
% houses which are considered outliers are those who have have total usage
% that is larger than the 70th percentile on at at least 20 days.

ncust = length(DATA(1,:)) - 4;
[~,n] = size(DATA);
[a,~,c] = unique(DATA(:,2));
SDU = zeros(length(a),ncust+1);
SDU(:,1) = a;
for p=5:n
   out = [a, accumarray(c,DATA(:,p),size(a),@sum)];
   SDU(:, p-5+2) = out(:,2);
end


temp = SDU(:,2:end);
sum_vec = temp(:);

sum_threshold = prctile(sum_vec,70);
exceedances = sum(SDU(:,2:end)>sum_threshold);
households = 1:ncust;

output1 = households(exceedances>20);
output2 = households(exceedances<=20);
end