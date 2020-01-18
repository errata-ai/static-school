if ($("#benchmark-formats").length) {
    Highcharts.chart('benchmark-formats', {
        exporting: {
            buttons: null,
        },
        credits: false,
        chart: {
            type: 'column'
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
    });
}

var formatOptions = [];
if (hasMd) {
    formatOptions.push({
        text: 'Markdown',
        onclick: function () {
            rebuildChart('Markdown')
        }
    });
}
if (hasAdoc) {
    formatOptions.push({
        text: 'AsciiDoc',
        onclick: function () {
            rebuildChart('AsciiDoc')
        }
    });
}
if (hasRst) {
    formatOptions.push({
        text: 'reStructuredText',
        onclick: function () {
            rebuildChart('reStructuredText')
        }
    });
}

var options = {
    credits: false,
    title: {
        text: 'Build Time by Generator'
    },

    subtitle: {
        text: 'Markdown'
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

     exporting: {
         buttons: {
             contextButton: {
                 enabled: false
             },
             toggle: {
                 text: 'Format',
                 menuItems: formatOptions
             }
         }
     },

    series: md
};

function rebuildChart(format) {
    console.log(format);

    formatsChart.destroy();

    options.subtitle.text = format;
    options.series = formatData[format];

    formatsChart = new Highcharts.chart('benchmark-ssgs', options);
}

var formatsChart = Highcharts.chart('benchmark-ssgs', options);
$('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
  formatsChart.destroy();
  formatsChart = new Highcharts.chart('benchmark-ssgs', options);
});
