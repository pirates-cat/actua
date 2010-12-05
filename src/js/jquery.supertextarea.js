/**
 * Supertextarea
 * Created by Truth <truth@truthanduntruth.com>
 * Copyright 2010
 */
(function ($) {
   $.fn.supertextarea = function (faith) {
      var area = $(this);
      var cont = area.parent();
         
      var hope = {
         minw: area.width()
         , maxw: cont.width()
         , minh: area.height()
         , maxh: cont.height()
         , tabr: {
            use: true
            , space: true
            , num: 3
         }
         , css: {}
         , maxl: 1000
         , dsrm: {
            use: true
            , text: 'Remaining'
            , css: {}
         }
      }
      var love = {}
      var justice = $.extend(love, hope, faith);
      if (!justice.minh) {
         justice.minh = area.height();
      }
      if (!justice.minw) {
         justice.minw = area.width();
      }
      if (justice.maxh < justice.minh) {
         justice.maxh = justice.minh;
      }
      if (justice.maxw < justice.minw) {
         justice.maxw = justice.minw;
      }
      area.css(justice.css);
      area.height(justice.minh).width(justice.minw);
      if (justice.tabr.use && justice.tabr.num < 1) {
         justice.tabr.num = 1;
      }

      var rep_css = [
         'paddingTop',
         'paddingRight',
         'paddingBottom',
         'paddingLeft',
         'fontSize',
         'lineHeight',
         'fontFamily',
         'fontWeight'
      ];

      if (typeof $.fn.supertextarea.counter == 'undefined') {
         $.fn.supertextarea.counter = 0;
      }
      var idcounter = $.fn.supertextarea.counter;
      $.fn.supertextarea.counter++;

      this.each(function () {
         if (this.type != 'textarea') {
            return false;
         }

         var beh = $('<div />').css({'position': 'absolute','display': 'none', 'word-wrap':'break-word'});
         var line = parseInt(area.css('line-height')) || parseInt(area.css('font-size'));
         var goalheight = 0;

         beh.appendTo(area.parent());
         for (var i = 0; i < rep_css.length; i++) {
            beh.css(rep_css[i].toString(), area.css(rep_css[i].toString()));
         }
         beh.css('max-width', justice.maxw);

         function eval_height(height, overflow){
            nh = Math.floor(parseInt(height));
            if (area.height() != nh) {
               area.css({'height': nh + 'px', 'overflow-y':overflow});
            }
         }

         function eval_width(width, overflow) {
            nw = Math.floor(parseInt(width));
            if (area.width() != nw) {
               area.css({'width': nw + 'px', 'overflow-x': overflow});
            }
         }

         function update(e) {
            if (justice.dsrm.use && justice.maxl) {
               if (!$("#textarea_dsrm" + area.data('partner')).length) {
                  var dsm = document.createElement('div');
                  dsm.id = "textarea_dsrm" + idcounter;
                  $(dsm).text(justice.maxl + ' ' + justice.dsrm.text);
                  $(dsm).css(justice.dsrm.css);
                  area.after(dsm);
                  area.data('partner', idcounter);
               }
               var txt = justice.maxl - area.val().length;
               txt = txt < 0 ? 0 : txt;
               $("#textarea_dsrm" + area.data('partner')).text(txt + ' ' + justice.dsrm.text);
            }
            if (justice.maxl && justice.maxl - area.val().length < 0) {
               area.val(area.val().substring(0, justice.maxl));
            }
            var ac = area.val().replace(/&/g,'&amp;').replace(/  /g, '&nbsp;&nbsp;').replace(/<|>/g, '&gt;').replace(/\n/g, '<br />');
            var bc = beh.html();

            if (ac + '&nbsp;' != bc) {
               beh.html(ac + '&nbsp;');
               if (Math.abs(beh.height() + line - area.height()) > 3) {
                  var nh = beh.height() + line;
                  var maxh = justice.maxh;
                  var minh = justice.minh;
                  if (nh >= maxh) {
                     eval_height(maxh, 'auto');
                  }
                  else if (nh <= minh) {
                     eval_height(minh, 'hidden');
                  }
                  else {
                     eval_height(nh, 'hidden');
                  }
               }
               if (Math.abs(beh.width() + line - area.width()) > 3) {
                  var nw = beh.width() + line;
                  var maxw = justice.maxw;
                  var minw = justice.minw;
                  if (nw >= maxw) {
                     eval_width(maxw, 'auto');
                  }
                  else if (nw <= minw) {
                     eval_width(minw, 'hidden');
                  }
                  else {
                     eval_width(nw, 'hidden');
                  }
               }
            }
            if (justice.tabr.use && e) {
               tab_replace(e);
            }
         }

         function tab_replace(e) {
            var key = e.keyCode ? e.keyCode : e.charChode ? e.charCode : e.which;
            var sp = justice.tabr.space ? " " : "\t";
            var str = new Array(justice.tabr.num + 1).join(sp);
            if (key == 9 && !e.shiftKey && !e.ctrlKey && !e.altKey) {
               var os = area.scrollTop();
               if (area.setSelectionRange) {
                  var ss = area.selectionStart;
                  var se = area.selectionEnd;
                  area.val(area.val().substring(0, ss) + str + area.val.substr(se));
                  area.focus();
               }
               else if (area.createTextRange) {
                  document.selection.createRange().text = str;
                  e.returnValue = false;
               }
               else {
                  area.val(area.val() + str);
               }
               area.scrollTop(os);
               if (e.preventDefault) {
                  e.preventDefault();
               }
               return false;
            }
            return true;
         }

         area.css({'overflow':'auto'})
            .keydown(function (e) { update(e); })
            .live('input paste', function () { setTimeout(update, 250); });

         update();
      });
   }
})(jQuery);
