$(document).ready(function(){
  var i = 1;
  $(".main-btn_test").on('click', function(e){
    $('#progress-scale' + i).toggleClass('progress-scale_active');
    $('#question' + i++).toggleClass('question_active');
    if(i != 5){
      $('#progress-scale' + i).toggleClass('progress-scale_active');
      $('#question' + i).toggleClass('question_active');
    } else {
      i = 1;
      $('#progress-scale' + i).toggleClass('progress-scale_active');
      $('#question' + i).toggleClass('question_active');
    }
  });
});