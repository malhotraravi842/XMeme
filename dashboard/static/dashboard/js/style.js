// Contact Form
$(".contact-form")
    .find(".form-control")
    .each(function () {
        var targetItem = $($(this).parent()).parent();
        if ($(this).val()) {
            $(targetItem).find("label").css({
                top: "10px",
                fontSize: "14px"
            });
        }
    });
$(".contact-form")
    .find(".form-control")
    .focus(function () {
        $(this).parent().find("label").animate(
            {
                top: "10px",
                fontSize: "14px"
            },
            300
        );
    });
$(".contact-form")
    .find(".form-control")
    .blur(function () {
        if ($(this).val().length == 0) {
            $(this).parent().find("label").animate(
                {
                    top: "35px",
                    fontSize: "18px"
                },
                300
            );
        }
    });


// Button
var btn = $('#button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});
