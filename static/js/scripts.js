// event saat link navbar di click
$('.page-scroll').click(function(e) {
  // alert( "Handler for .click() called." );
  // ambil isi href
  const tujuan = $(this).attr('href');
  // alert(tujuan);
  // tangkap elemen tujuan
  const elemen = $(tujuan);
  // console.log(elemen.offset().top);
  $('body, html').animate({
    scrollTop : elemen.offset().top - 50
  }, 1000);
  e.preventDefault();
});

// efek paralax
$(window).scroll(function() {
  const winscroll = $(this).scrollTop();

  // jumbotron
  $('.jumbotron img').css({
    'transform' : 'translate(0px, '+ winscroll/4 +'%)'
  });

  $('.jumbotron h1').css({
    'transform' : 'translate(0px, '+ winscroll/2 +'%)'
  });

  $('.jumbotron p').css({
    'transform' : 'translate(0px, '+ winscroll/1.5 +'%)'
  });

  // portofolio
  if (winscroll > $('.port').offset().top - 150) {

    const img = $('.port .img-thumbnail');
    $.each(img, function(i) {
      setTimeout(function() {
        img.eq(i).addClass('muncul');
        // console.log('ok');
      }, 500 * (i+1));
    });
    
  }
});
