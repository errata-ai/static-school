var ssgOptions = {
    credits: false,
    chart: {
        type: 'column',
        scrollablePlotArea: {
            minWidth: 576,
            scrollPositionX: 1
        }
    },
    title: {
        text: 'Build Time by Format (3-run average)'
    },
    subtitle: {
        text: versionInfo
    },
    xAxis: {
        categories: [
            '10 files',
            '100 files',
            '1,000 files'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Build Time (seconds)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b> {point.y:.1f} s</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: seriesData1
};

function getOptions(format) {
    return {
        credits: false,
        title: {
            text: 'Build Time by Generator'
        },

        subtitle: {
            text: format
        },

        yAxis: {
            title: {
                text: 'Build Time (seconds)'
            }
        },

        xAxis: {
            categories: [
                '10 files',
                '100 files',
                '1,000 files'
            ],
            crosshair: true
        },

        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },

        responsive: {
            rules: [{
                condition: {
                    maxWidth: 576
                },
                chartOptions: {
                    legend: {
                        align: 'center',
                        verticalAlign: 'bottom',
                        layout: 'horizontal'
                    }
                }
            }]
        },

        chart: {
            scrollablePlotArea: {
                minWidth: 576,
                scrollPositionX: 1
            }
        },

        series: formatData[format]
    };
}

var ssgChart = Highcharts.chart('benchmark-formats', ssgOptions);
var formatChart = Highcharts.chart('Markdown', getOptions('Markdown'));

$('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
    var selText = $(this).text();
    if (selText !== 'By Format') {
        formatChart.destroy();
        formatChart = Highcharts.chart(selText, getOptions(selText));
    } else {
        ssgChart.destroy();
        ssgChart = Highcharts.chart('benchmark-formats', ssgOptions);
    }
});
