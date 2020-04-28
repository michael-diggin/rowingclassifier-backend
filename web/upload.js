const api_url = 'http://127.0.0.1:5000/v1/predict'

$(function() {
  $('#upload-file-btn').click(function() {
      var form_data = new FormData($('#upload-file')[0]);
      $.ajax({
          type: 'POST',
          url: api_url,
          data: form_data,
          contentType: false,
          cache: false,
          processData: false,
          success: function(data) {
              console.log('Success!');
          },
      });
  });
});