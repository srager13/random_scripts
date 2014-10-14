clear all;
clc;

values_2 = csvread( 'scatter_plot_data.csv' );
x = 1:size(values_2,2);

%grid on;
%grid minor;
hold on;
axis([0 size(values_2,2) 0 size(values_2,1)])
for i=1:size(values_2,1)
    y1 = values_2(i,:) ~= 0;
    scatter( x(y1), values_2(i,y1)*i, 'MarkerEdgeColor',[0 .5 .5],'MarkerFaceColor',[0 .7 .7],'LineWidth',0.5 );
end

set(gca,'YTick', 0:10:150);
set(gca,'YGrid','on')

saveas(gcf,'scatter_plot_fig.pdf');