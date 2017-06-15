function output_mat = forecast2(input_mat)
% This forecast will give the same day forecast using unweighted mean i.e.
% for the coming Thursday, the mean, at each HH, of all past Thursday will
% be calculated and stored.

% The struction of the input matrix, input_mat, is taken to be: 
% Week Number   |   Day number |    HH    |     Day of the Week     | Customer 1 ...
D = unique(input_mat(:,4));
past = input_mat(input_mat(:,4)==D(1),:);
[~,n] = size(past);
[a,~,c]= unique(past(:,3)); %gives you the half hours
day1 = zeros(48,n-2);
day1(:,1) = a;
day1(:,2) = 1;
for p=5:n
    out = [a,accumarray(c,past(:,p),size(a),@mean)];
    day1(:,p-5+3) = out(:,2);
end

past = input_mat(input_mat(:,4)==D(2),:);
[~,n] = size(past);
[a,~,c]= unique(past(:,3)); %gives you the half hours
day2 = zeros(48,n-2);
day2(:,1) = a;
day2(:,2) = 2;
for p=5:n
    out = [a,accumarray(c,past(:,p),size(a),@mean)];
    day2(:,p-5+3) = out(:,2);
end


past = input_mat(input_mat(:,4)==D(3),:);
[~,n] = size(past);
[a,~,c]= unique(past(:,3)); %gives you the half hours
day3 = zeros(48,n-2);
day3(:,1) = a;
day3(:,2) = 3;
for p=5:n
    out = [a,accumarray(c,past(:,p),size(a),@mean)];
    day3(:,p-5+3) = out(:,2);
end


past = input_mat(input_mat(:,4)==D(4),:);
[~,n] = size(past);
[a,~,c]= unique(past(:,3)); %gives you the half hours
day4 = zeros(48,n-2);
day4(:,1) = a;
day4(:,2) = 4;
for p=5:n
    out = [a,accumarray(c,past(:,p),size(a),@mean)];
    day4(:,p-5+3) = out(:,2);
end


past = input_mat(input_mat(:,4)==D(5),:);
[~,n] = size(past);
[a,~,c]= unique(past(:,3)); %gives you the half hours
day5 = zeros(48,n-2);
day5(:,1) = a;
day5(:,2) = 5;
for p=5:n
    out = [a,accumarray(c,past(:,p),size(a),@mean)];
    day5(:,p-5+3) = out(:,2);
end


past = input_mat(input_mat(:,4)==D(6),:);
[~,n] = size(past);
[a,~,c]= unique(past(:,3)); %gives you the half hours
day6 = zeros(48,n-2);
day6(:,1) = a;
day6(:,2) = 6;
for p=5:n
    out = [a,accumarray(c,past(:,p),size(a),@mean)];
    day6(:,p-5+3) = out(:,2);
end

past = input_mat(input_mat(:,4)==D(7),:);
[~,n] = size(past);
[a,~,c]= unique(past(:,3)); %gives you the half hours
day7 = zeros(48,n-2);
day7(:,1) = a;
day7(:,2) = 7;
for p=5:n
    out = [a,accumarray(c,past(:,p),size(a),@mean)];
    day7(:,p-5+3) = out(:,2);
end

output_mat = [day1;day2;day3;day4;day5;day6;day7];
end