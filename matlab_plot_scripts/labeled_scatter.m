clear all;
clc;

values_3 = csvread( 'labeled_scatter_data.csv' );
x = 1:size(values_3,2);

hold on;
axis([0.25 size(values_3,2)+0.5 0.5 size(values_3,1)+0.5])
for i=1:size(values_3,1)
        y = ones(1,size(values_3,2))*i;
        %scatter( x, y, 800, 'MarkerEdgeColor','k', 'LineWidth',0.5, 'MarkerFaceColor', [211/255,211/255,211/255]);
    for j=1:size(values_3,2)
        scatter( j, i, 300 + values_3(i,j)*5, 'MarkerEdgeColor','k', 'LineWidth',0.5, 'MarkerFaceColor', [211/255,211/255,211/255]);
        if( values_3(i,j) > 99 )
            text(j-0.17,i,num2str(values_3(i,j)));
        else if( values_3(i,j) > 10 )
            text(j-0.14,i,num2str(values_3(i,j)));
        else
            text(j-0.05,i,num2str(values_3(i,j)));
        end
        end
    end
end

a=findobj(gcf);
alltext=findall(a,'Type','text');
set( alltext, 'FontWeight', 'bold' );

saveas(gcf,'labeled_scatter_fig_2.pdf');