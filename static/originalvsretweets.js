$( document ).ready(function() {
    Highcharts.chart('container', {
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Original Tweets vs Retweeted tweets'
    },
    plotOptions: {
        series: {
            dataLabels: {
                enabled: true,
                format: '{point.name}: {point.y:.1f}%'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
    },
    series: [{
        name: 'Tweets',
        colorByPoint: true,
        data: [{
            name: 'Retweeted Tweets',
            y: 59.3,
            drilldown: 'Retweeted Tweets'
        }, {
            name: 'Original Tweets',
            y: 40.7,
            drilldown: 'Original Tweets'
        }]
    }],
    drilldown: {
        series: [{
            name: 'Retweeted Tweets',
            id: 'Retweeted tweets',
            
        }, {
            name: 'Original Tweets',
            id: 'Original tweets',
            
        }]
    }
});
});
