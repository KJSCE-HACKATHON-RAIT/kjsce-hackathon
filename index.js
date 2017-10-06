function stock_sub() {
        
        var form_data = new FormData();
        form_data.append('vote_name',document.getElementById('vote_name').value);
            
        setTimeout(function() {

                $.ajax({
                   type: "POST",
                   url: "http://localhost:8888/stock",
                   data: form_data,
                   cache: false,
                   contentType: false,
                   processData: false,
                   dataType: 'json',
                   success: function (response) {
                       console.log(response);
                       create_chart(response);
                   },
                   error: function (response) {
                   }
                });
                
            },0); 
}

