console.log("ㅎㅇㅎㅇ");

function order() {
        let data = {
            "order-name" : $("#order-name").val(),
            "order-count": $("#order-count").val(),
            "order-address": $("#order-address").val(),
            "order-phone" : $("#order-phone").val()
         }
        console.log(data);

        $.ajax({
          type: "POST",
          url: "/order",
          data: { name_give: data["order-name"],
                  count_give: data["order-count"],
                  address_give: data["order-address"],
                  phone_give: data["order-phone"]
                 },
          success: function(response){ // 성공하면
            if (response['result'] == 'success') {
              alert('주문 성공!');
              window.location.reload(true);
            } else {
              alert('서버 오류!')
            }
          }
        })
      }