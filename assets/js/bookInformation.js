var page = parseInt(prompt("Kitabın səhifə sayı:"));
if (isNaN(page)) {
  alert("Hesablamada problem baş verdi");
} else {
  var days = parseInt(prompt("Neçə günə bitirməlisiniz?"));
  if (isNaN(days)) {
    alert("Hesablamada problem baş verdi");
  } else {
    var eachPage = parseInt(page / days);
    if (days == 0) {
      alert("Hesablamada problem baş verdi");
    } else {
      alert("Hər gün ən az " + eachPage + " səhifə oxumalısınız!");
      console.log("Səhifə sayı: " + page);
      console.log("Gün sayı: " + days);
      console.log("Nəticə: " + eachPage);
    }
  }
}
