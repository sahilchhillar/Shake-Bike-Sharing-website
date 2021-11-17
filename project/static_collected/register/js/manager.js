
(function () {
    $('.table .top').on('click', 'a', function () {
        $(this).addClass('active').siblings("a").removeClass("active");
        $(".table .box").eq($(this).index()).show().siblings(".box").hide();
    });
})();
(function(){
    var mychart = echarts.init(document.querySelector('.line'));

    var option = {
        tooltip: {
            trigger: 'axis',
        },
        toolbox: {
            feature: {
                dataView: { show: true, readOnly: true },
                magicType: { show: true, type: ['line', 'bar'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        legend: {},
        xAxis: [
            {
                type: 'category',
                data: ['location1', 'location2', 'location3', 'location4', 'location5'],
                axisPointer: {
                    type: 'shadow'
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: 'money',
                min: 0,
                max: 50,
                axisLabel: {
                    formatter: '{value}'
                }
            },
        ],
        series: [
            {
                name: 'location',
                type: 'bar',
                data: [
                    2.0, 4.9, 7.0, 23.2, 25
                ]
            },
        ]
    };
    mychart.setOption(option);
})();
(function(){
    var mychart = echarts.init(document.querySelector('.pie'));

    var option = {
        title: {
          text: 'Referer of a Website',
          subtext: 'Fake Data',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: 1048, name: 'Search Engine' },
              { value: 735, name: 'Direct' },
              { value: 580, name: 'Email' },
              { value: 484, name: 'Union Ads' },
              { value: 300, name: 'Video Ads' }
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
    mychart.setOption(option);
})();