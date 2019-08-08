console.log("ㅎㅇ");

window.onload=function() {
      get_orders();
}
 function get_orders() {
      $('#orders-box').empty('');

      $.ajax({
        type: "GET",
        url: "/order",
        data: {},
        success: function(response) {
          let orders = response['orders'];
          console.log(orders)
          for (let i = 0 ; i < orders.length ; i++) {
            let name = orders[i]['name'];
            let address = orders[i]['address'];
            let phone = orders[i]['phone'];
            let count = orders[i]['count'];

            make_table(name,address,phone,count);
          }
        }
      })
 }
 function make_table(name,address,phone,count) {
      let temp_html = '<tr>\
          <td>'+name+'</td>\
          <td>'+count+'</td>\
          <td>'+address+'</td>\
          <td>'+phone+'</td>\
        </tr>';
      $('#orders-box').append(temp_html);
 }
