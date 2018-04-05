Mock.mock(/\.json/, {    //匹配.json文件，可执行匹配成功的参数
  'list|1-10': [{      //数据模板
         'id|+1': 1,
         'email': '@EMAIL',
         'regexp3': /\d{5,10}/
     }]
 });

function sendData(url) {
    $.ajax({
         url: url,
         dataType: 'json'
     }).done(function(data, status, jqXHR) {
         //获得mock数据模板中的数据，打印到body上
         $('<pre>').text(JSON.stringify(data, null, 4)).appendTo('body');
     })
}
sendData("hello.json");