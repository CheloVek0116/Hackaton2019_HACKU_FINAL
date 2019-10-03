$(document).ready(function(){
  var i = 1;
  $(".main-btn_test").on('click', function(e){
    $('#progress-scale' + i).toggleClass('progress-scale_active');
    $('#question' + i++).toggleClass('question_active');
    if(i < 4){
      $('#progress-scale' + i).toggleClass('progress-scale_active');
      $('#question' + i).toggleClass('question_active');
    } else {
      sleep(1000)
      document.querySelector("#questions > button").click()
    }
  });
});