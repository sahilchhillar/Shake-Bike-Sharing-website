
(function () {
    $('.table .top').on('click', 'a', function () {
        $(this).addClass('active').siblings("a").removeClass("active");
        $(".table .box").eq($(this).index()).show().siblings(".box").hide();
    });
})();
(function(){
    var mychart = echarts.init(document.querySelector('.start'));

    var option = {
        tooltip: {
            trigger: 'axis',
        },
        toolbox: {
            feature: {
                dataView: { show: true, readOnly: true },
                magicType: { show: true, type: ['line', 'bar',] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        legend: {},
       

        xAxis: [
            {
                type: 'category',
                axisLabel: {
                  show: true,
                  interval:0,
                  rotate:20,
                  textStyle: {
                      color: '#333'
                  }
              },
                
                data: ['Glasgow School Of Art', 'University Of Glasgow', 'Buchanan Bus Station', 'Patrick Subway Station', 'Glasgow Botanic Gardens', 'University Of Strathclyde', 'Glasgow Central', 'Glasgow Cathedral', 'Glasgow Central Mosque'],
                axisPointer: {
                    type: 'shadow'
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: 'Number',
                min: 0,
                max: 50,
                axisLabel: {
                    formatter: '{value}'
                }
            },
        ],
        series: [
            {
                name: 'Rent Location',
                type: 'bar',
                data: [
                    2, 4, 7, 23, 25, 34, 45, 26, 12,
                ]
            },
        ]
    };
    mychart.setOption(option);
})();
(function(){
  var mychart = echarts.init(document.querySelector('.end'));

  var option = {
      tooltip: {
          trigger: 'axis',
      },
      toolbox: {
          feature: {
              dataView: { show: true, readOnly: true },
              magicType: { show: true, type: ['line', 'bar',] },
              restore: { show: true },
              saveAsImage: { show: true }
          }
      },
      legend: {},
     

      xAxis: [
          {
              type: 'category',
              axisLabel: {
                show: true,
                interval:0,
                rotate:20,
                textStyle: {
                    color: '#333'
                }
            },
              
              data: ['Glasgow School Of Art', 'University Of Glasgow', 'Buchanan Bus Station', 'Patrick Subway Station', 'Glasgow Botanic Gardens', 'University Of Strathclyde', 'Glasgow Central', 'Glasgow Cathedral', 'Glasgow Central Mosque'],
              axisPointer: {
                  type: 'shadow'
              }
          }
      ],
      yAxis: [
          {
              type: 'value',
              name: 'Number',
              min: 0,
              max: 50,
              axisLabel: {
                  formatter: '{value}'
              }
          },
      ],
      series: [
          {
              name: 'Return Location',
              type: 'bar',
              data: [
                  34, 43, 4, 6, 15, 47, 1, 25, 9,
              ]
          },
      ]
  };
  mychart.setOption(option);
})();
(function(){
  var mychart = echarts.init(document.querySelector('.money'));

  var option = {
    title: {
      text: 'Money Chart',
      subtext: 'Rent Place',
      left: 'center'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b} : {c} ({d}%)'
    },
    legend: {
      top: 'bottom'
    },
    toolbox: {
      show: true,
      feature: {
        mark: { show: true },
        dataView: { show: true, readOnly: false },
        restore: { show: true },
        saveAsImage: { show: true }
      }
    },
    series: [
      {
        name: 'Money Chart',
        type: 'pie',
        radius: [50, 250],
        center: ['50%', '50%'],
        roseType: 'area',
        itemStyle: {
          borderRadius: 8
        },
        data: [
          { value: 40, name: 'Glasgow School Of Art' },
          { value: 38, name: 'University Of Glasgow' },
          { value: 32, name: 'Buchanan Bus Station' },
          { value: 30, name: 'Patrick Subway Station' },
          { value: 28, name: 'Glasgow Botanic Gardens' },
          { value: 26, name: 'University Of Strathclyde' },
          { value: 22, name: 'Glasgow Central' },
          { value: 22, name: 'Glasgow Cathedral' },
          { value: 18, name: 'Glasgow Central Mosque' }
        ]
      }
    ]
  };
  mychart.setOption(option);
})();