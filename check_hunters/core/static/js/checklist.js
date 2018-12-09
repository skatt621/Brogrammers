function colorTableRows() {

    // grab all the tr tags
    var trTags = document.getElementsByTagName("tr");

    //loop over the tr tags
    for (var i = 0; i < trTags.length; i++) {

      // in each tr tag, the outstanding tag is element 9 and the paid is element 7
      // this is hardcoded right now which isn't good, but there's no time to fix
      var outstandingTd = trTags[i].getElementsByTagName("td")[9];
      var paidTd = trTags[i].getElementsByTagName("td")[7];

      // if the td tag actually is a row in the checks table and not part of another form, and the check is outstanding
      if (outstandingTd != null && outstandingTd.textContent === "yes") {
        //mark that check red
        trTags[i].style.backgroundColor = "#bf2020";
        trTags[i].style.color = "white";
        outstandingTd.style.borderStyleLeft = "none";

      // if the td tag actually is a row in the checks table and not part of another form, and the check has been paid
      } else if (paidTd != null &&  paidTd.getElementsByClassName("true").length != 0) {
        trTags[i].style.backgroundColor = "green";
        trTags[i].style.color = "white";
      }
    }
}


  window.onload = colorTableRows;
