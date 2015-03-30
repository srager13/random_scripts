x = csvread('data_x.csv');
y1 = csvread('data_y1.csv');
y2 = csvread('data_y2.csv');

font_size = 20;

[hAx,hLine1,hLine2] = plotyy(x,y1,x,y2);

xlabel('User', 'FontSize', font_size);
hyL = ylabel(hAx(1), 'Prediction Accuracy per User (%)', 'FontSize', font_size);
hyL2 = ylabel(hAx(2), 'Amount of Data (Thousands of Data Entries)', 'FontSize', font_size);

hLine1.LineStyle = '--';
hLine1.Color = 'b';
hyL.Color = 'b';

hLine2.LineStyle = '-';
hLine2.Color = 'r';
hyL2.Color = 'r';
