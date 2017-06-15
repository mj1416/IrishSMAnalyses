function output_mat = forecast1(input_mat)
% this function takes the matrix input_mat
% and gives a daily forcast that uses the 
% unweighted mean for each HH using all past
% data.some assumtion about input_mat include
% that the first column is week number, the
% second column is day number, the third is
% HH number and the fourth is day of the 
% week given from 1 to 7.
[~,n] = size(input_mat);
[a,~,c]= unique(input_mat(:,3));
output_mat = zeros(48,n-3);
output_mat(:,1) = a;
for p=5:n
    out = [a,accumarray(c,input_mat(:,p),size(a),@mean)];
    output_mat(:,p-5+2) = out(:,2);
end
end