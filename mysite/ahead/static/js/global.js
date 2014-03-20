jQuery(function ($) {

    // modal checkbox
    $('#sync-private').iCheck({
      labelHover: false,
      cursor: true,
      checkboxClass: 'icheckbox_square-blue',
    });
    $('#sync-weibo').iCheck({
      labelHover: false,
      cursor: true,
      checkboxClass: 'icheckbox_square-blue',
    });
    $('#sync-private').on('ifChecked', function(event){
        $('#sync-weibo').iCheck('uncheck');
        $('#sync-weibo').iCheck('disable');
    });
    $('#sync-private').on('ifUnchecked', function(event){
        $('#sync-weibo').iCheck('enable');
        $('#sync-weibo').iCheck('check');
    });
    // create a dream
    $(".dream-create-form").click(function(){
        $('#dream').parent().removeClass('has-error');
    });
    var is_ajax = true;
    $(".dream-create-form").submit(function() {
        if ( !$('#dream').val() ) {
            $('#dream').parent().addClass('has-error');
            return false;
        }
        if (!is_ajax) return false;
        var data = $(this).serialize();
        $.post("/dream/create/", data, function(data) {
            is_ajax = false;
            if (data.error == 1) {
                var alert = $('.modal-body > .alert');
                alert.removeClass('alert-warning').addClass('alert-danger');
                alert.html(data.info);
            } else {
                window.location.href = "/"
            }
            is_ajax = true;
        }, 'json');
        return false;
    });

    // click dream
    $('.bs-col').click(function(){
        var id = $(this).attr('dream-id');
        window.location.href = "/dream/" + id + "/";
    });
});