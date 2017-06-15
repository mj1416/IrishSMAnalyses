%==================        Set Directiory        ===============
cd('/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/')

%==================      Read and clean data     ===============
filename='/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx';
sheet = 2;
xlrange = 'A:UA';
DATA = xlsread(filename,sheet,xlrange);

[r,c] = find(isnan(DATA));
DATA(:,c) = []; %now data is complete


%==================         Day Profiles        ===============
Day1 = DATA(DATA(:,4)==1,:);
Day2 = DATA(DATA(:,4)==2,:);
Day3 = DATA(DATA(:,4)==3,:);
Day4 = DATA(DATA(:,4)==4,:);
Day5 = DATA(DATA(:,4)==5,:);
Day6 = DATA(DATA(:,4)==6,:);
Day7 = DATA(DATA(:,4)==7,:);

days_tot = zeros(48,7);
days_mean = zeros(48,7);
for p=1:48
    HH = p:48:336;
    days_mean(p,1) = mean(mean(Day1(HH,5:end)));
    days_mean(p,2) = mean(mean(Day2(HH,5:end)));
    days_mean(p,3) = mean(mean(Day3(HH,5:end)));
    days_mean(p,4) = mean(mean(Day4(HH,5:end)));
    days_mean(p,5) = mean(mean(Day5(HH,5:end)));
    days_mean(p,6) = mean(mean(Day6(HH,5:end)));
    days_mean(p,7) = mean(mean(Day7(HH,5:end)));
end

for p=1:48
    HH = p:48:336;
    days_tot(p,1) = sum(mean(Day1(HH,5:end)));
    days_tot(p,2) = sum(mean(Day2(HH,5:end)));
    days_tot(p,3) = sum(mean(Day3(HH,5:end)));
    days_tot(p,4) = sum(mean(Day4(HH,5:end)));
    days_tot(p,5) = sum(mean(Day5(HH,5:end)));
    days_tot(p,6) = sum(mean(Day6(HH,5:end)));
    days_tot(p,7) = sum(mean(Day7(HH,5:end)));
end

%==================             mean               ===============

plot(1:48,days_mean(:,1),'Color',[0,0,1],'LineWidth',2)
hold on
plot(1:48,days_mean(:,2),'Color',[1,0,0],'LineWidth',2)
plot(1:48,days_mean(:,3),'Color',[1,215/255.0,0],'LineWidth',2)
plot(1:48,days_mean(:,4),'Color',[128/255.0,0,128/250.0],'LineWidth',2)
plot(1:48,days_mean(:,5),'Color',[50/255.0,205/255.0,50/255.0],'LineWidth',2)
plot(1:48,days_mean(:,6),'Color',[1,0,1],'LineWidth',2)
plot(1:48,days_mean(:,7),'Color',[128/255.0,0,0],'LineWidth',2)

set(gca,'FontSize',12)
xticks([1 7 13 19 25 31 37 43 48])
xticklabels({'00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','23:30'})
xlabel('Time of Day','FontSize',14)
ylabel('Mean Electricity Consumption (kWh)','FontSize',14)
legend('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Location','NorthWest')
hold off
filename = 'days_mean.png';
saveas(gcf,filename)
%==================         sums        ===============
clf
plot(1:48,days_tot(:,1),'Color',[0,0,1],'LineWidth',2)
hold on
plot(1:48,days_tot(:,2),'Color',[1,0,0],'LineWidth',2)
plot(1:48,days_tot(:,3),'Color',[1,215/255.0,0],'LineWidth',2)
plot(1:48,days_tot(:,4),'Color',[128/255.0,0,128/250.0],'LineWidth',2)
plot(1:48,days_tot(:,5),'Color',[0,128/255.0,0],'LineWidth',2)
plot(1:48,days_tot(:,6),'Color',[1,0,1],'LineWidth',2)
plot(1:48,days_tot(:,7),'Color',[128/255.0,0,0],'LineWidth',2)

set(gca,'FontSize',12)
xticks([1 7 13 19 25 31 37 43 48])
xticklabels({'00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','23:30'})
xlabel('Time of Day','FontSize',14)
ylabel('Total Electricity Consumption (kWh)','FontSize',14)
legend('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Location','NorthWest')
hold off
filename = 'days_sum.png';
saveas(gcf,filename)

