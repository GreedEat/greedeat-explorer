total_width = (x) ->
  w = x.width();
  w += parseInt(x.css("padding-left"), 10) + parseInt(x.css("padding-right"), 10)
  w += parseInt(x.css("margin-left"), 10) + parseInt(x.css("margin-right"), 10)
  w += parseInt(x.css("borderLeftWidth"), 10) + parseInt(x.css("borderRightWidth"), 10)
  w

total_height = (x) ->
  h = x.height();
  h += parseInt(x.css("padding-top"), 10) + parseInt(x.css("padding-bottom"), 10)
  h += parseInt(x.css("margin-top"), 10) + parseInt(x.css("margin-bottom"), 10)
  h += parseInt(x.css("borderTopWidth"), 10) + parseInt(x.css("borderBottomWidth"), 10)
  h