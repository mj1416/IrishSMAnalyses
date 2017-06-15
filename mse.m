function output = mse(forecast,observation)
% mse calculates the mean square root error between the observations and
% the forecast, which are matrices.

output = sqrt(sum((forecast - observation).^2));

end