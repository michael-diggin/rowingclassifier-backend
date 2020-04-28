const api_url = 'http://127.0.0.1:5000/v1/predict'

$(function() {
  $('#upload-image-btn').click(function() {
      
      var form_data = new FormData($('#upload-image')[0]);
      $.ajax({
          type: 'POST',
          url: api_url,
          dataType: 'json',
          data: form_data,
          contentType: false,
          cache: false,
          processData: false,
          success: function(response) {
              $('#msg').html('');
              $.each(response, function (key, data) {
                  $('#msg').append(`${key} : ${data}<br/>`);
              })
              img_path = response.path;
              console.log(img_path);
              $('#img-name').attr('src', img_path);
              
          },
          error: function(response) {
              $('#msg').html(response.message);
          }
      });
  });
});
