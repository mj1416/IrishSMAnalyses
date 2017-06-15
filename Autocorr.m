%==================      Read and clean data     ===============
filename='/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx';
sheet = 2;
xlrange = 'A:UA';
DATA = xlsread(filename,sheet,xlrange);

[r,c] = find(isnan(DATA));
DATA(:,c) = []; %now data is complete

%==================      Auto-correlation Plots     ===============
%==================             For sums            ===============

[~,n] = size(DATA);
[a,~,c] = unique(DATA(:,2));
SDU = zeros(length(a),504);
SDU(:,1) = a;
for p=5:n
   out = [a, accumarray(c,DATA(:,p),size(a),@sum)];
   SDU(:, p-5+2) = out(:,2);
end

present = SDU(8:end,:); %can also be present = SDU(8:end,:); %for same day
past = SDU(1:end-7,:); %can also be past = SDU(1:end-7,:); %for same day

plot(present(:,2:end),past(:,2:end),'.')
xlabel('Total Daily Usage at on day d');
ylabel('Total Daily Usage at on day d-7'); %change appropriately.

%==================                means            ===============
[~,n] = size(DATA);
[a,~,c] = unique(DATA(:,2));
MDU = zeros(length(a),504);
MDU(:,1) = a;
for p=5:n
   out = [a, accumarray(c,DATA(:,p),size(a),@mean)];
   MDU(:, p-5+2) = out(:,2);
end

present = MDU(8:end,:); %can also be present = SDU(8:end,:); %for same day
past = MDU(1:end-7,:); %can also be past = SDU(1:end-7,:); %for same day

plot(present(:,2:end),past(:,2:end),'.')
xlabel('Mean Daily Usage at on day d');
ylabel('Mean Daily Usage at on day d-7'); %change appropriately.
