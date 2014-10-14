clear all;
clc;

values_1 = csvread( '3dplot.csv' );
val_1 = fliplr(values_1);
val_2 = transpose(values_1);

%bar3( val_1, 5 );
%bar3(0:10:90, val_2);
%bar3(val_2);
%bar3( 5:5:50, val_2, 0.55 );
%daspect( [150, 100, 100] );
%axis([0 10 0 150 0 75]);

%saveas(gcf,'three_d_plot_fig.pdf');

averages = zeros(1,10);
err = zeros(1,10);
for i=1:10
    averages(i) = mean( val_1(:,i) );
    err(i) = std( val_1(:,i) );
end

barwitherr(err, averages, 'FaceColor', [211/255,211/255,211/255]);

saveas(gcf,'avg_locations_fig.pdf');