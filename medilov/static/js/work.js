/**
 * main.js
 * http://www.codrops.com
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 *
 * Copyright 2015, Codrops
 * http://www.codrops.com
 *
 * @format
 */

(function() {
  var bodyEl = document.body,
    docElem = window.document.documentElement,
    support = { transitions: Modernizr.csstransitions },
    // transition end event name
    transEndEventNames = {
      WebkitTransition: "webkitTransitionEnd",
      MozTransition: "transitionend",
      OTransition: "oTransitionEnd",
      msTransition: "MSTransitionEnd",
      transition: "transitionend"
    },
    transEndEventName = transEndEventNames[Modernizr.prefixed("transition")],
    onEndTransition = function(el, callback) {
      var onEndCallbackFn = function(ev) {
        if (support.transitions) {
          if (ev.target != this) return;
          this.removeEventListener(transEndEventName, onEndCallbackFn);
        }
        if (callback && typeof callback === "function") {
          callback.call(this);
        }
      };
      if (support.transitions) {
        el.addEventListener(transEndEventName, onEndCallbackFn);
      } else {
        onEndCallbackFn();
      }
    },
    slider = document.querySelector(".stack-slider"),
    stackHeader = document.querySelector(".stack-title-header"),
    mobileHeader = document.querySelector(".stack-title-header-mobile"),
    mainHeader = document.querySelector(".codrops-header"),
    stacksWrapper = slider.querySelector(".stacks-wrapper"),
    stacks = [].slice.call(stacksWrapper.children),
    imghero = document.querySelector(".hero__back--mover"),
    simagehero = document.querySelector(".hero"),
    flkty,
    canOpen = true,
    canMoveHeroImage = true,
    isFirefox = typeof InstallTrigger !== "undefined",
    win = { width: window.innerWidth, height: window.innerHeight };

  function scrollY() {
    return window.pageYOffset || docElem.scrollTop;
  }

  // from http://www.sberry.me/articles/javascript-event-throttling-debouncing
  function throttle(fn, delay) {
    var allowSample = true;

    return function(e) {
      if (allowSample) {
        allowSample = false;
        setTimeout(function() {
          allowSample = true;
        }, delay);
        fn(e);
      }
    };
  }

  function init() {
    flkty = new Flickity(stacksWrapper, {
      autoPlay: true,
      pauseAutoPlayOnHover: false,
      selectedAttraction: 0.01,
      friction: 0.15,
      wrapAround: true,
      imagesLoaded: true,
      initialIndex: 0,
      setGallerySize: false,
      pageDots: false,
      prevNextButtons: false
    });

    // loading images...
    imagesLoaded(stacksWrapper, function() {
      classie.add(bodyEl, "view-init");
    });

    initEvents();
  }

  function initEvents() {
    stacks.forEach(closer);

    function closer(stack) {
      var titleEl = stack.querySelector(".stack-title");

      // expand/close the stack

      function toggler(ev) {
        ev.preventDefault();
        if (classie.has(stack, "is-selected")) {
          // current stack
          if (classie.has(bodyEl, "view-full")) {
            // stack is opened
            /*var closeStack = function() {
                        	classie.remove(bodyEl, 'move-items');
                        	setTimeout(function() { 
                        		classie.remove(mainHeader, 'cordrop-header-background');
                        		stackHeader.innerHTML = '';
                        		titleEl.style.display = 'inline-block'
                        	}, 250);
                        	console.log(stack)
                        	stackHeader.style.opacity = '0';
                        	stackHeader.style.transition = "opacity 0.25s linear 0s";
                        	onEndTransition(slider, function() {
                        		classie.remove(bodyEl, 'view-full');
                        		bodyEl.style.height = '';
                        		flkty.bindDrag();
                        		flkty.options.accessibility = true;
                        		canMoveHeroImage = true;
                        	});
                        };

                        // if the user scrolled down, let's first scroll all up before closing the stack.
                        var scrolled = scrollY();
                        if( scrolled > 0 ) {
                        	smooth_scroll_to(isFirefox ? docElem : bodyEl || docElem, 0, 500).then(function() {
                        		closeStack();
                        	});
                        }
                        else {
                        	closeStack();
                        }*/
          } else if (canOpen) {
            // stack is closed
            stack.removeEventListener("click", toggler);
            canMoveHeroImage = false;
            classie.add(bodyEl, "view-full");
            setTimeout(function() {
              classie.add(bodyEl, "move-items");
            }, 25);
            bodyEl.style.height = stack.offsetHeight + "px";
            flkty.unbindDrag();
            flkty.options.accessibility = false;
            var gap = document.createElement("div");
            gap.style.height = "100px";
            setTimeout(function() {
              classie.add(mainHeader, "cordrop-header-background");
              stackHeader.innerHTML = titleEl.innerHTML;
              titleEl.style.display = "none";
              stack.parentNode.insertBefore(gap, stack);
              simagehero.style.opacity = "0";
              simagehero.style.transition = "opacity 0.25s linear 0s";
              stackHeader.style.opacity = "1";
              stackHeader.style.transition = "opacity 0.25s linear 0s";
            }, 300);

            mobileHeader.addEventListener("click", function(ev) {
              if (classie.has(stack, "is-selected")) {
                // current stack
                if (classie.has(bodyEl, "view-full")) {
                  // stack is opened
                  var closeStack = function() {
                    classie.remove(bodyEl, "move-items");
                    setTimeout(function() {
                      classie.remove(mainHeader, "cordrop-header-background");
                      stackHeader.innerHTML = "";
                      titleEl.style.display = "inline-block";
                      gap.parentNode.removeChild(gap);
                      simagehero.style.opacity = "1";
                      simagehero.style.transition = "opacity 0.25s linear 0s";
                    }, 300);
                    onEndTransition(slider, function() {
                      classie.remove(bodyEl, "view-full");
                      bodyEl.style.height = "";
                      flkty.bindDrag();
                      flkty.options.accessibility = true;
                      canMoveHeroImage = true;
                    });
                  };

                  // if the user scrolled down, let's first scroll all up before closing the stack.
                  var scrolled = scrollY();
                  if (scrolled > 0) {
                    // smooth_scroll_to(
                    //   isFirefox ? docElem : bodyEl || docElem,
                    //   0,
                    //   500
                    // ).then(function() {
                    window.scrollTo({ top: 0, behavior: "smooth" });
                    closeStack();
                    stack.addEventListener("click", toggler);
                    // });
                  } else {
                    closeStack();
                    stack.addEventListener("click", toggler);
                  }
                }
              }
            });

            stackHeader.addEventListener("click", function(ev) {
              ev.preventDefault();
              if (classie.has(stack, "is-selected")) {
                // current stack
                if (classie.has(bodyEl, "view-full")) {
                  // stack is opened
                  var closeStack = function() {
                    classie.remove(bodyEl, "move-items");
                    setTimeout(function() {
                      classie.remove(mainHeader, "cordrop-header-background");
                      stackHeader.innerHTML = "";
                      titleEl.style.display = "inline-block";
                      gap.parentNode.removeChild(gap);
                      simagehero.style.opacity = "1";
                      simagehero.style.transition = "opacity 0.25s linear 0s";
                    }, 300);
                    stackHeader.style.opacity = "0";
                    stackHeader.style.transition = "opacity 0.25s linear 0s";
                    onEndTransition(slider, function() {
                      classie.remove(bodyEl, "view-full");
                      bodyEl.style.height = "";
                      flkty.bindDrag();
                      flkty.options.accessibility = true;
                      canMoveHeroImage = true;
                    });
                  };

                  // if the user scrolled down, let's first scroll all up before closing the stack.
                  var scrolled = scrollY();
                  if (scrolled > 0) {
                    // smooth_scroll_to(
                    //   isFirefox ? docElem : bodyEl || docElem,
                    //   0,
                    //   500
                    // ).then(function() {
                    window.scrollTo({ top: 0, behavior: "smooth" });
                    closeStack();
                    stack.addEventListener("click", toggler);
                    // });
                  } else {
                    closeStack();
                    stack.addEventListener("click", toggler);
                  }
                }
              }
            });
          }
        } else if (classie.has(stack, "stack-prev")) {
          flkty.previous(true);
        } else if (classie.has(stack, "stack-next")) {
          flkty.next(true);
        }
      }

      stack.addEventListener("click", toggler);

      titleEl.addEventListener("mouseenter", function(ev) {
        if (classie.has(stack, "is-selected")) {
          canMoveHeroImage = false;
          imghero.style.WebkitTransform =
            "perspective(1000px) translate3d(0,0,0) rotate3d(1,1,1,0deg)";
          imghero.style.transform =
            "perspective(1000px) translate3d(0,0,0) rotate3d(1,1,1,0deg)";
        }
      });

      titleEl.addEventListener("mouseleave", function(ev) {
        // if current stack and it's not opened..
        if (
          classie.has(stack, "is-selected") &&
          !classie.has(bodyEl, "view-full")
        ) {
          canMoveHeroImage = true;
        }
      });
    }

    window.addEventListener(
      "mousemove",
      throttle(function(ev) {
        if (!canMoveHeroImage) return false;
        var xVal = (-1 / (win.height / 2)) * ev.clientY + 1,
          yVal = (1 / (win.width / 2)) * ev.clientX - 1,
          transX = (20 / win.width) * ev.clientX - 10,
          transY = (20 / win.height) * ev.clientY - 10,
          transZ = (100 / win.height) * ev.clientY - 50;

        imghero.style.WebkitTransform =
          "perspective(1000px) translate3d(" +
          transX +
          "px," +
          transY +
          "px," +
          transZ +
          "px) rotate3d(" +
          xVal +
          "," +
          yVal +
          ",0,2deg)";
        imghero.style.transform =
          "perspective(1000px) translate3d(" +
          transX +
          "px," +
          transY +
          "px," +
          transZ +
          "px) rotate3d(" +
          xVal +
          "," +
          yVal +
          ",0,2deg)";
      }, 100)
    );

    // window resize
    window.addEventListener(
      "resize",
      throttle(function(ev) {
        // recalculate window width/height
        win = { width: window.innerWidth, height: window.innerHeight };
        // reset body height if stack is opened
        if (classie.has(bodyEl, "view-full")) {
          // stack is opened
          bodyEl.style.height = stacks[flkty.selectedIndex].offsetHeight + "px";
        }
      }, 50)
    );

    // Flickity events:
    flkty.on("cellSelect", function() {
      canOpen = false;
      classie.remove(bodyEl, "item-clickable");

      var prevStack = stacksWrapper.querySelector(".stack-prev"),
        nextStack = stacksWrapper.querySelector(".stack-next"),
        selidx = flkty.selectedIndex,
        cellsCount = flkty.cells.length,
        previdx = selidx > 0 ? selidx - 1 : cellsCount - 1;
      nextidx = selidx < cellsCount - 1 ? selidx + 1 : 0;

      if (prevStack) {
        classie.remove(prevStack, "stack-prev");
      }
      if (nextStack) {
        classie.remove(nextStack, "stack-next");
      }

      classie.add(stacks[previdx], "stack-prev");
      classie.add(stacks[nextidx], "stack-next");
    });

    flkty.on("dragStart", function() {
      canOpen = false;
      classie.remove(bodyEl, "item-clickable");
    });

    flkty.on("settle", function() {
      classie.add(bodyEl, "item-clickable");
      canOpen = true;
    });
  }

  init();
})();
