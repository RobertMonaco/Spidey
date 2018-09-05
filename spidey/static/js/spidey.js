$(document).ready(function()
{
    // Create input group elements around file input
    $('.file-input').wrap('<span class="btn btn-primary btn-file"></span>')
                    .before("Browse...")
    $('span.btn').wrap('<label class="input-group-btn"></label>')
    $('.input-group-btn').wrap('<div class="input-group"></div>')
                         .after('<input type="text" class="form-control" readonly>')

    // Define the callback for when a file is selected
    $(':file').on('fileselect', function(event, numFiles, label) {

          var input = $(this).parents('.input-group').find(':text'),
              log = numFiles > 1 ? numFiles + ' files selected' : label;

          if( input.length ) {
              input.val(log);
          } else {
              if( log ) alert(log);
          }

      });
});

// Detect a file change and trigger the file selected event
$(document).on('change', ':file', function() {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
});