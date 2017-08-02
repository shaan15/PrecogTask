// Create the chart
$( document ).ready(function() {
    Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Location wise tweets'
    },
    
    xAxis: {
        type: 'Locations'
    },
    yAxis: {
        title: {
            text: 'Number of Tweets'
        }

    },
    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.1f}%'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
    },

    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'India',
            y: 56.33,
            drilldown: 'India'
        }, {
            name: 'US',
            y: 24.03,
            drilldown: 'US'
        }, {
            name: 'UK',
            y: 10.38,
            drilldown: 'UK'
        }, {
            name: 'UAE',
            y: 4.77,
            drilldown: 'UAE'
        }, {
            name: 'Saudi Arabia',
            y: 0.91,
            drilldown: 'Saudi Arabia'
        }, {
            name: 'Australia',
            y: 0.2,
            drilldown: 'Australia'
        },
         {
            name: 'Others',
            y: 0.1,
            drilldown: null
        }]
    }],
    drilldown: {
        series: [{
            name: 'India',
            id: 'India',
            
            
        }, {
            name: 'US',
            id: 'US',
            
                
        }, {
            name: 'UK',
            id: 'UK',
           
        }, {
            name: 'UAE',
            id: 'UAE',
            
        }, {
            name: 'Saudi Arabia',
            id: 'Saudi Arabia',
            
        },
        {
            name: 'Australia',
            id: 'Australia',
            
        }]
    }
});
    });