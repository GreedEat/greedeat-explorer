go_stick = (x) ->
  id = ".anchor"
  top_str = "data-top"
  end_str = "data-end"
  y = x.prev(id)
  window_top = $(window).scrollTop()
  div_top = y.offset().top
  top = if x.attr(top_str)? then parseInt(x.attr top_str) else 0
  if window_top > div_top-top
    x.css "top" : top
    x.css "left" : y.offset().left
    y.css "height" : total_height x
    x.addClass "go-sticky"
  else
    x.css "top" : "auto"
    x.css "left" : 'auto'
    y.css "height" : 0
    x.removeClass "go-sticky"
###
  footer = if x.attr(end_str)? then $("#"+x.attr(end_str)) else
  if x.attr(end_str)?

  else
###





stick_make = (x) ->
  x.width x.width()
  x.height x.height()
  id = "#anchor"
  y = $("<div class='#{id[1..]}'></div>").insertBefore(x)
  y.width total_width x

stick_it = () ->
  go_stick $(obj) for obj in $(".sticky")

stick_start= ->
  stick_make $(obj) for obj in $(".sticky")
  $(window).scroll stick_it
  stick_it()

$ ->
  #stick_start()