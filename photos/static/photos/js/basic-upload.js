// csrf setup for ajax post, put, delete request
$(function() {
  $.ajaxSetup({
      headers: {
        "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
      }
  })
});

// upload file
$(function () {
  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    done: function (e, data) {
      if (data.result.is_valid) {
        $("#gallery tbody").prepend(
          `<tr>
            <td><a href="${data.result.url}">${data.result.name}</a></td>
            <td><a class="delete_file" href="/photos/delete_file/${data.result.id}/">删除</a></td>
          </tr>`
        )
      }
    }
  });

  // Delete File
  $('#gallery').on('click', '.delete_file', function (e) {
    e.preventDefault();
    var url = $(this).attr('href');
    var that = this;
    $.ajax({
      url: url,
      type: 'DELETE',
      success: function (data) {
        if (data.status) {
          $(that).parent().parent().fadeOut();
        }
      }
    });
  });

});
