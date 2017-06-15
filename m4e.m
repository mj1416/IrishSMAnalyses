function output = m4e(forecast,observation)
% m4e calculates the mean quartic root error between the observations and
% the forecast, which are matrices.

output = (sum((forecast - observation).^4)).^0.25;

end