$(document).ready(function () {

  $(".username")
    .focus(function(){
      $(".username-help").slideDown(500);
    })
    .blur(function(){
      $(".username-help").slideUp(500);
    });

  $(".email")
    .focus(function(){
      $(".email-help").slideDown(500);
    })
    .blur(function(){
      $(".email-help").slideUp(500);
    });

  $(".password")
    .focus(function(){
      $(".password-help").slideDown(500);
    })
    .blur(function(){
      $(".password-help").slideUp(500);
    });

  $(".confirm_password")
    .focus(function(){
      $(".confirm_password-help").slideDown(500);
    })
    .blur(function(){
      $(".confirm_password-help").slideUp(500);
    });

  $("#login-form").click(function () {
     $(this).addClass("active");
     $("#signup-form").removeClass("active");
  });

  $("#signup-form").click(function () {
    $(this).addClass("active");
    $("#login-form").removeClass("active");
  });

  document.getElementById("login-form").onclick = function () {
    location.href = "login";
  };

  document.getElementById("signup-form").onclick = function () {
    location.href = "register";
  };
});
