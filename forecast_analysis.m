%==================        Set Directiory        ===============
cd('/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/')

%==================      Read and clean data     ===============
filename='/Users/mj1416/Documents/MPECDT/MRes/Danica/Irish SM data/16_22_weeks.xlsx';
sheet = 2;
xlrange = 'A:UA';
DATA = xlsread(filename,sheet,xlrange);

[r,c] = find(isnan(DATA));
DATA(:,c) = []; %now data is complete

%==================      Isolate past data       ===============
A = DATA(:,1)<22;
Weeks5 = DATA(A,:);

%==================      Forecast All Houses     ===============
FORECAST_ALL = forecast2(Weeks5);

%==================          Find outliers       ===============
[outliers,non_outliers]=outlier1(DATA);
outliers = outliers+4;
non_outliers = non_outliers+4;

%==================      Forecast outliers       ===============
[n,~]=size(Weeks5);
input = zeros(n,length(outliers)+4);
input(:,1:4) = Weeks5(:,1:4);
input(:,5:end) = Weeks5(:,outliers);
OUTLIERS = forecast2(input);


%==================      Forecast non_outliers       ===============
[n,~]=size(Weeks5);
input = zeros(n,length(non_outliers)+4);
input(:,1:4) = Weeks5(:,1:4);
input(:,5:end) = Weeks5(:,non_outliers);
NON_OUTLIERS = forecast2(input);

%==================          Observations            ===============
A = DATA(:,1)==22;
OBS = DATA(A,:);

OBS_ALL = FORECAST_ALL*0;
OBS_ALL(:,1:2) = FORECAST_ALL(:,1:2);
OBS_ALL(:,3:end) = OBS(:,5:end);

OBS_outliers = OUTLIERS*0;
OBS_outliers(:,1:2) = OUTLIERS(:,1:2);
OBS_outliers(:,3:end) = OBS(:,outliers);

OBS_non_outliers = NON_OUTLIERS*0;
OBS_non_outliers(:,1:2) = NON_OUTLIERS(:,1:2);
OBS_non_outliers(:,3:end) = OBS(:,non_outliers);

%==================             Errors               ===============
m4e_all = m4e(FORECAST_ALL(:,3:end),OBS_ALL(:,3:end));
m4e_outliers = m4e(OUTLIERS(:,3:end),OBS_outliers(:,3:end));
m4e_non_outliers = m4e(NON_OUTLIERS(:,3:end),OBS_non_outliers(:,3:end));

mse_all = mse(FORECAST_ALL(:,3:end),OBS_ALL(:,3:end));
mse_outliers = mse(OUTLIERS(:,3:end),OBS_outliers(:,3:end));
mse_non_outliers = mse(NON_OUTLIERS(:,3:end),OBS_non_outliers(:,3:end));

%==================   Error: Forecast then cluster   ===============
threshold = prctile(m4e_all,70);
outliers2 = find(m4e_all>threshold);
err_outliers2 = mean(m4e_all(outliers2));

non_outliers2 = find(m4e_all<=threshold);
err_non_outliers2 = mean(m4e_all(non_outliers2)); 

%==================           Forecast plot          ===============
subplot(7,1,1)
plot(FORECAST_ALL(1:48,1),FORECAST_ALL(1:48,3))
hold on
plot(OBS_ALL(1:48,1),OBS_ALL(1:48,3))
subplot(7,1,2)

plot(FORECAST_ALL(49:96,1),FORECAST_ALL(49:96,3))
hold on
plot(OBS_ALL(49:96,1),OBS_ALL(49:96,3))

subplot(7,1,3)
plot(FORECAST_ALL(97:144,1),FORECAST_ALL(97:144,3))
hold on
plot(OBS_ALL(97:144,1),OBS_ALL(97:144,3))

subplot(7,1,4)
plot(FORECAST_ALL(145:192,1),FORECAST_ALL(145:192,3))
hold on
plot(OBS_ALL(145:192,1),OBS_ALL(145:192,3))

subplot(7,1,5)
plot(FORECAST_ALL(193:240,1),FORECAST_ALL(193:240,3))
hold on
plot(OBS_ALL(193:240,1),OBS_ALL(193:240,3))

subplot(7,1,6)
plot(FORECAST_ALL(241:288,1),FORECAST_ALL(241:288,3))
hold on
plot(OBS_ALL(241:288,1),OBS_ALL(241:288,3))

subplot(7,1,7)
plot(FORECAST_ALL(289:336,1),FORECAST_ALL(289:336,3))
hold on
plot(OBS_ALL(289:336,1),OBS_ALL(289:336,3))
