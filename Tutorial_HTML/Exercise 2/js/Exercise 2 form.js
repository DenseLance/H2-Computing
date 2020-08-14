$(".js-option").click(function () {
  //check if the selected option is others
      if ($(this).val() == "other") {
          $("#other-text").show();
      }else{
          $("#other-text").hide();
      }
  });